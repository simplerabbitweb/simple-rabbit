#!/usr/bin/env python3
"""
auto-blog.py — Daily blog automation for Simple Rabbit
Picks next post from blog-queue.json, generates content via Claude,
fetches a featured image from Unsplash, updates articles.html + sitemap.xml, deploys.
"""

import os, json, re, sys, subprocess, urllib.request, urllib.parse, urllib.error
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
QUEUE_FILE  = os.path.join(BASE, "blog-queue.json")
CONFIG_FILE = os.path.join(BASE, ".blog-config.json")
LOG_FILE    = os.path.join(BASE, "auto-blog.log")

# ── LOGGING ──────────────────────────────────────────────────────────────────

def log(msg):
    ts   = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")

# ── CONFIG ────────────────────────────────────────────────────────────────────

with open(CONFIG_FILE) as f:
    config = json.load(f)

UNSPLASH_KEY  = config["unsplash_key"]
ANTHROPIC_KEY = config["anthropic_key"]

# ── QUEUE ─────────────────────────────────────────────────────────────────────

def load_queue():
    with open(QUEUE_FILE) as f:
        return json.load(f)

def save_queue(q):
    with open(QUEUE_FILE, "w") as f:
        json.dump(q, f, indent=2)

def next_post(q):
    for post in q["posts"]:
        if not post["published"]:
            return post
    return None

# ── UNSPLASH ──────────────────────────────────────────────────────────────────

