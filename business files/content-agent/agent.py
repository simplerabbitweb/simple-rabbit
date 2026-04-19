#!/usr/bin/env python3
"""
Simple Rabbit Content Agent — Sage
Reads blog articles and generates on-brand social media content daily.

Posting schedule:
  Every day:   Threads (1), X/Twitter (1), Facebook (1)
  Mon/Wed/Fri: Instagram (1), LinkedIn (1)

Output: saves drafts to a weekly markdown file + emails Leann the day's posts.
No API connections required — just copy and paste.

Usage:
    python agent.py            # run today's content session
    python agent.py --dry-run  # generate posts but don't save or email anything
"""

import json
import os
import re
import sys
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path

import anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).parent.parent
BLOG_DIR = ROOT / "blog"
AGENT_DIR = Path(__file__).parent
DRAFTS_DIR = AGENT_DIR / "drafts"

load_dotenv(AGENT_DIR / ".env", override=True)

sys.path.insert(0, str(AGENT_DIR))
from tools.memory_tools import read_recent_memory, write_daily_log
from tools.email_notify import send_drafts_email
from tools.article_tools import (
    get_article_topic_override,
    clear_article_topic_override,
    get_next_pillar,
    mark_pillar_used,
    save_article_draft,
)

DRY_RUN = "--dry-run" in sys.argv


# ─────────────────────────────────────────────
# ARTICLE PARSING
# ─────────────────────────────────────────────

class _TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self._skip = False
        self._skip_tags = {"script", "style", "nav", "head"}
        self._block_tags = {"p", "h1", "h2", "h3", "h4", "li", "blockquote", "div"}

    def handle_starttag(self, tag, attrs):
        if tag in self._skip_tags:
            self._skip = True

    def handle_endtag(self, tag):
        if tag in self._skip_tags:
            self._skip = False
        elif tag in self._block_tags:
            self.parts.append(" ")

    def handle_data(self, data):
        if not self._skip:
            stripped = data.strip()
            if stripped:
                self.parts.append(stripped)

    def get_text(self) -> str:
        raw = " ".join(self.parts)
        return re.sub(r"\s{2,}", " ", raw).strip()


def parse_article(file_path: Path) -> dict:
    html = file_path.read_text(encoding="utf-8")

    meta = {}
    comment_match = re.search(r"<!--(.*?)-->", html, re.DOTALL)
    if comment_match:
        for line in comment_match.group(1).strip().splitlines():
            if ":" in line:
                key, _, value = line.partition(":")
                meta[key.strip()] = value.strip()

    canonical_match = re.search(r'<link rel="canonical" href="([^"]+)"', html)
    url = canonical_match.group(1) if canonical_match else ""

    extractor = _TextExtractor()
    extractor.feed(html)
    body = extractor.get_text()
    if len(body) > 3000:
        body = body[:3000] + "…"

    return {
        "title": meta.get("TITLE", file_path.stem),
        "slug": meta.get("SLUG", file_path.stem),
        "description": meta.get("META DESCRIPTION", ""),
        "url": url,
        "text": body,
    }


def load_all_articles() -> list[dict]:
    articles = []
    for f in sorted(BLOG_DIR.glob("*.html")):
        try:
            articles.append(parse_article(f))
        except Exception as e:
            print(f"  ⚠ Could not parse {f.name}: {e}")
    return articles


def format_articles_for_prompt(articles: list[dict]) -> str:
    lines = []
    for a in articles:
        lines.append(
            f"ARTICLE: {a['title']}\n"
            f"URL: {a['url']}\n"
            f"DESCRIPTION: {a['description']}\n"
            f"CONTENT EXCERPT: {a['text'][:1500]}\n"
        )
    return "\n---\n".join(lines)


# ─────────────────────────────────────────────
# SCHEDULE LOGIC
# ─────────────────────────────────────────────

def todays_platforms() -> list[str]:
    today = date.today().weekday()  # 0=Monday … 6=Sunday
    platforms = ["threads", "twitter", "facebook", "instagram"]
    if today in (0, 2, 4):  # Mon, Wed, Fri
        platforms += ["linkedin"]
    return platforms


