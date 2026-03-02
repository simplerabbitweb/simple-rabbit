#!/usr/bin/env python3
"""
Simple Rabbit Content Agent — Sage
Daily content generation and auto-posting agent using Claude Agent SDK.

Runs at 7am daily via launchd. Generates all platform content,
auto-posts to Threads and X, queues Instagram/Facebook/LinkedIn for approval,
and emails Leann the pending drafts.

Usage:
    python agent.py
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

import anthropic
from dotenv import load_dotenv

# ── local tools ──────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from tools.social import (
    post_to_facebook,
    post_to_instagram,
    post_to_linkedin,
    post_to_threads,
    post_to_twitter,
)
from tools.memory_tools import (
    get_todays_pillar,
    read_brand_context,
    read_recent_memory,
    save_pending_post,
    write_daily_log,
)
from tools.email_notify import send_approval_email

load_dotenv()

# ─────────────────────────────────────────────
# TOOL DEFINITIONS (Claude sees these)
# ─────────────────────────────────────────────

TOOLS = [
    {
        "name": "post_to_twitter",
        "description": (
            "Post content to X/Twitter immediately. "
            "Use this for the daily X post. Max 280 characters."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The tweet text. Must be 280 characters or fewer.",
                }
            },
            "required": ["content"],
        },
    },
    {
        "name": "post_to_threads",
        "description": (
            "Post content to Threads immediately. "
            "Use this for the daily Threads post. Max 500 characters."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "The Threads post text. Max 500 characters.",
                }
            },
            "required": ["content"],
        },
    },
    {
        "name": "queue_for_approval",
        "description": (
            "Save a post to the pending approval queue. "
            "Use this for Instagram, Facebook, and LinkedIn posts — "
            "Leann must approve these before they go live."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "platform": {
                    "type": "string",
                    "enum": ["instagram", "facebook", "linkedin"],
                    "description": "Which platform this post is for.",
                },
                "content": {
                    "type": "string",
                    "description": "The full post content/caption.",
                },
                "note": {
                    "type": "string",
                    "description": (
                        "Optional note for Leann (e.g., 'Instagram needs an image — "
                        "suggest a photo of your desk or workspace')."
                    ),
                },
            },
            "required": ["platform", "content"],
        },
    },
    {
        "name": "send_approval_email",
        "description": (
            "Send Leann the daily approval email with all pending posts. "
            "Call this AFTER all posts have been generated and queued. "
            "Pass a short summary of what was auto-posted today."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "auto_posted_summary": {
                    "type": "string",
                    "description": (
                        "Brief summary of what was auto-posted today "
                        "(e.g., 'X: posted ✅ | Threads: posted ✅')."
                    ),
                }
            },
            "required": ["auto_posted_summary"],
        },
    },
    {
        "name": "log_to_memory",
        "description": (
            "Write a note to today's memory log. "
            "Use this to record what was created, posted, or any observations. "
            "Call at the end of the session."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "content": {
                    "type": "string",
                    "description": "What to record in today's memory log.",
                }
            },
            "required": ["content"],
        },
    },
]


# ─────────────────────────────────────────────
# TOOL EXECUTOR
# ─────────────────────────────────────────────

def execute_tool(tool_name: str, tool_input: dict) -> str:
    """Execute a tool call and return a string result."""
    print(f"  → Tool: {tool_name}({json.dumps(tool_input, ensure_ascii=False)[:120]})")

    if tool_name == "post_to_twitter":
        result = post_to_twitter(tool_input["content"])
        if result["success"]:
            return f"Posted to Twitter successfully. Tweet ID: {result['id']}"
        return f"Twitter post failed: {result['error']}"

    elif tool_name == "post_to_threads":
        result = post_to_threads(tool_input["content"])
        if result["success"]:
            return f"Posted to Threads successfully. Post ID: {result['id']}"
        return f"Threads post failed: {result['error']}"

    elif tool_name == "queue_for_approval":
        platform = tool_input["platform"]
        content = tool_input["content"]
        note = tool_input.get("note", "")
        save_pending_post(platform, content, note)
        return f"Saved {platform} post to pending approval queue."

    elif tool_name == "send_approval_email":
        from tools.memory_tools import read_pending_posts
        pending = read_pending_posts()
        result = send_approval_email(
            pending_content=pending,
            auto_posted_summary=tool_input.get("auto_posted_summary", ""),
        )
        if result["success"]:
            return f"Approval email sent to {result['sent_to']}."
        return f"Email failed: {result['error']}"

    elif tool_name == "log_to_memory":
        write_daily_log(tool_input["content"])
        return "Memory log updated."

    return f"Unknown tool: {tool_name}"


# ─────────────────────────────────────────────
# MAIN AGENT LOOP
# ─────────────────────────────────────────────

def run_agent():
    today = date.today().strftime("%A, %B %-d, %Y")
    pillar = get_todays_pillar()
    brand_context = read_brand_context()
    recent_memory = read_recent_memory(days=3)

    system_prompt = f"""You are Sage, the content creator for Simple Rabbit — a premium web design studio for women-owned service businesses, founded by Leann Frank in Bergen County, NJ.

You have all the brand knowledge you need below. Your job right now is to write today's social media content and use your tools to distribute it.

{brand_context}

───────────────
TODAY'S SESSION
───────────────
Date: {today}
Today's content pillar: {pillar}

Recent memory (what's been posted):
{recent_memory}

───────────────
YOUR TASK TODAY
───────────────
Generate and distribute content for ALL platforms listed below. Use the tools available to you.

AUTO-POST (do these immediately using your tools):
- X/Twitter: 1 post — max 280 chars. Sharp, punchy, quotable. No hashtags.
- Threads: 1 post — up to 500 chars. Can be slightly longer/conversational.

QUEUE FOR APPROVAL (save these using queue_for_approval tool):
- Instagram: 1 caption — image caption style. Leann will add the image. Include a note suggesting a photo idea.
- Facebook (business page): 1 post — informative and warm. Can be longer than X.
- LinkedIn: 1 post — professional but human. Thought leadership angle.

THEN:
- Send the approval email using send_approval_email tool.
- Log what you did to memory using log_to_memory tool.

WRITING RULES (non-negotiable):
- No em-dashes (—). Ever.
- No "It's not X, it's Y" constructions.
- Vary sentence length. No staccato robots.
- Specific over generic. Real over theoretical.
- Sound like a confident, smart human. Not a content tool.
- CTA always links to simplerabbit.studio/contact when including a CTA.
- No corporate filler: no "leverage," "robust," "comprehensive solutions."

Go. Write great content, use your tools, get it done."""

    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    messages = [
        {
            "role": "user",
            "content": "Run today's content session. Generate all posts and distribute them.",
        }
    ]

    print(f"\n🐇 Sage is running — {today}")
    print(f"   Pillar: {pillar}\n")

    # Agentic loop — runs until Claude stops calling tools
    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8096,
            system=system_prompt,
            tools=TOOLS,
            messages=messages,
        )

        # Add assistant response to message history
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            # Claude is done
            final_text = " ".join(
                block.text for block in response.content if hasattr(block, "text")
            )
            if final_text:
                print(f"\nSage: {final_text}")
            print("\n✅ Session complete.")
            break

        elif response.stop_reason == "tool_use":
            # Process all tool calls in this response
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


if __name__ == "__main__":
    run_agent()
