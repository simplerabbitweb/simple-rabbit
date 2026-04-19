#!/usr/bin/env python3
"""
Simple Rabbit Operations Agent — Leo
Handles posting approved content and weekly strategy reviews.

Usage:
    python agent.py           # approve mode (review + post today's pending content)
    python agent.py --weekly  # weekly review mode (runs Sundays)
    python agent.py --status  # quick status check on today's posts
"""

import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# ── shared tools (live in content-agent) ─────
CONTENT_AGENT_DIR = Path(__file__).parent.parent / "content-agent"
sys.path.insert(0, str(CONTENT_AGENT_DIR))

from tools.social import post_to_facebook, post_to_instagram, post_to_linkedin
from tools.memory_tools import (
    read_recent_memory,
    write_daily_log,
    read_pending_posts,
    mark_pending_as_posted,
)
from tools.email_notify import send_approval_email

load_dotenv(CONTENT_AGENT_DIR / ".env")

# ─────────────────────────────────────────────
# TOOL DEFINITIONS
# ─────────────────────────────────────────────

APPROVE_TOOLS = [
    {
        "name": "read_pending_posts",
        "description": (
            "Read today's pending posts that Sage queued for approval. "
            "Call this at the start of every approve session."
        ),
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "post_to_instagram",
        "description": (
            "Post an approved caption to Instagram. "
            "Requires a public image URL — ask Leann for it before calling this. "
            "Only call after explicit approval."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "caption": {"type": "string", "description": "The Instagram caption to post."},
                "image_url": {
                    "type": "string",
                    "description": "A publicly accessible URL to the image (JPG or PNG).",
                },
            },
            "required": ["caption", "image_url"],
        },
    },
    {
        "name": "post_to_facebook",
        "description": "Post an approved post to the Simple Rabbit Facebook business page. Only call after explicit approval.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "The Facebook post text."}
            },
            "required": ["content"],
        },
    },
    {
        "name": "post_to_linkedin",
        "description": "Post an approved post to LinkedIn. Only call after explicit approval.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "The LinkedIn post text."}
            },
            "required": ["content"],
        },
    },
    {
        "name": "mark_as_posted",
        "description": "Mark a platform as posted in today's pending file. Call immediately after a successful post.",
        "input_schema": {
            "type": "object",
            "properties": {
                "platform": {
                    "type": "string",
                    "enum": ["instagram", "facebook", "linkedin"],
                }
            },
            "required": ["platform"],
        },
    },
    {
        "name": "log_to_memory",
        "description": "Write a note to today's memory log. Call at the end of the session to record what happened.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string", "description": "What to record in the memory log."}
            },
            "required": ["content"],
        },
    },
]

WEEKLY_TOOLS = [
    {
        "name": "read_weekly_memory",
        "description": "Read the last 7 days of memory logs to prepare the weekly review.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "send_weekly_recap",
        "description": "Email Leann the weekly strategy recap.",
        "input_schema": {
            "type": "object",
            "properties": {
                "recap": {
                    "type": "string",
                    "description": "The full weekly recap text to email Leann.",
                }
            },
            "required": ["recap"],
        },
    },
    {
        "name": "log_to_memory",
        "description": "Write the weekly review summary to today's memory log.",
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {"type": "string"}
            },
            "required": ["content"],
        },
    },
]

