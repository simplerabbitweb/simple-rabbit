# Blog Automation SOP — Simple Rabbit

## How It Works

Every **Thursday at 5:00 AM**, the system automatically:
1. Picks the next unpublished post from `blog-queue.json`
2. Writes the full article using Claude (Anthropic API)
3. Fetches a featured image from Unsplash
4. Builds the HTML file, updates `articles.html` and `sitemap.xml`
5. Deploys everything live to simplerabbit.studio

No action needed from you — it runs while you sleep.

---

## Key Files

| File | What It Does |
|------|-------------|
| `blog-queue.json` | The master list of post titles, slugs, and categories |
| `auto-blog.py` | The script that generates and publishes each post |
| `post.py` | Manual version — publish a one-off post on demand |
| `auto-blog.log` | Log of every run — check here if something looks off |
| `.blog-config.json` | API keys (Anthropic + Unsplash) — don't share or commit |
| `~/Library/LaunchAgents/studio.simplerabbit.autoblog.plist` | macOS scheduler — controls when the agent runs |

---

## Reviewing & Editing the Queue

Open `blog-queue.json` in any text editor (Cursor, VS Code, TextEdit).

Each entry looks like:
```json
{
  "id": 7,
  "title": "Your Post Title Here",
  "slug": "your-post-title-here",
  "category": "Local SEO",
  "published": false
}
```

**Rules:**
- `title` — what you want the post to be called (Claude will write to this)
- `slug` — becomes the URL: `simplerabbit.studio/blog/[slug]` — lowercase, hyphens only, no special characters
- `category` — shows as the label on the card. Current options: `Local SEO`, `Web Design`, `Strategy`, `Practice Building`, `Women's Wellness`, `Case Study`
- `published` — leave as `false`; the script flips it to `true` after publishing
- Posts publish **in order** — reorder entries to change what goes next

**Or:** paste updated titles into Claude and ask it to update the file.

---

## Adding New Titles to the Queue

Open `blog-queue.json` and add entries at the bottom before the closing `]`. Give each a unique `id` (increment from the last one) and set `"published": false`.

---

## Turning the Agent On/Off

**Stop it (pause auto-publishing):**
```bash
launchctl unload ~/Library/LaunchAgents/studio.simplerabbit.autoblog.plist
```

**Start it again:**
```bash
launchctl load ~/Library/LaunchAgents/studio.simplerabbit.autoblog.plist
```

Or just ask Claude: *"pause the auto-blog agent"* / *"turn the auto-blog agent back on"*

---

## Publishing a Post Manually (On Demand)

```bash
cd "/Users/leannfrank/simple rabbit"
python3 post.py "Your Post Title" "A short description of what the post covers"
```

Optional category flag:
```bash
python3 post.py "Title" "Description" --category "Local SEO"
```

---

## Checking the Log

```bash
tail -50 "/Users/leannfrank/simple rabbit/auto-blog.log"
```

Or open `auto-blog.log` in any text editor. Each run is timestamped and shows what was generated, fetched, and deployed.

---

## Important Notes

- **The queue drives everything.** Bad title = AI writes to it literally. Keep titles specific and on-brand.
- **Slugs must be unique.** If a slug already exists as a file, the post will overwrite it.
- **The ACRR checklist section is NOT auto-added by the agent** — posts published by `auto-blog.py` need the ACRR placeholder manually added after the fact, or the agent script needs to be updated to include it. (Ask Claude to add it after each auto-publish, or update `auto-blog.py` to inject it.)
- **Review posts after they go live.** The AI writes solid drafts but you should check each one for tone, accuracy, and alignment with the messaging map.
- **API costs:** Each post uses ~$0.10–0.30 in Anthropic API credits and 1 Unsplash API call (free tier).