# ─────────────────────────────────────────────
# DRAFT FILE HELPERS
# ─────────────────────────────────────────────

def get_week_file_path() -> Path:
    """Weekly draft file, named after Monday of the current week."""
    monday = date.today() - timedelta(days=date.today().weekday())
    DRAFTS_DIR.mkdir(parents=True, exist_ok=True)
    return DRAFTS_DIR / f"week-{monday.isoformat()}.md"


def week_file_header(monday: date) -> str:
    return f"# Simple Rabbit — Week of {monday.strftime('%B %-d, %Y')}\n"


def format_posts_as_markdown(day_label: str, posts: list[dict]) -> str:
    """Format a day's posts as a markdown section."""
    lines = [f"\n---\n\n## {day_label}\n"]
    for post in posts:
        platform = post["platform"].replace("twitter", "X / Twitter").title()
        note = f" _({post['note']})_" if post.get("note") else ""
        lines.append(f"### {platform}{note}\n")
        lines.append(post["content"].strip())
        lines.append("")  # blank line after content
    return "\n".join(lines)


def format_posts_for_email(day_label: str, posts: list[dict]) -> str:
    """Format a day's posts as plain text for email."""
    lines = [f"Your content for {day_label}:\n", "=" * 50]
    for post in posts:
        platform = post["platform"].replace("twitter", "X / Twitter").upper()
        note = f"  ({post['note']})" if post.get("note") else ""
        lines.append(f"\n{platform}{note}")
        lines.append("-" * len(platform))
        lines.append(post["content"].strip())
    lines.append("\n" + "=" * 50)
    lines.append("Copy and paste to each platform when you're ready.")
    return "\n".join(lines)


# ─────────────────────────────────────────────
# TOOL DEFINITIONS
# ─────────────────────────────────────────────

SAGE_TOOLS = [
    {
        "name": "read_articles",
        "description": (
            "Load all Simple Rabbit blog articles. "
            "Returns titles, URLs, descriptions, and content excerpts. "
            "Always call this first."
        ),
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "read_recent_memory",
        "description": (
            "Read the last 7 days of activity logs to see which articles and angles "
            "have been used recently. Use this to avoid repetition."
        ),
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "save_drafts",
        "description": (
            "Save today's drafted posts to the weekly file and email them to Leann. "
            "Call this once with ALL of today's posts together."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "posts": {
                    "type": "array",
                    "description": "All of today's posts in platform order.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "platform": {
                                "type": "string",
                                "enum": ["threads", "twitter", "facebook", "instagram", "linkedin"],
                                "description": "The platform this post is for.",
                            },
                            "content": {
                                "type": "string",
                                "description": "The full post text or caption.",
                            },
                            "note": {
                                "type": "string",
                                "description": (
                                    "Optional note for Leann, e.g. 'needs an image' for Instagram."
                                ),
                            },
                        },
                        "required": ["platform", "content"],
                    },
                }
            },
            "required": ["posts"],
        },
    },
    {
        "name": "send_newsletter_outline",
        "description": (
            "Save the weekly newsletter outline to the Notion page. "
            "Call this on Thursdays after saving the regular posts."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "outline": {
                    "type": "string",
                    "description": "The full newsletter outline.",
                }
            },
            "required": ["outline"],
        },
    },
    {
        "name": "draft_article",
        "description": (
            "Save a drafted blog article to content-agent/drafts/articles/ and email Leann "
            "a preview. Call this on Fridays after saving the regular social posts. "
            "Write a full 1,200–1,500 word article in Leann's voice. "
            "body_html should be the inner article content only — <p>, <h2>, <h3>, <ul>, "
            "<ol>, <blockquote>, <strong>, <a> tags. No outer <article> or <html> wrapper."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "slug": {
                    "type": "string",
                    "description": "URL-safe kebab-case slug, e.g. 'why-premium-clients-invest-in-design'.",
                },
                "title": {
                    "type": "string",
                    "description": "Full article title. Specific, promises a clear outcome.",
                },
                "category": {
                    "type": "string",
                    "description": "Display category for the article header, e.g. 'Web Design', 'Pricing & Positioning', 'AI & SEO'.",
                },
                "meta_description": {
                    "type": "string",
                    "description": "SEO meta description, 150–160 characters.",
                },
                "primary_keyword": {
                    "type": "string",
                    "description": "Main SEO keyword phrase.",
                },
                "body_html": {
                    "type": "string",
                    "description": "Full article body as HTML. ~1,200–1,500 words. Use <p>, <h2>, <h3>, <ul>, <ol>, <strong>, <a>. No <article> wrapper.",
                },
                "read_time": {
                    "type": "string",
                    "description": "Estimated read time, e.g. '6 min read'.",
                },
            },
            "required": ["slug", "title", "category", "meta_description", "primary_keyword", "body_html", "read_time"],
        },
    },
    {
        "name": "write_daily_log",
        "description": (
            "Write a session summary to the memory log. "
            "Include which article you used and what angles you took. "
            "Call this last."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "The log entry."}
            },
            "required": ["content"],
        },
    },
]


