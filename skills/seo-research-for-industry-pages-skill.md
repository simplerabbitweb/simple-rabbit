# SEO Research for Industry Pages

Use this skill when Leann needs SEO research for a "web design for [industry]" page on simplerabbit.studio. Trigger phrases: "do SEO research for [industry] page," "what should the [industry] page rank for," "research keywords for [industry]," "help me build the SEO for the [industry] page," or any variation that involves identifying ranking opportunities for a new or existing industry page on the site.

The four current target industries are:
- Women's hormone and menopause care
- Functional and integrative medicine
- Aesthetics and laser
- Holistic gynecology

This skill works for those four and any future industries Leann adds (e.g., concierge primary care, longevity, peptide clinics).

## What this skill is for

This skill produces SEO research that powers the structure and content of a service page targeting practitioners in a specific niche. The buyer is the practice owner (the practitioner herself), not her patients. The research output should let Leann or Claude Code build a page that ranks for the searches her real prospects are running.

The output is not a generic SEO report. It's a strategic brief tied to building one specific page.

## What this skill is NOT for

Not for: keyword research for a patient-facing page (that's a different intent), generic SEO audits of the existing site (use a different process for that), or backlink strategy (that's not the focus here).

## Inputs needed before starting

Before running the research, gather these:

1. **The industry name** in plain language (e.g., "Functional and integrative medicine," not "FM/IM")
2. **The geographic scope** (Bergen County only? Tri-state? National?)
3. **Whether Leann has any client examples in this industry yet** (affects what the page can promise)
4. **The current page status** (does the page already exist? Is this a new build? Are we updating an old page?)

If any of these are unclear, ask Leann before beginning research.

## The 5-step research process

### Step 1: Identify the buyer's actual search intent

Before running any keyword tools, write out the practitioner's likely search queries. This is the single highest-leverage step in the whole process. Most SEO research goes wrong because it starts with tools instead of with the buyer.

Ask: what would a real practitioner type into Google when she's actively looking for a web designer?

For each industry, the searches generally fall into three buckets:

**Service-specific searches** (highest intent):
- "web design for [industry] practice"
- "[industry] website designer"
- "website for [industry] practice"
- "best web designer for [industry]"

**Problem-specific searches** (medium intent):
- "[industry] website not getting patients"
- "how to get patients to find my [industry] practice"
- "SEO for [industry] practice"
- "why is my [industry] website not ranking"

**Identity-specific searches** (relationship-building intent):
- "marketing for [industry] practice"
- "[industry] practice growth"
- "how to grow a [industry] practice"

The service-specific bucket is what the page should rank for first. The problem-specific bucket is content for blog posts that link to the page. The identity bucket is for top-of-funnel content (newsletter, social).

### Step 2: Run the keyword research

Use these tools, in this order:

1. **Google's autocomplete and "People Also Ask."** Type the core query into Google and write down every autocomplete suggestion. Then scroll down to "People Also Ask" and capture the questions. Repeat with the [city] modifier and the "near me" modifier. This gives you real searches people are actually running, not just what a tool guesses.

2. **Free SEO tools.** Use Ubersuggest, AnswerThePublic, or Keyword Planner (Google Ads, free with an account) for search volume estimates. Filter for queries with at least 10 monthly searches and "low" or "medium" competition. Ignore high-competition single-word queries (e.g., "menopause") unless the page is being built to compete nationally.

3. **Competitor analysis.** Find the top 3 sites that rank for the main query ("web design for [industry] practice"). Look at their page structures, headings, and what they're targeting. The goal is not to copy them but to understand where the bar is.

For each query you find, capture:
- The exact query phrasing
- Estimated monthly search volume (if available)
- Competition level (low/medium/high)
- Whether the query is local-intent or broad-intent
- Whether there's a "People Also Ask" cluster around it

### Step 3: Map keywords to page structure

The keywords you identified should not become a list of phrases stuffed into the page. They should map to the structure of the page itself.

A good industry page on simplerabbit.studio follows this structure:

**H1:** The primary keyword phrase, written in natural language. (e.g., "Web design for women's hormone and menopause practices")

**Hero subhead:** A natural-sounding sentence that includes the secondary keyword variation. (e.g., "Custom websites and ongoing care for hormone and menopause specialists who want the right patients to find them.")

**Section 1 (problem):** Targets problem-specific keywords. The H2 might be "Why most hormone and menopause websites don't bring in the right patient." Body covers 1-2 problem queries.

