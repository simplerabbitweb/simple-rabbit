"""
Memory and state management tools for Simple Rabbit agents.
Used by both Sage (content-agent) and Leo (ops-agent).
"""

import json
from datetime import date, datetime, timedelta
from pathlib import Path

# Memory lives inside content-agent/memory/
CONTENT_AGENT_DIR = Path(__file__).parent.parent
MEMORY_DIR = CONTENT_AGENT_DIR / "memory"
PENDING_DIR = MEMORY_DIR / "pending"
LOGS_DIR = MEMORY_DIR / "logs"


# ─────────────────────────────────────────────
# DAILY LOGS
# ─────────────────────────────────────────────

def get_todays_log_path() -> Path:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    return LOGS_DIR / f"{date.today().isoformat()}.md"


def write_daily_log(content: str) -> None:
    """Append a timestamped entry to today's memory log."""
    path = get_todays_log_path()
    timestamp = datetime.now().strftime("%H:%M")
    with path.open("a") as f:
        f.write(f"\n---\n{timestamp} — {content}\n")


def read_recent_memory(days: int = 7) -> str:
    """Read the last N days of memory logs and return as a single string."""
    parts = []
    for i in range(days):
        d = date.today() - timedelta(days=i)
        log_path = LOGS_DIR / f"{d.isoformat()}.md"
        if log_path.exists():
            label = d.strftime("%A, %B %-d")
            parts.append(f"=== {label} ===\n{log_path.read_text().strip()}")
    return "\n\n".join(parts) if parts else "No recent memory found."


# ─────────────────────────────────────────────
# PENDING POSTS
# ─────────────────────────────────────────────

def get_todays_pending_path() -> Path:
    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    return PENDING_DIR / f"{date.today().isoformat()}.json"


def write_pending_posts(posts: list) -> None:
    """Write (overwrite) today's pending posts file."""
    path = get_todays_pending_path()
    data = {
        "date": date.today().isoformat(),
        "posts": posts,
    }
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def read_pending_posts() -> str:
    """Read today's pending posts and return as formatted text."""
    path = get_todays_pending_path()
    if not path.exists():
        return ""

    data = json.loads(path.read_text())
    lines = [f"Pending posts for {data['date']}:\n"]
    for i, post in enumerate(data.get("posts", []), 1):
        status = post.get("status", "pending")
        platform = post.get("platform", "").upper()
        content = post.get("content", "")
        needs_image = " [NEEDS IMAGE URL]" if post.get("needs_image") else ""
        lines.append(f"{i}. {platform} [{status}]{needs_image}\n{content}\n")

    return "\n".join(lines)


def add_pending_post(post: dict) -> None:
    """Add a single post to today's pending file (creates it if needed)."""
    path = get_todays_pending_path()
    if path.exists():
        data = json.loads(path.read_text())
    else:
        data = {"date": date.today().isoformat(), "posts": []}

    post.setdefault("status", "pending")
    post.setdefault("created_at", datetime.now().isoformat())
    data["posts"].append(post)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))


def mark_pending_as_posted(platform: str) -> None:
    """Mark the first pending post for a platform as 'posted'."""
    path = get_todays_pending_path()
    if not path.exists():
        return

    data = json.loads(path.read_text())
    for post in data.get("posts", []):
        if post.get("platform") == platform and post.get("status") == "pending":
            post["status"] = "posted"
            break

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
