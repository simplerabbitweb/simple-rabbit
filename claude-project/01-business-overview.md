# Simple Rabbit — Business Overview

## What Simple Rabbit Does

Simple Rabbit is a one-person web studio run by Leann Frank, based in Bergen County, NJ. It builds custom websites for private-pay functional medicine, women's health, and concierge medicine practices — and keeps those sites running long after launch via ongoing care plans.

This is not a template shop, a Squarespace flipper, or a generalist agency. Every project is custom, every site is built for local SEO from day one, and every client has one person to call when something goes wrong.

---

## The ACRR Framework

All consulting and marketing work is organized around the ACRR framework:

**Attract. Convert. Retain. Refer.**

- **Attract** — Organic search, content strategy, site visibility, and targeted messaging that pulls in the right-fit patient before the first phone call
- **Convert** — Website copy, page architecture, calls to action, and trust signals that turn site visitors into booked appointments
- **Retain** — Patient experience, onboarding, and communication systems that keep patients engaged and coming back
- **Refer** — Practice reputation, patient satisfaction signals, and referral systems that generate word-of-mouth without asking for it

The ACRR Patient Acquisition Checklist (at simplerabbit.myflodesk.com/acrr-checklist) is the primary lead magnet. Practitioners score their practice across all four areas and identify their weakest link.

---

## Core Positioning

**One-sentence:** Simple Rabbit builds custom websites for private-pay women's wellness practices, and keeps them running long after launch.

**Three anchors that appear in all content:**
1. Custom, never templated — your practice isn't generic, your website shouldn't be either
2. Built to be found — local SEO is built in from day one, not bolted on later
3. Cared for, not abandoned — the launch is the start of the relationship, not the end

**North star sentence:** "You should never have to think about your website again."

---

## Who the Business Serves

Private-pay practitioners in functional medicine, women's health, hormone therapy, concierge medicine, and integrative/precision medicine. Almost always:
- Solo practitioner or very small practice (1–3 providers)
- Left or leaving the insurance system
- Smart, science-trained, skeptical of marketing
- Running a $650K–$2M+ private-pay practice
- Wants patients handled, not just more traffic

See `03-ideal-client-avatar.md` for the full client profile.

---

## Revenue Model

| Offer | Price Range | Type |
|-------|------------|------|
| ACRR Growth Strategy | $9,500–$12,500 | One-time project |
| ACRR Growth Accelerator | $22,000–$28,000 | One-time project |
| Monthly Retainer | $2,750–$4,500/mo | Recurring |
| Custom Website | $8,500–$15,000+ | Project (separate) |
| Care Plan | $250–$600/mo | Recurring |

Primary revenue driver is the consulting offer (Growth Strategy or Growth Accelerator) followed by a retainer. Website builds are a separate service line managed under the same studio brand.

See `02-offers-and-pricing.md` for full deliverables and positioning.

---

## Go-to-Market Strategy

### Primary Channel: Organic Content
- Blog on simplerabbit.studio (auto-published weekly via auto-blog.py, Thursdays 5 AM)
- Newsletter: "The Hutch" — educational, low-frequency, relationship-building
- LinkedIn and Instagram presence (content repurposed from blog)

### Secondary Channels
- Referrals from existing clients
- Medical conference networking (ACRR framework as educational content)
- Guest posts and podcast appearances in the functional medicine space

### Lead Magnet
- ACRR Patient Acquisition Checklist (Flodesk landing page → email sequence)
- Discovery call booked after lead magnet → proposal

### Sales Process
1. Lead downloads ACRR checklist
2. Email nurture sequence (positions Leann as the expert on private-pay patient acquisition)
3. Discovery call (30–45 min, focus on practice audit, not pitch)
4. Proposal delivered within 48 hours
5. Signed → onboarding call → project kickoff

---

## 90-Day Go-to-Market Roadmap

### Month 1: Foundation
- ACRR checklist live and promoted
- 4 blog posts targeting high-intent search terms
- LinkedIn content strategy launched (3x/week)
- Email sequence built (5-email nurture from checklist opt-in)
- Discovery call booking page live

### Month 2: Outreach
- Direct outreach to 20 functional medicine practices via LinkedIn
- 2 guest podcast pitches sent
- First case study published (Smooth Laser Center or equivalent)
- Referral program soft-launched to existing clients
- Blog SEO audit and optimization

### Month 3: Conversion
- First paid webinar or masterclass (ACRR framework overview)
- Retargeting ads to checklist downloaders
- Testimonial collection from first consulting clients
- Second case study in development
- Monthly reporting system established for retainer clients

---

## HIPAA Compliance Strategy

Simple Rabbit works adjacent to HIPAA but does not touch PHI (Protected Health Information). Key guardrails:

- **No patient data handled.** Websites built for practices, not for patient portals or EMR integrations.
- **Contact forms** use Formspree (no PHI fields). Appointment booking integrations (if needed) use HIPAA-compliant third-party tools (e.g., Jane App, SimplePractice) via embed/link only.
- **No medical advice** ever included in any website copy or content.
- **Business Associate Agreements (BAA):** Not required for website-only work, but offered if client's legal team requests.
- **Content compliance:** All blog and website copy avoids specific treatment claims, guarantees of patient outcomes, or language that could constitute medical advice.

---

## Operations

- **Location:** Bergen County, NJ (remote-first)
- **Team:** Solo (Leann Frank)
- **Tools:** WordPress, Claude API (blog automation), Unsplash (blog images), SiteGround (hosting), Formspree (forms), Flodesk (email)
- **Version control:** Git (all site files in `/Users/leannfrank/simple rabbit/`)
- **Deploy:** `bash deploy.sh "message"` from project root
- **Auto-blog:** macOS Launch Agent fires `auto-blog.py` every Thursday at 5 AM
- **Blog queue:** `blog-queue.json` — edit to add or reorder upcoming posts
- **Client comms:** Signed "Leann" (first name only)

---

## Key URLs

| Page | URL |
|------|-----|
| Homepage | simplerabbit.studio |
| Packages | simplerabbit.studio/packages |
| Apply | simplerabbit.studio/apply |
| Case Studies | simplerabbit.studio/case-studies |
| Blog | simplerabbit.studio/articles |
| ACRR Checklist | simplerabbit.myflodesk.com/acrr-checklist |
| Contact form endpoint | https://formspree.io/f/mojndlrg (NEVER change) |
| Apply form endpoint | https://formspree.io/f/mgoqyroq |
