# Session 6: Navigation + Homepage Signals
**Date:** 2026-05-21 | **Status:** For review — no changes applied yet

---

## Task 1: Navigation Audit and Rebuild

### Current state

**Desktop nav (left → right):**
About | Portfolio | Services | Articles | [Book a Clarity Call]

**Mobile nav:**
About | Portfolio | Services | Articles | [Book a Clarity Call]

**Footer nav (left side):**
Privacy Policy | Client Portal | Contact

**Footer nav (right side — social):**
Facebook | Instagram | LinkedIn | Newsletter

**What's missing:**
- No niche signal anywhere in the nav. "Services" could be a law firm or a bakery.
- Bergen County page exists but is not linked from nav or footer.
- /website-audit is a paid product and a key conversion path — not surfaced in nav.
- 9 specialty pillar pages exist and none are findable from the nav.
- The dropdown CSS is fully built into the codebase but not being used. The HTML structure to activate it is not in place.

---

### Proposed new structure

**Desktop nav:**
About | Portfolio | **Specialties ▾** | Articles | [Book a Clarity Call]

**Specialties dropdown (replaces "Services" in the main nav):**

| Item | URL |
|---|---|
| Functional Medicine | /functional-medicine-web-design |
| Menopause Practice | /menopause-practice-web-design |
| Holistic Gynecology | /holistic-gynecology-web-design |
| Concierge Primary Care | /concierge-primary-care-web-design |
| Aesthetics | /aesthetics-web-design |
| Fertility Practice | /fertility-practice-web-design |
| Cash-Pay Psychiatry | /cash-pay-psychiatry-web-design |
| Pelvic Floor Therapy | /pelvic-floor-physical-therapy-web-design |
| Lactation & Postnatal | /lactation-postnatal-web-design |
| ─── | |
| Website Audit ($297) | /website-audit |
| All services → | /services |

**Why Services moves to the dropdown:** "Services" as a top-level nav item is generic. Swapping it for "Specialties" makes the niche visible from the very first glance at the nav bar. The /services page is still accessible — it becomes the "All services →" link at the bottom of the dropdown. /website-audit surfaces as a direct nav item for the first time, giving warm leads a clear path.

**Desktop nav side-by-side:**

| Before | After |
|---|---|
| About | About |
| Portfolio | Portfolio |
| Services | Specialties ▾ |
| Articles | Articles |
| Book a Clarity Call | Book a Clarity Call |

**Mobile nav:**
About | Portfolio | **Specialties +** (expandable) | Articles | [Book a Clarity Call]

The mobile nav already has toggle logic in the JavaScript — the structure just needs to be activated in the HTML. Expandable sub-items would show the same specialty list when tapped.

**Footer — add:**
Bergen County → /web-design-bergen-county-nj (add next to Contact in the footer left side)

**Implementation note:** The dropdown CSS (`.nav-item`, `.nav-dropdown`, `.nav-item:hover .nav-dropdown`) is already present in every page's `<style>` block. What's needed is wrapping the "Specialties" nav link in a `<div class="nav-item">` and adding a `<div class="nav-dropdown">` with the links. The mobile toggle logic (`.mobile-nav-toggle`, `.mobile-nav-sub`) is also already in the JS — it just needs the HTML elements in the mobile nav.

---

## Task 2: Homepage Signal Audit

### 1. Does the H1 mention functional medicine or women's health?

**Current H1:** "Attract the patients who'd rather pay out-of-pocket than be rushed."

**Assessment: No — but it's doing real work.**

The H1 doesn't name the niche. It doesn't have to — the hero CTA and the "Practices I build for" grid immediately below it are niche-specific. But the subheadline is where the niche should be named explicitly, and right now it isn't (see below).

The H1 is strong copywriting. Changing it risks losing the emotional hook that speaks directly to the practitioner who is tired of the wrong patients. Recommend keeping the H1 and fixing the subheadline instead.

