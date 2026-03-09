# Simple Rabbit — Design System Reference

A living reference for all CSS patterns, components, and design decisions.
Use this alongside `kickoff-prompt.md` for building client sites.

---

## Color Palette

| Variable | Value | Use |
|----------|-------|-----|
| `--black` | `#000` | Primary text, buttons, borders on hover |
| `--white` | `#fff` | Backgrounds, reversed text |
| `--tone` | `#f7f7f8` | Section backgrounds, card fills, hover states |
| `--accent` | `#0872cc` | Links, overlines, CTAs, highlights — **replace per client** |
| `--accent-dark` | `#0660ab` | Hover state for accent |
| `--accent-light` | `#c2cdff` | Accent tints, borders on accent elements |
| `--mid` | `#949698` | Subheadings, labels, meta text, placeholder text |
| `--dark` | `#4c4c4b` | Body copy, secondary text |
| `--light-border` | `#dfe0e1` | Section dividers, input borders, card borders |
| `--green` | `#1a7a4a` | Success states, "included" badges |
| `--green-bg` | `#edf7f1` | Success state backgrounds |
| `--green-border` | `#b3dfc6` | Success state borders |

**For Simple Rabbit's own site:** The palette above is fixed — change nothing.

**Adapting for a client:** The full palette is driven by the client's brand. At minimum, replace `--accent`, `--accent-dark`, and `--accent-light` with the client's brand color and its variants. If the client's brand has a strong secondary color, neutral tone, or specific background color, introduce additional variables as needed. Client sites are not required to use black as the primary button/CTA color — use whatever the client's brand calls for.

---

## Typography

### Font loading
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Font roles
| Font | Variable | Role |
|------|----------|------|
| Optima | `--font-display` | All headings (h1–h4), logo |
| Outfit | `--font-body` | Body copy, buttons, inputs, navigation |
| DM Mono | `--font-mono` | Overlines, labels, tags, nav badges, metadata |

### Responsive headline sizes
```css
/* Hero H1 */
font-size: clamp(44px, 6vw, 72px);
letter-spacing: -2px;
line-height: 1.06;

/* Section H1 / major heading */
font-size: clamp(36px, 5vw, 60px);
letter-spacing: -2px;
line-height: 1.1;

/* Section H2 */
font-size: clamp(32px, 4.5vw, 52px);
letter-spacing: -1px;
line-height: 1.1;

/* Sub-heading H2 */
font-size: clamp(22px, 3vw, 36px);
letter-spacing: -0.5px;
line-height: 1.2;

/* Card / component heading H3 */
font-size: 22px;
line-height: 1.3;
font-weight: 400;
```

### Body text
```css
/* Standard body */
font-size: 16px;
line-height: 1.8;
color: var(--dark);

/* Article body */
font-size: 17px;
line-height: 1.85;
color: var(--dark);

/* Small / hint text */
font-size: 13px;
line-height: 1.55;
color: var(--mid);
```

### Overline labels
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

## Layout

### Max widths
| Content type | Max width |
|-------------|-----------|
| Full site content | 1100px |
| Text-heavy (articles, forms) | 720px |
| Narrow (hero subheads, CTA sections) | 520–680px |

### Section padding
```css
/* Desktop */
padding: 80px 48px;    /* standard section */
padding: 100px 48px;   /* major CTA or hero */
padding: 60px 48px;    /* tighter section */

/* Mobile (max-width: 768px) */
padding: 60px 24px;
padding: 80px 24px;
```

### Section separation
Use borders, not margins between sections:
```css
border-bottom: 1px solid var(--light-border);
/* or */
border-top: 1px solid var(--light-border);
```

---

## Components

### Navigation

Standard sticky nav with mobile hamburger:

```html
<nav class="nav">
  <div class="nav-inner">
    <a href="/"><img src="logo.svg" alt="[Client Name]" style="max-height:56px;display:block;"></a>
    <div class="nav-links">
      <a href="/about">About</a>
      <a href="/portfolio">Portfolio</a>
      <a href="/articles">Articles</a>
      <a href="/contact" class="nav-link-hide">Contact</a>
      <a href="/contact" class="nav-cta">Book a Call</a>
    </div>
    <button class="hamburger" id="hamburger" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
<div class="mobile-nav" id="mobile-nav">
  <a href="/about">About</a>
  <a href="/portfolio">Portfolio</a>
  <a href="/articles">Articles</a>
  <a href="/contact">Contact</a>
  <a href="/contact" class="mobile-nav-cta">Book a Call</a>
</div>
```

