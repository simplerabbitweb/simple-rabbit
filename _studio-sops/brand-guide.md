# Simple Rabbit Studio — Brand Guidelines

A complete reference for how Simple Rabbit looks, sounds, and shows up.
Use this whenever creating anything for the studio: website updates, social content, proposals, emails, or client-facing materials.

---

## 01 — Brand Foundation

### Who We Are

Simple Rabbit is a premium web design studio for women-owned service businesses. We build clean, modern websites with SEO baked in from day one, so high-paying clients find you, trust you, and book you without the runaround.

### Guiding Statement

> *Simple Rabbit provides website design and management for founders building toward six- and seven-figure growth who want a clean, modern online presence that reflects the quality of their work, attracts higher-paying clients, and supports a business that fits their life, not one that consumes it.*

### Who We Serve

Women-owned service businesses, typically 2–3 years in. They're established and good at what they do. Their website is the problem — it was built early, patched over time, and no longer reflects who they've become. They're attracting the wrong clients, undercharging, or both.

**Known challenges:**
- Website is a patchwork of additions over years — it shows
- No one managing it, so they can't make changes when they need to
- Embarrassed to share it with people they meet
- On every sales call, they have to explain what they do because the site doesn't

**What they want:**
- Better clients who don't question their rates
- High-value, qualified leads coming in consistently
- More time selling and delivering — less time wrestling with a website

**Why they haven't fixed it yet:**
- DIY (Squarespace, Wix) isn't an option — they're not designers and don't have the time
- They've been burned by designers who disappear after launch

### What Sets Us Apart

| Niche | Ease | Speed | Partnership |
|-------|------|-------|-------------|
| Built specifically for local service providers 2–3 years in | We handle everything — design, tech, copy direction | Sites live within 2 weeks. Changes done within 24 hours | We stay. This isn't a project, it's an ongoing partnership |

### Starting Price
$4,800

---

## 02 — Logo

**File:** `logo.svg` (root of every project)

**Usage rules:**
- Always use the SVG — never stretch, recolor, or apply effects
- Minimum height: 32px (digital)
- On dark backgrounds: use white version if available; on light backgrounds: use default
- Clear space: maintain at least the height of the logo's letterforms as padding on all sides
- Never place the logo on busy photos without a solid color overlay

---

## 03 — Color Palette

### Primary Colors

| Name | Variable | Hex | Use |
|------|----------|-----|-----|
| Black | `--black` | `#000000` | Primary text, all buttons, borders on hover, headings |
| White | `--white` | `#FFFFFF` | Page backgrounds, reversed text |
| Tone | `--tone` | `#F7F7F8` | Section backgrounds, card fills, subtle hover states |

### Brand Accent

| Name | Variable | Hex | Use |
|------|----------|-----|-----|
| Accent | `--accent` | `#0872CC` | Links, overlines, CTAs, highlights, active states |
| Accent Dark | `--accent-dark` | `#0660AB` | Hover state for anything using `--accent` |
| Accent Light | `--accent-light` | `#C2CDFF` | Tinted backgrounds, borders on accent elements |

### Neutrals

| Name | Variable | Hex | Use |
|------|----------|-----|-----|
| Dark | `--dark` | `#4C4C4B` | Body copy, secondary text |
| Mid | `--mid` | `#949698` | Subheadings, labels, meta text, placeholder text |
| Light Border | `--light-border` | `#DFE0E1` | Section dividers, input borders, card borders |

### Semantic

| Name | Variable | Hex | Use |
|------|----------|-----|-----|
| Green | `--green` | `#1A7A4A` | Success states, "included" indicators |
| Green BG | `--green-bg` | `#EDF7F1` | Success state backgrounds |
| Green Border | `--green-border` | `#B3DFC6` | Success state borders |

### Color Hierarchy Rules