def fetch_unsplash(query, slug):
    """Download a landscape photo. Returns (local_path, html_credit_string)."""
    # Try the specific query, then progressively broader fallbacks
    fallbacks = [query, "professional workspace laptop", "woman working desk", "laptop minimal desk"]

    results = []
    used_query = query
    for attempt in fallbacks:
        encoded = urllib.parse.quote(attempt)
        url = (
            f"https://api.unsplash.com/search/photos"
            f"?query={encoded}&orientation=landscape&per_page=5&order_by=relevant"
        )
        req = urllib.request.Request(url, headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        results = data.get("results", [])
        if results:
            used_query = attempt
            if attempt != query:
                log(f"  Unsplash fallback query used: '{attempt}'")
            break

    if not results:
        raise RuntimeError(f"No Unsplash results for any query variant of: {query}")

    photo            = results[0]
    img_url          = photo["urls"]["regular"]
    download_trigger = photo["links"]["download_location"]
    photographer     = photo["user"]["name"]
    photographer_url = photo["user"]["links"]["html"] + "?utm_source=simplerabbit&utm_medium=referral"

    # Trigger required download endpoint (Unsplash API terms)
    try:
        dl_req = urllib.request.Request(
            download_trigger,
            headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"}
        )
        urllib.request.urlopen(dl_req, timeout=10)
    except Exception:
        pass  # Non-fatal

    local_path = os.path.join(BASE, "previews", f"{slug}.jpg")
    with urllib.request.urlopen(img_url, timeout=30) as resp:
        with open(local_path, "wb") as f:
            f.write(resp.read())

    credit = (
        f'Photo by <a href="{photographer_url}">{photographer}</a> on '
        f'<a href="https://unsplash.com?utm_source=simplerabbit&utm_medium=referral">Unsplash</a>'
    )
    log(f"  Unsplash: saved previews/{slug}.jpg (by {photographer})")
    return local_path, credit

# ── CLAUDE CONTENT GENERATION ─────────────────────────────────────────────────

VOICE = """
VOICE: Direct. Warm. Quietly confident.
- Fewest words that work. No padding. No hedging.
- Active voice. Specific nouns. Concrete verbs.
- Contractions fine. Sounds like a real person writing to a smart peer.
- Articles format: more conversational, first person, "you." Like Leann talking with a friend who runs a practice.

SENTENCE RULES (hard):
- Short sentences. Vary length, lean short.
- No em-dashes. Use commas, colons, or periods instead.
- No: "Not just X, but Y" / triple adjective lists / "But here's the thing" / "Here's the truth"
- No: "in today's digital landscape" / "when it comes to" / "at the end of the day" / "simply put"

WORDS TO AVOID (cut on sight):
elevate, unlock, empower, transform, level up, game-changer, journey, passion, dedicated,
premium experience, bespoke, curated, thoughtfully crafted, delve into, navigate the complexities,
comprehensive guide, dive deep, unpack, demystify, seamless, robust, innovative,
scaling, hustle, glow up, soul-led, heart-centered, abundance, manifest

WORDS THAT FIT:
built, designed, written, structured, ranked, found, visible, clear, specific, careful
practice, provider, practitioner, patient, private-pay, independent, specialty
brings in the right patients, ranks on Google, does the selling before anyone picks up the phone
"""

INTERNAL_LINKS = """
Available internal links (use 1-2 where they fit naturally, not forced):
/contact — "Start a Project"
/services — services overview
/portfolio — portfolio and case studies
/articles — all articles
/blog/about-page-service-business — about page strategy article
/blog/convert-visitors-to-clients — converting visitors to patients
/blog/5-things-premium-clients — attracting premium clients
/blog/case-study-smooth-laser-center — Smooth Laser Center case study
/blog/google-business-profile-not-getting-clicks — Google Business Profile article
/blog/mobile-friendly-websites-2026 — mobile-friendly website article
"""

def generate_content(post):
    """Call Claude API. Returns dict with html, excerpt, meta_description, h1, unsplash_query."""
    import anthropic
    client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

    prompt = f"""You are writing a blog post for Simple Rabbit, a boutique web design studio run by Leann Frank in Bergen County, NJ. She builds custom websites for private-pay women's wellness practices.

{VOICE}

{INTERNAL_LINKS}

POST TO WRITE:
Title: {post['title']}
Category: {post['category']}

INSTRUCTIONS:
Write an article of approximately 1,200-1,400 words. Return a JSON object with exactly these keys:

- "html": the full article body in HTML (no wrapping <article> tags, just the content)
- "h1": display title for the <h1> (can reword slightly for readability; no trailing period)
- "meta_description": SEO meta description, 140-155 characters, plain text
- "excerpt": 1-2 sentence article card summary, ~25 words, plain text
- "unsplash_query": 2-4 word Unsplash search query for a professional featured image (think clean workspace, wellness, laptop, woman professional, medical consultation, etc.)

HTML rules:
- Use only: <p>, <h2>, <h3>, <ul>/<li>, <ol>/<li>, <strong>, <blockquote><p></blockquote>, <a href="...">, <hr>
- Open with a strong first paragraph that immediately identifies the reader's problem
- End naturally with a paragraph that connects back to Simple Rabbit's work and includes one internal link
- No "Conclusion" section label
- No markdown, no code fences, no explanation outside the JSON

Return ONLY valid JSON. Nothing before or after it."""

    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()
    # Strip markdown fences if model added them
    raw = re.sub(r'^```json\s*', '', raw, flags=re.MULTILINE)
    raw = re.sub(r'^```\s*',     '', raw, flags=re.MULTILINE)
    raw = re.sub(r'\s*```$',     '', raw)

    return json.loads(raw)

# ── HTML BUILDER ──────────────────────────────────────────────────────────────

CSS = """
    *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
    :root{
      color-scheme:light only;
      --black:#000;--white:#fff;--tone:#E2D8D6;
      --accent:#AA737D;--accent-dark:#8a5d66;
      --mid:#111;--dark:#333;--light-border:#dfe0e1;
      --font-display:'Raleway',sans-serif;
      --font-body:'DM Sans',system-ui,sans-serif;
      --font-mono:'DM Sans',sans-serif;
    }
    html{overflow-x:hidden;}body{font-family:var(--font-body);color:var(--black);background:var(--white);-webkit-font-smoothing:antialiased;overflow-x:hidden;}
    h1,h2,h3,h4{font-family:var(--font-display);letter-spacing:-0.5px;font-weight:400;}
    a{color:inherit;}
    .reveal{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
    .reveal.visible{opacity:1;transform:translateY(0);}
    .nav{position:sticky;top:0;background:#474D73;border-bottom:1px solid rgba(255,255,255,0.1);z-index:100;padding-bottom:8px;}
    .nav-inner{max-width:1100px;margin:0 auto;padding:0 48px 0 16px;display:flex;align-items:center;justify-content:space-between;height:64px;}
    .nav-links{display:flex;align-items:center;gap:32px;}
    .nav-links a{font-size:14px;color:rgba(255,255,255,0.85);text-decoration:none;transition:color 0.2s;}
    .nav-links a:hover{color:var(--white);}
    .nav-cta{background:var(--white)!important;color:var(--black)!important;padding:10px 24px;font-size:13px;font-weight:500;transition:background 0.2s!important;}
    .nav-cta:hover{background:#e8e8e8!important;color:var(--black)!important;}
    .article-header{padding:72px 48px 56px;border-bottom:1px solid var(--light-border);}
    .article-header-inner{max-width:720px;margin:0 auto;}
    .article-category{font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:20px;}
    .article-title{font-size:clamp(32px,4.5vw,52px);letter-spacing:-1.5px;line-height:1.1;margin-bottom:24px;}
    .article-meta{display:flex;gap:24px;align-items:center;font-family:var(--font-mono);font-size:11px;letter-spacing:1px;color:var(--mid);}
    .article-hero-img{width:100%;max-width:720px;margin:0 auto;display:block;padding:48px 48px 0;}
    .article-hero-img img{width:100%;height:auto;display:block;aspect-ratio:16/9;object-fit:cover;}
    .article-hero-credit{max-width:720px;margin:0 auto;padding:8px 48px 0;font-family:var(--font-mono);font-size:10px;color:var(--mid);}
    .article-hero-credit a{color:var(--mid);text-decoration:underline;text-underline-offset:2px;}
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
    footer{border-top:none;padding:32px 48px;display:flex;justify-content:space-between;align-items:center;background:#474D73;}
    .footer-link{font-size:12px;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s;}
    .footer-link:hover{color:#fff;}
    .hamburger{display:none;flex-direction:column;justify-content:center;gap:5px;background:none;border:none;cursor:pointer;padding:4px;}
    .hamburger span{display:block;width:22px;height:2px;background:var(--white);transition:transform 0.3s,opacity 0.3s;}
    .hamburger.open span:nth-child(1){transform:translateY(7px) rotate(45deg);}
    .hamburger.open span:nth-child(2){opacity:0;}
    .hamburger.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg);}
    .mobile-nav{display:none;position:fixed;top:64px;left:0;right:0;bottom:0;background:#474D73;z-index:99;flex-direction:column;overflow-y:auto;border-top:1px solid rgba(255,255,255,0.1);}
    .mobile-nav.open{display:flex;}
    .mobile-nav a{font-size:16px;color:rgba(255,255,255,0.85);text-decoration:none;padding:20px 24px;border-bottom:1px solid rgba(255,255,255,0.1);font-family:var(--font-body);}
    .mobile-nav a:hover{color:var(--white);}
    .mobile-nav a.mobile-nav-cta{background:var(--white);color:var(--black)!important;text-align:center;font-weight:500;border-bottom:none!important;margin:16px 24px;display:block;}
    .mobile-nav a.mobile-nav-cta:hover{background:#e8e8e8!important;}
    .article-cta{background:#474D73;color:var(--white);padding:80px 48px;text-align:center;}
    .article-cta h3{font-size:clamp(24px,3vw,32px);letter-spacing:-0.5px;line-height:1.2;margin-bottom:20px;color:var(--white);font-family:var(--font-display);font-weight:400;}
    .article-cta p{font-size:17px;line-height:1.7;color:rgba(255,255,255,0.8);margin:0 auto 36px;max-width:560px;}
    .article-cta-btn{display:inline-block;background:var(--white);color:var(--black);padding:16px 48px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);transition:background 0.2s;}
    .article-cta-btn:hover{background:#e8e8e8;}
    @media(max-width:900px){
      .article-header{padding:48px 32px 40px;}
      .article-body{padding:48px 32px 64px;}
      .article-hero-img{padding:40px 32px 0;}
      .article-hero-credit{padding:8px 32px 0;}
      .nav-inner{padding:0 24px;}
      footer{padding:24px;}
      .article-cta{padding:64px 32px;}
    }
    @media(max-width:768px){
      .hamburger{display:flex!important;}
      .nav-links{display:none!important;}
      .nav-inner a img{max-height:44px!important;}
    }
    @media(max-width:600px){
      .article-header{padding:40px 24px 32px;}
      .article-body{padding:40px 24px 56px;}
      .article-hero-img{padding:32px 24px 0;}
      .article-hero-credit{padding:8px 24px 0;}
      .article-body p,.article-body li{font-size:16px;}
      .article-meta{flex-direction:column;align-items:flex-start;gap:8px;}
      footer{padding:24px;flex-direction:column;gap:12px;text-align:center;}
      footer>div{flex-wrap:wrap;justify-content:center;gap:12px;}
      .article-cta{padding:48px 24px;}
      .article-cta h3{font-size:22px;}
    }
"""

JS_INLINE = """
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0 });
  document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
  setTimeout(function(){document.querySelectorAll('.reveal:not(.visible)').forEach(function(el){el.classList.add('visible');});},1500);
"""

JS_HAMBURGER = """
var hbtn=document.getElementById('hamburger'),mnav=document.getElementById('mobile-nav');
if(hbtn&&mnav){hbtn.addEventListener('click',function(){hbtn.classList.toggle('open');mnav.classList.toggle('open');document.body.style.overflow=mnav.classList.contains('open')?'hidden':'';if(mnav.classList.contains('open')){var navEl=document.querySelector('.nav');mnav.style.top=navEl?navEl.getBoundingClientRect().bottom+'px':'64px';}});mnav.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){hbtn.classList.remove('open');mnav.classList.remove('open');document.body.style.overflow='';});});}
"""


def build_html(post, generated, slug, img_credit, pub_date_display, pub_date_iso):
    h1       = generated.get("h1", post["title"])
    meta     = generated.get("meta_description", post["title"])
    category = post["category"]
    body_html = generated["html"]

    word_count = len(re.findall(r'\w+', body_html))
    read_min   = max(4, round(word_count / 200))

    schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": h1,
        "author": {"@type": "Person", "name": "Leann Frank", "url": "https://simplerabbit.studio/about"},
        "publisher": {
            "@type": "Organization", "name": "Simple Rabbit",
            "url": "https://simplerabbit.studio",
            "logo": {"@type": "ImageObject", "url": "https://simplerabbit.studio/logo.png"}
        },
        "datePublished":  pub_date_iso,
        "dateModified":   pub_date_iso,
        "image":          f"https://simplerabbit.studio/previews/{slug}.jpg",
        "url":            f"https://simplerabbit.studio/blog/{slug}",
        "description":    meta
    }, indent=2)

    return f"""<!DOCTYPE html>
<!--
TITLE: {post['title']}
SLUG: {slug}
META DESCRIPTION: {meta}
PUBLISHED: {pub_date_display}
-->
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{h1} | Simple Rabbit</title>
  <meta name="description" content="{meta}">
  <meta property="og:title" content="{h1} | Simple Rabbit">
  <meta property="og:description" content="{meta}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://simplerabbit.studio/blog/{slug}">
  <meta property="og:image" content="https://simplerabbit.studio/previews/{slug}.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="canonical" href="https://simplerabbit.studio/blog/{slug}">
  <link rel="icon" type="image/png" href="../favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Raleway:wght@300;400;500;600&display=swap" rel="stylesheet">
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-PLFL8E7Z8F"></script>
  <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-PLFL8E7Z8F');</script>
  <style>{CSS}  </style>
  <noscript><style>.reveal{{opacity:1!important;transform:none!important;}}</style></noscript>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="/"><img src="../logo.png" alt="Simple Rabbit" style="max-height:88px;display:block;"></a>
    <div class="nav-links">
      <a href="/about">About</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/services">Services</a>
      <a href="/articles">Articles</a>
      <a href="/contact" class="nav-cta">Start a Project</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Open menu"><span></span><span></span><span></span></button>
  </div>
</nav>
<div class="mobile-nav" id="mobile-nav">
  <a href="/about">About</a>
  <a href="/portfolio">Portfolio</a>
  <a href="/services">Services</a>
  <a href="/articles">Articles</a>
  <a href="/contact" class="mobile-nav-cta">Start a Project</a>
</div>

<!-- ARTICLE HEADER -->
<header class="article-header reveal">
  <div class="article-header-inner">
    <a href="/articles" class="back-link">&larr; All articles</a>
    <span class="article-category">{category}</span>
    <h1 class="article-title">{h1}</h1>
    <div class="article-meta">
      <span>By Leann Frank</span>
      <span>&middot;</span>
      <span>{pub_date_display}</span>
      <span>&middot;</span>
      <span>{read_min} min read</span>
    </div>
  </div>
</header>

<!-- FEATURED IMAGE -->
<div class="article-hero-img">
  <img src="../previews/{slug}.jpg" alt="{h1}" loading="lazy">
</div>
<p class="article-hero-credit">{img_credit}</p>

<!-- ARTICLE BODY -->
<article class="article-body reveal">

{body_html}

</article>

<!-- FULL-WIDTH CTA -->
<section style="position:relative;min-height:500px;display:flex;align-items:center;justify-content:center;overflow:hidden;">
  <div class="parallax-bg" style="position:absolute;inset:0;background-image:url('/CTA-banner.jpg');background-size:cover;background-position:center;background-attachment:fixed;"></div>
  <div style="position:relative;z-index:1;background:rgba(255,255,255,0.18);backdrop-filter:blur(24px) saturate(160%);-webkit-backdrop-filter:blur(24px) saturate(160%);border:1px solid rgba(255,255,255,0.28);box-shadow:0 8px 32px rgba(0,0,0,0.10);padding:64px 56px;max-width:520px;width:calc(100% - 48px);text-align:center;" class="cta-box">
    <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#fff;display:block;margin-bottom:16px;">Next step</span>
    <h2 style="font-family:var(--font-display);font-size:clamp(28px,3.5vw,40px);letter-spacing:-1px;line-height:1.15;margin-bottom:16px;font-weight:400;color:#fff;">Let&rsquo;s build a site that brings in the patients you actually want.</h2>
    <p style="font-size:15px;line-height:1.75;color:#fff;margin-bottom:32px;">Tell us about your practice. If we&rsquo;re the right fit, we&rsquo;ll map out a plan together.</p>
    <a href="/contact" style="display:inline-block;background:#474D73;color:var(--white);padding:14px 40px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);transition:background 0.2s;">Start a Project &rarr;</a>
  </div>
</section>

<!-- NEWSLETTER BANNER -->
<section style="background:var(--white);border-top:1px solid var(--light-border);border-bottom:1px solid var(--light-border);padding:64px 48px;text-align:center;">
  <div style="max-width:560px;margin:0 auto;">
    <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:2px;text-transform:uppercase;color:var(--accent);display:block;margin-bottom:16px;">The Hutch, Free Newsletter</span>
    <h2 style="font-family:var(--font-display);font-size:clamp(24px,3vw,32px);letter-spacing:-0.5px;line-height:1.2;margin-bottom:16px;font-weight:400;">SEO insights and web design thinking, every week</h2>
    <p style="font-size:15px;line-height:1.75;color:var(--dark);margin-bottom:32px;">SEO insights, web design thinking, and the occasional look behind the curtain. Delivered weekly.</p>
    <a href="https://leannfrank.myflodesk.com/jointhehutch" target="_blank" rel="noopener" style="display:inline-block;background:#474D73;color:var(--white);padding:14px 40px;font-size:14px;font-weight:500;letter-spacing:0.5px;text-decoration:none;font-family:var(--font-body);transition:background 0.2s;">Join The Hutch &rarr;</a>
  </div>
</section>

<!-- SCRIPTURE -->
<div style="border-top:1px solid var(--light-border);padding:20px 48px;text-align:center;">
  <p style="font-size:12px;font-family:var(--font-mono);letter-spacing:0.5px;color:var(--mid);font-style:italic;">&ldquo;For I am not ashamed of the gospel, because it is the power of God that brings salvation to everyone who believes.&rdquo; &mdash; Romans 1:16</p>
</div>

<!-- FOOTER -->
<footer>
  <span class="footer-link" style="cursor:default;">&#169; 2026 Simple Rabbit LLC &middot; Bergen County, NJ</span>
  <div style="display:flex;gap:24px;align-items:center;">
    <a href="/privacy-policy" class="footer-link">Privacy Policy</a>
    <a href="tel:5514862779" class="footer-link">551.486.2779</a>
    <a href="mailto:hello@simplerabbit.studio" class="footer-link">hello@simplerabbit.studio</a>
    <a href="https://instagram.com/leannmfrank" target="_blank" class="footer-link">Instagram</a>
    <a href="https://www.facebook.com/simplerabbitnj/" target="_blank" class="footer-link">Facebook</a>
    <a href="https://leannfrank.myflodesk.com/jointhehutch" target="_blank" rel="noopener" class="footer-link">Newsletter</a>
  </div>
</footer>

<script type="application/ld+json">
{schema}
</script>
<script>{JS_INLINE}</script>
<script>{JS_HAMBURGER}</script>
</body>
</html>"""


