# Simple Rabbit — New Project Kickoff Prompt

Paste this into Claude Code at the start of every new client project **together with the filled-out Client Brief**.
- This file covers: stack, structure, components, forms, SEO, and deployment standards — the same for every project
- The Client Brief covers: client-specific CSS variables, fonts, colors, pages, CTA copy, and content — different for every project

Fill in the [BRACKETED] placeholders in the Client Brief before pasting both documents.

---

## PASTE BELOW THIS LINE

You are helping me build a website for a new client of Simple Rabbit Studio — my premium web design studio for women-owned service businesses.

The attached Client Brief has all the client-specific details: business info, brand colors, fonts, pages to build, services, CTA copy, and contact form fields. Use those values everywhere in the build.

**Hosting:** SiteGround, FTP deployment (credentials in Client Brief)
**Forms:** Formspree (endpoint ID in Client Brief)
**Analytics:** Google Analytics GA4 (measurement ID in Client Brief)

---

## HOW SIMPLE RABBIT BUILDS SITES

### Stack
- Pure static HTML/CSS/JS — no React, no WordPress, no page builders
- One CSS file per page (inlined in `<style>`) — no external stylesheet
- Vanilla JS only, inlined in `<script>` at bottom of body
- FTP deployment via Python script (deploy.sh)
- Formspree for all contact forms (paid account — separate endpoint per form)
- Google Analytics GA4
- GitHub for version control

### File naming and structure
```
/
  index.html
  about.html
  portfolio.html   (or work.html, services.html — depends on client)
  contact.html
  thank-you.html
  404.html
  .htaccess        (clean URLs, 301 redirects, www→non-www)
  robots.txt
  sitemap.xml
  purge-cache.php
  deploy.sh
  logo.svg
  favicon.png
  /blog/           (individual article HTML files)
  /previews/       (OG images, portfolio preview images)
```

### Clean URLs
All pages use clean URLs (no .html extension). Configured via .htaccess:
```apache
Options -MultiViews
RewriteEngine On
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]
```

---

## DESIGN SYSTEM

### CSS Variables (use these in every file)

**The exact values for `--accent`, `--accent-dark`, `--accent-light`, `--font-display`, and `--font-body`
come from the Client Brief. Copy the complete `:root {}` block from there.**

The base variables below are the same on every project — never change these:

```css
:root {
  color-scheme: light only;

  /* ── Base — identical on every project ── */
  --black: #000;
  --white: #fff;
  --tone: #f7f7f8;           /* off-white background tint */
  --mid: #949698;            /* muted text, labels */
  --dark: #4c4c4b;           /* body text */
  --light-border: #dfe0e1;   /* borders, dividers */
  --green: #1a7a4a;          /* success states */
  --green-bg: #edf7f1;
  --green-border: #b3dfc6;

  /* ── From Client Brief — different for every project ── */
  --accent: [see Client Brief];
  --accent-dark: [see Client Brief];
  --accent-light: [see Client Brief];
  --font-display: [see Client Brief];
  --font-body: [see Client Brief];
  --font-mono: 'DM Mono', monospace;   /* stays DM Mono unless Client Brief specifies otherwise */
}
```

### Typography

**The Google Fonts `<link>` tag and specific font names come from the Client Brief.**
Use the preconnect + stylesheet link from the brief in every page `<head>`.

```css
/* Font roles — same on every project */
body { font-family: var(--font-body); -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4 { font-family: var(--font-display); font-weight: 400; }

/* Responsive headline sizing — same on every project */
font-size: clamp(44px, 6vw, 72px);   /* hero h1 */
font-size: clamp(32px, 4.5vw, 52px); /* section h2 */
font-size: clamp(22px, 3vw, 36px);   /* sub-heading h2 */
letter-spacing: -2px;                /* large headings */
letter-spacing: -0.5px;              /* medium headings */
```

### Overline labels (section markers)
```css
.overline {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
}
```

