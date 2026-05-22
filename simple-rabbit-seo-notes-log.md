# Simple Rabbit SEO Notes Log

Running log of SEO decisions, changes, and recommendations for simplerabbit.studio. Each note gets a number, a status, and a date when deployed.

**Statuses:** `pending` · `approved` · `✅ DEPLOYED [date]` · `skipped`

---

## Session 1–2: URL structure + redirects

**001** — Added 8 county page redirects to `.htaccess` (essex, hudson, morris, passaic, sussex, warren, rockland, westchester → /web-design-bergen-county-nj) · ✅ DEPLOYED 2026-05-21

**002** — Removed Bergen County → /articles redirect from `.htaccess` · ✅ DEPLOYED 2026-05-21

**003** — Added `noindex, nofollow` to 8 off-niche county HTML files · ✅ DEPLOYED 2026-05-21

**004** — Added `noindex, nofollow` to `thank-you.html` · ✅ DEPLOYED 2026-05-21

**005** — Cleaned `sitemap.xml`: removed 5 retired blog posts and 8 off-niche county pages (51 → 38 URLs) · ✅ DEPLOYED 2026-05-21

**006** — Corrected WordPress references in `seo-project-brief.md` (site is static HTML, not WP) · ✅ DEPLOYED 2026-05-21

---

## Session 4: FM and HG page rewrites

**007** — FM page title: 76 chars → 46 chars ("Functional Medicine Web Design | Simple Rabbit") · ✅ DEPLOYED 2026-05-22

**008** — FM page meta: 165 chars → 146 chars · ✅ DEPLOYED 2026-05-22

**009** — FM page: remove both WordPress references, replace sidebar line with /website-audit CTA · ✅ DEPLOYED 2026-05-22

**010** — FM page: add telehealth/virtual FAQ entry · ✅ DEPLOYED 2026-05-22

**011** — FM page: add /website-audit mention to redesign FAQ · ✅ DEPLOYED 2026-05-22

**012** — FM page: add link to /blog/how-to-rank-for-functional-medicine-near-me in local SEO FAQ · ✅ DEPLOYED 2026-05-22

**013** — HG page title: 60 chars → 46 chars ("Holistic Gynecology Web Design | Simple Rabbit") · ✅ DEPLOYED 2026-05-22

**014** — HG page meta: 175 chars → 144 chars · ✅ DEPLOYED 2026-05-22

**015** — HG page: remove both WordPress references · ✅ DEPLOYED 2026-05-22

**016** — HG page: add patient specificity paragraph (PCOS, endometriosis, perimenopause) to Problem section · ✅ DEPLOYED 2026-05-22

**017** — HG page: add /website-audit FAQ entry · ✅ DEPLOYED 2026-05-22

**018** — HG page: add local keywords blog link to SEO FAQ · ✅ DEPLOYED 2026-05-22

---

## Session 5: Cluster audit + internal linking

**019** — Noindex `blog/case-study-the-home-refresh` (off-niche, home organizing) · ✅ DEPLOYED 2026-05-22

**020** — Noindex `blog/how-to-drive-traffic-to-your-website` (attracts wrong searcher — DIY business owners, 96 impressions, 0 conversions) · ✅ DEPLOYED 2026-05-22

**021** — `how-to-rank-for-functional-medicine-near-me` → added link to `/functional-medicine-web-design` · ✅ DEPLOYED 2026-05-22

**022** — `why-menopause-practice-websites-dont-rank-locally` → added link to `/menopause-practice-web-design` · ✅ DEPLOYED 2026-05-22

**023** — `how-womens-wellness-practices-get-found-on-google` → added link to `/holistic-gynecology-web-design` · ✅ DEPLOYED 2026-05-22

**024** — Fixed 6 broken internal links: replaced `/blog/google-business-profile-not-getting-clicks` with `/blog/google-business-profile-virtual-practice` in 5 posts; removed referencing paragraph from `google-business-profile-virtual-practice` post · ✅ DEPLOYED 2026-05-22

**025** — `local-keywords-your-wellness-practice-should-target` → add links to FM, HG, and menopause pillar pages · `pending`

**026** — `google-business-profile-virtual-practice` → add links to FM and menopause pillar pages · `pending`

**027** — `diy-website-wrong-price` → add link to FM pillar (opening para already names FM and women's health — just needs the link) · `pending`

**028** — `local-seo-for-private-pay-practices` → add HG and menopause pillar links (already links to FM) · `pending`

**029** — Priority 3 general posts: add FM pillar link to charge-more, convert-visitors, 5-things-premium-clients, website-losing-you-clients, hesitate-before-sending · `pending`

**030** — `why-your-practice-isnt-showing-up-in-local-map-pack` → add links to /web-design-bergen-county-nj and /pelvic-floor-physical-therapy-web-design · `pending`

---

## Session 6: Navigation + homepage (proposals + QA)

**031** — Nav: replace "Services" top-level item with "Specialties ▾" dropdown listing all 9 pillar pages + /website-audit + /services · `pending`

**032** — Nav: add Bergen County link to footer · `pending`

**033** — QA: 15 redirects verified — all pass · `✅ DEPLOYED 2026-05-21` (verified, no action needed)

**034** — QA: sitemap clean — no retired URLs · `✅ DEPLOYED 2026-05-21` (verified, no action needed)

**035** — QA: canonical tags correct on all spot-checked pages · `✅ DEPLOYED 2026-05-21` (verified, no action needed)

---

## Pass 1: Homepage quick wins

**127** — Homepage overline: "Custom websites · Local SEO · Lead generation · Care plans" → "Websites for functional medicine + women's health practices" · ✅ DEPLOYED 2026-05-21

**128** — Homepage hero subheadline: replaced process description with niche-named subheadline ("Custom websites for functional medicine, menopause, and women's health practices...") · ✅ DEPLOYED 2026-05-21

**129** — Homepage schema: both `aggregateRating` reviewCount blocks updated 3 → 2 · ✅ DEPLOYED 2026-05-21

**130** — Homepage schema: Melissa Simon / The Home Refresh review removed from `LocalBusiness` review array · ✅ DEPLOYED 2026-05-21

**131** — Homepage schema: 9 specialty service types added to `serviceType` array in `ProfessionalService` block · ✅ DEPLOYED 2026-05-21

**132** — Homepage schema: FAQPage "what types of practices" answer updated to name all 9 specialties · ✅ DEPLOYED 2026-05-21

---

## Session 7: Package section removal

**133** — `services.html`: removed "THREE WAYS TO WORK TOGETHER" section (Seed / Bloom / Flourish cards) · ✅ DEPLOYED 2026-05-21

**134** — `packages.html`: removed "THREE WAYS TO WORK TOGETHER" section (Lead Path Audit / Foundation Build / Care Plan cards) · ✅ DEPLOYED 2026-05-21

---

## How to use this log

- Add new notes at the bottom of the relevant session block, or start a new block for each pass/session
- Number sequentially from where the last entry left off
- When a change deploys, update status to `✅ DEPLOYED [date]`
- Cross-reference rewrite docs in `/rewrites/` for full old-vs-new details on major changes
