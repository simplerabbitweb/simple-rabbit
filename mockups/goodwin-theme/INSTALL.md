# Goodwin Decorative Finishes — theme install

Classic WordPress theme built from the approved mockup. No build step, no page
builder, no npm. Plain CSS and one JavaScript file.

## 1. Install

1. Zip the `goodwin-finishes` folder (`goodwin-finishes.zip` is already built beside this file).
2. WordPress → Appearance → Themes → Add New → Upload Theme → Activate.

On activation the theme registers the Projects post type, creates the five
Finish terms (Microcement, Venetian / Marmorino, Lime wash, Decorative / Faux,
Commercial), and flushes permalinks. It flushes again after any in-place update.

**This is a single-page site.** Projects are edited in the admin but have no
public URL of their own, and tiles are not clickable — the gallery simply sits on
the page, filtered by finish. Hovering a tile shows its title, finish and
location. There is no project archive, no finish archives, and no lightbox.

Because nothing opens, a project shows exactly one photo: its **Main image**. The
Photos gallery field is stored but not displayed anywhere — see Known gaps.

## 2. Plugins

| Plugin | Why | Required? |
|---|---|---|
| **Advanced Custom Fields Pro** | The Photos field on a project is a Gallery field, which is Pro-only | Yes |
| **Rank Math** | Titles, meta, LocalBusiness + Service schema, sitemap | Yes |
| **Smash Balloon Instagram Feed** | Real feed in the "Follow the work" strip | Yes |
| WP Rocket or similar | Caching | Recommended |

The field group is registered in code (`inc/acf-fields.php`), so it appears as
soon as ACF Pro is active — nothing to import. Without ACF Pro the site still
runs; projects just show titles and main images, and the admin shows a warning.

Until the Instagram plugin is connected, the strip falls back to the six most
recent project photos, so the section never looks broken.

## 3. Settings

- **Settings → General** — phone, email, studio address, Instagram handle, licence
  number. These fill the header, contact block and footer. Set the licence number
  or that row hides itself.
- **Settings → Permalinks** — Post name.
- **Settings → Reading** — set a static front page.
- **Appearance → Menus** — create a menu, assign it to *Primary*. Without one the
  header falls back to Projects / Finishes / About / Contact.
- The enquiry form posts straight to Formspree (`https://formspree.io/f/mqpzjnyl`)
  and needs no form plugin. The endpoint is editable in Settings → General if it
  ever changes.

## 4. Adding a project (this is the client-facing bit)

Projects → Add project:

- **Title** — what it is: "Curved ensuite".
- **Main image** (featured image) — the one that shows in the grid. Portrait works best.
- **Photos** — currently not displayed anywhere on the site (see Known gaps).
- **Location / Finish used / Space** — shown beside the description and used in image alt text.
- **Show on homepage** — decides which project supplies the big hero image. The
  gallery below shows every project regardless.
- **Finishes** (right sidebar) — tick one or more. These drive the filter buttons;
  a finish with no projects doesn't get a button.
- **Editor** — a short paragraph about the job. Not displayed on the site as it
  stands, but worth writing: it's there if a project view is ever added back.

The projects list shows a thumbnail, location and a star for featured, and can be
filtered by finish.

## 5. Templates

| File | What it renders |
|---|---|
| `front-page.php` | The site — hero, intro, finishes, full gallery, about, testimonials |
| `template-parts/*.php` | Page sections. **Copy is edited here**, not in the editor |
| `inc/cpt.php` | Post type, taxonomy, admin columns |
| `inc/acf-fields.php` | Field group |
| `inc/template-tags.php` | `gw_tile()` — the tile markup and its lightbox payload |
| `assets/js/gallery.js` | Filters, lightbox, mobile nav |
| `page.php`, `index.php`, `404.php` | Fallbacks, in case a page is ever added |

Every button on the page links to `#work` or `#contact`. Filters update the URL
(`/?finish=microcement`), so a filtered view can still be linked to and shared.

## 6. Before launch

- [ ] Replace `screenshot.png` with a real screenshot of the built homepage.
- [ ] Set the licence number in Settings → General (the row hides while empty).
- [ ] Register `gw-grid` sizes against existing images — run Regenerate Thumbnails
      after importing the media library, or the grid will serve full-size photos.
- [ ] Because everything lives on one page, all SEO rests on it. Rank Math title
      and meta should lead with microcement + Newcastle, and the page needs enough
      real copy to rank — the project descriptions are not indexed anywhere now.
- [ ] Rank Math: LocalBusiness schema with the Mayfield East address, NAP matching
      Google Business Profile, title pattern leading with the finish + Newcastle.
- [ ] Check alt text on imported images — the theme composes alt from title, finish
      and location, but only for images added through the Photos field.
- [ ] Send one real test enquiry — Formspree needs a first submission from the live
      domain before it starts delivering, and the address it forwards to is set in
      the Formspree dashboard, not here.
- [ ] WebP conversion + caching.

## 7. Known gaps

- Homepage hero, intro, about and testimonial copy live in template files. That was
  a deliberate call — it's copy that changes once a year, and keeping it out of a
  builder is the point. If Lauren needs to edit it herself, the About section already
  reads from an About page (excerpt + featured image) when one exists; the same
  pattern can be extended.
- Testimonials are an array in `template-parts/testimonials.php`.
- **The Photos field and the project description have nowhere to appear.** With no
  project view, each project contributes one image to the grid. Either drop those
  fields, or render every photo as its own tile so nothing is hidden — worth
  deciding before Lauren starts loading projects with multiple shots.
- Nothing here has run against a live WordPress install yet — PHP syntax is clean,
  but expect to fix small things on first load.
