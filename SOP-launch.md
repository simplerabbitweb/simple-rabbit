# SOP: Launching a New Simple Rabbit Website

Use this when you are building and launching a brand new version of the site from scratch.

---

## What You Need Before Starting

- Mac with Claude Code installed
- Project folder: `/Users/leannfrank/Desktop/simple rabbit`
- GitHub account: `simplerabbitweb`
- SiteGround account with FTP access
- Domain pointed to SiteGround

---

## Step 1 — Build the Site Locally

Open Claude Code in the project folder and use the build prompt:

```
claude
```

Reference `claude-code-build-prompt.md` for the full site spec. Tell Claude what pages, copy, and images you need.

**Preview locally at any time:**
```bash
python3 -m http.server 3456 --directory "/Users/leannfrank/Desktop/simple rabbit"
```
Then open `localhost:3456` in your browser.

---

## Step 2 — Add Your Assets

Drop these files into `/Users/leannfrank/Desktop/simple rabbit/`:

| File | Purpose |
|------|---------|
| `leann.jpg` | Hero/about photo (lowercase filename) |
| `leann-2.jpg` | Secondary photo |
| `leann-3.jpg` | Third photo |
| `logo.svg` | Nav logo |
| `previews/*.png` | Portfolio + article preview screenshots |

**Important:** All image filenames must be **lowercase** — the server is case-sensitive.

**For portfolio preview screenshots:**
Take a screenshot of each client website at 1280×800px, name it `clientname.png`, and drop it in the `previews/` folder.

---

## Step 3 — Connect to GitHub

Only needed for a brand new project:

```bash
cd "/Users/leannfrank/Desktop/simple rabbit"
git init
git config user.name "Leann Frank"
git config user.email "lennfrank9@gmail.com"
git add -A
git commit -m "Initial commit"
git remote add origin git@github.com:simplerabbitweb/REPO-NAME.git
git push -u origin main
```

Create the GitHub repo first at **github.com/new** (no README, no .gitignore).

---

## Step 4 — Set Up FTP Credentials

The `deploy.sh` script has the SiteGround FTP credentials hardcoded. If credentials change, update them in `deploy.sh`:

```
HOST = "35.212.30.12"
USER = "hello@simplerabbit.studio"
PASS = "your-password"
REMOTE = "simplerabbit.studio/public_html"
```

**Note:** `deploy.sh` is gitignored so credentials never go to GitHub.

---

## Step 5 — Deploy Live

```bash
cd "/Users/leannfrank/Desktop/simple rabbit"
./deploy.sh "Initial launch"
```

This will:
1. Upload all HTML, images, and assets to SiteGround via FTP
2. Commit and push everything to GitHub

**Verify it's live:**
- Homepage: `https://simplerabbit.studio`
- About: `https://simplerabbit.studio/about.html`
- Blog post: `https://simplerabbit.studio/blog/[slug].html`

---

## Step 6 — Final Checks

- [ ] All pages load (no 404s)
- [ ] Images show on homepage, about, portfolio
- [ ] All 6 blog posts are accessible
- [ ] Contact form submits correctly
- [ ] Logo displays in nav
- [ ] Mobile looks good (resize browser to 375px)
- [ ] Footer links work (Facebook, Instagram)

---

## File Structure Reference

```
simple rabbit/
├── index.html          ← Homepage
├── about.html
├── articles.html
├── portfolio.html
├── contact.html
├── thank-you.html      ← After form submit
├── 404.html
├── logo.svg
├── leann.jpg
├── leann-2.jpg
├── leann-3.jpg
├── blog/
│   └── [slug].html     ← One file per article
├── previews/
│   ├── [client].png    ← Portfolio previews
│   └── article-*.png   ← Article card images
└── deploy.sh           ← Run to go live (gitignored)
```
