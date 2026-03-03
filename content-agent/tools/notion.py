"""
Notion API tool for Simple Rabbit.
Appends daily social media drafts to the Daily Social Posts page.
"""

import os
import requests

NOTION_API_URL = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"
PAGE_ID = "317f8941c2ab8034af3acdc0e6a1f843"


def _headers() -> dict:
    return {
        "Authorization": f"Bearer {os.getenv('NOTION_API_KEY')}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION,
    }


def _text_block(block_type: str, content: str) -> dict:
    """Build a simple Notion text block (paragraph, heading_2, heading_3)."""
    # Notion caps rich_text at 2000 chars per block — split if needed
    chunks = [content[i:i+2000] for i in range(0, len(content), 2000)]
    rich_text = [{"type": "text", "text": {"content": chunk}} for chunk in chunks]
    return {
        "object": "block",
        "type": block_type,
        block_type: {"rich_text": rich_text},
    }


def _divider() -> dict:
    return {"object": "block", "type": "divider", "divider": {}}


def clear_notion_page() -> dict:
    """Delete all blocks from the Daily Social Posts page. Runs every Monday."""
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"success": False, "error": "NOTION_API_KEY not set."}

    deleted = 0
    cursor = None

    while True:
        params = {"page_size": 100}
        if cursor:
            params["start_cursor"] = cursor

        response = requests.get(
            f"{NOTION_API_URL}/blocks/{PAGE_ID}/children",
            headers=_headers(),
            params=params,
        )
        if not response.ok:
            return {"success": False, "error": f"Notion API error {response.status_code}: {response.text}"}

        data = response.json()
        blocks = data.get("results", [])

        for block in blocks:
            requests.delete(
                f"{NOTION_API_URL}/blocks/{block['id']}",
                headers=_headers(),
            )
            deleted += 1

        if not data.get("has_more"):
            break
        cursor = data.get("next_cursor")

    return {"success": True, "cleared": deleted}


def write_newsletter_outline_to_notion(date_label: str, outline: str) -> dict:
    """Append the weekly newsletter outline to the Daily Social Posts Notion page."""
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"success": False, "error": "NOTION_API_KEY not set."}

    blocks = [
        _text_block("heading_2", f"NEWSLETTER OUTLINE — {date_label}"),
    ]

    # Split outline into paragraphs and add each as a block
    for para in outline.split("\n"):
        stripped = para.strip()
        if stripped:
            blocks.append(_text_block("paragraph", stripped))

    blocks.append(_divider())

    for i in range(0, len(blocks), 100):
        chunk = blocks[i:i+100]
        response = requests.patch(
            f"{NOTION_API_URL}/blocks/{PAGE_ID}/children",
            headers=_headers(),
            json={"children": chunk},
        )
        if not response.ok:
            return {
                "success": False,
                "error": f"Notion API error {response.status_code}: {response.text}",
            }

    return {"success": True}


def write_posts_to_notion(day_label: str, posts: list[dict]) -> dict:
    """
    Append today's posts to the Daily Social Posts Notion page.
    Each day gets a heading, then each platform as a subheading + content block.
    """
    api_key = os.getenv("NOTION_API_KEY")
    if not api_key:
        return {"success": False, "error": "NOTION_API_KEY not set."}

    blocks = []

    # Day heading
    blocks.append(_text_block("heading_2", day_label))

    for post in posts:
        platform = post["platform"].replace("twitter", "X / Twitter").upper()
        note = f"  ({post['note']})" if post.get("note") else ""
        blocks.append(_text_block("heading_3", f"{platform}{note}"))
        blocks.append(_text_block("paragraph", post["content"].strip()))

    # Divider at the end of the day
    blocks.append(_divider())

    # Notion API allows max 100 blocks per request — chunk if needed
    for i in range(0, len(blocks), 100):
        chunk = blocks[i:i+100]
        response = requests.patch(
            f"{NOTION_API_URL}/blocks/{PAGE_ID}/children",
            headers=_headers(),
            json={"children": chunk},
        )
        if not response.ok:
            return {
                "success": False,
                "error": f"Notion API error {response.status_code}: {response.text}",
            }

    return {"success": True}
