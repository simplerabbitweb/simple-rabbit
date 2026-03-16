# Simple Rabbit — Build Checklist

A linear checklist for every new website project, from kickoff to post-launch.
Work through this in order. Check items off as you go.

---

## Phase 1 — Project Setup

- [ ] Create local project folder: `/[client-name]/`
- [ ] Initialize git repo: `git init`
- [ ] Create GitHub repo (private)
- [ ] Paste `kickoff-prompt.md` into Claude Code with client details filled in
- [ ] Confirm domain, hosting credentials, and FTP details
- [ ] Get Formspree endpoint ID (or create new form in Formspree dashboard)
- [ ] Get Google Analytics GA4 measurement ID
- [ ] Create `deploy.sh` from template (fill in FTP credentials)
- [ ] Create `.gitignore` — at minimum: `.env`, `node_modules/`, `.DS_Store`

---

## Phase 2 — Assets Collection

- [ ] Logo (SVG preferred, also PNG fallback)
- [ ] Favicon (favicon.png, 32×32 or 64×64)
- [ ] Brand colors (hex codes)
- [ ] Brand fonts (or confirm using Simple Rabbit system fonts)
- [ ] Professional photos — headshots, workspace, lifestyle (or plan for stock)
- [ ] Client-written copy (or interview client for homepage content)
- [ ] Testimonials (at least 2–3, with full name and title)
- [ ] OG / social share images — create 1200×630px per page (use `/previews/`)

---

## Phase 3 — File Structure

Create these files and folders before building:

```
/
  index.html
  about.html
  contact.html
  thank-you.html
  404.html
  .htaccess
  robots.txt
  sitemap.xml       ← build this last
  purge-cache.php
  deploy.sh
  logo.svg
  favicon.png
  /blog/            ← create even if no blog yet
  /previews/        ← OG images go here
```

Add additional pages based on client needs:
- `portfolio.html` / `work.html` — for any client with case studies or a portfolio
- `services.html` — if services are complex enough to warrant their own page
- `web-design-[city-state].html` — local SEO landing page (highly recommended)
- `articles.html` — if blog is planned

---

## Phase 4 — Build Pages

### Homepage (index.html)
- [ ] Nav + mobile hamburger
- [ ] Hero — headline, sub-headline, CTA button
- [ ] Social proof strip (logos, media mentions) — if available
- [ ] Services / what you offer (3-card grid or feature rows)
- [ ] Process (numbered steps)
- [ ] Portfolio preview (2–3 case study cards)
- [ ] About / founder section
- [ ] Testimonials (2–3)
- [ ] Final CTA section
- [ ] Newsletter signup — if applicable
- [ ] Footer
- [ ] Mobile CTA bar
- [ ] All OG / meta tags complete
- [ ] Schema markup (LocalBusiness JSON-LD)
- [ ] Reveal animations on sections
- [ ] Google Analytics
- [ ] Hamburger JS wired up

### About page (about.html)
- [ ] Founder story — personal, specific, not generic
- [ ] Why this work / mission
- [ ] Photo(s)
- [ ] Values or differentiators
- [ ] CTA → contact
- [ ] Standard meta / OG tags

### Contact page (contact.html)
- [ ] H1 + subhead
- [ ] "How it works" — 2–3 clear steps
- [ ] Contact form (Formspree) — name, email, message + qualifying fields
- [ ] Form submits to thank-you.html
- [ ] novalidate + custom JS validation
- [ ] Standard meta / OG tags

### Thank-you page (thank-you.html)
- [ ] Confirmation message
- [ ] "What happens next" — sets expectations
- [ ] Optional newsletter signup
- [ ] Link back to homepage
- [ ] noindex (optional — fine either way)

### 404 page (404.html)
- [ ] Friendly copy
- [ ] Links to homepage and contact
- [ ] Configured in .htaccess: `ErrorDocument 404 /404.html`

### Local SEO page (web-design-[city].html) — if applicable
- [ ] Primary keyword in H1, title, meta description
- [ ] City/region throughout the copy naturally
- [ ] Map embed or address callout
- [ ] Local testimonials if possible
- [ ] Schema markup for LocalBusiness
- [ ] Internal links to homepage and contact

---

## Phase 5 — Technical Setup

- [ ] `.htaccess` — clean URLs, HTTPS redirect, www redirect, caching, compression
- [ ] `robots.txt` — allow everything except client portal pages
- [ ] `sitemap.xml` — all public pages, correct lastmod dates
- [ ] `purge-cache.php` — uploaded to server root
- [ ] OG images created for all pages (1200×630px, saved to `/previews/`)
- [ ] Favicon tested in browser tab

