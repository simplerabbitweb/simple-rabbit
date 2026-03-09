# Simple Rabbit Studio — Brand Guide SOP

A studio-wide reference for how Simple Rabbit approaches brand systems for every client project.
Use this alongside `kickoff-prompt.md` and a completed `client-brief-template.md` at the start of every build.

This document covers how to define, document, and apply a client's brand — from foundation through deliverables. It is not specific to any one client. Simple Rabbit is referenced only where it is the actor performing a task.

---

## 01 — Client Brand Foundation

Every project begins by documenting the client's brand foundation. This information comes from the intake form and discovery call. It lives in the Client Brief and drives every design and copy decision.

### What to Capture

- **Business name** and legal entity name (if different)
- **Industry / niche** — be specific (e.g., "family law attorney" not just "attorney")
- **Location** — city, state; service radius if relevant
- **Ideal client profile** — who they serve, where those people are in life or business
- **What makes them different** — the thing competitors cannot honestly claim
- **Brand vibe in three words** — pulled directly from intake; use these as a filter for every design decision
- **Guiding statement** — one to two sentences describing what the client does, for whom, and why it matters
- **Starting price or pricing approach** — affects how the site positions them

### How to Use It

The brand foundation is not decorative. It informs headline copy, hero messaging, section order, and which services to lead with. Before writing a single line of copy or choosing a color, read the foundation and ask: does this decision reflect who this client is and who they're trying to attract?

---

## 02 — Logo

### What to Collect

- **SVG format** — required; PNG fallback if SVG is unavailable
- **Light version** (white or reversed) — for use on dark backgrounds
- **Dark version** (black or full color) — for use on light backgrounds
- **Any existing brand standards** the client has already established

### How to Apply It

- Never stretch, recolor, skew, or apply effects to the logo
- Minimum display height: **32px** on screen
- On dark backgrounds: use the light/white version
- On light backgrounds: use the dark/primary version
- Clear space: maintain padding on all sides equal to at least the cap-height of the logo's letterforms
- Never place the logo directly on a busy photo — use a solid overlay or a clear section of the image
- Save as `logo.svg` in the project root; additional versions go in `/assets/` if needed

---

## 03 — Color System

### How to Build a Client's Color Palette

Every client gets a color system built from their brand. The palette is not a default — it is derived from the client's colors, industry, audience, and aesthetic.

#### Required Variables (all projects)

These base variables are structural and functional. They are the same on every project and are never changed.

| Variable | Value | Use |
|----------|-------|-----|
| `--black` | `#000` | Primary text, high-contrast UI elements |
| `--white` | `#fff` | Page backgrounds, reversed text |
| `--tone` | `#f7f7f8` | Off-white section backgrounds, card fills |
| `--dark` | `#4c4c4b` | Body copy, secondary text |
| `--mid` | `#949698` | Labels, meta text, placeholder text |
| `--light-border` | `#dfe0e1` | Section dividers, input borders, card borders |
| `--green` | `#1a7a4a` | Success states |
| `--green-bg` | `#edf7f1` | Success state backgrounds |
| `--green-border` | `#b3dfc6` | Success state borders |

#### Client Accent Variables (every project, always customized)

| Variable | Derived from | Use |
|----------|-------------|-----|
| `--accent` | Client's primary brand color | Links, overlines, CTAs, highlights, active states |
| `--accent-dark` | Primary color darkened ~15% | Hover states on accent elements |
| `--accent-light` | Primary color at ~15% opacity | Tinted backgrounds, borders on accent elements |

#### Additional Client Variables (when needed)

If the client's brand has a secondary color, a strong neutral, or a specific background color that differs from `--tone`, introduce additional variables. Name them clearly:

```css
--secondary: [hex];
--secondary-dark: [hex];
--bg-dark: [hex];   /* e.g. for a dark hero section */
```

Do not force a client's multi-color brand into a single accent variable. Build the palette the brand actually calls for.

### Color Hierarchy Principles

- **One primary action color per page.** Use `--accent` for CTAs, links, and overlines. If the client's brand color is dark, it can do what `--black` does on other projects.
- **Background colors are intentional.** `--tone` is the default off-white; change it to suit the client if their brand reads warmer, cooler, or richer.
- **Shadows and tints are tools.** Box shadows, color overlays, and tinted section backgrounds are all appropriate when the client's aesthetic calls for them.
- **The palette should match the client's audience.** A luxury interior designer and a family attorney do not share the same color energy. Let the intake responses and inspiration sites guide the direction.

### How to Pick Accent Variants

- **`--accent-dark`:** take the primary color and darken it 15–20% using a color picker (HSL: reduce lightness; or use the "shade" function in any color tool)
- **`--accent-light`:** take the primary color and drop opacity to ~12–18%, or mix it with white to create a tint — use for subtle backgrounds and borders

---

## 04 — Typography

### How to Select Fonts Per Client

Fonts come from the Client Brief. If the client has existing brand fonts, use them. If they have no preference, select fonts that suit their brand personality and audience.

#### Font Roles (consistent across all projects)