### 2. Does the hero subheadline name the ideal client?

**Current subheadline:** "The complete patient journey, built with you. I map the strategy, build the website and email pieces that need building, and guide the rest so your practice gets found, converts, and books."

**Assessment: No.** This reads as a description of a process, not a description of who this is for. It could describe a web studio serving restaurants or retail. The ideal client is not named anywhere in the hero block.

### 3. Are testimonials on the homepage niche-aligned?

**Displayed testimonial (on-page):** Mona Perez, Smooth Laser Center — labeled "Women's Wellness · Bergen County, NJ" ✓
This is fine. The attribution frames it as women's wellness, which aligns.

**Schema reviews (in structured data — not visible on page, but read by Google):**
- Mona Perez (Smooth Laser Center) → ✓ on-niche
- **Melissa Simon (The Home Refresh)** → ✗ OFF-NICHE. Home organizing practice. Her review is embedded in the `aggregateRating` schema block. Google sees this.
- Laura Gonzalez (practice type not specified) → neutral, strong testimonial

**Action needed:** Remove Melissa Simon from the schema review list. She can stay in the case study blog post but should not be in the homepage structured data.

### 4. Are case studies on the homepage niche-aligned?

**Featured case studies:**
- Smooth Laser Center (aesthetics) → ✓ on-niche
- "Coming Soon · Specialty Practice" placeholder → ✓

The Home Refresh case study is NOT featured on the homepage — that's already been handled correctly. No action needed here beyond keeping it that way.

### 5. Schema markup — does it identify the niche?

**What's there:**
- `LocalBusiness` and `ProfessionalService` types ✓
- Description: "web design studio for private practitioners in women's health" ✓
- `serviceType`: includes "Web Design for Women's Wellness Practices" ✓
- Three `Review` items: Mona Perez ✓, Melissa Simon ✗ (off-niche), Laura Gonzalez ✓

**What's missing:**
- Specific specialty names in serviceType (functional medicine, menopause, holistic gynecology, etc.)
- The `aggregateRating` reviewCount is 3 — if Melissa Simon is removed, it should become 2

**FAQPage schema assessment:**
- Q: "What types of practices does Simple Rabbit build websites for?" → A: "private-pay women's wellness practices in Bergen County and the NY metro" — OK but could be more specific
- Q: "Does Simple Rabbit work with practices outside New Jersey?" → A: "Yes... our process is fully remote." — ✓ keeps the national scope option open

### 6. Internal links to pillar pages from homepage?

**Via icon grid ("Practices I build for"):** All 9 pillar pages are linked ✓
**Via hero body copy:** None
**Via statement strip / testimonial section:** None
**Via body text anywhere:** None

The grid does the heavy lifting. It's above the fold on desktop for most screen sizes. This is acceptable — every pillar page is one click from the homepage. No structural problem here.

---

## Task 3: Homepage Rewrite Recommendations

### 3a. Overline (above H1)

**Current:** "Custom websites · Local SEO · Lead generation · Care plans"

**Proposed:** "Websites for functional medicine + women's health practices"

*Why:* The current overline describes services. The proposed overline names the niche. This is the very first text a visitor reads above the H1 — one line, 11px, all caps. It takes zero design space and immediately tells the right practitioner "this is for me."

---

### 3b. Hero subheadline

**Current:** "The complete patient journey, built with you. I map the strategy, build the website and email pieces that need building, and guide the rest so your practice gets found, converts, and books."

**Proposed:** "Custom websites for functional medicine, menopause, and women's health practices. Built to get found by the patients who are already searching for what you offer and are ready to pay for it."

*Why:* Names the primary specialties. Speaks to the patient quality concern (patients who are already searching, already willing to pay) which is the core anxiety of every private-pay practitioner. Stays at 8th-grade reading level. No em-dashes, no AI-language.

If the services-as-process language is important to keep, an alternative:

**Proposed alt:** "I build the website, write the copy, and set up the local SEO for functional medicine and women's health practices that are done waiting on referrals."

