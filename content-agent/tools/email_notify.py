"""
Email notification for Simple Rabbit content agent.
Sends daily approval emails with pending post drafts.
Uses Gmail SMTP (or any SMTP provider).
"""

import os
import smtplib
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def send_approval_email(pending_content: str, auto_posted_summary: str = "") -> dict:
    """
    Send Leann the daily approval email with pending post drafts.

    Args:
        pending_content: The raw text of pending posts (from pending/YYYY-MM-DD.md)
        auto_posted_summary: Summary of what was already auto-posted today

    Returns:
        dict with success/error status
    """
    try:
        smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_user = os.getenv("SMTP_USER")
        smtp_password = os.getenv("SMTP_PASSWORD")
        to_email = os.getenv("APPROVAL_EMAIL")
        today = date.today().strftime("%A, %B %-d")

        subject = f"Simple Rabbit — Content for Approval ({today})"

        # Build plain text body
        body_parts = [
            f"Hi Leann,\n\nHere's your content for today ({today}).\n",
        ]

        if auto_posted_summary:
            body_parts.append(
                "\n────────────────────────────\n"
                "ALREADY POSTED (no action needed)\n"
                "────────────────────────────\n"
                f"{auto_posted_summary}\n"
            )

        body_parts.append(
            "\n────────────────────────────\n"
            "NEEDS YOUR APPROVAL\n"
            "────────────────────────────\n"
            "Review the posts below. When you're ready to approve them, "
            "open Terminal and run:\n\n"
            "    cd ~/Desktop/simple\\ rabbit/content-agent\n"
            "    python approve.py\n\n"
            "That will walk you through each post and post the approved ones.\n"
        )

        body_parts.append(
            "\n────────────────────────────\n"
            "PENDING POSTS\n"
            "────────────────────────────\n"
        )
        body_parts.append(pending_content)

        body_parts.append(
            "\n\n────────────────────────────\n"
            "— Sage, your Simple Rabbit content agent 🐇\n"
        )

        body = "".join(body_parts)

        # Build HTML version for better readability
        html_body = body.replace("\n", "<br>").replace(
            "────────────────────────────",
            "<hr style='border:1px solid #eee;'>",
        )
        html_body = f"<html><body style='font-family:Georgia,serif;max-width:600px;margin:auto;padding:20px;color:#222;'>{html_body}</body></html>"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = smtp_user
        msg["To"] = to_email
        msg.attach(MIMEText(body, "plain"))
        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, to_email, msg.as_string())

        return {"success": True, "sent_to": to_email}
    except Exception as e:
        return {"success": False, "error": str(e)}
