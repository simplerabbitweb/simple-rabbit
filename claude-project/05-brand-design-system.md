# Simple Rabbit — Brand Design System

## Overview

Simple Rabbit uses a two-palette system: a violet/dark palette for high-trust sections (nav, testimonials, footer, ACRR section) and a light/warm palette for content sections (hero, case studies, blog, offers). The typographic pairing is Instrument Serif (display/headings) + DM Sans (body/UI).

---

## CSS Custom Properties (Design Tokens)

Copy this `:root` block as the starting point for any new page or component:

```css
:root {
  /* Violet palette — used in: nav, leann section, testimonials, footer, ACRR section */
  --bg:       #474D73;   /* primary violet background */
  --bg-dk:    #2D3154;   /* darker violet (footer, deep sections) */
  --bg-mid:   #3B4168;   /* mid violet */
  --bg-lt:    #535980;   /* light violet */

  /* Light palette — used in: hero, featured-in, case studies, offers, blog */
  --white:    #FDFAF7;   /* warm white — main light background */
  --warm:     #F5F0EB;   /* warm off-white — alt light sections */
  --black:    #0A0905;   /* near-black — primary text on light */
  --mid-lt:   #7A756E;   /* medium gray — secondary text on light */

  /* Shared */
  --accent:   #AA737D;   /* dusty rose — accent, rarely used */
  --mid-vt:   #B0B5D0;   /* lavender-gray — body text on violet backgrounds */
  --rule-dk:  rgba(0,0,0,0.10);       /* dividers on light backgrounds */
  --rule-vt:  rgba(255,255,255,0.10); /* dividers on violet backgrounds */
  --rule-lt:  rgba(255,255,255,0.12); /* alternate divider on violet */

  /* Typography */
  --font-d:   'Instrument Serif', Georgia, serif;  /* display — headings, pull quotes */
  --font-b:   'DM Sans', system-ui, sans-serif;    /* body — UI, labels, body copy */
}
```

---

## Color Reference

### Violet Palette

| Token | Hex | Use |
|-------|-----|-----|
| `--bg` | `#474D73` | Primary violet background |
| `--bg-dk` | `#2D3154` | Footer, deepest sections |
| `--bg-mid` | `#3B4168` | Mid-depth violet sections |
| `--bg-lt` | `#535980` | Hover states, lighter violet panels |
| `--mid-vt` | `#B0B5D0` | Body text on violet, secondary labels |
| `--rule-vt` | `rgba(255,255,255,0.10)` | Borders/dividers on violet backgrounds |

### Light Palette

| Token | Hex | Use |
|-------|-----|-----|
| `--white` | `#FDFAF7` | Primary light background (slightly warm) |
| `--warm` | `#F5F0EB` | Alternate warm white for section contrast |
| `--black` | `#0A0905` | Primary text on light (near-black, warm) |
| `--mid-lt` | `#7A756E` | Secondary text on light, nav links |
| `--rule-dk` | `rgba(0,0,0,0.10)` | Borders/dividers on light backgrounds |

### Accent

| Token | Hex | Use |
|-------|-----|-----|
| `--accent` | `#AA737D` | Dusty rose — used sparingly for decorative detail |

---

## Typography

### Typefaces

**Display (headings, pull quotes, editorial):** Instrument Serif, Georgia, serif  
**Body (UI, nav, labels, paragraphs):** DM Sans, system-ui, sans-serif  