---

### 3c. H1

**Current:** "Attract the patients who'd rather pay out-of-pocket than be rushed."

**Recommendation: Keep as-is.** This is the strongest copy on the homepage. It identifies the ideal patient by her mindset and signals the practitioner type without being clinical. Changing it to add "functional medicine" would make it longer and more generic. The overline change handles the niche signal.

---

### 3d. Schema changes

**Remove from the `review` array:** Melissa Simon / The Home Refresh

**Update `aggregateRating`:** reviewCount: "3" → reviewCount: "2"

**Add to `serviceType` array:**
```
"Web Design for Functional Medicine Practices",
"Web Design for Menopause and Hormone Practices",
"Web Design for Holistic Gynecology Practices",
"Web Design for Concierge Primary Care Practices",
"Web Design for Cash-Pay Psychiatry Practices",
"Web Design for Fertility Practices",
"Web Design for Aesthetics Practices",
"Web Design for Pelvic Floor Physical Therapy Practices",
"Web Design for Lactation and Postnatal Practices"
```

**Update FAQPage "what types of practices" answer:**
Current: "Simple Rabbit builds websites for private-pay women's wellness practices in Bergen County and the NY metro."
Proposed: "Simple Rabbit builds websites for private-pay women's health practices: functional medicine, menopause and hormone care, holistic gynecology, concierge primary care, aesthetics, fertility, pelvic floor PT, lactation and postnatal, and cash-pay psychiatry."

---

### 3e. Testimonials — no homepage display changes needed

Only Mona Perez is shown on-page. She stays. The removal of Melissa Simon is a schema-only change (structured data, not visible copy).

---

## Task 4: Final QA Checklist

### Redirects (Sessions 1 + 2)

| Redirect | Target | Target Exists? | Status |
|---|---|---|---|
| /web-design-essex-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-hudson-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-morris-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-passaic-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-sussex-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-warren-county-nj → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-rockland-county-ny → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /web-design-westchester-county-ny → /web-design-bergen-county-nj | Bergen page | ✓ | PASS |
| /blog/google-business-profile-not-getting-clicks → /articles | /articles page | ✓ | PASS |
| /blog/google-business-profile-mistakes-wellness-practices → /articles | /articles page | ✓ | PASS |
| /blog/ai-search-visibility-service-business → /articles | /articles page | ✓ | PASS |
| /blog/nj-businesses-need-solid-website → /articles | /articles page | ✓ | PASS |
| /blog/about-page-service-business → /articles | /articles page | ✓ | PASS |
| /audit → /website-audit | website-audit.html | ✓ | PASS |
| /playbook → /fully-booked | fully-booked.html | ✓ | PASS |

No broken chains. All redirect targets resolve.

---

### Sitemap

Verified in prior sessions. Current sitemap contains:
- 8 main pages ✓
- 9 specialty pillar pages ✓
- 1 Bergen County local page ✓
- 18 blog posts ✓
- /website-audit ✓
- /fully-booked ✓

Retired county pages and closed blog posts removed from sitemap in Session 1 ✓
No retired or redirected URLs remain in the sitemap ✓

---

### Internal links to retired posts

**FAIL — 6 active blog posts still link to redirected URLs.**

| Post | Broken Link | Redirects To |
|---|---|---|
| why-menopause-practice-websites-dont-rank-locally | /blog/google-business-profile-not-getting-clicks | /articles |
| why-menopause-practice-websites-dont-rank-locally | /blog/ai-search-visibility-service-business | /articles |
| why-your-practice-isnt-showing-up-in-local-map-pack | /blog/google-business-profile-not-getting-clicks | /articles |
| how-to-rank-for-functional-medicine-near-me | /blog/google-business-profile-not-getting-clicks | /articles |
| google-business-profile-virtual-practice | /blog/google-business-profile-not-getting-clicks | /articles |
| how-womens-wellness-practices-get-found-on-google | /blog/google-business-profile-not-getting-clicks | /articles |
| local-keywords-your-wellness-practice-should-target | /blog/google-business-profile-not-getting-clicks | /articles |

