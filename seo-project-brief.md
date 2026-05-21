# Simple Rabbit SEO Project Brief

This is the reference document for the Simple Rabbit SEO restructure project. Read this first before starting any session.

## The business

**Simple Rabbit Studio** is a one-person web design studio (owner: Leann Frank) based in Bergen County, NJ. Building custom WordPress sites, primarily on Divi 5 for client work, with some custom themes built via Claude Code.

**The niche pivot:** Simple Rabbit is moving from a broad service business focus to specializing in cash-pay functional medicine and women's health practices. This includes:
- Functional/integrative medicine
- Menopause specialists
- Concierge primary care
- Cash-pay psychiatry
- Holistic gynecology
- Fertility practices
- Aesthetics
- Lactation and postnatal care
- Pelvic floor physical therapy

The common thread: cash-pay healthcare practices that need patient-education-heavy, trust-signaling websites and don't deal with insurance.

**The local layer:** Bergen County, NJ remains the home base and only local geographic target. All other county pages (Sussex, Warren, Morris, Essex, Westchester, Hudson, Rockland, Passaic) were built under the old broad positioning and need to go.

## The current SEO problem (in plain terms)

Over roughly 3 months of Search Console data:
- 1,520 total impressions
- 23 total clicks
- 1.5% CTR
- Average position: 26.9 (page 3 of Google)

The homepage carries almost all the clicks (12 of 23). Every niche page gets impressions but zero clicks because they rank too low and lack supporting content.

**What's going wrong:**
1. Off-niche county pages are still indexed and getting impressions for searches that won't convert
2. Multiple URL versions are indexed (http vs https, www vs non-www, legacy .html), splitting authority
3. Niche pillar pages don't have a topical cluster of supporting blog content
4. The site is sending mixed signals: am I a local generalist or a national niche specialist?

## Search Console data snapshot

### Top queries pulling impressions (with zero clicks)
- "website design warren county nj" — 49 impressions
- "how to direct traffic to your website" — 46 impressions
- "simple rabbit" — 25 impressions
- "website development company sussex county" — 24 impressions
- "custom website design sussex county" — 23 impressions
- "custom website designers in sussex county" — 21 impressions
- "bergen county website design" — 20 impressions
- "functional medicine website design" — 20 impressions
- "ob gyn website design" — 16 impressions
- "seo bergen county" — 16 impressions

The pattern: off-niche county terms and generic web design searches dominate. Actual niche terms (functional medicine, ob/gyn) are present but lower.

### Top pages by impressions
- Homepage `/` — 216 impressions, 12 clicks (the only real winner)
- `/web-design-bergen-county-nj` — 151 impressions, 2 clicks
- `/functional-medicine-web-design` — 132 impressions, 0 clicks
- `/web-design-sussex-county-nj` — 97 impressions, 0 clicks
- `/blog/how-to-drive-traffic-to-your-website` — 96 impressions, 0 clicks
- `/web-design-warren-county-nj` — 93 impressions, 0 clicks
- `/about` — 87 impressions, 1 click
- `/web-design-morris-county-nj` — 79 impressions, 0 clicks
- `/holistic-gynecology-web-design` — 69 impressions, 0 clicks
- `/web-design-essex-county-nj` — 61 impressions, 0 clicks

### Duplicate URL indexing (proof of canonical issue)
Both `http://simplerabbit.studio/` and `https://simplerabbit.studio/` are appearing in Search Console. Legacy `.html` versions of `/about`, `/articles`, `/contact`, and `/portfolio` are also indexed.

## Page inventory

### Keep and strengthen (niche pillar pages)
- `/functional-medicine-web-design`
- `/holistic-gynecology-web-design`
- `/menopause-practice-web-design`
- `/concierge-primary-care-web-design`
- `/cash-pay-psychiatry-web-design`
- `/fertility-practice-web-design`
- `/aesthetics-web-design`
- `/lactation-postnatal-web-design`
- `/pelvic-floor-physical-therapy-web-design`

### Keep (local presence)
- `/web-design-bergen-county-nj`

### Redirect away from (off-niche geography)
- `/web-design-sussex-county-nj`
- `/web-design-warren-county-nj`
- `/web-design-morris-county-nj`
- `/web-design-essex-county-nj`
- `/web-design-westchester-county-ny`
- `/web-design-hudson-county-nj`
- `/web-design-rockland-county-ny`
- `/web-design-passaic-county-nj`

All redirect to `/web-design-bergen-county-nj` (or homepage if Bergen page doesn't fit contextually).

## Technical environment

- **CMS:** None — simplerabbit.studio is a **static HTML site** (no WordPress, no CMS)
- **Hosting:** SiteGround
- **Deploy pipeline:** Python FTP script (`deploy.sh`) + GitHub push
- **Redirects:** Handled entirely in `.htaccess` — no Redirection plugin, no WordPress needed
- **Note:** Divi 5 / WP are used for *client* builds, not for simplerabbit.studio itself

## Case studies and proof

- **Published niche case study:** Mona Perez of Smooth Laser Center (Washington Township) — currently live at `/blog/case-study-smooth-laser-center`
- **In-progress case study:** Dr. Lisa Milli, NP, Milli Women's Health & Menopause LLC (Old Tappan) — menopause practice. Will be the flagship when published.
- **Off-niche case study to watch:** `/blog/case-study-the-home-refresh` — currently gets 44 impressions and 2 clicks. Don't remove yet, but it's not aligned with the niche.

## Voice and writing rules (non-negotiable)

When proposing any new copy, follow these:
- No em-dashes anywhere
- No "if not X, then Y" sentence structure
- Never use the word "fluff"
- 8th grade reading level
- Conversational, not corporate
- Soft CTAs (no "Book now!" energy)
- Nothing AI-sounding: no "in today's landscape," no "leverage," no "navigate the complexities of," no "unlock," no "elevate," no "robust," no "synergy"
- Sound like a one-person studio owner who actually knows her clients, not a marketing agency

## Project constraints

- **Don't delete pages.** Use redirects and noindex. Deletion is permanent and we may want to repurpose content later.
- **Don't change design system, color palette, or visual identity.** This is structural and content-positioning work only.
- **Always show proposed changes before applying them to the live site.** Especially for redirects, internal link changes, and any homepage edits.
- **All changes are made directly in HTML files and `.htaccess`.** No builder dependencies — everything is plain code.
- **Work in sessions.** Don't try to do everything at once. Each session has a defined scope and deliverable.

## Lead magnets and conversion paths (for context)

The site supports two main lead magnets:
- "The Cash-Pay Practice Website Checklist"
- "Patient Onboarding Playbook"

These should be linked from relevant pillar pages and blog posts. The `/website-audit` page offers a paid audit ($297, applicable as credit toward a full build within 6 months). This is a key conversion path for warm leads.

## What "done" looks like

By the end of this project:
- One canonical URL version, all variants redirect cleanly
- Off-niche county pages redirected and out of the sitemap
- Niche pillar pages have strong titles, meta descriptions, and at least 3-5 supporting blog posts each linking to them
- Homepage signals the niche clearly within 2 seconds
- Navigation tells the niche story without geographic clutter
- Blog content either supports a pillar, gets noindexed, or gets rewritten to align
- Search Console starts showing improvement in 4-8 weeks: rising positions on niche queries, falling impressions on off-niche county queries (which is good, not bad)

## How to reference this brief

At the start of each session prompt, include: "Read `seo-project-brief.md` for full context before starting."

This way you don't have to paste the business context, voice rules, and constraints into every session.