```css
.nav { position: sticky; top: 0; background: var(--white); border-bottom: 1px solid var(--light-border); z-index: 100; }
.nav-inner { max-width: 1100px; margin: 0 auto; padding: 0 48px 0 16px; display: flex; align-items: center; justify-content: space-between; height: 64px; }
.nav-links { display: flex; align-items: center; gap: 32px; }
.nav-links a { font-size: 14px; color: var(--dark); text-decoration: none; transition: color 0.2s; }
.nav-links a:hover { color: var(--black); }
.nav-cta { background: var(--black) !important; color: var(--white) !important; padding: 10px 24px; font-size: 13px; font-weight: 500; }
.nav-cta:hover { background: var(--dark) !important; }
.hamburger { display: none; flex-direction: column; justify-content: center; gap: 5px; background: none; border: none; cursor: pointer; padding: 4px; }
.hamburger span { display: block; width: 22px; height: 2px; background: var(--black); transition: transform 0.3s, opacity 0.3s; }
.hamburger.open span:nth-child(1) { transform: translateY(7px) rotate(45deg); }
.hamburger.open span:nth-child(2) { opacity: 0; }
.hamburger.open span:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
.mobile-nav { display: none; position: fixed; top: 64px; left: 0; right: 0; bottom: 0; background: var(--white); z-index: 99; flex-direction: column; overflow-y: auto; border-top: 1px solid var(--light-border); }
.mobile-nav.open { display: flex; }
.mobile-nav a { font-size: 16px; color: var(--dark); text-decoration: none; padding: 20px 24px; border-bottom: 1px solid var(--light-border); }
.mobile-nav-cta { background: var(--black) !important; color: var(--white) !important; text-align: center; margin: 24px !important; border-bottom: none !important; font-weight: 500 !important; }
@media (max-width: 768px) { .hamburger { display: flex !important; } .nav-links { display: none !important; } }
```

```js
var hbtn = document.getElementById('hamburger'), mnav = document.getElementById('mobile-nav');
if (hbtn && mnav) {
  hbtn.addEventListener('click', function() {
    hbtn.classList.toggle('open');
    mnav.classList.toggle('open');
    document.body.style.overflow = mnav.classList.contains('open') ? 'hidden' : '';
  });
  mnav.querySelectorAll('a').forEach(function(a) {
    a.addEventListener('click', function() {
      hbtn.classList.remove('open');
      mnav.classList.remove('open');
      document.body.style.overflow = '';
    });
  });
}
```

---

### Buttons

```css
/* Primary — black fill */
.btn-primary {
  display: inline-block;
  background: var(--black); color: var(--white);
  padding: 14px 40px; font-size: 14px; font-weight: 500;
  letter-spacing: 0.5px; text-decoration: none;
  font-family: var(--font-body); border: none; cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover { background: var(--dark); }

/* Ghost — outlined */
.btn-ghost {
  display: inline-block;
  background: transparent; color: var(--dark);
  border: 1px solid var(--light-border);
  padding: 13px 28px; font-size: 14px; font-weight: 500;
  text-decoration: none; font-family: var(--font-body);
  cursor: pointer; transition: all 0.2s;
}
.btn-ghost:hover { border-color: var(--black); color: var(--black); }
```

**Rules:**
- Primary CTA text: always "Book a Call →" (for Simple Rabbit sites) — adjust per client
- The CSS above is the Simple Rabbit default. For client sites, adapt to match their brand: button color uses the client's primary color, border-radius matches their aesthetic (0 for sharp, 4–8px for soft, full pill for rounded), and shadows are fine if the design calls for it
- Hover states, transition timing, and animation style can all vary per client

---

### Form inputs

```css
.field-label { display: block; font-size: 13px; font-weight: 500; color: var(--dark); margin-bottom: 8px; }
.field-group { margin-bottom: 32px; }
.field-input {
  width: 100%; border: none; border-bottom: 1px solid var(--light-border);
  padding: 10px 0; font-size: 15px; background: transparent;
  outline: none; font-family: var(--font-body); color: var(--black);
  transition: border-color 0.2s;
}
.field-input:focus { border-bottom-color: var(--black); }
.field-input::placeholder { color: var(--mid); }
textarea.field-input {
  border: 1px solid var(--light-border); padding: 14px;
  resize: vertical; min-height: 130px;
}
textarea.field-input:focus { border-color: var(--black); }
.field-hint { font-size: 13px; color: var(--mid); margin-top: 8px; line-height: 1.55; }
```

---

### Footer