STATUS_TOOLS = [
    {
        "name": "read_pending_posts",
        "description": "Read today's pending posts to check status.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
    {
        "name": "read_today_memory",
        "description": "Read today's memory log to see what's been posted.",
        "input_schema": {"type": "object", "properties": {}, "required": []},
    },
]


# ─────────────────────────────────────────────
# TOOL EXECUTOR
# ─────────────────────────────────────────────

def execute_tool(tool_name: str, tool_input: dict) -> str:
    print(f"  → {tool_name}({json.dumps(tool_input, ensure_ascii=False)[:100]})")

    if tool_name == "read_pending_posts":
        content = read_pending_posts()
        return content if content else "No pending posts found for today."

    elif tool_name == "post_to_instagram":
        result = post_to_instagram(tool_input["caption"], tool_input["image_url"])
        if result["success"]:
            return f"Posted to Instagram. ID: {result['id']}"
        return f"Instagram post failed: {result['error']}"

    elif tool_name == "post_to_facebook":
        result = post_to_facebook(tool_input["content"])
        if result["success"]:
            return f"Posted to Facebook. ID: {result['id']}"
        return f"Facebook post failed: {result['error']}"

    elif tool_name == "post_to_linkedin":
        result = post_to_linkedin(tool_input["content"])
        if result["success"]:
            return f"Posted to LinkedIn. ID: {result['id']}"
        return f"LinkedIn post failed: {result['error']}"

    elif tool_name == "mark_as_posted":
        mark_pending_as_posted(tool_input["platform"])
        return f"Marked {tool_input['platform']} as posted."

    elif tool_name == "log_to_memory":
        write_daily_log(tool_input["content"])
        return "Memory log updated."

    elif tool_name == "read_weekly_memory":
        return read_recent_memory(days=7)

    elif tool_name == "read_today_memory":
        from tools.memory_tools import get_todays_log_path
        path = get_todays_log_path()
        return path.read_text() if path.exists() else "No memory log for today yet."

    elif tool_name == "send_weekly_recap":
        recap = tool_input["recap"]
        today = date.today().strftime("%A, %B %-d")
        result = send_approval_email(
            pending_content=recap,
            auto_posted_summary=f"Weekly strategy recap — {today}",
        )
        if result["success"]:
            return f"Weekly recap emailed to {result['sent_to']}."
        return f"Email failed: {result['error']}"

    return f"Unknown tool: {tool_name}"


# ─────────────────────────────────────────────
# AGENT RUNNERS
# ─────────────────────────────────────────────

def read_leo_context() -> str:
    soul = (Path(__file__).parent / "SOUL.md").read_text()
    identity = (Path(__file__).parent / "IDENTITY.md").read_text()
    agents = (Path(__file__).parent / "AGENTS.md").read_text()
    return f"{soul}\n\n{identity}\n\n{agents}"


def run_approve_mode():
    today = date.today().strftime("%A, %B %-d, %Y")
    recent = read_recent_memory(days=2)
    context = read_leo_context()

    system_prompt = f"""You are Leo, operations agent for Simple Rabbit.

{context}

Today is {today}.

Recent memory:
{recent}

YOUR TASK:
Run an approval session. Use your tools to:
1. Read today's pending posts (from Sage)
2. Present each post to Leann — show the platform and content clearly
3. Ask for her decision on each one
4. Post the approved ones immediately using the appropriate tool
5. For Instagram, ask for the image URL before posting
6. After all posts are handled, log a summary to memory

Be direct. Show the content, ask for a decision, act on it. Don't pad your messages."""

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    messages = [{"role": "user", "content": "Run today's approval session."}]

    print(f"\n🦁 Leo — Approval Session")
    print(f"   {today}\n")

    _run_loop(client, system_prompt, APPROVE_TOOLS, messages)


def run_weekly_mode():
    today = date.today().strftime("%A, %B %-d, %Y")
    context = read_leo_context()

    system_prompt = f"""You are Leo, operations agent for Simple Rabbit.

{context}

Today is {today} (Sunday — weekly review day).

YOUR TASK:
Run the weekly strategy review. Use your tools to:
1. Read the last 7 days of memory logs
2. Summarize what was posted across all platforms
3. Note which content pillars were covered and which were missed
4. Identify any gaps (days with no posts, platforms that went dark)
5. Write a brief, practical strategy note for next week
6. Email the recap to Leann using send_weekly_recap
7. Log a summary to memory

Keep it concise. Leann doesn't need a dissertation — she needs a clear picture of the week and one or two actionable notes for next week."""

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    messages = [{"role": "user", "content": "Run the weekly strategy review."}]

    print(f"\n🦁 Leo — Weekly Review")
    print(f"   {today}\n")

    _run_loop(client, system_prompt, WEEKLY_TOOLS, messages)


def run_status_mode():
    today = date.today().strftime("%A, %B %-d, %Y")
    context = read_leo_context()

    system_prompt = f"""You are Leo, operations agent for Simple Rabbit.

{context}

Today is {today}.

YOUR TASK:
Give a quick status check. Read the pending posts and today's memory log, then summarize:
- What Sage queued today
- What's been posted so far
- What's still pending
Keep it short — this is a status check, not a full session."""

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    messages = [{"role": "user", "content": "What's the status today?"}]

    print(f"\n🦁 Leo — Status Check")
    print(f"   {today}\n")

    _run_loop(client, system_prompt, STATUS_TOOLS, messages)


def _run_loop(client, system_prompt, tools, messages):
    """Core agentic loop — runs until Claude stops calling tools."""
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        # Print any text Claude outputs (these are Leo talking to Leann)
        for block in response.content:
            if hasattr(block, "text") and block.text:
                print(f"\n{block.text}")

        if response.stop_reason == "end_turn":
            print("\n✅ Done.\n")
            break

        elif response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    result_text = execute_tool(block.name, block.input)
                    print(f"     ✓ {result_text}")
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
    mode = sys.argv[1] if len(sys.argv) > 1 else "--approve"

    if mode == "--weekly":
        run_weekly_mode()
    elif mode == "--status":
        run_status_mode()
    else:
        run_approve_mode()