# ── ARTICLES.HTML UPDATE ──────────────────────────────────────────────────────

def update_articles_html(slug, h1, category, excerpt, pub_date_display):
    path = os.path.join(BASE, "articles.html")
    with open(path) as f:
        content = f.read()

    card = f"""
    <!-- {pub_date_display} -->
    <a href="/blog/{slug}" class="article-card reveal">
      <div class="article-card-img"><img src="previews/{slug}.jpg" alt="{h1}" loading="lazy"></div>
      <div class="article-card-body">
        <span class="overline">{category}</span>
        <h3 style="font-family:var(--font-display);font-size:22px;line-height:1.3;font-weight:400;margin-bottom:16px;">{h1}</h3>
        <p style="font-size:14px;line-height:1.75;color:var(--dark);">{excerpt}</p>
      </div>
      <div class="article-card-arrow">
        <span style="font-family:var(--font-mono);font-size:11px;letter-spacing:1px;text-transform:uppercase;">Read article</span>
        <span>&rarr;</span>
      </div>
    </a>
"""

    marker = '<div class="article-grid">'
    if marker not in content:
        raise RuntimeError("Could not find article-grid marker in articles.html")

    content = content.replace(marker, marker + card, 1)
    with open(path, "w") as f:
        f.write(content)
    log(f"  Updated articles.html with card for /blog/{slug}")


