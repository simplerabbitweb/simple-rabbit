# [CLIENT NAME] — Client Brief

Fill this out using the client's intake questionnaire responses before starting any build.
When starting the project in Claude Code, paste **both** this document and `kickoff-prompt.md` together.

---

## Client Overview

| Field | Value |
|-------|-------|
| Client name | [intake: Your Name] |
| Business name | [intake: Business Name] |
| Industry / niche | [intake: Industry / Niche] |
| City, State | [intake: Business Address — extract city + state] |
| Full address | [intake: Business Address — full, for schema markup] |
| ZIP code | [intake: Business Address — ZIP] |
| Business phone | [intake: Business Phone] |
| Contact email | [intake: Your Email — also where form submissions go] |
| Domain | [confirm with client] |
| Current site | [intake: Current Website] |
| Formspree endpoint ID | [create in Formspree dashboard → new form] |
| GA4 measurement ID | [from client's GA account, or create new] |
| FTP host | [from hosting credentials] |
| FTP user | [from hosting credentials] |
| FTP pass | [from hosting credentials] |
| Remote path | [e.g. yourdomain.com/public_html] |

---

## Brand Positioning

**Ideal client:**
[intake: Who is your ideal client?]

**What makes them different:**
[intake: What makes you different from competitors?]

**Brand vibe (3 words):**
[intake: Three words that describe your brand's vibe]

---

## Design System

### Colors (from intake)
> Paste what the client wrote here verbatim, then translate below.

[intake: Brand Colors — e.g. "Navy #002B5B, Cream #F5F0E8, Gold #C9A84C"]

### Fonts (from intake)
> Paste what the client wrote here verbatim, then translate below.

[intake: Brand Fonts — e.g. "Cormorant Garamond headings, Lato body" or blank]

---

### CSS Variables Block
> Translate the client's colors and fonts into the variables below.
> Keep all base variables exactly as shown. Only replace `--accent`, `--accent-dark`, `--accent-light`, and font variables.
>
> **To pick `--accent-dark`:** take the primary color and darken it ~15% (use a color picker or just desaturate slightly).
> **To pick `--accent-light`:** take the primary color and lighten it to ~15% opacity (great for tinted backgrounds and borders).

```css
:root {
  color-scheme: light only;

  /* ── Base — never change ── */
  --black: #000;
  --white: #fff;
  --tone: #f7f7f8;
  --mid: #949698;
  --dark: #4c4c4b;
  --light-border: #dfe0e1;
  --green: #1a7a4a;
  --green-bg: #edf7f1;
  --green-border: #b3dfc6;

  /* ── Client accent ── */
  --accent: [PRIMARY BRAND COLOR HEX];
  --accent-dark: [~15% DARKER — hover states];
  --accent-light: [~85% LIGHTER / TINT — backgrounds, borders];

  /* ── Client fonts ── */
  --font-display: '[HEADING FONT NAME]', [system fallback], serif;
  --font-body: '[BODY FONT NAME]', system-ui, sans-serif;
  --font-mono: 'DM Mono', monospace;
}
```

**Notes on font choices:**
- If the client has no font preference → use defaults: `Optima` display, `Outfit` body, `DM Mono` mono
- `--font-display` is used for all headings (h1–h4) and the logo
- `--font-body` is used for body copy, buttons, nav, and inputs
- `--font-mono` stays as DM Mono unless the client specifically uses another mono font

---

### Google Fonts Import
> Replace with the correct Google Fonts URL for this client's fonts.
> If using Optima (a system font), no `<link>` needed — just set the CSS variable.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=[FONT+NAME]:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=[SECOND+FONT]:wght@400;500&display=swap" rel="stylesheet">
```

> **Defaults (use if no client fonts):**
> ```html
> <link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
> ```
> (Optima is a system font — no import needed)

---

## Pages to Build

Check all that apply. Every project always gets the first five.

- [ ] `index.html` — Homepage
- [ ] `about.html` — About / Founder story
- [ ] `contact.html` — Contact + form
- [ ] `thank-you.html` — Post-form confirmation
- [ ] `404.html` — Error page
- [ ] `portfolio.html` or `work.html` — Case studies / portfolio (if client has this)
- [ ] `services.html` — Dedicated services page (if offerings are complex)
- [ ] `web-design-[city-state].html` — Local SEO landing page (recommended for most clients)
- [ ] `articles.html` — Blog index (if blog is planned)

**Notes on page decisions:**
[your notes — any pages that need special treatment or are being skipped]

---

## Contact Form Fields

From intake Section 03 — mark what the client selected:

- [ ] Name *(always included)*
- [ ] Email *(always included)*
- [ ] Phone number
- [ ] Service of interest
- [ ] How did you hear about us?
- [ ] Budget range
- [ ] Timeline / start date
- [ ] Message / tell us more

**Custom questions from intake:**
[intake: Any custom questions? — paste verbatim]

---

## Services & Pricing

From intake Section 04 — list each service the client entered:

| # | Service name | Short description | Pricing display |
|---|-------------|-------------------|-----------------|
| 1 | [name] | [description] | Starting at / Price range / By quote / Not shown |
| 2 | [name] | [description] | Starting at / Price range / By quote / Not shown |
| 3 | [name] | [description] | Starting at / Price range / By quote / Not shown |

> Add rows as needed. The pricing display column tells Claude how to present this on the site.

---

## Photography

**Has professional photos:** [Yes / Some / Not yet — from intake Section 05]

**Photo notes:**
[intake: Photo notes or Photo plan — paste verbatim]

**My notes:**
[your assessment — do we need stock? is there a photoshoot planned? what do we have to work with at launch?]

---

## Primary CTA

> Select the best fit from the table, or write a custom one.
> Always end with ` →`. Never use exclamation points.

| Client type | CTA |
|-------------|-----|
| General service business | Book a Free Call → |
| Therapist / coach | Schedule a Consultation → |
| Interior designer | Start Your Project → |
| Attorney / legal | Request a Consultation → |
| Health / wellness | Book Your First Session → |
| Event / hospitality | Get a Quote → |
| Creative (photographer, etc.) | Let's Work Together → |

**Selected CTA for this client:**
[write it here — e.g. "Schedule a Consultation →"]

---

## Inspiration & Competitive Context

**Sites the client loves (and why):**
[intake: Websites you love — paste verbatim]

**Competitor sites:**
[intake: Competitor websites — paste verbatim]

**My design direction notes:**
[your notes — what to lean into, what to avoid, overall aesthetic direction, anything that stood out from the intake responses]

---

## Social Media

From intake Section 06:

| Platform | Handle / URL |
|----------|-------------|
| Instagram | [handle or URL] |
| Facebook | [URL] |
| LinkedIn | [URL] |
| Twitter/X | [handle] |
| Other | [any others] |

---

## Additional Notes

**From intake (Anything Else section):**
[intake: Section 07 — paste verbatim]

**From discovery call:**
[your notes from the kickoff call — anything not captured in the form]

---

## Checklist Before Handing to Claude Code

- [ ] CSS variables block is filled in with real values (not placeholders)
- [ ] Google Fonts import URL is correct for this client's fonts
- [ ] Formspree endpoint ID is created and filled in
- [ ] FTP credentials are filled in
- [ ] GA4 measurement ID is filled in
- [ ] Pages to build section is checked
- [ ] Contact form fields are marked
- [ ] Primary CTA is selected
- [ ] Services table is filled in
- [ ] All `[intake: ...]` placeholders replaced with real content

---

## Generate the Client Style Guide

Once this brief is complete, paste it into Claude Code with the following instruction to generate a client-specific `style-guide.html`:

---

**Paste this prompt into Claude Code (with this brief attached):**

> Using the client brief above, generate a `style-guide.html` for this client. Follow the exact same structure as `/Users/leannfrank/Desktop/simple rabbit/style-guide.html` but make these specific changes:
>
> 1. **Title tag** → `[CLIENT BUSINESS NAME] — Style Guide`
> 2. **Page heading** → `[CLIENT BUSINESS NAME] Style Guide`
> 3. **Page subtitle** → `Brand reference for [CLIENT BUSINESS NAME]. Use these tokens across every page.`
> 4. **Google Fonts import** → replace with the import from this brief
> 5. **CSS `:root` variables** → replace the accent colors and font variables with the values from this brief; keep all base variables (black, white, tone, mid, dark, light-border, green) identical
> 6. **Color swatches** → update the accent/accent-dark/accent-light swatch boxes and hex labels to match this client's colors; leave all other swatches unchanged
> 7. **Typography samples** → update the font-family references in `.type-sample h1/h2/h3` to match this client's display font
> 8. **Nav logo preview** → replace "Brand Name" with "[CLIENT BUSINESS NAME]"
> 9. **Primary CTA button text** → replace "Start a Project →" with this client's CTA from the brief
> 10. **Pricing mono sample** → replace "Projects start at $4,800" with the client's starting price or "pricing by quote" if undisclosed
> 11. **Footer preview** → replace "Brand Name LLC · Location" with "[CLIENT BUSINESS NAME] · [CITY, STATE]"
> 12. **Save the file** → `style-guide.html` in the client's project root folder
>
> Everything else in the file stays exactly the same — all component demos, spacing values, animation code, breakpoints, and page structure examples are universal and do not change.

---

> **Note:** The style guide is a client-facing deliverable. It lives in the client's project folder as `style-guide.html`. It is not deployed to their live site — it's an internal reference file for you and the client to align on design before and during the build.