| Role | Variable | Used for |
|------|----------|---------|
| Display | `--font-display` | All headings (H1–H4), logo text if text-based |
| Body | `--font-body` | Body copy, buttons, navigation, inputs |
| Mono | `--font-mono` | Overline labels, tags, metadata, nav badges |

#### Defaults (when client has no font preference)

| Role | Font | Source |
|------|------|--------|
| Display | Optima | System font — no import needed |
| Body | Outfit | Google Fonts |
| Mono | DM Mono | Google Fonts |

These are starting points, not requirements. A warmer brand might call for a serif like Cormorant Garamond. A modern brand might use Inter or Neue Haas. A luxury brand might use a custom or paid typeface the client already owns.

#### Type Scale (consistent across all projects)

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

#### Typography Rules (all projects)

- All headings use `font-weight: 400` — never bold headings unless the client's brand specifically calls for it
- Large headings use negative letter-spacing
- Body copy uses the body font, never the display font
- The mono font is for labels only — not for body copy or headings
- Match headline casing to the client's brand voice (lowercase, sentence case, or title case — choose one, apply consistently)

#### Overline Labels

Used above section headings to orient the reader. Always mono font, always uppercase, always in `--accent`.

```css
.overline {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--accent);
}
```

---

## 05 — Voice & Tone

### How to Define a Client's Voice

Voice is built from the Client Brief — specifically: the brand vibe words, ideal client profile, and what the client wrote in the intake form (in their own words). The goal is to write copy that sounds like the client at their most confident and clear, not like a generic service business.

### Establishing the Voice

Ask: what three words did the client use to describe their brand? Map those to copy decisions:

| Vibe word | Copy direction |
|-----------|---------------|
| Warm | Second person, shorter sentences, conversational but not casual |
| Luxurious | Unhurried pacing, specific details, never hyperbolic |
| Direct | Short paragraphs, active voice, no qualifiers |
| Approachable | Simple words, questions, acknowledgment of the reader's situation |
| Expert / authoritative | Specificity over claims, results over adjectives |
| Bold | Strong verb-first sentences, short punchy headlines |

### Universal Writing Rules (all client projects)

**Always:**
- Write in second person — speak directly to the client's ideal client ("you", "your")
- Use the arrow `→` at the end of every CTA
- End sentences with periods. End CTAs with `→`. End nothing with `!`
- Be specific — use real results, real services, real timelines where available
- Write short paragraphs — 2–4 sentences max

**Never:**
- Em-dashes — don't use them anywhere
- "It's not X, it's Y" constructions — overused and hollow
- Choppy one-sentence staccato paragraphs — write in connected thoughts
- Exclamation points — on anything
- Filler words: "game-changing", "revolutionary", "innovative", "synergy", "seamless"
- Passive voice in headlines
- Vague claims without proof ("high-quality service" — say what result instead)

### CTA Copy

Always ends with `→`. Select based on the client's service type and audience relationship:

| Client type | Primary CTA |
|-------------|-------------|
| General service business | Book a Free Call → |
| Therapist / coach | Schedule a Consultation → |
| Interior designer | Start Your Project → |
| Attorney / legal | Request a Consultation → |
| Health / wellness | Book Your First Session → |
| Event / hospitality | Get a Quote → |
| Creative (photographer, etc.) | Let's Work Together → |

The selected CTA lives in the Client Brief and is used consistently across every page and every button on that client's site.

### Tone by Context

| Context | Tone |
|---------|------|
| Website headlines | Matches client voice — bold, punchy, or warm depending on brand |
| Website body copy | Warm, specific, direct — speaks to the ideal client's actual situation |
| Error messages / 404 | Friendly, brief, immediately helpful |
| Form confirmation | Warm, clear, tells them exactly what happens next |

---

## 06 — Design Principles

### Universal Standards (all projects)

These apply regardless of the client's aesthetic direction.

**1. Borders over margins for section separation**
Use `border-top` or `border-bottom` to separate sections, not large margin gaps. This keeps the layout structured.

**2. Whitespace is intentional**
Generous padding — 80–100px vertical on desktop, 60px on mobile. Content is never crowded. Let things breathe.

**3. Hierarchy through size, not weight**
Headings use `font-weight: 400` as a default. Distinction comes from size, spacing, and font choice — not bolding. Bold is used sparingly for key terms and UI labels.

**4. Reveal on scroll**
Every major section gets a reveal-on-scroll animation. The default is a subtle fade-up — `opacity: 0 → 1` with `translateY(20px → 0)` over 0.6s. Style and timing may vary per client.

**5. One primary action color per page**
Never compete for the eye with two accent colors. One brand color, one hover variant.

**6. Mobile-first**
Every layout is built and tested on mobile first. The sticky nav, mobile hamburger, and bottom CTA bar are present on every project.

### Client-Driven Decisions (varies per project)

These are not defaults — they come from the Client Brief and the client's direction.