# ── SITEMAP UPDATE ────────────────────────────────────────────────────────────

def update_sitemap(slug, pub_date_iso):
    path = os.path.join(BASE, "sitemap.xml")
    with open(path) as f:
        content = f.read()

    new_url = f"""  <url>
    <loc>https://simplerabbit.studio/blog/{slug}</loc>
    <lastmod>{pub_date_iso}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""
    content = content.replace("</urlset>", new_url + "</urlset>")
    with open(path, "w") as f:
        f.write(content)
    log(f"  Updated sitemap.xml with /blog/{slug}")


# ── DEPLOY ────────────────────────────────────────────────────────────────────

def deploy(slug, pub_date_display):
    msg = f"Auto-publish: {slug} ({pub_date_display})"
    log(f"  Running deploy.sh ...")
    result = subprocess.run(
        ["bash", os.path.join(BASE, "deploy.sh"), msg],
        cwd=BASE, capture_output=True, text=True, timeout=300
    )
    if result.stdout:
        for line in result.stdout.strip().splitlines():
            log(f"  deploy: {line}")
    if result.returncode != 0:
        log(f"  deploy.sh exited {result.returncode}")
        if result.stderr:
            log(f"  stderr: {result.stderr[:500]}")


# ── MAIN ──────────────────────────────────────────────────────────────────────

def main():
    log("=" * 60)
    log("auto-blog.py starting")

    queue = load_queue()
    post  = next_post(queue)

    if not post:
        log("Queue complete. All 29 posts published. No action taken.")
        return

    slug = post["slug"]
    log(f"Next post: [{post['id']}] {post['title']}")
    log(f"  Slug: {slug}")

    # Idempotency: skip if file already exists (e.g. script ran twice today)
    blog_path = os.path.join(BASE, "blog", f"{slug}.html")
    if os.path.exists(blog_path):
        log(f"  {slug}.html already exists. Marking published and exiting.")
        for p in queue["posts"]:
            if p["slug"] == slug:
                p["published"] = True
                p["published_date"] = datetime.now().strftime("%Y-%m-%d")
        save_queue(queue)
        return

    now              = datetime.now()
    pub_date_display = now.strftime("%B %-d, %Y")   # e.g. "April 28, 2026"
    pub_date_iso     = now.strftime("%Y-%m-%d")     # e.g. "2026-04-28"

    # 1. Generate content via Claude
    log("  Calling Claude API ...")
    generated = generate_content(post)
    h1      = generated.get("h1", post["title"])
    excerpt = generated.get("excerpt", "")
    unsplash_query = generated.get("unsplash_query", "wellness professional workspace")
    log(f"  h1: {h1}")
    log(f"  Unsplash query: {unsplash_query}")

    # 2. Fetch Unsplash image
    log("  Fetching Unsplash image ...")
    _, img_credit = fetch_unsplash(unsplash_query, slug)

    # 3. Build and save blog HTML
    html = build_html(post, generated, slug, img_credit, pub_date_display, pub_date_iso)
    with open(blog_path, "w") as f:
        f.write(html)
    log(f"  Saved blog/{slug}.html")

    # 4. Update articles.html
    update_articles_html(slug, h1, post["category"], excerpt, pub_date_display)

    # 5. Update sitemap.xml
    update_sitemap(slug, pub_date_iso)

    # 6. Deploy
    deploy(slug, pub_date_display)

    # 7. Mark published
    for p in queue["posts"]:
        if p["slug"] == slug:
            p["published"]      = True
            p["published_date"] = pub_date_iso
    save_queue(queue)

    log(f"Done. Live at https://simplerabbit.studio/blog/{slug}")
    log("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        log(f"FATAL ERROR: {e}")
        log(traceback.format_exc())
        sys.exit(1)
