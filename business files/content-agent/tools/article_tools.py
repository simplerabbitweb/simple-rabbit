"""
Article generation and publishing tools for Simple Rabbit.

Used by:
  - content-agent/agent.py  (Sage) — Friday drafting
  - content-agent/article_approve.py — approval + publishing to the live site
"""

import json
import re
from datetime import date
from ftplib import FTP
from pathlib import Path

# ─────────────────────────────────────────────
# PATHS
# ─────────────────────────────────────────────

CONTENT_AGENT_DIR   = Path(__file__).parent.parent
ROOT_DIR            = CONTENT_AGENT_DIR.parent
MEMORY_DIR          = CONTENT_AGENT_DIR / "memory"
DRAFTS_ARTICLES_DIR = CONTENT_AGENT_DIR / "drafts" / "articles"

TOPIC_OVERRIDE_FILE = MEMORY_DIR / "article-topic.txt"
PILLARS_FILE        = MEMORY_DIR / "article-pillars.json"

BLOG_DIR      = ROOT_DIR / "blog"
ARTICLES_HTML = ROOT_DIR / "articles.html"
SITEMAP_XML   = ROOT_DIR / "sitemap.xml"

# ─────────────────────────────────────────────
# FTP (matches deploy.sh)
# ─────────────────────────────────────────────

FTP_HOST   = "35.212.30.12"
FTP_PORT   = 21
FTP_USER   = "hello@simplerabbit.studio"
FTP_PASS   = "e~`1443{52$1"
FTP_REMOTE = "simplerabbit.studio/public_html"

# ─────────────────────────────────────────────
# CONTENT PILLARS
# ─────────────────────────────────────────────

CONTENT_PILLARS = [
    "Pricing & Positioning",
    "AI & SEO",
    "Premium Client Attraction",
    "Web Design Education",
    "Behind the Scenes",
    "Women in Business",
]

# ─────────────────────────────────────────────
# TOPIC OVERRIDE
# ─────────────────────────────────────────────

def get_article_topic_override() -> str:
    """Return the manually set topic, or empty string if none."""
    if TOPIC_OVERRIDE_FILE.exists():
        return TOPIC_OVERRIDE_FILE.read_text(encoding="utf-8").strip()
    return ""


def clear_article_topic_override() -> None:
    """Clear the topic override file after it's been used."""
    if TOPIC_OVERRIDE_FILE.exists():
        TOPIC_OVERRIDE_FILE.write_text("", encoding="utf-8")


# ─────────────────────────────────────────────
# PILLAR ROTATION
# ─────────────────────────────────────────────

def get_pillar_history() -> dict:
    """Return {pillar_name: last_used_iso_date} dict."""
    if PILLARS_FILE.exists():
        return json.loads(PILLARS_FILE.read_text(encoding="utf-8"))
    return {}


def get_next_pillar() -> str:
    """Return the content pillar used least recently (never-used first)."""
    history = get_pillar_history()
    return min(CONTENT_PILLARS, key=lambda p: history.get(p, "0000-00-00"))


def mark_pillar_used(pillar: str) -> None:
    """Record that this pillar was used today."""
    history = get_pillar_history()
    history[pillar] = date.today().isoformat()
    PILLARS_FILE.parent.mkdir(parents=True, exist_ok=True)
    PILLARS_FILE.write_text(json.dumps(history, indent=2), encoding="utf-8")


# ─────────────────────────────────────────────
# HTML TEMPLATE
# Uses __TOKEN__ placeholders — no conflict with CSS/JS braces
# ─────────────────────────────────────────────