**Section 2 (offer):** Targets service-specific keywords. H2 might be "What goes into a hormone and menopause practice website." Body covers what the build includes, with naturally placed mentions of "SEO," "Google Business Profile," "custom design."

**Section 3 (proof):** If there's a case study or testimonial, this is where it goes. H2 references the industry directly.

**Section 4 (process):** Reuses general process content. Targets keywords like "[industry] website project process," "[industry] web design timeline."

**Section 5 (FAQ):** Targets long-tail keywords directly. Each question is a real search someone runs. (e.g., "How is a website for a hormone clinic different from a regular medical website?")

**Section 6 (CTA):** Conversion-focused. Targets the buyer who's ready to talk.

The full page should be 1,500-2,500 words. Less than 1,500 won't rank for competitive industries. More than 2,500 risks losing the reader.

### Step 4: Identify supporting content

A single industry page rarely ranks for everything you want it to. The page needs supporting content that links back to it. Identify 3-5 blog post topics that:

- Target problem-specific keywords (the medium-intent bucket from Step 1)
- Link naturally back to the industry page
- Earn links from other sites if possible

For each blog post, capture:
- The target query
- A working title
- A 2-sentence content angle
- Where in the buyer's journey this post catches her

Example for hormone and menopause:
- Target query: "menopause website not getting patients"
- Working title: "Why most menopause and hormone clinic websites don't rank locally (and how to fix it)"
- Angle: Most menopause websites rely on the practitioner's reputation instead of being built to be found. This post walks through the structural reasons they don't rank, and what to fix.
- Buyer journey: Stage 2 (recently left insurance, struggling to fill the practice).

### Step 5: Output the brief

The final deliverable from this skill is a structured brief Leann (or Claude Code) can use to build the page. Save it as a markdown file at `/mnt/user-data/outputs/seo-brief-[industry-slug].md`.

The brief should contain:

```
# SEO Brief: Web Design for [Industry]

## The buyer
A 2-3 sentence description of the specific practitioner this page is for. Include her stage (considering leaving insurance, recently left, established) if known, and what she's likely searching for.

## Primary target keyword
The single highest-priority phrase the page should rank for. Include estimated monthly search volume.

## Secondary target keywords
A list of 5-10 keyword variations and related phrases the page should naturally cover. Group by intent (service, problem, identity).

## Page structure recommendation
A complete H1, hero subhead, and section-by-section H2 outline matching the structure from Step 3. Include keyword placement notes.

## Supporting content recommendations
3-5 blog post ideas with target query, title, and angle.

## Competitive notes
Top 3 competing pages for the primary keyword, with a note on what they do well and where there's an opening for Simple Rabbit.

## Internal linking recommendations
Where the new industry page should link FROM (other pages on the site that should link to it) and TO (other content this page should reference).

## Open questions
Anything that needs Leann's input before the page is built (e.g., "Do you have a case study in this industry?" or "What's your current pricing for this niche?").
```

## Voice and content guidelines

When outputting recommended copy or H1/H2 examples, follow Simple Rabbit's voice:

- Direct, calm, first-person ("I" not "we" when referring to the work)
- No em-dashes
- No "cash-pay" (use "private-pay" instead)
- No "not just X but Y" sentence structures
- No corporate filler (elevate, transform, unlock, journey, vision)
- Niche language: "practice" not "business," "patients" not "clients," "private-pay" not "cash-pay"

## Quality checks before delivering the brief

Before handing off the brief, run these checks:

1. **Does the primary keyword have enough search volume to be worth chasing?** If the primary target has under 10 monthly searches, the page should target a broader keyword and use the niche term as a secondary signal.

2. **Is the buyer real?** Reread the brief and ask: does this page speak to a specific person, or to a category? If it's the latter, narrow it.

3. **Are the keywords being honored, or stuffed?** The page structure should hold up if you removed all the SEO context. If the H2s only make sense as keyword targets, rewrite them as natural section openers.

4. **Are there gaps in the proof?** If Simple Rabbit has no case study in this niche yet, the brief should flag this and recommend a workaround (anonymous patterns, adjacent case studies, or a soft launch with the page targeting the niche but not over-promising results).

## When to NOT use this skill

Don't use this skill when:
- The request is for general SEO advice (use a different process)
- The page already exists and just needs minor copy tweaks (just edit, don't research)
- The industry is too small or too generic to support a dedicated page (recommend a blog post instead)

## Handoff

When the brief is complete, present it to Leann with a summary of the top 3 recommendations and ask whether she wants to proceed to building the page (Claude Code) or wants to iterate on the brief first.
