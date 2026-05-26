#!/usr/bin/env python3
"""
update-blog-feed.py
Reads all blog/*.html files, finds the 3 most recent non-case-study posts,
and updates the 'From the blog' section in index.html between marker comments.

Run automatically by deploy.sh before each deploy.
"""

import re
import sys
from pathlib import Path

SITE_ROOT = Path(__file__).parent.parent
BLOG_DIR = SITE_ROOT / "blog"
INDEX    = SITE_ROOT / "index.html"
MARKER_START = "<!-- BLOG-FEED-START -->"
MARKER_END   = "<!-- BLOG-FEED-END -->"

posts = []

for f in sorted(BLOG_DIR.glob("*.html")):
    slug = f.stem

    # Case studies live in their own section on the homepage — skip them here
    if slug.startswith("case-study"):
        continue

    html = f.read_text(encoding="utf-8")

    # datePublished from JSON-LD
    date_match = re.search(r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"', html)
    if not date_match:
        continue
    date = date_match.group(1)

    # Title from og:title, strip site suffix
    title_match = re.search(r'<meta property="og:title" content="([^"]+)"', html)
    if not title_match:
        continue
    title = title_match.group(1).replace(" | Simple Rabbit", "").strip()

    # Preview image — relative path (strip domain)
    img_match = re.search(
        r'<meta property="og:image" content="https://simplerabbit\.studio/([^"]+)"', html
    )
    img = img_match.group(1) if img_match else "previews/article-default.jpg"

    # Category label from article body
    cat_match = re.search(r'<span class="article-category">([^<]+)</span>', html)
    category = cat_match.group(1).strip() if cat_match else "From the Blog"

    posts.append({"date": date, "slug": slug, "title": title, "img": img, "category": category})

# Sort newest first, take top 3
posts.sort(key=lambda p: p["date"], reverse=True)
top3 = posts[:3]

if not top3:
    print("⚠️  No blog posts found — skipping blog feed update.")
    sys.exit(0)


def card_html(p):
    # Escape < > & in title for safe HTML insertion
    safe_title = (
        p["title"]
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("'", "&rsquo;")
        .replace('"', "&ldquo;")
    )
    safe_category = p["category"].replace("&", "&amp;")
    return (
        f'      <a href="/blog/{p["slug"]}" class="card reveal">\n'
        f'        <div class="card-img"><img src="{p["img"]}" alt="{safe_title}" loading="lazy"></div>\n'
        f'        <div class="card-body">\n'
        f'          <span style="font-family:var(--font-b);font-size:11px;font-weight:500;letter-spacing:2.5px;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:16px;">{safe_category}</span>\n'
        f'          <h3 style="font-family:var(--font-d);font-size:22px;line-height:1.3;font-weight:400;letter-spacing:-0.5px;margin-bottom:16px;">{safe_title}</h3>\n'
        f'        </div>\n'
        f'        <div class="card-foot"><span>Read article</span><span>&rarr;</span></div>\n'
        f'      </a>'
    )


cards_html = "\n\n".join(card_html(p) for p in top3)
new_block = f"{MARKER_START}\n{cards_html}\n      {MARKER_END}"

index_html = INDEX.read_text(encoding="utf-8")
new_index, count = re.subn(
    rf"{re.escape(MARKER_START)}.*?{re.escape(MARKER_END)}",
    new_block,
    index_html,
    flags=re.DOTALL,
)

if count == 0:
    print("⚠️  Blog feed markers not found in index.html — no changes made.")
    sys.exit(1)

INDEX.write_text(new_index, encoding="utf-8")
slugs = [p["slug"] for p in top3]
print(f"  ✓ Blog feed updated → {', '.join(slugs)}")