_ARTICLE_TEMPLATE = """<!DOCTYPE html>
<!--
TITLE: __TITLE__
SLUG: __SLUG__
META DESCRIPTION: __META_DESC__
PRIMARY KEYWORD: __PRIMARY_KW__
CATEGORY: __CATEGORY__
WORD COUNT: ~__WORD_COUNT__
-->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__ | Simple Rabbit</title>
  <meta name="description" content="__META_DESC__">
  <meta property="og:title" content="__TITLE__ | Simple Rabbit">
  <meta property="og:description" content="__META_DESC__">
  <meta property="og:type" content="article">
  <meta property="og:url" content="__CANONICAL__">
  <meta property="og:image" content="https://simplerabbit.studio/previews/article-placeholder.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="__CANONICAL__">
  <link rel="icon" type="image/png" href="../favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    :root{
      color-scheme:light only;
      --black:#000;--white:#fff;--tone:#f7f7f8;
      --accent:#0872cc;--accent-dark:#0660ab;
      --mid:#949698;--dark:#4c4c4b;--light-border:#dfe0e1;
      --font-display:'Optima','Optima Nova','Candara','Segoe UI',sans-serif;
      --font-body:'Outfit',system-ui,sans-serif;
      --font-mono:'DM Mono',monospace;
    }
    body{font-family:var(--font-body);color:var(--black);background:var(--white);-webkit-font-smoothing:antialiased;}
    h1,h2,h3,h4{font-family:var(--font-display);letter-spacing:-0.5px;font-weight:400;}
    a{color:inherit;}
    .reveal{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
    .reveal.visible{opacity:1;transform:translateY(0);}
    .nav{position:sticky;top:0;background:var(--white);border-bottom:1px solid var(--light-border);z-index:100;}
    .nav-inner{max-width:1100px;margin:0 auto;padding:0 48px 0 16px;display:flex;align-items:center;justify-content:space-between;height:64px;}
    .nav-links{display:flex;align-items:center;gap:32px;}
    .nav-links a{font-size:14px;color:var(--dark);text-decoration:none;transition:color 0.2s;}
    .nav-links a:hover{color:var(--black);}
    .nav-cta{background:var(--black)!important;color:var(--white)!important;padding:10px 24px;font-size:13px;font-weight:500;transition:background 0.2s!important;}
    .nav-cta:hover{background:var(--dark)!important;color:var(--white)!important;}
    .btn-primary{display:inline-block;background:var(--black);color:var(--white);padding:14px 40px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);border:none;cursor:pointer;transition:background 0.2s;}
    .btn-primary:hover{background:var(--dark);}
    .article-header{padding:72px 48px 56px;border-bottom:1px solid var(--light-border);}
    .article-header-inner{max-width:720px;margin:0 auto;}
    .article-category{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:20px;}
    .article-title{font-size:clamp(32px,4.5vw,52px);letter-spacing:-1.5px;line-height:1.1;margin-bottom:24px;}
    .article-meta{display:flex;gap:24px;align-items:center;font-family:var(--font-mono);font-size:11px;letter-spacing:1px;color:var(--mid);}
    .article-body{max-width:720px;margin:0 auto;padding:64px 48px 80px;}
    .article-body p{font-size:17px;line-height:1.85;color:var(--dark);margin-bottom:28px;}
    .article-body h2{font-size:26px;line-height:1.25;letter-spacing:-0.5px;margin:52px 0 18px;color:var(--black);}
    .article-body h3{font-size:20px;line-height:1.3;margin:36px 0 14px;color:var(--black);}
    .article-body ul,.article-body ol{margin:0 0 28px 24px;}
    .article-body li{font-size:17px;line-height:1.8;color:var(--dark);margin-bottom:10px;}
    .article-body strong{color:var(--black);font-weight:600;}
    .article-body hr{border:none;border-top:1px solid var(--light-border);margin:52px 0;}
    .article-body blockquote{border-left:3px solid var(--accent);padding:4px 0 4px 24px;margin:36px 0;}
    .article-body blockquote p{font-size:19px;line-height:1.7;font-style:italic;color:var(--black);margin-bottom:0;}
    .article-body a{color:var(--accent);text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px;}
    .article-body a:hover{color:var(--accent-dark);}
    .back-link{font-family:var(--font-mono);font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--mid);text-decoration:none;display:inline-flex;align-items:center;gap:6px;margin-bottom:32px;transition:color 0.2s;}
    .back-link:hover{color:var(--black);}
    footer{border-top:1px solid var(--light-border);padding:32px 48px;display:flex;justify-content:space-between;align-items:center;}
    .footer-link{font-size:12px;color:var(--mid);text-decoration:none;transition:color 0.2s;}
    .footer-link:hover{color:var(--black);}
    .mobile-cta-bar{display:none;position:fixed;bottom:0;left:0;right:0;background:var(--black);z-index:200;}
    .mobile-cta-bar a{display:block;text-align:center;color:var(--white);text-decoration:none;font-size:14px;font-weight:500;padding:18px;letter-spacing:0.5px;}
    @media(max-width:900px){
      .article-header{padding:48px 32px 40px;}
      .article-body{padding:48px 32px 64px;}
      .nav-inner{padding:0 24px;}
      footer{padding:24px;}
    }
    @media(max-width:600px){
      .article-header{padding:40px 24px 32px;}
      .article-body{padding:40px 24px 56px;}
      .article-body p,.article-body li{font-size:16px;}
      .article-meta{flex-direction:column;align-items:flex-start;gap:8px;}
      .mobile-cta-bar{display:block;}
      body{padding-bottom:60px;}
      footer{flex-direction:column;gap:12px;text-align:center;}
    }
    .hamburger{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;}
    .hamburger span{display:block;width:22px;height:2px;background:var(--black);transition:transform 0.3s,opacity 0.3s;}
    .hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
    .hamburger.open span:nth-child(2){opacity:0;}
    .hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
    .mobile-nav{display:none;position:fixed;top:64px;left:0;right:0;bottom:0;background:var(--white);z-index:99;flex-direction:column;overflow-y:auto;border-top:1px solid var(--light-border);}
    .mobile-nav.open{display:flex;}
    .mobile-nav a{font-size:16px;color:var(--dark);text-decoration:none;padding:20px 24px;border-bottom:1px solid var(--light-border);font-family:var(--font-body);}
    .mobile-nav a:hover{color:var(--black);}
    .mobile-nav-cta{background:var(--black)!important;color:var(--white)!important;text-align:center;margin:24px!important;border-bottom:none!important;font-weight:500!important;}
    @media(max-width:768px){.hamburger{display:flex!important;}.nav-links{display:none!important;}.nav-inner a img{max-height:44px!important;}}
  </style>
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-77EEVJRJJD"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-77EEVJRJJD');
  </script>
  <noscript><style>.reveal{opacity:1!important;transform:none!important;}</style></noscript>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="/"><img src="../logo.svg" alt="Simple Rabbit" style="max-height:88px;display:block;"></a>
    <div class="nav-links">
      <a href="/about">About</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/articles">Articles</a>
      <a href="/contact">Contact</a>
      <a href="/contact" class="nav-cta">Book a Call</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-nav" id="mobile-nav">
  <a href="/about">About</a>
  <a href="/portfolio">Portfolio</a>
  <a href="/articles">Articles</a>
  <a href="/contact">Contact</a>
  <a href="/contact" class="mobile-nav-cta">Book a Call</a>
</div>

<!-- ARTICLE HEADER -->
<header class="article-header reveal">
  <div class="article-header-inner">
    <a href="/articles" class="back-link">&larr; All articles</a>
    <span class="article-category">__CATEGORY__</span>
    <h1 class="article-title">__TITLE__</h1>
    <div class="article-meta">
      <span>By Leann Frank</span>
      <span>&middot;</span>
      <span>__PUB_DATE__</span>
      <span>&middot;</span>
      <span>__READ_TIME__</span>
    </div>
  </div>
</header>

<!-- ARTICLE BODY -->
<article class="article-body reveal">

__BODY_HTML__

  <hr>
  <p style="text-align:center;font-size:16px;color:var(--dark);">Ready to build a site that works as hard as you do? <a href="/contact">Book a free call &rarr;</a></p>

</article>

<!-- NEWSLETTER -->
<section style="padding:80px 48px;border-top:1px solid var(--light-border);border-bottom:1px solid var(--light-border);">
  <div style="max-width:520px;margin:0 auto;text-align:center;">
    <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:16px;">Newsletter</span>
    <h2 style="font-family:var(--font-display);font-size:clamp(32px,4.5vw,52px);line-height:1.1;letter-spacing:-1px;margin-bottom:16px;font-weight:400;">Join The Hutch</h2>
    <p style="font-size:15px;line-height:1.75;color:var(--dark);margin-bottom:32px;">SEO insights, web design thinking, and the occasional behind-the-scenes look at what we're building.</p>
    <form id="newsletter-form" style="display:flex;max-width:440px;margin:0 auto;">
      <input type="email" name="email" required placeholder="Your email address" style="flex:1;border:none;border-bottom:1px solid var(--light-border);padding:10px 0;font-size:15px;background:transparent;outline:none;font-family:var(--font-body);color:var(--black);">
      <button type="submit" style="background:var(--black);color:var(--white);border:none;padding:10px 24px;font-size:13px;font-weight:500;cursor:pointer;font-family:var(--font-body);white-space:nowrap;transition:background 0.2s;flex-shrink:0;">Subscribe</button>
    </form>
  </div>
</section>

<!-- CTA -->
<section style="padding:100px 48px;text-align:center;border-top:1px solid var(--light-border);border-bottom:1px solid var(--light-border);">
  <div style="max-width:520px;margin:0 auto;">
    <h2 style="font-family:var(--font-display);font-size:clamp(28px,3.5vw,40px);line-height:1.15;margin-bottom:12px;font-weight:400;">Ready to book better clients?</h2>
    <h3 style="font-family:var(--font-display);font-size:22px;line-height:1.25;font-weight:400;color:var(--mid);margin-bottom:36px;">Let&rsquo;s build a website that does the selling for you</h3>
    <a href="/contact" class="btn-primary">Book a Call &rarr;</a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <span class="footer-link" style="cursor:default;">&copy; 2026 Simple Rabbit LLC &middot; Bergen County, NJ</span>
  <div style="display:flex;gap:24px;align-items:center;">
    <a href="tel:5514862779" class="footer-link">551.486.2779</a>
    <a href="mailto:hello@simplerabbit.studio" class="footer-link">hello@simplerabbit.studio</a>
    <a href="https://instagram.com/leannmfrank" target="_blank" class="footer-link">Instagram</a>
    <a href="https://www.facebook.com/simplerabbitnj/" target="_blank" class="footer-link">Facebook</a>
  </div>
</footer>

<div class="mobile-cta-bar">
  <a href="/contact">Book a Call &rarr;</a>
</div>

<script>
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  setTimeout(function(){document.querySelectorAll('.reveal:not(.visible)').forEach(function(el){el.classList.add('visible');});},1500);

  document.getElementById('newsletter-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    try {
      await fetch('https://formspree.io/f/mlgpewwb', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: this.email.value, type: 'newsletter signup' })
      });
      this.innerHTML = `<p style="font-size:14px;color:var(--dark);">Thanks! You're subscribed.</p>`;
    } catch(err) { console.error(err); }
  });
</script>
<script>
var hbtn=document.getElementById('hamburger'),mnav=document.getElementById('mobile-nav');
if(hbtn&&mnav){hbtn.addEventListener('click',function(){hbtn.classList.toggle('open');mnav.classList.toggle('open');document.body.style.overflow=mnav.classList.contains('open')?'hidden':'';});mnav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){hbtn.classList.remove('open');mnav.classList.remove('open');document.body.style.overflow='';});});}
</script>
</body>
</html>"""


