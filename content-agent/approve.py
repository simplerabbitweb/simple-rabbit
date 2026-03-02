#!/usr/bin/env python3
"""
Simple Rabbit — Approval & Posting Script

Run this after you receive Sage's morning email to review and post
the pending Instagram, Facebook, and LinkedIn content.

Usage:
    python approve.py

For Instagram, you'll be prompted to provide a public image URL.
"""

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tools.social import post_to_facebook, post_to_instagram, post_to_linkedin
from tools.memory_tools import mark_pending_as_posted, read_pending_posts

# ANSI colors for terminal readability
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"
DIM = "\033[2m"


def parse_pending_posts(raw: str) -> list[dict]:
    """
    Parse the pending markdown file into a list of post dicts.
    Format expected:
        ## PLATFORM
        content
        _Note: ..._
    """
    posts = []
    # Split on section headers
    sections = re.split(r"\n---\n", raw)
    for section in sections:
        match = re.search(r"##\s+(\w+)\s*\n(.*?)(?:\n_Note:\s*(.+?)_)?$", section.strip(), re.DOTALL)
        if match:
            platform = match.group(1).lower()
            content = match.group(2).strip()
            note = match.group(3).strip() if match.group(3) else ""
            if platform in ("instagram", "facebook", "linkedin") and content:
                posts.append({"platform": platform, "content": content, "note": note})
    return posts


def prompt_action(platform: str) -> str:
    """Ask user what to do with a pending post. Returns 'approve', 'skip', or 'quit'."""
    while True:
        choice = input(f"\n  [{BOLD}A{RESET}]pprove  [{BOLD}S{RESET}]kip  [{BOLD}Q{RESET}]uit  → ").strip().lower()
        if choice in ("a", "approve"):
            return "approve"
        if choice in ("s", "skip"):
            return "skip"
        if choice in ("q", "quit"):
            return "quit"
        print("  Please enter A, S, or Q.")


def handle_instagram(content: str, note: str) -> None:
    """Instagram needs an image URL. Prompt for it, then post."""
    print(f"\n  {YELLOW}Instagram requires a public image URL.{RESET}")
    if note:
        print(f"  Sage's suggestion: {DIM}{note}{RESET}")
    print("  The image must be hosted online (e.g., your website, Dropbox public link).")
    image_url = input("  Image URL: ").strip()
    if not image_url:
        print("  No URL provided. Skipping Instagram.")
        return
    result = post_to_instagram(content, image_url)
    if result["success"]:
        print(f"  {GREEN}Posted to Instagram. ✅{RESET}")
        mark_pending_as_posted("instagram")
    else:
        print(f"  Post failed: {result['error']}")


def handle_facebook(content: str) -> None:
    result = post_to_facebook(content)
    if result["success"]:
        print(f"  {GREEN}Posted to Facebook. ✅{RESET}")
        mark_pending_as_posted("facebook")
    else:
        print(f"  Post failed: {result['error']}")


def handle_linkedin(content: str) -> None:
    result = post_to_linkedin(content)
    if result["success"]:
        print(f"  {GREEN}Posted to LinkedIn. ✅{RESET}")
        mark_pending_as_posted("linkedin")
    else:
        print(f"  Post failed: {result['error']}")


def main():
    today = date.today().strftime("%A, %B %-d")
    raw = read_pending_posts()

    print(f"\n{BOLD}🐇 Simple Rabbit — Approval Session{RESET}")
    print(f"   {today}\n")

    if not raw:
        print("No pending posts found for today. Either Sage hasn't run yet, or everything was already posted.")
        return

    posts = parse_pending_posts(raw)
    if not posts:
        print("Could not parse any pending posts. Check content-agent/pending/ manually.")
        print(f"\nRaw file:\n{raw}")
        return

    print(f"Found {len(posts)} post(s) pending approval:\n")

    for i, post in enumerate(posts, 1):
        platform = post["platform"].upper()
        content = post["content"]
        note = post["note"]

        print(f"{'─' * 50}")
        print(f"{CYAN}{BOLD}[{i}/{len(posts)}] {platform}{RESET}")
        print(f"{'─' * 50}")
        print(f"\n{content}\n")
        if note:
            print(f"{DIM}Note: {note}{RESET}")

        action = prompt_action(platform)

        if action == "quit":
            print("\nStopped. Remaining posts are still in the pending queue.")
            break
        elif action == "skip":
            print(f"  Skipped {platform}.")
            continue
        elif action == "approve":
            if post["platform"] == "instagram":
                handle_instagram(content, note)
            elif post["platform"] == "facebook":
                handle_facebook(content)
            elif post["platform"] == "linkedin":
                handle_linkedin(content)

    print(f"\n{'─' * 50}")
    print("Approval session complete.\n")


if __name__ == "__main__":
    main()
