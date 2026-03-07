#!/usr/bin/env python3
"""
Simple Rabbit — Article Approve & Publish

Run this after Sage emails you an article draft on Friday.
It lists pending drafts, lets you review, and publishes to the live site.

Usage:
    python content-agent/article_approve.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from tools.article_tools import list_article_drafts, publish_article


def main():
    print("\n📝  Simple Rabbit — Article Approve & Publish")
    print("=" * 50)

    drafts = list_article_drafts()

    if not drafts:
        print("\nNo article drafts found.")
        print(f"Sage saves drafts to: content-agent/drafts/articles/")
        print("Sage generates them on Fridays. Run agent.py to trigger.\n")
        return

    # ── List available drafts ──────────────────────────────────────
    print(f"\nFound {len(drafts)} draft(s):\n")
    for i, d in enumerate(drafts, 1):
        print(f"  [{i}] {d['draft_date']}  {d['title']}")
        print(f"      Category:  {d['category']}")
        print(f"      Keywords:  {d['primary_keyword']}")
        print(f"      Words:     {d['word_count']}")
        print(f"      File:      {Path(d['path']).name}")
        print()

    # ── Select draft ──────────────────────────────────────────────
    if len(drafts) == 1:
        selected = drafts[0]
        print(f"One draft found. Using: {selected['title']}\n")
    else:
        while True:
            try:
                choice = input("Which draft do you want to publish? Enter number: ").strip()
                idx = int(choice) - 1
                if 0 <= idx < len(drafts):
                    selected = drafts[idx]
                    break
                print(f"  Please enter a number between 1 and {len(drafts)}.")
            except (ValueError, KeyboardInterrupt):
                print("\nAborted.\n")
                return

    # ── Confirm ───────────────────────────────────────────────────
    print(f"\nAbout to publish:")
    print(f"  Title:    {selected['title']}")
    print(f"  Category: {selected['category']}")
    print(f"  URL:      https://simplerabbit.studio/blog/{selected['slug']}")
    print(f"\nThis will:")
    print(f"  • Copy draft to blog/{selected['slug']}.html")
    print(f"  • Add a card to the top of articles.html")
    print(f"  • Add the URL to sitemap.xml")
    print(f"  • Upload all three files via FTP")
    print(f"  • Purge the SiteGround cache")
    print(f"\n  Note: The article card will show a placeholder image.")
    print(f"  Add previews/article-{selected['slug']}.png when ready.")
    print()

    confirm = input("Publish now? [y/N] ").strip().lower()
    if confirm != "y":
        print("\nAborted. Draft is still in content-agent/drafts/articles/\n")
        return

    # ── Publish ───────────────────────────────────────────────────
    print("\nPublishing...")
    try:
        result = publish_article(Path(selected["path"]))
    except Exception as e:
        print(f"\n❌  Error during publish: {e}\n")
        return

    print()
    print("✅  Published successfully!")
    print(f"   URL:      {result['url']}")
    print(f"   Date:     {result['pub_date']}")
    print(f"   FTP:      {result['ftp']}")
    print(f"   Cache:    {result['cache']}")
    print(f"   Archived: {Path(result['archived_to']).name}")
    print()
    print("Next steps:")
    print(f"  1. Add a featured image:  previews/article-{result['slug']}.png  (1200x630)")
    print(f"  2. Run deploy.sh to update the image + articles page card")
    print()


if __name__ == "__main__":
    main()