# ─────────────────────────────────────────────
# BUILD + SAVE DRAFT
# ─────────────────────────────────────────────

def build_article_html(
    slug: str,
    title: str,
    category: str,
    meta_description: str,
    primary_keyword: str,
    body_html: str,
    read_time: str,
    pub_date: date,
) -> str:
    """Fill in the article template and return the complete HTML string."""
    canonical  = f"https://simplerabbit.studio/blog/{slug}"
    pub_date_str = pub_date.strftime("%B %-d, %Y")

    # Rough word count from body_html (strip tags, count words)
    plain = re.sub(r"<[^>]+>", " ", body_html)
    word_count = str(len(plain.split()))

    return (
        _ARTICLE_TEMPLATE
        .replace("__TITLE__",       title)
        .replace("__SLUG__",        slug)
        .replace("__META_DESC__",   meta_description)
        .replace("__PRIMARY_KW__",  primary_keyword)
        .replace("__CATEGORY__",    category)
        .replace("__WORD_COUNT__",  word_count)
        .replace("__CANONICAL__",   canonical)
        .replace("__PUB_DATE__",    pub_date_str)
        .replace("__READ_TIME__",   read_time)
        .replace("__BODY_HTML__",   body_html)
    )


def save_article_draft(
    slug: str,
    title: str,
    category: str,
    meta_description: str,
    primary_keyword: str,
    body_html: str,
    read_time: str,
) -> Path:
    """
    Generate the HTML and save it to drafts/articles/.
    pub_date is set to today (will be updated on actual publish).
    Returns the path of the saved draft.
    """
    DRAFTS_ARTICLES_DIR.mkdir(parents=True, exist_ok=True)
    html = build_article_html(
        slug=slug,
        title=title,
        category=category,
        meta_description=meta_description,
        primary_keyword=primary_keyword,
        body_html=body_html,
        read_time=read_time,
        pub_date=date.today(),
    )
    draft_path = DRAFTS_ARTICLES_DIR / f"{date.today().isoformat()}-{slug}.html"
    draft_path.write_text(html, encoding="utf-8")
    return draft_path


