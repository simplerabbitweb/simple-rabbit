# Simple Rabbit — Case Study Writing Guide

How to write, build, and publish a client case study article from scratch.

---

## 1. Information to collect before you start

You need answers to all of these before writing anything.

**Client basics**
- Client's full name
- Business name and URL (e.g. thehomerefresh.com)
- Location (city, state — ideally town + county for local SEO)
- Industry / service type (be specific: "full-service home organizing", not just "organizer")
- Number of pages in the project (e.g. "8-page custom website")

**The before situation**
- What was wrong with the old website? (outdated, no SEO, wrong audience, poor copy, ugly design, etc.)
- What was the client's biggest frustration or pain point?
- Was there an old site to screenshot or PDF?

**What was built**
- What pages were created?
- What was the strategic focus? (positioning, specific audience, local SEO, etc.)
- Any notable design choices or features?

**Results**
- What changed after launch? Be as specific as possible.
- Numbers if available: inquiries, bookings, search traffic, client type change
- If no hard numbers: describe the qualitative shift ("booked solid", "referrals now converting", etc.)
- 3 punchy result stats for the results grid (see Section 4)

**Testimonial**
- Direct quote from the client, unedited
- Use the full quote — don't trim it

**Images needed** (see Section 3 for naming and placement)
- Screenshot of old homepage (before)
- Screenshot of new homepage (after)
- Mobile screenshot of new site
- Full-site PDF of old site (optional but great)
- Full-site PDF of new site (optional but great)
- Card thumbnail image (for articles.html)

---

## 2. File setup

**Create the HTML file:**
`/blog/case-study-[client-slug].html`

Example: `blog/case-study-the-home-refresh.html`

The slug should be: `case-study-` + hyphenated business name, lowercase, no special characters.

**Place image files in:**
`/previews/`

Naming convention:
- `[client-slug]-website.png` — card thumbnail for articles.html (also used as OG image)
- `[client-slug]-mobile.png` — mobile screenshot
- `[client-slug]-old-homepage.png` — before screenshot (homepage only)
- `[client-slug]-new-homepage.png` — after screenshot (homepage only)
- `[client-slug]-full-old.pdf` — full site PDF, old
- `[client-slug]-full-new.pdf` — full site PDF, new

---

## 3. HTML template

Copy `blog/case-study-the-home-refresh.html` as the starting template. Then make these substitutions:

### Head section — update these values:

```
TITLE:          Case Study: How [Business Name] [result headline]
SLUG:           case-study-[client-slug]
META DESC:      [1–2 sentence summary of project and result]
PRIMARY KW:     web design for [industry]
OG IMAGE:       https://simplerabbit.studio/previews/[client-slug]-website.png
CANONICAL URL:  https://simplerabbit.studio/blog/case-study-[client-slug]
```

### Article header — update:
- `<span class="article-category">Case Study</span>` — keep as-is
- `<h1 class="article-title">` — use a result-forward headline (see Section 5)
- Date in `<span>` inside `.article-meta` — use publish date

### Client overview card — 4 fields:
| Field | What to put |
|---|---|
| Client | First + Last Name, linked to their URL |
| Location | City, State |
| Industry | Specific service type |
| Project | "X-page custom website" |

### Body sections in order:
1. Intro paragraph — establish the client and their reputation
2. "The problem" — what the old site was doing (or not doing)
3. "What Simple Rabbit built" — describe the project pages + strategy
4. Before/After homepage compare grid (if images available)
5. Mobile screenshot (if available)
6. Full-site PDF comparison (if PDFs available)
7. "What happened after launch" — results
8. Results grid (3 stats)
9. Deeper analysis paragraph — why this result makes sense
10. Testimonial blockquote
11. "What this kind of result requires" — closing analysis
12. Internal link paragraph → relevant article + /portfolio
13. `<hr>` divider
14. Closing CTA paragraph → /contact

### Results grid (3 cells):
Each cell has:
- `.results-grid-stat` — a bold word or number (e.g. "Booked", "Dozens", "Growing", "2×", "#1")
- `.results-grid-label` — 3–5 word description below it

Use real numbers when available. If not, use impactful qualitative words.

### Testimonial blockquote:
```html
<blockquote>
  <p>"[Full quote]"</p>
  <p style="font-size:14px;font-style:normal;font-family:'DM Mono',monospace;letter-spacing:1px;text-transform:uppercase;color:var(--mid);margin-top:16px;">
    [Client Name], <a href="[client URL]" target="_blank" rel="noopener noreferrer">[Business Name]</a>
  </p>
</blockquote>
```

### Lightbox — include when you have clickable images or PDFs:
The lightbox HTML block goes right before the footer. Copy it exactly from the template:

```html
<div class="lb-overlay" id="lb" onclick="lbClose()">
  <button class="lb-close" id="lb-close" onclick="lbClose()" aria-label="Close">&times;</button>
  <div class="lb-inner" id="lb-inner" onclick="event.stopPropagation()"></div>
</div>
```

To make an image open in the lightbox:
```html
<div onclick="lbOpen('img','../previews/FILENAME.png')" role="button" tabindex="0">
  <img src="../previews/FILENAME.png" alt="Description">
</div>
```