These are 301 redirects so they're not hard-broken — visitors and crawlers reach /articles. But they waste link equity and look sloppy in a crawl. Flagged for fix in the internal linking pass (Session 5, Task 4, Priority 4).

---

### Canonical tags

Spot-checked all key pages:

| Page | Canonical | Status |
|---|---|---|
| Homepage | https://simplerabbit.studio/ | ✓ PASS |
| /functional-medicine-web-design | https://simplerabbit.studio/functional-medicine-web-design | ✓ PASS |
| /holistic-gynecology-web-design | https://simplerabbit.studio/holistic-gynecology-web-design | ✓ PASS |
| /menopause-practice-web-design | https://simplerabbit.studio/menopause-practice-web-design | ✓ PASS |
| /about | https://simplerabbit.studio/about | ✓ PASS |
| /about/simple-rabbit | https://simplerabbit.studio/about/simple-rabbit | ✓ PASS |
| /services | https://simplerabbit.studio/services | ✓ PASS |
| /thank-you | noindex present | ✓ PASS |
| County pages (essex, sussex, warren) | noindex present | ✓ PASS |

No canonical issues found. All pages self-canonical and correct.

---

### Robots.txt

```
User-agent: *
Allow: /

AI crawlers: all explicitly welcomed (GPTBot, ClaudeBot, PerplexityBot, etc.)
Sitemap: https://simplerabbit.studio/sitemap.xml
```

✓ PASS. Not blocking anything. AI crawlers explicitly welcomed — good for AI search visibility.

---

## Prioritized Action List

### Apply immediately (before next deploy):

**1. Homepage — overline text change (1 line of HTML)**
Old: `Custom websites &middot; Local SEO &middot; Lead generation &middot; Care plans`
New: `Websites for functional medicine + women&rsquo;s health practices`

**2. Homepage — hero subheadline rewrite (1 paragraph)**
Old: "The complete patient journey, built with you. I map the strategy..."
New: "Custom websites for functional medicine, menopause, and women's health practices. Built to get found by the patients who are already searching for what you offer and are ready to pay for it."

**3. Homepage schema — remove Melissa Simon review + update reviewCount**
Remove the Melissa Simon review object from both `aggregateRating` schema blocks. Change reviewCount from "3" to "2".

**4. Homepage schema — add specific specialties to serviceType**
Add the 9 specialty service names to the `serviceType` array in the ProfessionalService block.

**5. Blog — 7 broken internal links (Session 5 Task 4 Priority 4)**
Fix posts that link to retired blog posts. Swap `/blog/google-business-profile-not-getting-clicks` → `/blog/google-business-profile-virtual-practice` in 6 posts.

**6. Blog — 3 critical pillar links missing (Session 5 Task 4 Priority 1)**
- `how-to-rank-for-functional-medicine-near-me` → add link to `/functional-medicine-web-design`
- `why-menopause-practice-websites-dont-rank-locally` → add link to `/menopause-practice-web-design`
- `how-womens-wellness-practices-get-found-on-google` → add link to `/holistic-gynecology-web-design`

### After approval (requires design discussion):

**7. Nav — add Specialties dropdown**
Wrap the nav Specialties item in `.nav-item` div, add `.nav-dropdown` with all 9 specialty pages + /website-audit + /services link. Activate mobile-nav-toggle in mobile nav.

**8. Footer — add Bergen County link**
Add `<a href="/web-design-bergen-county-nj">Bergen County</a>` to the footer left nav row.

### Later (FM and HG page rewrites — Session 4 doc ready for apply):

**9. Apply FM page changes** (from rewrites/fm-page-rewrite.md)
**10. Apply HG page changes** (from rewrites/hg-page-rewrite.md)