### Section spacing
- Desktop padding: `80px 48px` or `100px 48px` for major sections
- Mobile padding: `60px 24px`
- Max content width: `1100px` (or `720px` for article/text-heavy content)
- Section separation: `border-top: 1px solid var(--light-border)` or `border-bottom`

### Reveal animations
Every major section gets a reveal-on-scroll effect:
```html
<section class="reveal sp">...</section>
```
```css
.reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```
```js
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0 });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
// Fallback: force visible after 1.5s
setTimeout(() => document.querySelectorAll('.reveal:not(.visible)').forEach(el => el.classList.add('visible')), 1500);
```

---

## STANDARD COMPONENTS

### Navigation (sticky, with hamburger for mobile)
- Logo left, nav links + CTA button right
- Mobile: hamburger icon → full-screen overlay nav
- CTA button: black background, "Book a Call →"
- Sticky: `position: sticky; top: 0; z-index: 100;`
- Height: 64px

### Buttons

> Button style is **client-specific** — adapt everything below to match the Client Brief's design direction. Color, border-radius, shadows, and hover behavior should all reflect what the client asked for. The code below is the Simple Rabbit default; it is not a universal template.

```css
/* Primary — adapt color, radius, and shadow to client brand */
.btn-primary {
  background: var(--accent); color: var(--white);
  padding: 14px 40px; font-size: 14px; font-weight: 500;
  letter-spacing: 0.5px; text-decoration: none;
  display: inline-block; border-radius: 0; /* adjust per client */
  transition: background 0.2s;
}
.btn-primary:hover { background: var(--accent-dark); }

/* Ghost (outlined) — adjust border color and radius to client brand */
.btn-ghost {
  background: transparent; color: var(--dark);
  border: 1px solid var(--light-border);
  padding: 13px 28px; font-size: 14px; font-weight: 500;
  border-radius: 0; /* adjust per client */
  transition: all 0.2s;
}
.btn-ghost:hover { border-color: var(--accent); color: var(--accent); }
```

### Form inputs (underline style)
```css
.field-input {
  width: 100%; border: none;
  border-bottom: 1px solid var(--light-border);
  padding: 10px 0; font-size: 15px;
  background: transparent; outline: none;
  font-family: var(--font-body); color: var(--black);
  transition: border-color 0.2s;
}
.field-input:focus { border-bottom-color: var(--black); }
.field-input::placeholder { color: var(--mid); }

/* Textarea variant */
textarea.field-input {
  border: 1px solid var(--light-border);
  padding: 14px; resize: vertical; min-height: 130px;
}
textarea.field-input:focus { border-color: var(--black); }
```

### Two-column field grid
```css
.field-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0 48px; }
.field-grid .span-2 { grid-column: 1 / -1; }
@media (max-width: 768px) { .field-grid { grid-template-columns: 1fr; } }
```

---

## STANDARD PAGES

### Every page must have
- `<meta charset="UTF-8">`
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`
- Unique `<title>` — "[Page Topic] | [Client Name]"
- Unique `<meta name="description">` — 150–160 chars
- OG tags: og:title, og:description, og:type, og:url, og:image (1200×630)
- `<meta name="twitter:card" content="summary_large_image">`
- `<link rel="canonical" href="https://[domain]/[path]">`
- `<link rel="icon" ...>`
- Google Analytics snippet
- `color-scheme: light only` in `:root`

### Homepage (index.html)
Sections in order:
1. Nav
2. Hero — big headline, sub-headline, CTA button, optional trust element
3. Social proof strip — logos or "As seen in" badges (if applicable)
4. Services / what you do — 3-column card grid or feature rows
5. Process — numbered steps ("How it works")
6. Work / portfolio preview — 2-3 case study cards
7. About / founder — photo + copy + secondary CTA
8. Testimonials — 2-3 quotes with name/title
9. FAQ — accordion (optional)
10. Final CTA — big, centered, strong headline + "Book a Call" button
11. Footer

### Contact page (contact.html)
- H1 + brief subhead
- "How it works" — 2–3 steps (e.g. "Fill out the form. We'll schedule a call.")
- Contact form (Formspree): name, email, message + any qualifying fields
- Form submits to thank-you.html
- Add `novalidate` on `<form>`, validate with JS before submit

### Thank-you page (thank-you.html)
- Confirmation message
- What happens next (e.g. "Expect a reply within 1 business day")
- Newsletter signup (optional)
- Link back to homepage

### 404 page (404.html)
- Friendly message
- Link back to homepage and contact

### .htaccess (always include)
```apache
Options -MultiViews
RewriteEngine On