To make a PDF open in the lightbox:
```html
<div onclick="lbOpen('pdf','../previews/FILENAME.pdf')" role="button" tabindex="0">
  <!-- content -->
</div>
```

### Schema JSON-LD — update at the bottom of the file:
```json
{
  "headline": "Case Study: ...",
  "datePublished": "YYYY-MM-DD",
  "dateModified": "YYYY-MM-DD",
  "description": "...",
  "mainEntityOfPage": { "@id": "https://simplerabbit.studio/blog/case-study-[slug]" },
  "about": {
    "@type": "LocalBusiness",
    "name": "[Business Name]",
    "url": "[client URL]",
    "address": {
      "addressLocality": "[City]",
      "addressRegion": "[State abbreviation]"
    }
  }
}
```

---

## 4. Writing the content

### Voice rules
- Confident, direct, warm — no hedging, no filler
- No em dashes (use commas or restructure the sentence)
- No "It's not X, it's Y" sentence constructions
- No choppy staccato rhythm — sentences should flow and vary in length
- Write to a smart reader who respects expertise
- Don't oversell. Let the result speak. The writing should be understated.

### Headline formula
The headline should lead with the result, not the project.

**Format:** `How [Business Name] [past-tense result verb] [from X] [to Y]`

Examples:
- "How The Home Refresh went from an outdated website to booked solid"
- "How [Client] stopped competing on price and started booking premium clients"
- "How [Client] doubled their consultation requests in 60 days"

Avoid: "Simple Rabbit builds a new website for [Client]" — no one cares.

### Section by section

**Intro (2–3 paragraphs)**
Open by establishing the client's real-world reputation and what they had already built. Then pivot: the website didn't reflect any of that. End the intro on a clean, short sentence that frames the gap.

**The problem (2–3 paragraphs)**
Don't just describe the visual issues. Explain WHY the problem matters in terms of how clients make decisions. Make the reader (who may have the same problem) see themselves in it.

**What was built (3–5 paragraphs)**
Walk through the strategy, not just the deliverables. Don't write "we built a homepage." Write what the homepage was designed to accomplish and for whom. Include the before/after images here naturally, not at the end.

**After launch (2–4 paragraphs)**
Lead with the headline result. Then explain how the mechanics work — why a better site produces this outcome. Don't just list results; analyze them slightly so the reader understands the cause.

**Closing analysis (2 paragraphs)**
Pull back to the bigger picture. This client's result isn't magic — it's what happens when a site matches the quality of the service. Transition the reader toward their own situation.

**Internal links**
Always link to:
- A relevant blog article (pick the one that connects most logically)
- `/portfolio`
- `/contact`

---

## 5. Adding the card to articles.html

Add a new card at the top of the articles grid in `articles.html`. Case studies go first (they're the most persuasive content).

```html
<a href="/blog/case-study-[slug]" class="article-card reveal">
  <div class="article-card-img">
    <img src="previews/[client-slug]-website.png" alt="[Business Name] website case study">
  </div>
  <div class="article-card-body">
    <span class="overline">Case Study</span>
    <h3 style="font-family:var(--font-display);font-size:22px;line-height:1.25;font-weight:400;margin-bottom:12px;">
      [Same headline as the article]
    </h3>
    <p style="font-size:14px;line-height:1.7;color:var(--mid);">
      [1–2 sentence teaser — who is the client and what changed]
    </p>
  </div>
  <div class="article-card-arrow" style="padding:0 24px 24px;font-size:13px;color:var(--mid);">
    Read case study &rarr;
  </div>
</a>
```

---

## 6. Deploy checklist

Before running deploy.sh, confirm:

- [ ] HTML file saved to `/blog/case-study-[slug].html`
- [ ] All image files placed in `/previews/` with correct names
- [ ] OG image URL in `<head>` matches the actual filename in `/previews/`
- [ ] Canonical URL matches the actual slug
- [ ] Schema JSON-LD updated with correct date, client, URL
- [ ] Article card added to `articles.html`
- [ ] Internal links in article body are correct (no broken hrefs)
- [ ] Client's live website URL is correct and working

Then run:
```
cd "/Users/leannfrank/Desktop/simple rabbit" && bash deploy.sh
```

GitHub push will fail (known `.env` secrets issue in git history — does not affect the live site). FTP upload to SiteGround is what publishes the site.

---

## 7. Images — how to get them

**Homepage screenshots (before + after):**
Open the site in Chrome. Set viewport to 1440px wide. Screenshot just the above-the-fold area, cropped to roughly 1440×900px. Save as PNG.

**Mobile screenshot:**
In Chrome DevTools, set device to iPhone 12 Pro (390px). Screenshot the full above-the-fold area. Save as PNG.

**Card thumbnail (for articles.html + OG image):**
Screenshot the homepage at 1440px wide, crop to 1200×630px. This is also the Facebook/social share image. Save as PNG.

**Full-site PDFs:**
In Chrome, go to Print → Save as PDF. Set paper to A4, scale to fit. This captures the whole page as a scrollable PDF. Save as `[client-slug]-full-new.pdf` and `[client-slug]-full-old.pdf`.

---

*Last updated: March 2026*
