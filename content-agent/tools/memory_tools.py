"""
Memory management for the Simple Rabbit content agent.
Reads/writes daily logs, content queue, and pillar rotation tracking.
"""

import os
from datetime import date, timedelta
from pathlib import Path

MEMORY_DIR = Path(__file__).parent.parent / "memory"
PENDING_DIR = Path(__file__).parent.parent / "pending"

CONTENT_PILLARS = [
    "Pricing & positioning — why websites affect what clients pay",
    "AI & SEO visibility — how to get found in 2026",
    "Premium client attraction — filtering for the right clients",
    "Web design education — what makes a site actually work",
    "Behind the scenes — Simple Rabbit work, process, results",
    "Women in business — mindset, growth, charging what you're worth",
]


def get_todays_log_path() -> Path:
    return MEMORY_DIR / f"{date.today().isoformat()}.md"


def get_pending_path() -> Path:
    return PENDING_DIR / f"{date.today().isoformat()}.md"


def read_recent_memory(days: int = 3) -> str:
    """Read the last N days of memory logs. Returns combined text."""
    lines = []
    for i in range(days):
        day = date.today() - timedelta(days=i)
        path = MEMORY_DIR / f"{day.isoformat()}.md"
        if path.exists():
            lines.append(f"\n\n--- {day.isoformat()} ---\n")
            lines.append(path.read_text())
    return "".join(lines) if lines else "No recent memory found."


def get_todays_pillar() -> str:
    """
    Rotate through the 6 content pillars based on day-of-year.
    Ensures variety without tracking state.
    """
    day_number = date.today().timetuple().tm_yday
    pillar = CONTENT_PILLARS[day_number % len(CONTENT_PILLARS)]
    return pillar


def write_daily_log(content: str) -> None:
    """Write or append to today's memory log."""
    path = get_todays_log_path()
    MEMORY_DIR.mkdir(exist_ok=True)
    if path.exists():
        existing = path.read_text()
        path.write_text(existing + "\n" + content)
    else:
        path.write_text(f"# {date.today().isoformat()} Content Log\n\n" + content)


def save_pending_post(platform: str, content: str, note: str = "") -> None:
    """Save a post to today's pending approval file."""
    path = get_pending_path()
    PENDING_DIR.mkdir(exist_ok=True)

    separator = "\n---\n"
    entry = f"\n## {platform.upper()}\n\n{content}\n"
    if note:
        entry += f"\n_Note: {note}_\n"

    if path.exists():
        path.write_text(path.read_text() + separator + entry)
    else:
        path.write_text(f"# Pending Approval — {date.today().isoformat()}\n" + entry)


def read_pending_posts() -> str:
    """Read today's pending posts file."""
    path = get_pending_path()
    if not path.exists():
        return ""
    return path.read_text()


def mark_pending_as_posted(platform: str) -> None:
    """
    Update today's pending file to mark a platform as posted.
    Appends a posted marker — does not delete the original entry.
    """
    path = get_pending_path()
    if not path.exists():
        return
    content = path.read_text()
    marker = f"\n✅ {platform.upper()} — POSTED\n"
    path.write_text(content + marker)


def read_brand_context() -> str:
    """Read all brand context files and return combined text."""
    base = Path(__file__).parent.parent
    files = ["SOUL.md", "IDENTITY.md", "AGENTS.md"]
    parts = []
    for filename in files:
        filepath = base / filename
        if filepath.exists():
            parts.append(f"\n\n=== {filename} ===\n\n{filepath.read_text()}")
    return "".join(parts)