# ─────────────────────────────────────────────
# TOOL EXECUTOR
# ─────────────────────────────────────────────

def execute_tool(tool_name: str, tool_input: dict) -> str:
    print(f"  → {tool_name}({json.dumps(tool_input, ensure_ascii=False)[:120]})")

    if tool_name == "read_articles":
        articles = load_all_articles()
        return format_articles_for_prompt(articles)

    elif tool_name == "read_recent_memory":
        return read_recent_memory(days=7)

    elif tool_name == "save_drafts":
        posts = tool_input.get("posts", [])
        today = date.today()
        day_label = today.strftime("%A, %B %-d")

        if DRY_RUN:
            print(f"\n--- DRY RUN: posts for {day_label} ---")
            for p in posts:
                print(f"\n[{p['platform'].upper()}]")
                print(p["content"])
            print("--- end ---\n")
            return "[DRY RUN] Would have saved to weekly file and emailed Leann."

        # Write to weekly markdown file
        week_file = get_week_file_path()
        monday = today - timedelta(days=today.weekday())
        if not week_file.exists():
            week_file.write_text(week_file_header(monday))
        with week_file.open("a") as f:
            f.write(format_posts_as_markdown(day_label, posts))

        # Email today's drafts to Leann
        email_body = format_posts_for_email(day_label, posts)
        email_result = send_drafts_email(
            subject=f"Simple Rabbit — {day_label} content drafts",
            body=email_body,
        )
        email_status = (
            f"Email sent to {email_result['sent_to']}."
            if email_result["success"]
            else f"Email failed: {email_result['error']}"
        )

        return f"Saved {len(posts)} posts to {week_file.name}. {email_status}"

    elif tool_name == "send_newsletter_outline":
        outline = tool_input["outline"]
        if DRY_RUN:
            print(f"\n--- DRY RUN: newsletter outline ---\n{outline}\n---\n")
            return "[DRY RUN] Would have emailed newsletter outline."
        today = date.today()
        date_label = today.strftime("%B %-d, %Y")
        result = send_drafts_email(
            subject=f"Simple Rabbit — Newsletter outline for {date_label}",
            body=outline,
        )
        if result["success"]:
            return f"Newsletter outline emailed to {result['sent_to']}."
        return f"Email failed: {result['error']}"

    elif tool_name == "draft_article":
        slug            = tool_input["slug"]
        title           = tool_input["title"]
        category        = tool_input["category"]
        meta_description = tool_input["meta_description"]
        primary_keyword = tool_input["primary_keyword"]
        body_html       = tool_input["body_html"]
        read_time       = tool_input["read_time"]

        if DRY_RUN:
            print(f"\n--- DRY RUN: article draft ---")
            print(f"  Title:    {title}")
            print(f"  Slug:     {slug}")
            print(f"  Category: {category}")
            print(f"  Read time:{read_time}")
            print(f"  Body:     {body_html[:300]}...")
            print("--- end ---\n")
            return "[DRY RUN] Would have saved article draft and emailed Leann."

        # Save the draft HTML file
        draft_path = save_article_draft(
            slug=slug,
            title=title,
            category=category,
            meta_description=meta_description,
            primary_keyword=primary_keyword,
            body_html=body_html,
            read_time=read_time,
        )

        # Mark the pillar as used
        mark_pillar_used(category)

        # Clear the topic override (so next Friday rotates pillars again)
        clear_article_topic_override()

        # Email Leann a preview
        today_str = date.today().strftime("%B %-d, %Y")
        email_body = (
            f"Article draft ready — {today_str}\n"
            f"{'=' * 50}\n\n"
            f"TITLE\n-----\n{title}\n\n"
            f"CATEGORY\n--------\n{category}\n\n"
            f"META DESCRIPTION\n----------------\n{meta_description}\n\n"
            f"READ TIME\n---------\n{read_time}\n\n"
            f"DRAFT FILE\n----------\n{draft_path.name}\n\n"
            f"{'=' * 50}\n"
            f"To publish: run  python content-agent/article_approve.py\n"
            f"Note: a placeholder image is used until you add a featured image to previews/.\n"
        )
        email_result = send_drafts_email(
            subject=f"Simple Rabbit — Article draft ready: {title}",
            body=email_body,
        )
        email_status = (
            f"Email sent to {email_result['sent_to']}."
            if email_result["success"]
            else f"Email failed: {email_result['error']}"
        )

        return f"Article draft saved to {draft_path.name}. {email_status}"

    elif tool_name == "write_daily_log":
        if not DRY_RUN:
            write_daily_log(tool_input["content"])
        return "Memory log updated."

    return f"Unknown tool: {tool_name}"