---

## Phase 6 — Forms and Integrations

- [ ] Contact form — tested end-to-end (submit → email received at client address)
- [ ] Thank-you page redirect working after form submit
- [ ] Formspree notification email goes to correct address
- [ ] Newsletter form (if applicable) — separate Formspree endpoint
- [ ] Google Analytics confirmed receiving data (check Real-Time in GA4)

---

## Phase 7 — SEO Audit

Run through every public page:

- [ ] Unique title tag on every page
- [ ] Unique meta description on every page (150–160 chars)
- [ ] One H1 per page — includes primary keyword
- [ ] H2s support H1 — use secondary keywords naturally
- [ ] All images have descriptive alt text
- [ ] Canonical tags present and correct
- [ ] Internal links — every page links to at least 2 others
- [ ] No broken links
- [ ] Sitemap submitted to Google Search Console
- [ ] Schema markup validated at schema.org/SchemaValidator

---

## Phase 8 — Performance + Mobile QA

- [ ] All images optimized (JPG < 200KB, PNG < 500KB, WebP preferred)
- [ ] No unused CSS or JS
- [ ] Fonts loading from Google Fonts (preconnect tag included)
- [ ] Mobile layout tested at 375px, 430px, 768px widths
- [ ] No horizontal scroll on any page at mobile sizes
- [ ] Hamburger menu opens, links work, menu closes after clicking a link
- [ ] Tap targets (buttons, links) are at least 44×44px on mobile
- [ ] Mobile CTA bar visible and not covering page content
- [ ] PageSpeed Insights score: aim for 85+ on mobile, 95+ on desktop

---

## Phase 9 — Pre-Launch Review

- [ ] Read every page out loud — does it sound like the client? No placeholder text?
- [ ] All photos are real (no stock placeholders at launch)
- [ ] Copyright year in footer is correct
- [ ] Phone number and email in footer are correct and linked (tel:, mailto:)
- [ ] Social links go to the right profiles and open in a new tab
- [ ] "Book a Call" CTA goes to the correct contact page or booking link
- [ ] Privacy policy / terms linked if required (especially if collecting emails)
- [ ] Cookie banner needed? (if running ads or in EU — check with client)
- [ ] OG images test correctly: visit opengraph.xyz with the live URL

---

## Phase 10 — Deployment

- [ ] Run `./deploy.sh "Initial launch"` — confirm all files upload without errors
- [ ] Visit live site — check every page loads correctly
- [ ] Check that HTTPS is working (`https://` not `http://`)
- [ ] Check that www redirects to non-www (or vice versa)
- [ ] Check clean URLs work (`/about` loads, `/about.html` redirects)
- [ ] Check 404 page works (`/nonexistent`)
- [ ] Check contact form still works on live site (not just localhost)
- [ ] Check Google Analytics receiving live traffic
- [ ] Push final code to GitHub

---

## Phase 11 — Client Handoff

- [ ] Send client the live URL
- [ ] Confirm client has GA4 access
- [ ] Confirm client has Formspree account (or confirm notifications go to them)
- [ ] Send client the Simple Rabbit change request form link (`/client-changes`)
- [ ] Walk client through how to submit change requests
- [ ] Document login credentials (hosting, GA4, Formspree) in a secure note for client
- [ ] Explain turnaround times for content changes

---

## Post-Launch (ongoing)

- [ ] Monitor Google Search Console — submit sitemap, watch for crawl errors
- [ ] Check GA4 after first week — are goals (form submissions) tracking correctly?
- [ ] Client change requests handled within 3 business days
- [ ] Meta / LinkedIn tokens refreshed every 60 days (if social agent is set up)
- [ ] Annual review — update copyright year, refresh content, check for broken links

---

## Quick reference — common CTA copy by service type

| Client type | Primary CTA |
|-------------|-------------|
| General service business | "Book a Free Call →" |
| Therapist / coach | "Schedule a Consultation →" |
| Interior designer | "Start Your Project →" |
| Attorney / legal | "Request a Consultation →" |
| Health / wellness | "Book Your First Session →" |
| Event / hospitality | "Get a Quote →" |
| Creative (photographer, etc.) | "Let's Work Together →" |

Always use an arrow (`→`) at the end of CTA copy. Never use exclamation points.
