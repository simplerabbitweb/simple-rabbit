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

### UI Style Choices

Translate the client's vibe and inspiration into concrete style decisions. These drive how you write the CSS — they are not in the variables block but inform every component.

| Decision | Options | This client |
|----------|---------|-------------|
| Button corner radius | 0 (sharp), 4–6px (soft), 8–12px (rounded), full pill | [fill in] |
| Button style | Solid fill, outlined/ghost, text + arrow | [fill in] |
| Button color | Accent color, black, white, custom | [fill in] |
| Card style | Flat border, drop shadow, no border, colored bg | [fill in] |
| Card corner radius | 0 (sharp), 4–8px (soft), 12px+ (rounded) | [fill in] |
| Input style | Underline only, full border, filled bg | [fill in] |
| Animation preference | Subtle fade-up (default), slide-in, scale, stagger, none | [fill in] |
| Section backgrounds | White/tone only, full-bleed color, photo/texture | [fill in] |

**My design direction notes:**
[your notes — what to lean into, what to avoid, overall aesthetic, anything that stood out from intake or inspiration sites]

---

### CSS Variables Block
> Translate the client's colors and fonts into the variables below.
> The base structural variables (black, white, tone, mid, dark, light-border, green) stay the same on every project.
> The accent and font variables are always client-specific.
> Add additional custom variables if the client's palette needs more than one brand color.
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

> Using the client brief above, generate a `style-guide.html` for this client. Use `/Users/leannfrank/Desktop/simple rabbit/style-guide.html` as the structural reference, but adapt the design to match this client — not Simple Rabbit's own aesthetic.
>
> **Client-specific changes (required):**
> 1. **Title tag** → `[CLIENT BUSINESS NAME] — Style Guide`
> 2. **Page heading** → `[CLIENT BUSINESS NAME] Style Guide`
> 3. **Page subtitle** → `Brand reference for [CLIENT BUSINESS NAME]. Use these tokens across every page.`
> 4. **Google Fonts import** → replace with the import from this brief
> 5. **CSS `:root` variables** → replace accent colors and font variables with this brief's values; keep base structural variables (black, white, tone, mid, dark, light-border, green) the same
> 6. **Color swatches** → update all swatches to reflect this client's full palette
> 7. **Typography samples** → update font-family references to match this client's fonts
> 8. **Nav logo preview** → replace "Brand Name" with "[CLIENT BUSINESS NAME]"
> 9. **Primary CTA button text** → replace with this client's CTA
> 10. **Pricing mono sample** → replace with the client's starting price or "pricing by quote"
> 11. **Footer preview** → replace with "[CLIENT BUSINESS NAME] · [CITY, STATE]"
>
> **Design adaptation (required — this is a client site, not Simple Rabbit):**
> 12. **Button demos** → reflect the client's button style from the UI Style Choices above: use their brand color, their corner radius, and their hover state — not Simple Rabbit black
> 13. **Card demos** → use this client's card style (shadow, flat border, or no border) and corner radius
> 14. **Shadows** → include if the client's aesthetic calls for them
> 15. **Animation style** → match the client's animation preference from the brief
>
> 16. **Save the file** → `style-guide.html` in the client's project root folder

---

> **Note:** The style guide is an internal reference — it lives in the client's project folder as `style-guide.html` and is not deployed to the live site. Use it to align on design during the build.

---

## Generate the Client Brand Guide PDF

After the site launches, Simple Rabbit delivers a polished brand guide PDF to the client. This is their ongoing reference for staying on-brand in everything they create after handoff — social posts, email templates, presentations, future marketing materials.

**To generate the PDF:**

1. Open `_studio-sops/generate-brand-guide.py`
2. Fill in the `CLIENT` dict at the top with this client's information:
   - Copy colors from the CSS variables block above
   - Copy fonts from the Google Fonts section above
   - Copy voice rules from this brief
   - Copy logo rules from this brief
   - Set `"slug"` to a short kebab-case version of the business name (used for the filename)
3. Run: `python3 generate-brand-guide.py`
4. Output: `[client-slug]-brand-guide.pdf` in the `_studio-sops/` folder
5. Move or copy the PDF to the client's project folder and email it at handoff

**What the PDF includes:**
- Brand foundation (guiding statement, ideal client, brand vibe)
- Full color palette with swatches, hex codes, and usage notes
- Typography (fonts, source, and usage for each role)
- Voice & tone (always/never rules, CTA copy)
- Logo usage rules
- Quick reference card
