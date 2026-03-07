# Simple Rabbit — Studio SOPs

Standard operating procedures for every website Simple Rabbit builds.

---

## Full Project Workflow

### Phase 1 — Client Brief (before touching code)

**1. Get the intake form response**
Client submits `simplerabbit.studio/client-intake` → Formspree emails you the responses.

**2. Create the client brief**
Duplicate `client-brief-template.md` → save as `[client-name]-brief.md` inside their new project folder (e.g. `/sarah-chen/sarah-chen-brief.md`).
Fill in every field using the intake email. This takes 10–15 minutes.

**3. Translate colors and fonts**
In the brief's **Design System** section, convert the client's color/font responses into the actual CSS variables block. Pick specific hex values for `--accent`, `--accent-dark`, and `--accent-light`. Set the `--font-display` and `--font-body` stacks. Update the Google Fonts import URL.

**4. Generate the style guide**
Open Claude Code in the client's project folder. Use the prompt at the bottom of the filled brief to generate `style-guide.html` — a live HTML file showing their colors, fonts, buttons, and components. Share with the client before starting the build to confirm the direction.

---

### Phase 2 — Build

**5. Start the build**
Paste `kickoff-prompt.md` + the filled client brief together as your first message to Claude Code. Claude now has the full build system AND all client-specific design details.

**6. Work through the build checklist**
Follow `build-checklist.md` phase by phase — file structure → pages → technical setup → forms → SEO → QA → deployment.

**7. Reference the design system as needed**
`design-system.md` has every CSS pattern, component, and code snippet as a deep reference.

---

### Phase 3 — Launch and Handoff

**8. Deploy**
Run `./deploy.sh "Initial launch"` — uploads all files via FTP, purges cache, pushes to GitHub.

**9. Final QA**
Work through the pre-launch and deployment sections of `build-checklist.md`. Test every page live.

**10. Hand off to client**
Send live URL, confirm GA4 access, confirm Formspree notifications, send change request form link.

---

## Files in this folder

| File | What it's for | When to use it |
|------|---------------|----------------|
| `README.md` | This file — full workflow overview | Whenever you need to orient yourself |
| `client-brief-template.md` | Per-client design spec + style guide generator | Phase 1 — before every build |
| `kickoff-prompt.md` | Paste into Claude Code to start the build | Phase 2 — first message in Claude Code |
| `brand-guide.md` | Simple Rabbit's own brand — colors, fonts, voice, principles | Any time you're creating SR content |
| `design-system.md` | Deep CSS reference — every component with copy-paste code | Phase 2 — during the build |
| `build-checklist.md` | 11-phase linear checklist from kickoff to post-launch | Phase 2 & 3 — throughout the build |

---

## The Simple Rabbit stack (quick reference)

- **HTML/CSS/JS** — static, no frameworks, no page builders
- **Hosting** — SiteGround shared hosting, FTP deployment
- **Forms** — Formspree (paid account, separate endpoint per form)
- **Analytics** — Google Analytics GA4
- **Version control** — GitHub
- **Fonts** — client-specific (set in Client Brief); defaults are Optima/Outfit/DM Mono
- **Deployment** — Python `deploy.sh` → FTP upload + cache purge + git push

---

## Updating these docs

When you make a decision on a project that should apply to all future builds — a new component pattern, a better form approach, a smarter SEO trick — update the relevant file here. These are living documents.

---

## The Simple Rabbit stack (quick reference)

- **HTML/CSS/JS** — static, no frameworks, no page builders
- **Hosting** — SiteGround shared hosting, FTP deployment
- **Forms** — Formspree (paid account, separate endpoint per form)
- **Analytics** — Google Analytics GA4
- **Version control** — GitHub
- **Fonts** — client-specific (specified in Client Brief); defaults are Optima/Outfit/DM Mono
- **Deployment** — Python deploy.sh → FTP upload + cache purge + git push