```html
<footer>
  <span class="footer-link" style="cursor:default;">© 2026 [Client Business] · [City], [State]</span>
  <div style="display:flex;gap:24px;align-items:center;">
    <a href="tel:[PHONE]" class="footer-link">[FORMATTED PHONE]</a>
    <a href="mailto:[EMAIL]" class="footer-link">[EMAIL]</a>
    <a href="[INSTAGRAM URL]" target="_blank" class="footer-link">Instagram</a>
    <a href="[FACEBOOK URL]" target="_blank" class="footer-link">Facebook</a>
  </div>
</footer>
```

```css
footer { border-top: 1px solid var(--light-border); padding: 32px 48px; display: flex; justify-content: space-between; align-items: center; }
.footer-link { font-size: 12px; color: var(--mid); text-decoration: none; transition: color 0.2s; }
.footer-link:hover { color: var(--black); }
@media (max-width: 600px) { footer { flex-direction: column; gap: 12px; text-align: center; padding: 24px; } }
```

---

### Mobile CTA bar (sticky, bottom)

Shown on mobile to keep a CTA always visible:

```html
<div class="mobile-cta-bar">
  <a href="/contact">Book a Call →</a>
</div>
```

```css
.mobile-cta-bar { display: none; position: fixed; bottom: 0; left: 0; right: 0; background: var(--black); z-index: 200; }
.mobile-cta-bar a { display: block; text-align: center; color: var(--white); text-decoration: none; font-size: 14px; font-weight: 500; padding: 18px; }
@media (max-width: 600px) { .mobile-cta-bar { display: block; } body { padding-bottom: 60px; } }
```

---

### Reveal animation

```css
.reveal { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }
.reveal.visible { opacity: 1; transform: translateY(0); }
```

```js
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
}, { threshold: 0 });
document.querySelectorAll('.reveal').forEach(el => obs.observe(el));
setTimeout(() => document.querySelectorAll('.reveal:not(.visible)').forEach(el => el.classList.add('visible')), 1500);
```

---

### Testimonial card

```html
<div class="testimonial-card">
  <p class="testimonial-text">"Quote goes here."</p>
  <div class="testimonial-author">
    <strong>[Name]</strong>
    <span>[Title / Business]</span>
  </div>
</div>
```

```css
.testimonial-card { padding: 40px; border: 1px solid var(--light-border); }
.testimonial-text { font-family: var(--font-display); font-size: 19px; line-height: 1.7; font-style: italic; color: var(--black); margin-bottom: 24px; font-weight: 400; }
.testimonial-author strong { display: block; font-size: 14px; font-weight: 600; margin-bottom: 4px; }
.testimonial-author span { font-size: 13px; color: var(--mid); font-family: var(--font-mono); letter-spacing: 1px; }
```

---

### Process steps (numbered)

```html
<div class="process-steps">
  <div class="process-step">
    <div class="step-num">01</div>
    <div class="step-body">
      <h3>[Step Title]</h3>
      <p>[Step description]</p>
    </div>
  </div>
  <!-- repeat -->
</div>
```

```css
.process-steps { display: flex; flex-direction: column; gap: 0; }
.process-step { display: flex; gap: 32px; align-items: flex-start; padding: 40px 0; border-bottom: 1px solid var(--light-border); }
.process-step:last-child { border-bottom: none; }
.step-num { font-family: var(--font-mono); font-size: 13px; letter-spacing: 2px; color: var(--mid); min-width: 28px; padding-top: 4px; }
.step-body h3 { font-size: 20px; line-height: 1.3; margin-bottom: 10px; }
.step-body p { font-size: 15px; line-height: 1.75; color: var(--dark); }
@media (max-width: 600px) { .process-step { flex-direction: column; gap: 12px; } }
```

---

## Page-level CSS reset (include on every page)

```css
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--font-body); color: var(--black); background: var(--white); -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4 { font-family: var(--font-display); font-weight: 400; }
a { color: inherit; }
img { max-width: 100%; display: block; }
```

---

## Google Analytics snippet (every page)

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=[GA4_ID]"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', '[GA4_ID]');
</script>
```

---

## Hidden / client-only pages

Pages not meant for public visitors:
- Add `<meta name="robots" content="noindex,nofollow">`
- Access via direct link only
- Include a "Client Portal" badge in the nav instead of normal nav links

```html
<span class="nav-badge">Client Portal</span>
```

```css
.nav-badge { font-family: var(--font-mono); font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: var(--mid); border: 1px solid var(--light-border); padding: 5px 12px; }
```
