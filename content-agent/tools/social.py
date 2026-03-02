"""
Social media posting functions for Simple Rabbit content agent.
Handles: Twitter/X, Threads, Instagram, Facebook, LinkedIn
"""

import os
import time
import requests
import tweepy
from dotenv import load_dotenv

load_dotenv()


# ─────────────────────────────────────────────
# TWITTER / X
# ─────────────────────────────────────────────

def post_to_twitter(content: str) -> dict:
    """Post a tweet to X/Twitter. Returns success/failure dict."""
    try:
        client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
        )
        response = client.create_tweet(text=content)
        tweet_id = response.data["id"]
        return {"success": True, "platform": "twitter", "id": tweet_id}
    except Exception as e:
        return {"success": False, "platform": "twitter", "error": str(e)}


# ─────────────────────────────────────────────
# THREADS
# ─────────────────────────────────────────────

def post_to_threads(content: str) -> dict:
    """Post a text post to Threads via Meta Graph API."""
    try:
        user_id = os.getenv("THREADS_USER_ID")
        token = os.getenv("META_ACCESS_TOKEN")
        base = "https://graph.threads.net/v1.0"

        # Step 1: Create media container
        container_resp = requests.post(
            f"{base}/{user_id}/threads",
            params={
                "media_type": "TEXT",
                "text": content,
                "access_token": token,
            },
            timeout=30,
        )
        container_resp.raise_for_status()
        creation_id = container_resp.json()["id"]

        # Step 2: Publish (Meta recommends a short delay)
        time.sleep(3)
        publish_resp = requests.post(
            f"{base}/{user_id}/threads_publish",
            params={
                "creation_id": creation_id,
                "access_token": token,
            },
            timeout=30,
        )
        publish_resp.raise_for_status()
        post_id = publish_resp.json()["id"]
        return {"success": True, "platform": "threads", "id": post_id}
    except Exception as e:
        return {"success": False, "platform": "threads", "error": str(e)}


# ─────────────────────────────────────────────
# FACEBOOK PAGE
# ─────────────────────────────────────────────

def post_to_facebook(content: str) -> dict:
    """Post to the Simple Rabbit Facebook business page."""
    try:
        page_id = os.getenv("FACEBOOK_PAGE_ID")
        token = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN")

        resp = requests.post(
            f"https://graph.facebook.com/v20.0/{page_id}/feed",
            data={"message": content, "access_token": token},
            timeout=30,
        )
        resp.raise_for_status()
        post_id = resp.json().get("id")
        return {"success": True, "platform": "facebook", "id": post_id}
    except Exception as e:
        return {"success": False, "platform": "facebook", "error": str(e)}


# ─────────────────────────────────────────────
# INSTAGRAM (caption only — image must be provided)
# ─────────────────────────────────────────────

def post_to_instagram(caption: str, image_url: str) -> dict:
    """
    Post a photo to Instagram. Requires a publicly accessible image URL.
    image_url must be a direct link to a JPG/PNG hosted online.
    """
    try:
        ig_user_id = os.getenv("INSTAGRAM_USER_ID")
        token = os.getenv("META_ACCESS_TOKEN")
        base = f"https://graph.facebook.com/v20.0/{ig_user_id}"

        # Step 1: Create media container
        container_resp = requests.post(
            f"{base}/media",
            params={
                "image_url": image_url,
                "caption": caption,
                "access_token": token,
            },
            timeout=30,
        )
        container_resp.raise_for_status()
        creation_id = container_resp.json()["id"]

        # Step 2: Publish
        time.sleep(3)
        publish_resp = requests.post(
            f"{base}/media_publish",
            params={"creation_id": creation_id, "access_token": token},
            timeout=30,
        )
        publish_resp.raise_for_status()
        post_id = publish_resp.json()["id"]
        return {"success": True, "platform": "instagram", "id": post_id}
    except Exception as e:
        return {"success": False, "platform": "instagram", "error": str(e)}


# ─────────────────────────────────────────────
# LINKEDIN
# ─────────────────────────────────────────────

def post_to_linkedin(content: str) -> dict:
    """Post a text post to LinkedIn as the authenticated member."""
    try:
        token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        author_urn = os.getenv("LINKEDIN_PERSON_URN")  # e.g. "urn:li:person:XXXXXXXX"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Restli-Protocol-Version": "2.0.0",
        }
        payload = {
            "author": author_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": content},
                    "shareMediaCategory": "NONE",
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            },
        }
        resp = requests.post(
            "https://api.linkedin.com/v2/ugcPosts",
            headers=headers,
            json=payload,
            timeout=30,
        )
        resp.raise_for_status()
        post_id = resp.headers.get("x-restli-id", "unknown")
        return {"success": True, "platform": "linkedin", "id": post_id}
    except Exception as e:
        return {"success": False, "platform": "linkedin", "error": str(e)}
