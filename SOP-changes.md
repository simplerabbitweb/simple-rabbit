# SOP: Making Changes to the Website

Use this any time you need to update copy, add a blog post, swap an image, or make any other change to the live site.

---

## The Basic Workflow

**Edit → Preview → Deploy**

That's it. Every change follows this same three-step process.

---

## Step 1 — Make the Change

**Option A — Use Claude Code (recommended)**

Open Terminal, navigate to the project, and start Claude:

```bash
cd "/Users/leannfrank/Desktop/simple rabbit"
claude
```

Then just describe what you want:
- *"Change the homepage headline to..."*
- *"Add a new blog post about..."*
- *"Update the portfolio to add a new client..."*
- *"Fix the typo on the about page..."*

Claude will edit the files directly.

**Option B — Edit manually**

Open the file in any text editor (VS Code recommended) and make your changes directly.

Key files:
| Page | File |
|------|------|
| Homepage | `index.html` |
| About | `about.html` |
| Portfolio | `portfolio.html` |
| Articles listing | `articles.html` |
| Contact | `contact.html` |
| Thank You | `thank-you.html` |
| 404 | `404.html` |
| Blog posts | `blog/[slug].html` |

---

## Step 2 — Preview Locally

Before pushing live, always preview your changes:

```bash
python3 -m http.server 3456 --directory "/Users/leannfrank/Desktop/simple rabbit"
```

Open `localhost:3456` in your browser. Refresh after any edit.

Stop the server when done: `Ctrl + C`

---

## Step 3 — Deploy Live

When you're happy with the change:

```bash
cd "/Users/leannfrank/Desktop/simple rabbit"
./deploy.sh "brief description of what changed"
```

Examples:
```bash
./deploy.sh "Update homepage headline"
./deploy.sh "Add new blog post - DIY websites"
./deploy.sh "Add Revive and Bloom to portfolio"
```

This will:
1. Upload changed files to SiteGround (live within seconds)
2. Commit + push to GitHub (backed up)

---

## Adding a New Blog Post

1. Copy an existing post as a starting point:
```bash
cp "/Users/leannfrank/Desktop/simple rabbit/blog/bergen-county-web-design.html" \
   "/Users/leannfrank/Desktop/simple rabbit/blog/your-new-slug.html"
```

2. Edit the new file — update the title, meta description, category, and body content.

3. Add the article card to `articles.html` (copy an existing card block and update the title, excerpt, category, slug, and image).

4. Add the article card to `thank-you.html` if replacing one of the two shown there.

5. Take a screenshot of the blog post at 1280×800px, save it as `previews/article-[slug].png`.

6. Deploy:
```bash
./deploy.sh "Add new post: [title]"
```

---

## Adding a New Portfolio Client

1. Take a screenshot of the client's website at 1280×800px.
2. Save it as `previews/[clientname].png` (lowercase, no spaces).
3. Add the client to the work list in `index.html` and `portfolio.html`.
4. Deploy:
```bash
./deploy.sh "Add [client name] to portfolio"
```

---

## Swapping an Image

1. Add the new image file to the project folder (match the exact filename of the old one, or update the HTML reference).
2. **Filenames must be lowercase** — the server is case-sensitive.
3. Preview, then deploy.

---

## If Something Breaks

- Check the browser console (right-click → Inspect → Console) for errors.
- Make sure image filenames are lowercase.
- Make sure file paths are correct (e.g., `blog/` and `previews/` are subfolders).
- To undo a change, open Claude Code and describe what to revert — or use git:
```bash
git diff        # see what changed
git checkout -- index.html   # revert a specific file
```

---

## Quick Reference

| Task | Command |
|------|---------|
| Start local preview | `python3 -m http.server 3456 --directory "/Users/leannfrank/Desktop/simple rabbit"` |
| Deploy to live site | `./deploy.sh "message"` |
| Open Claude Code | `cd "/Users/leannfrank/Desktop/simple rabbit" && claude` |
| Check git history | `git log --oneline` |