| Decision | What drives it |
|----------|---------------|
| Button style | Client's brand vibe and UI Style Choices in the brief |
| Button color | Client's primary brand color — not always black |
| Border-radius | Client's aesthetic — 0 for sharp, 4–12px for soft, pill for rounded |
| Shadows | Client's aesthetic — fine to use on cards, buttons, nav when it suits the brand |
| Color of section backgrounds | Client's palette — can be full-bleed color, image, gradient, or neutral |
| Animation style | Client's preference — fade, slide, scale, stagger, or none |
| Card style | Client's aesthetic — border, shadow, or no-border depending on feel |
| Form input style | Can be underline-only or full-border depending on the client's visual tone |
| Display font | Client's brand — headings do not have a single default |

### Layout Constants (all projects)

- Max content width: **1100px** (full layouts), **720px** (text-heavy / articles / forms)
- Desktop section padding: `80px 48px` standard; `100px 48px` for hero or major CTA
- Mobile section padding: `60px 24px`
- Navigation height: **64px**

---

## 07 — Photography & Imagery

### What to Collect from the Client

- Professional headshots (preferred) — high-res JPG or PNG
- Workspace, studio, or location photos if applicable
- Any existing brand photography from prior shoots
- Product or service-in-action photos if the service is visual (interior design, finishes, events, etc.)

### How to Handle Photos

- **Real over stock.** Use the client's actual photos wherever possible. Stock is a last resort.
- **Consistent crop.** On any given page, all photos in a section use the same crop format (square, rectangle, or full-width). Avoid mixing.
- **No circular crops.** Use square or rectangular crops.
- **Warm and professional.** Natural light preferred. Avoid heavily filtered or oversaturated images.
- **On-brand color.** Photos should feel consistent with the client's palette — don't use a warm brand's hero photo if it reads cold and corporate.

### OG / Social Share Images

- Size: **1200 × 630px**
- Format: PNG, saved to `/previews/`
- Style: Clean background (white or `--tone`), brand typography, one clear headline, client logo

### Client Headshot Placement

- About page and founder section on homepage — always
- Consistent format for the section it appears in
- Never stretch or distort; always crop to the correct aspect ratio

---

## 08 — Quality Standards

These apply to every project regardless of client or aesthetic direction.

### Visual

- ✗ More than one accent color competing for attention on a single page
- ✗ Centered body copy (headlines and pull quotes only — never paragraphs)
- ✗ All-caps headings (overlines yes, section headings no)
- ✗ Clashing fonts — each font has one job; never mix their roles
- ✗ Unoptimized images — JPG under 200KB, PNG under 500KB, WebP preferred
- ✗ Inconsistent spacing — if the rhythm changes, it should be intentional

### Copy

- ✗ Em-dashes anywhere
- ✗ Exclamation points on CTAs, buttons, or headlines
- ✗ Passive voice in headlines
- ✗ Vague claims without proof ("we deliver results" — say what result)
- ✗ Bullet-point-heavy, choppy paragraph style — write in connected thoughts
- ✗ Jargon: "synergy", "innovative", "game-changing", "seamless", "holistic"
- ✗ Generic pain points not specific to this client's actual audience

### Technical

- ✗ Missing canonical tags
- ✗ Missing OG images
- ✗ Broken internal links
- ✗ Console errors on launch
- ✗ Forms that haven't been tested end-to-end
- ✗ Pages missing unique title tags or meta descriptions

---

## 09 — Client Deliverables

At the end of every project, Simple Rabbit delivers the following:

### Style Guide (internal reference)

A `style-guide.html` file in the client's project folder. This is an internal reference — not deployed to the live site. It shows:
- Color swatches with hex codes and CSS variables
- Typography samples at each scale level
- Button demos (primary and ghost)
- Form input demos
- Nav preview
- Spacing reference

Generate using the prompt in `client-brief-template.md`. Adapt all component demos — buttons, cards, inputs — to the client's actual design choices from the UI Style Choices section of the brief.

### Brand Guide PDF (client-facing)

A polished PDF delivered to the client after the site launches. This is their reference document for staying on-brand as they grow — for anything they create themselves: social posts, email templates, presentations, future marketing materials.

**Contents of the client-facing brand PDF:**
- Business name and logo usage rules
- Color palette — swatches, hex codes, and how to use each color
- Typography — fonts, weights, and where each is used
- Voice & tone — personality words, writing rules, what to avoid
- CTA copy and when to use it
- Social media handles and link

**How to generate it:** Use the PDF generation prompt in `client-brief-template.md` along with the completed brief. Simple Rabbit delivers this as `[client-slug]-brand-guide.pdf`.

---

## 10 — Studio Defaults

When a client has no preference in a given area, Simple Rabbit uses these defaults as a starting point. They are not required — override whenever the client's brand calls for something different.

| Decision | Default |
|----------|---------|
| Display font | Optima (system) |
| Body font | Outfit (Google Fonts) |
| Mono font | DM Mono (Google Fonts) |
| Button style | Solid fill, client's accent color |
| Button radius | 0 (sharp) |
| Card style | 1px border, no shadow |
| Section animation | Fade-up, 0.6s ease |
| Section background | White or `--tone` |
| Input style | Underline-only (full border on textarea) |
