"""
Social media posting tools for Simple Rabbit.
Used by both Sage (content-agent) and Leo (ops-agent).
"""

import os
import time
import requests
import tweepy


def post_to_twitter(content: str) -> dict:
    """Post to X/Twitter via Tweepy v4."""
    try:
        client = tweepy.Client(
            consumer_key=os.getenv("TWITTER_API_KEY"),
            consumer_secret=os.getenv("TWITTER_API_SECRET"),
            access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
            access_token_secret=os.getenv("TWITTER_ACCESS_SECRET"),
        )
        response = client.create_tweet(text=content)
        return {"success": True, "id": str(response.data["id"])}
    except Exception as e:
        return {"success": False, "error": str(e)}


def post_to_threads(content: str) -> dict:
    """Post a text post to Threads via the Threads Graph API."""
    user_id = os.getenv("THREADS_USER_ID")
    token = os.getenv("THREADS_ACCESS_TOKEN")

    if not user_id or not token:
        return {"success": False, "error": "THREADS_USER_ID or THREADS_ACCESS_TOKEN not set."}

    try:
        # Step 1: Create a media container
        r = requests.post(
            f"https://graph.threads.net/v1.0/{user_id}/threads",
            params={
                "media_type": "TEXT",
                "text": content,
                "access_token": token,
            },
            timeout=15,
        )
        r.raise_for_status()
        container_id = r.json().get("id")
        if not container_id:
            return {"success": False, "error": f"No container ID returned: {r.text}"}

        # Brief pause before publishing (recommended by Meta)
        time.sleep(2)

        # Step 2: Publish
        r2 = requests.post(
            f"https://graph.threads.net/v1.0/{user_id}/threads_publish",
            params={
                "creation_id": container_id,
                "access_token": token,
            },
            timeout=15,
        )
        r2.raise_for_status()
        post_id = r2.json().get("id")
        return {"success": True, "id": str(post_id)}

    except requests.HTTPError as e:
        return {"success": False, "error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def post_to_instagram(caption: str, image_url: str) -> dict:
    """Post an image + caption to Instagram via the Instagram Graph API."""
    user_id = os.getenv("INSTAGRAM_USER_ID")
    token = os.getenv("INSTAGRAM_ACCESS_TOKEN")

    if not user_id or not token:
        return {"success": False, "error": "INSTAGRAM_USER_ID or INSTAGRAM_ACCESS_TOKEN not set."}

    try:
        # Step 1: Create media container
        r = requests.post(
            f"https://graph.instagram.com/v18.0/{user_id}/media",
            params={
                "image_url": image_url,
                "caption": caption,
                "access_token": token,
            },
            timeout=20,
        )
        r.raise_for_status()
        container_id = r.json().get("id")
        if not container_id:
            return {"success": False, "error": f"No container ID: {r.text}"}

        time.sleep(3)

        # Step 2: Publish
        r2 = requests.post(
            f"https://graph.instagram.com/v18.0/{user_id}/media_publish",
            params={
                "creation_id": container_id,
                "access_token": token,
            },
            timeout=20,
        )
        r2.raise_for_status()
        post_id = r2.json().get("id")
        return {"success": True, "id": str(post_id)}

    except requests.HTTPError as e:
        return {"success": False, "error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def post_to_facebook(content: str) -> dict:
    """Post to a Facebook Page via the Graph API."""
    page_id = os.getenv("FACEBOOK_PAGE_ID")
    token = os.getenv("FACEBOOK_ACCESS_TOKEN")

    if not page_id or not token:
        return {"success": False, "error": "FACEBOOK_PAGE_ID or FACEBOOK_ACCESS_TOKEN not set."}

    try:
        r = requests.post(
            f"https://graph.facebook.com/v18.0/{page_id}/feed",
            params={
                "message": content,
                "access_token": token,
            },
            timeout=15,
        )
        r.raise_for_status()
        post_id = r.json().get("id")
        return {"success": True, "id": str(post_id)}

    except requests.HTTPError as e:
        return {"success": False, "error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}


def post_to_linkedin(content: str) -> dict:
    """Post to LinkedIn via the UGC Posts API v2."""
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    person_id = os.getenv("LINKEDIN_PERSON_ID")

    if not token or not person_id:
        return {"success": False, "error": "LINKEDIN_ACCESS_TOKEN or LINKEDIN_PERSON_ID not set."}

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    payload = {
        "author": f"urn:li:person:{person_id}",
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

    try:
        r = requests.post(
            "https://api.linkedin.com/v2/ugcPosts",
            headers=headers,
            json=payload,
            timeout=15,
        )
        r.raise_for_status()
        post_id = r.headers.get("x-restli-id", r.json().get("id", "unknown"))
        return {"success": True, "id": str(post_id)}

    except requests.HTTPError as e:
        return {"success": False, "error": f"HTTP {e.response.status_code}: {e.response.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}