# ─────────────────────────────────────────────
# SAGE SYSTEM PROMPT
# ─────────────────────────────────────────────

def build_system_prompt(platforms: list[str], today_str: str, article_topic: str = "", next_pillar: str = "") -> str:
    soul = (AGENT_DIR / "SOUL.md").read_text()
    identity = (AGENT_DIR / "IDENTITY.md").read_text()
    platform_list = ", ".join(p.upper() for p in platforms)
    is_thursday = date.today().weekday() == 3
    is_friday   = date.today().weekday() == 4

    thursday_section = """
## THURSDAY: NEWSLETTER OUTLINE

After saving the regular posts, generate a newsletter outline for Leann and email it
using send_newsletter_outline. It will arrive as a separate email in her inbox.

Leann writes the newsletter herself — your job is to give her a strong starting point.
Structure the outline like this:

---
NEWSLETTER OUTLINE — [date]
========================================

THEME: [One clear idea that ties the whole issue together]

OPENING HOOK
------------
Suggest an inspirational story, real person, historical moment, or surprising idea
that connects emotionally to the theme. 2–3 sentences describing the hook.
Note why it resonates for women business owners specifically.

SECTION 1: [Suggested heading]
------------------------------
Key idea: [the business insight]
Drawn from: [which article + the angle to use]
Prompt for Leann: [a question to help her add her own voice, e.g. "When did you first notice this with a client?"]

SECTION 2: [Suggested heading]
------------------------------
Key idea: ...
Drawn from: ...
Prompt for Leann: ...

SECTION 3: [Suggested heading — optional, only include if it adds something]
------------------------------
...

CLOSING
-------
Suggested wrap-up sentence or thought.
CTA: simplerabbit.studio/contact

WRITING PROMPTS
---------------
3–4 questions to help Leann find her voice and personal angle:
- [Question]
- [Question]
- [Question]
---

Keep it practical. Leann should be able to read this, pick the parts that resonate,
and start writing within a few minutes.
""" if is_thursday else ""

    thursday_task = """
7. Call send_newsletter_outline with the newsletter outline (Thursday only)""" if is_thursday else ""

    if is_friday:
        if article_topic:
            topic_instruction = f'Write about this specific topic Leann requested: "{article_topic}"'
        else:
            topic_instruction = f'Pick this content pillar (least used recently): **{next_pillar}**'

        friday_section = f"""

## FRIDAY: BLOG ARTICLE

After saving the regular social posts, write a full blog article and call `draft_article`.

**TOPIC:** {topic_instruction}

**ARTICLE GUIDELINES:**
- 1,200–1,500 words. Meaty and useful — not fluffy.
- Headline: specific, promises a clear outcome or insight. No clickbait.
- 3–5 H2 sections with real substance in each.
- Write in Leann's voice: confident, direct, warm, expert. No em-dashes.
- Include 2–3 external links to studies, data, or credible sources.
- Include 2–3 internal links: /contact, /portfolio, or other blog articles.
- End the article body (before the template CTA) with a clear takeaway paragraph.
- body_html: inner HTML only — <p>, <h2>, <h3>, <ul>, <ol>, <strong>, <a> tags.
  Do NOT wrap in <article>, <body>, or any outer tag.
- slug: lowercase kebab-case, SEO-friendly, no date prefix.
- category: short display label (e.g. "Web Design", "Pricing & Positioning", "AI & SEO").
- meta_description: 150–160 characters, includes primary keyword naturally.
- read_time: based on ~200 words per minute, format as "X min read"."""

        friday_task = "\n7. Call draft_article with the full blog article (Friday only)"
    else:
        friday_section = ""
        friday_task    = ""

    return f"""{soul}

{identity}

---

## TODAY

Today is {today_str}.
You are drafting content for: {platform_list}
{friday_section}
## PLATFORM GUIDELINES

**THREADS** (every day)
Conversational and direct. A take, a tip, or a short story. 2–4 short paragraphs.
Under 500 characters. No hashtags. Write like you're talking to a peer.

**X / TWITTER** (every day)
One sharp insight. Hard limit: 280 characters — stay well under it.
No jargon. One clean hashtag max if it genuinely adds something.

**FACEBOOK** (every day)
Warm and educational. 2–4 short paragraphs. End with a question or a link to the article.
Make the first line count.

**INSTAGRAM** (every day)
Visual-first. The first line is a scroll-stopping hook.
3–5 short paragraphs. Hashtags at the end: 10–15 that mix niche and specific tags.
Always include note: "needs an image" when saving this post.

**LINKEDIN** (Mon/Wed/Fri only)
Professional insight. 3–5 paragraphs, narrative or list format. No hashtags.
Write for business owners. End with a clear takeaway or question.
{thursday_section}
## YOUR TASK

1. Call read_articles to load the source material
2. Call read_recent_memory to see which articles and angles were used recently
3. Choose ONE primary article to anchor today's content — pick the one least used recently,
   or the angle that fits a content pillar you haven't covered lately
4. Write all posts for today — each one pulls a different angle from the same article.
   A stat for Twitter. A story for Facebook. A strong opinion for Threads.
   A practical tip for LinkedIn. A visual concept for Instagram.
5. Call save_drafts with all posts together (this saves the file and emails Leann)
6. Call write_daily_log with a brief summary: which article, what angles, what pillar{thursday_task}{friday_task}

Make it good. Give real value. This is Leann's voice.
"""