Both are loaded via Google Fonts:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
```

### Type Scale

**Hero / major section heading (H1/H2):**
```css
font-family: var(--font-d);
font-size: clamp(44px, 6.5vw, 88px);
line-height: 1.0;
letter-spacing: -2px;
font-weight: 300;
```

**Section heading (H2):**
```css
font-family: var(--font-d);
font-size: clamp(32px, 4vw, 60px);
line-height: 1.1;
letter-spacing: -1.5px;
font-weight: 300;
```

**Sub-section heading (H3):**
```css
font-family: var(--font-d);
font-size: clamp(24px, 3vw, 40px);
line-height: 1.15;
letter-spacing: -1px;
font-weight: 300;
```

**ACRR section H2:**
```css
font-family: var(--font-d);
font-size: clamp(28px, 3vw, 48px);
line-height: 1.1;
letter-spacing: -1.5px;
font-weight: 300;
```

**Body / paragraph:**
```css
font-family: var(--font-b);
font-size: 17px;
line-height: 1.8;
color: var(--mid-lt); /* on light backgrounds */
/* or */
color: var(--mid-vt); /* on violet backgrounds */
```

**Nav links:**
```css
font-size: 14px;
font-weight: 500;
letter-spacing: 1.5px;
text-transform: uppercase;
color: var(--mid-lt);
```

**Button / CTA label:**
```css
font-size: 15px;
font-weight: 600;
letter-spacing: 1.2px;
text-transform: uppercase;
font-family: var(--font-b);
```

**Category / eyebrow label:**
```css
font-size: 11px;
font-weight: 600;
letter-spacing: 2px;
text-transform: uppercase;
font-family: var(--font-b);
```

---

## Navigation

### Desktop Nav

```css
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--white);
  border-bottom: 1px solid var(--rule-dk);
}
.nav-inner {
  padding: 0 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 36px;
}
```

### Nav CTA Button

```css
.nav-cta {
  background: var(--black) !important;
  color: var(--white) !important;
  padding: 10px 24px;
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  transition: background 0.2s !important;
}
.nav-cta:hover { background: var(--bg) !important; }
```

### Nav Links

- Logo → `index.html`
- Services → `services.html`
- Case Studies → `case-studies.html`
- Articles → `articles.html`
- Apply to Work Together → `apply.html` (uses `.nav-cta` class)

---

## Button Styles

### Primary CTA (dark background, used on light sections)

```css
background: var(--black);
color: var(--white);
padding: 16px 48px;
font-size: 15px;
font-weight: 600;
letter-spacing: 1.2px;
text-transform: uppercase;
font-family: var(--font-b);
text-decoration: none;
display: inline-block;
/* No border-radius — sharp corners are intentional */
```

### Primary CTA (light background, used on violet sections)

```css
background: var(--white);
color: var(--black);
padding: 16px 48px;
font-size: 15px;
font-weight: 600;
letter-spacing: 1.2px;
text-transform: uppercase;
font-family: var(--font-b);
text-decoration: none;
display: inline-block;
```

**No border-radius on any buttons.** Square corners are part of the brand language.

---

## Layout Grid

### Standard two-column (50/50)

```css
display: grid;
grid-template-columns: 1fr 1fr;
min-height: 500px;
```

Mobile breakpoint (≤768px): collapse to single column.

### Content max-width

```css
max-width: 1200px;
margin: 0 auto;
padding: 0 64px; /* desktop */
padding: 0 24px; /* mobile */
```

---

## Section Patterns

### Light section

```css
background: var(--white); /* or var(--warm) for alternating */
padding: 100px 64px;
```

### Violet section

```css
background: var(--bg);
border-bottom: 1px solid var(--rule-vt);
padding: 100px 64px;
```

**Headings on violet sections:** `color: var(--white)`  
**Body text on violet sections:** `color: var(--mid-vt)`

---

## ACRR Section (appears at bottom of every blog post)

This component is injected via `acrr-section.js`. The source of truth is that file. Never hard-code this section into individual HTML files.

```html
<div id="acrr-section"></div>
<script src="../acrr-section.js"></script>
```

Visual: full-width two-column grid. Image fills the left column (flush, no padding, `object-fit: cover`). Right column on violet background (`--bg`) with H2, body paragraph, and white CTA button.

Placement in blog posts: directly above `<!-- MORE FROM THE BLOG -->` section.

---

## Animation / Reveal

All above-the-fold sections load immediately. Content sections below the fold use scroll reveal:

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

Triggered by an IntersectionObserver added to the body JS (in `tracking.js` or inline at page bottom).

---

## Imagery

**Photography style:**
- Real photos of real people (practitioners, patients) over stock
- Warm, natural light
- Not clinical (no stethoscopes, white coats, exam rooms unless intentional)
- Colors that complement the warm white palette

**Key images:**
- `hero-Leann.jpg` — homepage hero (Leann, professional but warm)
- `Logo-light.png` — logo for use on light backgrounds (root pages)
- `../Logo-light.png` — logo path for blog pages (relative up one level)
- `acrr-checklist.png` — ACRR section image (used in acrr-section.js via absolute path `/acrr-checklist.png`)

**Blog post images:** Fetched from Unsplash at publish time via auto-blog.py.

---

## Brand Voice (Summary)

**Tone:** Direct. Warm. Quietly confident.

**Avoid:** em-dashes, triple adjective lists, "not just X but Y," "But here's the thing," "elevate," "transform," "unlock," "journey," "cash-pay," anything that sounds like a spa, a life coach, or a generic marketing agency.

**Use:** Short sentences. Active voice. Specific nouns. Real outcomes ("ranks on Google") over abstract benefits ("drives visibility").

See `voice-guideline.md` for the full set of rules.

---

## File Naming and Paths

| Asset | Path |
|-------|------|
| Logo (root pages) | `Logo-light.png` |
| Logo (blog pages) | `../Logo-light.png` |
| ACRR image | `/acrr-checklist.png` (absolute — works everywhere) |
| Blog post images | `/blog/[slug]-hero.jpg` |
| New blog template | `/blog/NEW-POST-TEMPLATE.html` |

---

## Mobile Breakpoints

Primary breakpoint: `768px`

Key adjustments at ≤768px:
- Nav: hide desktop links, show hamburger
- Two-column grids: collapse to single column
- Section padding: reduce to `48px 24px` from `100px 64px`
- Hero font size: clamp starts at smaller value (e.g., `clamp(36px,5.5vw,72px)` instead of `clamp(44px,6.5vw,88px)`)
- Add `padding-left: 24px; padding-right: 24px` to hero sections with custom padding