# Clean URLs
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^([^\.]+)$ $1.html [NC,L]

# www → non-www
RewriteCond %{HTTP_HOST} ^www\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [R=301,L]

# Force HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]

# Compression
<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>

# Cache headers
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/png "access plus 1 month"
  ExpiresByType image/jpeg "access plus 1 month"
  ExpiresByType image/svg+xml "access plus 1 month"
  ExpiresByType text/css "access plus 1 week"
  ExpiresByType application/javascript "access plus 1 week"
</IfModule>
```

---

## FORMS (FORMSPREE)

- Use Formspree for all forms — no backend needed
- Create a **separate endpoint for each form type** (contact, newsletter, intake, etc.)
- For file uploads: use `FormData` (multipart), no `Content-Type` header
- For text-only: use `JSON.stringify`, `Content-Type: application/json`
- Always add `_subject` field for readable email subjects
- Always `novalidate` on `<form>` + custom JS validation
- On success: redirect to thank-you page or show inline confirmation
- On error: show inline error message, re-enable submit button

```js
// Standard Formspree submit pattern
document.getElementById('contact-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const btn = this.querySelector('[type="submit"]');
  btn.disabled = true;
  btn.textContent = 'Sending…';
  try {
    const res = await fetch('https://formspree.io/f/[ENDPOINT_ID]', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
      body: JSON.stringify({
        name: this.name.value,
        email: this.email.value,
        message: this.message.value,
        _subject: 'New inquiry from ' + this.name.value,
      }),
    });
    if (res.ok) {
      window.location.href = '/thank-you';
    } else {
      throw new Error('Server error');
    }
  } catch {
    btn.disabled = false;
    btn.textContent = 'Send Message';
    alert('Something went wrong. Please email us directly.');
  }
});
```

---

## SEO CHECKLIST (per page)

- [ ] Unique title tag — includes primary keyword + brand name
- [ ] Meta description — 150–160 chars, includes primary keyword, compelling
- [ ] H1 — one per page, includes primary keyword
- [ ] H2s — support the H1, use secondary keywords naturally
- [ ] Canonical tag
- [ ] OG image — 1200×630px, saved to `/previews/`
- [ ] Schema markup on homepage (LocalBusiness or Service)
- [ ] Internal links — every page links to at least 2 others
- [ ] Image alt text — descriptive, not keyword-stuffed
- [ ] sitemap.xml — includes all public pages
- [ ] robots.txt — disallows nothing important
- [ ] No noindex on public pages

### LocalBusiness schema (homepage)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "[CLIENT BUSINESS NAME]",
  "description": "[ONE SENTENCE DESCRIPTION]",
  "url": "https://[DOMAIN]",
  "telephone": "[PHONE]",
  "email": "[EMAIL]",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[STREET]",
    "addressLocality": "[CITY]",
    "addressRegion": "[STATE]",
    "postalCode": "[ZIP]",
    "addressCountry": "US"
  },
  "areaServed": "[CITY/REGION]",
  "priceRange": "$$"
}
</script>
```

---

## DEPLOYMENT (deploy.sh)

Every project gets a `deploy.sh` at the root. Fill in the credentials from the Client Brief.