- **Black and white carry the weight.** Accent is used sparingly — it draws the eye, so use it intentionally.
- **Tone (#F7F7F8)** is the only allowed background color other than white or black. Never use tinted grays or other off-whites.
- **Never use multiple accent colors on one page.** One brand color, one hover variant.
- **For client sites:** keep all base variables the same. Replace only `--accent`, `--accent-dark`, and `--accent-light` with the client's color.

---

## 04 — Typography

### Typefaces

| Font | Role | Variable | Source |
|------|------|----------|--------|
| **Optima** | Display — all headings (H1–H4), logo mark | `--font-display` | System font (macOS/iOS); fallbacks: Optima Nova, Candara, Segoe UI |
| **Outfit** | Body — body copy, buttons, inputs, navigation | `--font-body` | Google Fonts |
| **DM Mono** | Mono — overlines, labels, tags, nav badges, metadata | `--font-mono` | Google Fonts |

### Why These Fonts

- **Optima** is editorial and authoritative without being stiff. Its slightly flared strokes read as high-end without being precious. It projects confidence.
- **Outfit** is clean, readable, and modern. It doesn't compete with Optima — it supports it.
- **DM Mono** adds precision and structure. Used exclusively for small labels and metadata, never body copy.

### Google Fonts Import (for Outfit + DM Mono)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

*(Optima is a system font — no import needed.)*

### Type Scale

| Element | Size | Weight | Letter Spacing | Line Height |
|---------|------|--------|----------------|-------------|
| Hero H1 | `clamp(44px, 6vw, 72px)` | 400 | -2px | 1.06 |
| Section H1 | `clamp(36px, 5vw, 60px)` | 400 | -2px | 1.1 |
| Section H2 | `clamp(32px, 4.5vw, 52px)` | 400 | -1px | 1.1 |
| Sub-heading H2 | `clamp(22px, 3vw, 36px)` | 400 | -0.5px | 1.2 |
| Card H3 | 22px | 400 | 0 | 1.3 |
| Body | 16px | 400 | 0 | 1.8 |
| Article body | 17px | 400 | 0 | 1.85 |
| Small / hint | 13px | 400 | 0 | 1.55 |
| Overline | 11px | 400 | 2px | — |
| Button | 14px | 500 | 0.5px | — |

### Overline Label Style

Used above section headings to orient the reader. Always DM Mono, always uppercase, always in `--accent`.

```
OVERLINE EXAMPLE — 11PX · DM MONO · 2PX TRACKING · ALL CAPS · ACCENT COLOR
```

### Typography Rules

- All headings use `font-weight: 400` — never bold headings
- Large headings use negative letter-spacing (`-2px` for hero, `-1px` for section)
- Body copy uses Outfit, not Optima
- Never use Optima for body paragraphs
- DM Mono is for labels only — not for body copy or headings
- Headlines on the website use **lowercase** (e.g., "charge more", "book a call")

---

## 05 — Voice & Tone

### Brand Personality

Simple Rabbit sounds like a sharp, experienced woman who has been in the room — and knows exactly what she's talking about. She's direct without being cold. Warm without being soft. She doesn't perform expertise; she demonstrates it.

**In three words:** Confident. Direct. Invested.

### Core Messaging

| Message | How We Say It |
|---------|---------------|
| Your website is costing you clients | "You're getting clients. Just not the right ones." |
| We build premium, conversion-focused sites | "Websites that attract the clients you want to work with." |
| We stay after launch | "Most designers launch your site and vanish. We stay." |
| Your prices aren't the problem | "It's not your prices. It's a DIY website that's misaligned." |
| We work with women building serious businesses | "Built for women ready to stop playing small." |

### Writing Rules

**Always:**
- Write in second person — speak directly to *her* ("you", "your")
- Use the arrow `→` at the end of every CTA
- End sentences with periods. End CTAs with `→`. End nothing with `!`
- Use lowercase for headline copy on the website ("book a call", "charge more")
- Be specific — use real results, real client names, real timelines
- Write short paragraphs — 2–4 sentences max

**Never:**
- Em-dashes — don't use them anywhere
- "It's not X, it's Y" constructions — this is overused and sounds like a social media template
- Choppy one-sentence staccato paragraphs — write in connected, flowing thoughts
- Exclamation points — on anything
- Filler phrases: "game-changing", "revolutionary", "innovative", "synergy"
- Passive voice when active is available
- Generic claims without proof ("we're the best" — say what result instead)

### CTA Copy

Always ends with `→`. Select based on service type:

| Client type | Primary CTA |
|-------------|-------------|
| General service business | Book a Free Call → |
| Therapist / coach | Schedule a Consultation → |
| Interior designer | Start Your Project → |
| Attorney / legal | Request a Consultation → |
| Health / wellness | Book Your First Session → |
| Event / hospitality | Get a Quote → |
| Creative | Let's Work Together → |

**Simple Rabbit's own CTA:** Book a Free Call →

### Tone by Context

| Context | Tone |
|---------|------|
| Website headlines | Bold, punchy, lowercase |
| Website body copy | Warm, specific, direct — speaks to her pain |
| Social media | Confident, educational, behind-the-scenes honest |
| Email to client | Warm, clear, professional — no jargon |
| Proposals / scope docs | Precise, thorough, no fluff |
| Error messages / 404 | Friendly, brief, immediately helpful |

### Content Activation (what to write about and when)

| Pain point | Opening frame |
|------------|---------------|
| People don't want to pay your prices | "You're feeling discouraged because the people you have sales calls with cringe at your prices." |
| People have no clue what you do | "You're frustrated because on every sales call you have to explain what you do and don't do." |
| You're embarrassed to share your website | "You're a high-end service provider, but you're embarrassed to share your website. You know it's bad." |
| You're attracting the wrong clients | "Your website doesn't filter people at the right level, so you end up saying yes to projects that drain time, energy, or profit." |

---

## 06 — Design Principles

### The Visual Language

Simple Rabbit's aesthetic is minimal, editorial, and premium. Think high-end magazine meets boutique studio — clean layouts, deliberate whitespace, sharp edges, and one strong accent color.

### Principles

**1. Borders, not margins**
Sections are separated with `1px solid var(--light-border)` — never big bottom margins or padding gaps. This creates the editorial, structured feel.

**2. Sharp corners everywhere**
No border-radius on buttons, cards, inputs, or containers. Everything is square. Rounded corners signal casual; sharp corners signal precision.

**3. Black is the primary color**
Buttons, borders on hover, most headings, and all CTAs use pure black (`#000`). Accent blue is used for links, overlines, and interactive cues — it's supporting, not dominant.

**4. Whitespace is intentional**
Generous padding (80–100px vertical on desktop, 60px on mobile). Content is never crowded. Let things breathe.

**5. One font does one job**
Optima for headings only. Outfit for everything else readable. DM Mono for labels only. Never mix their jobs.

**6. Reveal on scroll**
Every major section fades up into view as the user scrolls. The animation is subtle — `opacity: 0 → 1` with `translateY(20px → 0)` over 0.6s. Not flashy; respectful.

**7. Hierarchy through size, not weight**
Headings are `font-weight: 400`. Distinction comes from size and spacing, not bold. Bold is used sparingly — only for names, key terms, or UI labels.

### Layout Rules

- Max content width: **1100px** (full layouts), **720px** (text-heavy / articles / forms)
- Desktop section padding: `80px 48px` standard; `100px 48px` for hero or major CTA
- Mobile section padding: `60px 24px`
- Navigation height: **64px**

### Component Rules

- **Buttons:** Square corners. Primary = black fill. Ghost = transparent with border. No gradients.
- **Forms:** Underline-only inputs (no box border) — except textarea, which uses a full border
- **Cards:** `1px solid var(--light-border)` border. No shadow, no radius.
- **Testimonials:** Optima italic for the quote. DM Mono for the attribution. No quote marks that are graphically oversized.
- **Process steps:** Numbered with DM Mono `01`, `02` etc. Separated by `border-bottom`, not cards.

---

## 07 — Photography & Imagery

### Photo Style

- **Real, not stock.** Leann's headshots and workspace photos are used on the Simple Rabbit site. Client work uses actual screenshots of live sites.
- **Warm and professional.** Natural light preferred. Avoid overly styled or corporate-feeling shots.
- **On-brand color.** Photos should feel consistent with the palette — warm neutrals, not saturated or heavily filtered.

### Headshot Usage (Leann)

Available files: `Leann.jpg`, `Leann-2.jpg`, `Leann-3.jpg`, `Leann-4.jpg`

- Use on About page and Founder section on homepage
- Always cropped to a consistent format for the section it appears in
- No circular crops — use square or rectangular

### OG / Social Share Images

- Size: **1200 × 630px**
- Format: PNG, saved to `/previews/`
- Style: Clean background (white or `--tone`), brand typography, one clear headline

### Portfolio Screenshots

- Full-width desktop screenshots of live client sites
- Saved to `/previews/` folder
- No device mockup frames required — clean crops are preferred

---

## 08 — Digital Applications

### Website (simplerabbit.studio)

- Every page has a sticky nav (64px), mobile hamburger, and mobile CTA bar
- Every section has a reveal animation
- Primary CTA: **Book a Free Call →** → links to `/contact`
- Footer: copyright, phone, email, social links
- No `.html` extensions in URLs (clean URLs via `.htaccess`)

### Social Media

- **Instagram:** Behind-the-scenes, client results, design education, positioning
- **LinkedIn:** Thought leadership, business case for premium websites
- **Facebook:** Community, client work announcements
- **X/Twitter:** Short-form takes on web design, pricing, SEO

All CTAs in social posts link to `simplerabbit.studio/contact`

### Email

- From: `hello@simplerabbit.studio`
- Subject lines: Direct and specific — no clickbait, no all-caps
- Signature: Name, title, website URL, one CTA link max
- No fancy HTML email templates — plain text or simple single-column layout

---

## 09 — What Not to Do

**Visual:**
- ✗ Rounded corners on any UI element
- ✗ Drop shadows on cards or buttons
- ✗ Gradients
- ✗ More than one accent color per page
- ✗ Centered body copy (headlines only)
- ✗ All-caps headings (overlines yes, headings no)
- ✗ Stock photos on the Simple Rabbit site

**Copy:**
- ✗ Em-dashes anywhere
- ✗ "It's not X, it's Y" sentence structures
- ✗ Exclamation points on CTAs or buttons
- ✗ Passive voice in headlines
- ✗ Vague claims without proof ("premium results" — say what result)
- ✗ Bullet-point-heavy, choppy paragraphs
- ✗ Jargon — "synergy", "innovative", "game-changing"

**Brand:**
- ✗ Adding taglines that don't appear in brand materials
- ✗ Using Optima for body copy
- ✗ Using DM Mono for anything longer than a label
- ✗ Adjusting the base color palette (--black, --white, --tone, --mid, --dark, --light-border are fixed)

---

## 10 — Client Proof Points

Use these in proposals, pitches, social content, and the website:

**Laura Gonzalez, Education Attorney**
- Started getting calls through Google Search within 2 weeks of launch
- Professional presentation began booking high-value clients
- Established herself as an expert in her field

**Melissa Simon, Full-Service Home Organizer**
- Consistent flow of leads through the website
- Launched email newsletter to nurture leads — added to site post-launch
- Booked a high-paying mansion project — continues to be fully booked
- Fully focused on running her business instead of managing her website

**Jessica Semioli (testimonial)**
> "When Leann sent me my logo and website, it was like she had the exact picture of what was in my brain."

**Lauren Goodwin, Decorative Finishes (testimonial)**
> "Leann was easy to work with, and she could read my mind. Now I have a website that represents my services beautifully, and I couldn't be happier with the outcome and the ease with which it all came together."

---

## Quick Reference

| Need | Answer |
|------|--------|
| Primary brand color | `#0872CC` |
| Display font | Optima (system) |
| Body font | Outfit (Google) |
| Mono / label font | DM Mono (Google) |
| Primary CTA | Book a Free Call → |
| Email | hello@simplerabbit.studio |
| Website | simplerabbit.studio |
| Starting price | $4,800 |
| Client niche | Women-owned service businesses, 2–3 years in |
| Guiding principle | Minimal, editorial, premium — never casual |