# ─────────────────────────────────────────────
# MAIN AGENT LOOP
# ─────────────────────────────────────────────

def run_sage():
    today = date.today()
    today_str = today.strftime("%A, %B %-d, %Y")
    platforms = todays_platforms()

    # Friday: load topic override + next pillar for the system prompt
    article_topic = get_article_topic_override() if today.weekday() == 4 else ""
    next_pillar   = get_next_pillar()            if today.weekday() == 4 else ""

    system_prompt = build_system_prompt(platforms, today_str, article_topic, next_pillar)
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    print(f"\n🌿 Sage — Content Session")
    print(f"   {today_str}")
    print(f"   Platforms today: {', '.join(platforms)}")
    if today.weekday() == 4:
        topic_display = article_topic if article_topic else f"[auto: {next_pillar}]"
        print(f"   Friday article topic: {topic_display}")
    if DRY_RUN:
        print("   [DRY RUN — nothing will be saved or emailed]\n")
    else:
        print()

    messages = [{"role": "user", "content": "Run today's content session."}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system_prompt,
            tools=SAGE_TOOLS,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(f"\n{block.text}")

        if response.stop_reason == "end_turn":
            print("\n✅ Sage done.\n")
            break

        elif response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result_text = execute_tool(block.name, block.input)
                    print(f"     ✓ {result_text[:120]}")
                    tool_results.append(
                        {
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": result_text,
                        }
                    )
            messages.append({"role": "user", "content": tool_results})

        else:
            print(f"Unexpected stop reason: {response.stop_reason}")
            break


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    run_sage()