```bash
#!/bin/bash
MSG="${1:-Update site}"
DIR="$(cd "$(dirname "$0")" && pwd)"
echo "🚀 Deploying [CLIENT BUSINESS NAME]..."   # ← from Client Brief

python3 << PYEOF
import os
from ftplib import FTP

BASE   = "$DIR"
HOST   = "[FTP HOST]"       # ← from Client Brief
PORT   = 21
USER   = "[FTP USER]"       # ← from Client Brief
PASS   = "[FTP PASS]"       # ← from Client Brief
REMOTE = "[REMOTE PATH]"    # ← from Client Brief, e.g. domain.com/public_html

ROOT_FILES = [
    "index.html","about.html","contact.html","thank-you.html","404.html",
    "logo.svg","favicon.png",
    ".htaccess","purge-cache.php","sitemap.xml","robots.txt",
]
SUBDIRS = ["blog","previews"]

ftp = FTP()
ftp.connect(HOST, PORT, timeout=30)
ftp.login(USER, PASS)
ftp.set_pasv(True)
ftp.cwd(REMOTE)

def upload(ftp, local_path, remote_name):
    with open(local_path, 'rb') as f:
        ftp.storbinary(f"STOR {remote_name}", f)
    print(f"  ✓ {remote_name}")

def mkdir_safe(ftp, d):
    try: ftp.mkd(d)
    except: pass

for fname in ROOT_FILES:
    p = os.path.join(BASE, fname)
    if os.path.exists(p):
        upload(ftp, p, fname)

for d in SUBDIRS:
    mkdir_safe(ftp, d)
    local_d = os.path.join(BASE, d)
    if os.path.isdir(local_d):
        for f in sorted(os.listdir(local_d)):
            if f.startswith('.'): continue
            fp = os.path.join(local_d, f)
            if os.path.isfile(fp):
                upload(ftp, fp, f"{d}/{f}")

ftp.quit()
print("  FTP upload complete.")
PYEOF

echo "🧹 Purging server cache..."
curl -s "https://[DOMAIN]/purge-cache.php" | tr '\n' ' '   # ← domain from Client Brief
echo ""

echo ""
echo "📦 Pushing to GitHub..."
cd "$DIR"
git add -A
git commit -m "$MSG" 2>/dev/null && git push || echo "  (nothing new to commit)"

echo ""
echo "✅ Done! Live at https://[DOMAIN]"   # ← domain from Client Brief
```

### purge-cache.php (upload to server root)
```php
<?php
if (function_exists('sg_cachepress_purge_cache')) {
    sg_cachepress_purge_cache();
    echo "SiteGround cache purged.";
} else {
    echo "Cache plugin not active.";
}
```

---

## LAUNCH CHECKLIST

Run through this before handing off any site:

**Content**
- [ ] All placeholder text replaced with real content
- [ ] All images optimized (JPG < 200KB, PNG < 500KB, use WebP where possible)
- [ ] All links tested — no broken links, no links still going to `#`
- [ ] Contact form tested end-to-end (submit → confirmation email received)
- [ ] Thank-you page works after form submit

**SEO**
- [ ] Title tags unique on every page
- [ ] Meta descriptions unique on every page
- [ ] sitemap.xml submitted to Google Search Console
- [ ] Google Analytics confirmed receiving data
- [ ] Schema markup validated (schema.org validator)
- [ ] OG images display correctly (test with opengraph.xyz)

**Technical**
- [ ] Site loads on mobile without horizontal scroll
- [ ] Hamburger menu opens and closes correctly
- [ ] All pages load under 3 seconds on mobile (test with PageSpeed Insights)
- [ ] HTTPS working and www redirects to non-www (or vice versa)
- [ ] 404 page working (visit /nonexistent-page)
- [ ] Clean URLs working (visit /about not /about.html)
- [ ] No console errors

**Handoff**
- [ ] Client has login to Google Analytics
- [ ] Client has Formspree account with correct notification email
- [ ] Client change request form set up (if using Simple Rabbit client portal)
- [ ] deploy.sh credentials documented and tested
- [ ] GitHub repo set up (private)