# ─────────────────────────────────────────────
# DRAFT METADATA PARSING
# ─────────────────────────────────────────────

def parse_draft_metadata(draft_path: Path) -> dict:
    """
    Extract metadata from the HTML comment block at the top of a draft.
    Returns dict with keys: title, slug, meta_description, primary_keyword,
    category, word_count, draft_date.
    """
    html = draft_path.read_text(encoding="utf-8")
    meta = {}
    comment_match = re.search(r"<!--(.*?)-->", html, re.DOTALL)
    if comment_match:
        for line in comment_match.group(1).strip().splitlines():
            if ":" in line:
                key, _, value = line.partition(":")
                meta[key.strip()] = value.strip()

    # Draft date from filename: YYYY-MM-DD-slug.html
    name = draft_path.stem  # e.g. "2026-03-07-my-article"
    parts = name.split("-", 3)
    draft_date = "-".join(parts[:3]) if len(parts) >= 3 else ""

    return {
        "title":           meta.get("TITLE", draft_path.stem),
        "slug":            meta.get("SLUG", draft_path.stem),
        "meta_description":meta.get("META DESCRIPTION", ""),
        "primary_keyword": meta.get("PRIMARY KEYWORD", ""),
        "category":        meta.get("CATEGORY", ""),
        "word_count":      meta.get("WORD COUNT", ""),
        "draft_date":      draft_date,
        "path":            draft_path,
    }


