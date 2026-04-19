"""
Email tools for Simple Rabbit agents.
Uses Gmail SMTP with an App Password.
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_drafts_email(subject: str, body: str) -> dict:
    """
    Email today's content drafts to Leann.
    Plain text, formatted for easy copy/paste.
    """
    gmail = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_APP_PASSWORD")
    notify = os.getenv("NOTIFY_EMAIL", gmail)

    if not gmail or not password:
        return {"success": False, "error": "GMAIL_ADDRESS or GMAIL_APP_PASSWORD not set."}

    # Strip spaces/non-breaking spaces (Google's app passwords copy with them)
    password = password.replace("\xa0", "").replace(" ", "")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = gmail
    msg["To"] = notify
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail, password)
            server.sendmail(gmail, notify, msg.as_string())
        return {"success": True, "sent_to": notify}
    except Exception as e:
        return {"success": False, "error": str(e)}


# Keep this for backward compatibility with ops-agent
def send_approval_email(pending_content: str, auto_posted_summary: str = "") -> dict:
    return send_drafts_email(
        subject="Simple Rabbit — Content Ready for Approval",
        body=pending_content,
    )
