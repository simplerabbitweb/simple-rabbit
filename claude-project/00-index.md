# Simple Rabbit — Claude Project Reference Files

Upload all files in this folder to your Claude project. Together they give Claude full context on your business so any copy, content, or strategy work is on-brand from the first message.

---

## Files in This Folder

| File | What's Inside |
|------|--------------|
| `01-business-overview.md` | ACRR framework, positioning, go-to-market strategy, 90-day roadmap, HIPAA guardrails, key URLs, ops details |
| `02-offers-and-pricing.md` | Growth Strategy ($9.5k–$12.5k), Growth Accelerator ($22k–$28k), Retainer ($2.75k–$4.5k/mo), website builds, care plans, full deliverables for each, pricing philosophy, sales notes |
| `03-ideal-client-avatar.md` | Dr. Elena Ramirez composite profile — age, specialty, psychographics, fears, goals, buying behavior, buyer stages (A/B/C), where to find her, language that resonates, who she is NOT |
| `04-pain-points-and-messaging.md` | Six core pain points with copy guidance for each, website copy reference (hero, problem, solution, about, CTAs), content pillars, messaging hierarchy, objection handling, hard copy rules |
| `05-brand-design-system.md` | Full CSS design tokens, color palettes, typography scale, nav and button styles, layout patterns, section patterns, ACRR section placement, mobile breakpoints, file paths |

---

## Also Uploaded to This Project

These two files are stored in the project memory (not this folder) and should already be available:

- **`voice-guideline.md`** — Complete brand voice rules: sentence structure, words to use/avoid, tone by format, AI-tell patterns to skip, hard rules
- **`messaging-map.md`** — Source of truth for all messaging: buyer stages, hopes and dreams, anxieties, positioning, pain points, the offer, objections, CTAs, content pillars, north star sentence

---

## Key Hard Rules (Never Break These)

1. **Contact form endpoint is `https://formspree.io/f/mojndlrg` — never change it**
2. **"cash-pay" is banned — always use "private-pay"**
3. **Every new blog post must include the ACRR checklist section** placed above `<!-- MORE FROM THE BLOG -->`:
   ```html
   <div id="acrr-section"></div><script src="../acrr-section.js"></script>
   ```
4. **No em-dashes anywhere**
5. **Start every new blog post from `/Users/leannfrank/simple rabbit/blog/NEW-POST-TEMPLATE.html`**

---

## Quick Context for Claude

- **What is Simple Rabbit?** A one-person web studio (Leann Frank, Bergen County NJ) building custom WordPress websites and providing ACRR-based consulting for private-pay functional medicine and women's health practices.
- **Who is the client?** Female practitioners aged 40–58 who left insurance-based medicine, running solo private-pay practices ($650K–$2M+ revenue).
- **What does the work solve?** Inconsistent patient flow, wrong-fit leads, invisible on Google, generic-looking websites, and technical maintenance nobody wants to own.
- **What's the brand voice?** Direct. Warm. Quietly confident. Short sentences. Specific nouns. No em-dashes, no corporate jargon, no coach-speak.
- **What should every blog post do?** Connect at least one content pillar (The Right Patient / Found Online / The Build / The Care) to the life the buyer is trying to build. End with the ACRR checklist CTA section.
