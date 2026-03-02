# Simple Rabbit Content Agent — Setup Guide

Sage runs daily, writes all your social content, auto-posts to Threads and X, and emails you the Instagram/Facebook/LinkedIn drafts for approval.

---

## 1. Install Python Dependencies

```bash
cd ~/Desktop/simple\ rabbit/content-agent
pip3 install -r requirements.txt
```

---

## 2. Set Up Your API Keys

```bash
cp .env.example .env
```

Open `.env` and fill in every key. Here's where to get each one:

### Anthropic (Claude)
- Go to https://console.anthropic.com/keys
- Create an API key
- Paste it as `ANTHROPIC_API_KEY`

### Twitter / X
- Go to https://developer.twitter.com/en/portal/dashboard
- Create a project + app with **Read and Write** permissions
- Generate Access Token & Secret (for your own account)
- Fill in all 4 `TWITTER_*` values

### Meta (Instagram, Facebook, Threads)
All three use the same Meta access token.
- Go to https://developers.facebook.com/tools/explorer/
- Select your app, grant: `pages_manage_posts`, `instagram_basic`, `instagram_content_publish`, `threads_content_publish`
- Generate a long-lived token (lasts 60 days — you'll need to refresh it periodically)
- Fill in: `META_ACCESS_TOKEN`, `INSTAGRAM_USER_ID`, `FACEBOOK_PAGE_ID`, `FACEBOOK_PAGE_ACCESS_TOKEN`, `THREADS_USER_ID`

**To find your IDs:**
```
# Facebook Page ID
https://graph.facebook.com/me/accounts?access_token=YOUR_TOKEN

# Instagram User ID (must be a Business/Creator account connected to your Facebook Page)
https://graph.facebook.com/v20.0/me?fields=instagram_business_account&access_token=YOUR_TOKEN
```

### LinkedIn
- Go to https://www.linkedin.com/developers/apps
- Create an app, request `w_member_social` permission
- Complete OAuth flow to get your access token (lasts 60 days)
- Fill in `LINKEDIN_ACCESS_TOKEN` and `LINKEDIN_PERSON_URN`
  - Your URN looks like: `urn:li:person:XXXXXXXX`
  - Find it at: https://api.linkedin.com/v2/me (with your token)

### Email (Approval Notifications)
- Using Gmail: create an App Password at https://myaccount.google.com/apppasswords
- Fill in `SMTP_USER` (your Gmail), `SMTP_PASSWORD` (the App Password), `APPROVAL_EMAIL`

---

## 3. Test It Manually

Run the agent once manually to verify everything works:

```bash
cd ~/Desktop/simple\ rabbit/content-agent
python3 agent.py
```

Watch the terminal. It should:
1. Generate content for all platforms
2. Post to Twitter and Threads immediately
3. Save Instagram/Facebook/LinkedIn to `pending/YYYY-MM-DD.md`
4. Email you the drafts

---

## 4. Approve and Post Pending Content

After you get the email and review the drafts:

```bash
cd ~/Desktop/simple\ rabbit/content-agent
python3 approve.py
```

It walks you through each post. Press A to approve (posts immediately), S to skip, Q to quit.

For Instagram, you'll be prompted to paste a public image URL.

---

## 5. Schedule Daily Runs (macOS)

```bash
# Copy the plist to LaunchAgents
cp scheduler/com.simplerabbit.agent.plist ~/Library/LaunchAgents/

# Load it (starts the schedule)
launchctl load ~/Library/LaunchAgents/com.simplerabbit.agent.plist
```

Sage will now run every morning at 7:00 AM automatically.

**To check logs:**
```bash
tail -f /tmp/simplerabbit-agent.log
tail -f /tmp/simplerabbit-agent-error.log
```

**To stop the schedule:**
```bash
launchctl unload ~/Library/LaunchAgents/com.simplerabbit.agent.plist
```

---

## 6. Instagram Note

Instagram requires an image for every post. When you run `approve.py`, you'll be prompted to enter a public image URL (e.g., hosted on your website or a Dropbox public link). Sage will suggest a photo concept in the post note — use that as your guide.

---

## File Structure

```
content-agent/
├── agent.py          ← main agent (runs daily)
├── approve.py        ← you run this to approve + post
├── requirements.txt
├── .env              ← your API keys (never commit this)
├── .env.example      ← template
├── SOUL.md           ← Sage's brand rules
├── IDENTITY.md       ← who Sage is
├── AGENTS.md         ← session instructions
├── tools/
│   ├── social.py     ← Twitter, Threads, Instagram, Facebook, LinkedIn APIs
│   ├── memory_tools.py
│   └── email_notify.py
├── memory/           ← daily logs of what was created/posted
├── pending/          ← posts waiting for your approval
└── scheduler/
    └── com.simplerabbit.agent.plist  ← macOS scheduler
```

---

## Refreshing Tokens

Meta and LinkedIn tokens expire after 60 days. Set a calendar reminder to refresh them.

**Meta:** Use the Graph API Explorer to generate a new long-lived token.
**LinkedIn:** Go through the OAuth flow again in your app dashboard.