def list_article_drafts() -> list[dict]:
    """Return a list of parsed metadata dicts for all drafts, newest first."""
    if not DRAFTS_ARTICLES_DIR.exists():
        return []
    drafts = []
    for f in sorted(DRAFTS_ARTICLES_DIR.glob("*.html"), reverse=True):
        try:
            drafts.append(parse_draft_metadata(f))
        except Exception:
            pass
    return drafts


# ─────────────────────────────────────────────
# ARTICLES.HTML CARD INJECTION
# ─────────────────────────────────────────────

def _build_article_card(slug: str, title: str, category: str, excerpt: str) -> str:
    """Return the HTML string for one article card (no featured image — placeholder)."""
    return (
        f'\n    <!-- {title} -->\n'
        f'    <a href="/blog/{slug}" class="article-card reveal">\n'
        f'      <div class="article-card-img" style="background:var(--tone);display:flex;'
        f'align-items:center;justify-content:center;">\n'
        f'        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;'
        f'text-transform:uppercase;color:var(--mid);">Image coming soon</span>\n'
        f'      </div>\n'
        f'      <div class="article-card-body">\n'
        f'        <span class="overline">{category}</span>\n'
        f'        <h3 style="font-family:var(--font-display);font-size:22px;line-height:1.3;'
        f'font-weight:400;margin-bottom:16px;">{title}</h3>\n'
        f'        <p style="font-size:14px;line-height:1.75;color:var(--dark);">{excerpt}</p>\n'
        f'      </div>\n'
        f'      <div class="article-card-arrow">\n'
        f'        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:1px;'
        f'text-transform:uppercase;">Read article</span>\n'
        f'        <span>&rarr;</span>\n'
        f'      </div>\n'
        f'    </a>\n'
    )


def inject_article_card(slug: str, title: str, category: str, excerpt: str) -> None:
    """
    Prepend a new article card at the top of the article grid in articles.html.
    Inserts immediately after <div class="article-grid">.
    """
    html = ARTICLES_HTML.read_text(encoding="utf-8")
    marker = '<div class="article-grid">'
    if marker not in html:
        raise ValueError(f'Could not find "{marker}" in articles.html')
    card = _build_article_card(slug, title, category, excerpt)
    html = html.replace(marker, marker + card, 1)
    ARTICLES_HTML.write_text(html, encoding="utf-8")


# ─────────────────────────────────────────────
# SITEMAP UPDATE
# ─────────────────────────────────────────────

def update_sitemap(slug: str, pub_date: date) -> None:
    """Add a new blog article URL to sitemap.xml."""
    xml = SITEMAP_XML.read_text(encoding="utf-8")
    new_entry = (
        f"\n  <url>\n"
        f"    <loc>https://simplerabbit.studio/blog/{slug}</loc>\n"
        f"    <lastmod>{pub_date.isoformat()}</lastmod>\n"
        f"    <changefreq>monthly</changefreq>\n"
        f"    <priority>0.7</priority>\n"
        f"  </url>"
    )
    # Insert before the closing </urlset>
    xml = xml.replace("</urlset>", new_entry + "\n\n</urlset>")
    SITEMAP_XML.write_text(xml, encoding="utf-8")


# ─────────────────────────────────────────────
# FTP PUBLISH
# ─────────────────────────────────────────────

def ftp_publish_article(slug: str) -> str:
    """
    Upload 3 files to SiteGround via FTP:
      blog/{slug}.html, articles.html, sitemap.xml
    Returns a status string.
    """
    blog_file = BLOG_DIR / f"{slug}.html"
    files_to_upload = [
        (str(blog_file),   f"blog/{slug}.html"),
        (str(ARTICLES_HTML), "articles.html"),
        (str(SITEMAP_XML),   "sitemap.xml"),
    ]

    uploaded = []
    try:
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT, timeout=30)
        ftp.login(FTP_USER, FTP_PASS)
        ftp.set_pasv(True)
        ftp.cwd(FTP_REMOTE)

        # Ensure blog/ subdir exists
        try:
            ftp.mkd("blog")
        except Exception:
            pass

        for local_path, remote_name in files_to_upload:
            with open(local_path, "rb") as f:
                ftp.storbinary(f"STOR {remote_name}", f)
            uploaded.append(remote_name)

        ftp.quit()
    except Exception as e:
        return f"FTP error: {e}"

    return f"Uploaded: {', '.join(uploaded)}"


def purge_cache() -> str:
    """Hit the SiteGround cache purge endpoint."""
    import urllib.request
    try:
        with urllib.request.urlopen(
            "https://simplerabbit.studio/purge-cache.php", timeout=10
        ) as resp:
            return f"Cache purged ({resp.status})"
    except Exception as e:
        return f"Cache purge skipped: {e}"


# ─────────────────────────────────────────────
# FULL PUBLISH PIPELINE
# ─────────────────────────────────────────────

def publish_article(draft_path: Path) -> dict:
    """
    Full publish pipeline for an approved article draft:
      1. Re-generate HTML with today's date as pub_date
      2. Copy to blog/{slug}.html
      3. Inject card into articles.html
      4. Add URL to sitemap.xml
      5. FTP upload (3 files)
      6. Purge cache
      7. Archive draft (rename to .published)

    Returns a dict with status info.
    """
    meta = parse_draft_metadata(draft_path)
    slug       = meta["slug"]
    title      = meta["title"]
    category   = meta["category"]
    excerpt    = meta["meta_description"]
    pub_date   = date.today()

    # Re-read the draft and update pub_date in the article header
    html = draft_path.read_text(encoding="utf-8")
    pub_date_str = pub_date.strftime("%B %-d, %Y")

    # Replace the draft date placeholder with today's date
    # The pub_date in the template is between <span> tags after the middot
    # Pattern: after "By Leann Frank" block, the date span
    html = re.sub(
        r'(<span>By Leann Frank</span>\s*<span>&middot;</span>\s*<span>)[^<]*(</span>)',
        r'\g<1>' + pub_date_str + r'\g<2>',
        html,
        count=1,
    )

    # Write to blog/
    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    blog_dest = BLOG_DIR / f"{slug}.html"
    blog_dest.write_text(html, encoding="utf-8")

    # Update articles.html
    inject_article_card(slug, title, category, excerpt)

    # Update sitemap.xml
    update_sitemap(slug, pub_date)

    # FTP upload
    ftp_status = ftp_publish_article(slug)

    # Purge cache
    cache_status = purge_cache()

    # Archive draft
    archived = draft_path.with_suffix(".published")
    draft_path.rename(archived)

    return {
        "slug":         slug,
        "title":        title,
        "url":          f"https://simplerabbit.studio/blog/{slug}",
        "pub_date":     pub_date_str,
        "ftp":          ftp_status,
        "cache":        cache_status,
        "archived_to":  str(archived),
    }
