---
name: slides-design
description: Build, convert or revise a polished 16:9 HTML slide deck presented in a browser instead of PowerPoint — from md/txt notes, an existing .pptx or an older HTML deck, using ready templates (BytePlus pitch in dark or light, brand-free light AI tech, work review, Bible study, design studio). Use whenever the user asks for slides, a deck, a presentation or "ppt" without naming a file format, says "turn this pptx/md into slides", "md updated, update html" or "pptx is updated", or wants a slide added, fixed or restyled. Not for producing a .pptx file.
---

# Slides Design

The goal is a **presentation, not a web page**: one self-contained HTML file (+ an asset folder) that a presenter
opens in a browser, drives with arrow keys, and that looks finished at any 16:9 window size.

## Route the task

| Situation | Read first |
|---|---|
| New deck from notes / md / txt | `references/intake-and-story.md` → `references/design-systems.md` → `references/components-and-layouts.md` |
| Convert an existing `.pptx` | `references/intake-and-story.md` (pptx section) + run `scripts/pptx_extract.py` |
| Deck has video, popups, tabs, zoom, speaker notes | `references/media-popups-runtime.md` |
| Needs a generated illustration, logo cut-out, or background match | `references/images-and-assets.md` |
| Editing an existing deck ("md updated", "pptx is updated", "move X by N px") | `references/qa-export-gotchas.md` (Edit safely) first, then the deck's own `README.md` |
| Before every delivery | `references/qa-export-gotchas.md` (QA checklist) |

## Workflow

1. **Inventory.** Read the source (md/txt/pptx), list every asset with its ratio and role, find the project's
   `README.md` if one exists (it replaces conversation history — read it fully before touching anything).
2. **Story map.** Write the one-sentence deck promise and a slide table (job · takeaway title · content · asset).
   Each slide does one job. Detail that doesn't fit goes behind a click (popup / lightbox), not into tiny text.
3. **Pick the design system.** Start from a ready template in `templates/` (see the table below; each folder has
   `template.html`, `template.json`, `design.md`) or one of the systems in `references/design-systems.md`. If none
   fits, build 3 quick cover-slide previews in different styles and let the user choose.
   Match the logo variant to the background (dark logo ⇒ all-dark deck).
4. **Generate, don't hand-edit (for decks that will change).** For a BytePlus deck (dark `byteplus` or light `byteplus-light`) or a brand-free `ai-tech-light` deck, copy `scripts/build_deck.py`
   into the project's `tools/`: it builds on `templates/byteplus/`, slide text lives in small slide functions, and
   `python tools/build_deck.py` writes the HTML — every later change is a script edit + rebuild. Short decks
   (a Bible study, a one-off review) can be a hand-edited copy of the template.
5. **Media through the template's components.** `.frame` / `frame()` for content images (zoomable, never
   cropped), `.vid` / `video()` for clips (auto-plays once, never loops), popups as siblings of `#deck` (inside the
   slide on the fixed-canvas bible-study template). See `references/media-popups-runtime.md`.
6. **Verify for real.** `node scripts/validate_deck.js deck.html`, then `python scripts/screenshot_deck.py deck.html`
   and *look* at every changed slide at 1600×900 and 1280×720. Measure overflow against the footer's top edge.
   Compare every md/pptx line with the slide text.
7. **Hand over.** Open the HTML for the user, give the path, say what changed and what to check. Keep the
   project `README.md` current (quick start, folder map, slide outline, design tokens, decisions, gotchas,
   dated change log) — the next session starts from it.

## Non-negotiables (learned the hard way)

1. **Titles state the takeaway** and are the same size on every ordinary slide. **Always Title Case** every English
   title and heading — slide titles, card/step/panel headings, popup titles, sub-headings, labels: capitalise first,
   last and major words, minor words (a, an, the, and, or, of, in, to, with, by…) lower-case mid-title, hyphenated
   parts each capitalised (Self-Operated). This applies even when the source pptx/md/pdf uses sentence case; only the
   case changes — keep the source's wording and the user's spellings (NextAPI, BitSpace, SaaS stay as written). Run
   `scripts/title_case.py deck.html` before delivery.
2. **Never crop or distort content media.** `object-fit: contain`, natural ratio; `cover` only for decorative
   backgrounds or a box whose aspect ratio already equals the media's (the `--r` pattern).
3. **No unreadable text.** Smallest text on any slide/popup ≥ 18 px at 1600×900 (≈1.125u). If it doesn't fit,
   cut words or move them into a popup.
4. **Scale with `--u: min(1vw, 1.7778vh)`** and write sizes as `calc(N * var(--u))` so the slide never outgrows a
   short or wide window. Convert any raw `vw` you add.
5. **Anchor the title; don't vertically centre ordinary slides.** Distribute surplus height through gaps and group
   positions; keep well-proportioned cards at their natural size.
6. **Side-by-side panels that must align row by row are one CSS grid** (each field = one row spanning both
   columns), not two independent flex columns.
7. **Popups/lightbox are siblings of `#deck`**, never children (the deck's `transform` breaks `position: fixed`).
   Text inside them needs explicit colours.
8. **Videos never loop**; auto-play once on first view; multi-video slides stagger 5 s; at most one plays with
   sound per slide; full-screen videos block slide navigation underneath.
9. **Text in generated images is baked in** — keep it short, spell it exactly in the prompt, proofread at full
   resolution. Long text belongs in HTML.
10. **Respect scope.** Change only what was asked; don't redesign approved slides; when copying a slide, copy its
    full markup *and* effective CSS/behaviour. When a pptx/md update implies an interaction-model decision (not
    just content), ask before building.
11. **Never put credentials in the deck folder.** API keys and config files (`config.json`, `credential.json`) stay outside it.

## Templates (`templates/`, indexed in `templates/index.json`)

Each has the same structure: `template.html` (working sample deck), `template.json` (metadata for
picking), `design.md` (tokens in YAML front matter + rules). Read `design.md` before editing a copy.

| Template | Use for | Engine |
|---|---|---|
| `byteplus/` | BytePlus solution / product pitches with image + video proof; brand logos + timeline in `assets/img/` | fluid navy/gold slides + media runtime |
| `byteplus-light/` | the same BytePlus deck in the light look of the official BytePlus pptx master (pale blue gradient backgrounds, dark logo, BytePlus blue); best for pptx conversions and architecture diagrams | same as `byteplus`, generated from it |
| `ai-tech-light/` | brand-free AI tech deck in the byteplus-light look: no logo, AI icon in concentric circles on cover / part / end, generic About-[Organisation] timeline; for AI product or solution pitches by any organisation | same as `byteplus`, generated from it |
| `work-review/` | generic review of project progress or work performance (no personal / company info): results vs goals, workstreams, initiatives, reflections, next steps, popups | fluid navy/gold slides + popup system |
| `bible-study/` | Bible study, sermons, Sunday school, small groups (Chinese-first) — verse cards, popups, discussion questions | fixed 1920×1080 canvas, inline engine |
| `studio/` | loud design-studio / brand showcase (black + acid yellow) | horizontal slide strip |

To start: copy the template folder into the project, rename `template.html`, delete/duplicate slides, replace
`[bracketed]` text and `.ph` placeholders with real media, then validate + screenshot.

## Bundled resources

| Path | What it is |
|---|---|
| `scripts/build_deck.py` | Generator on top of `templates/byteplus/`, `templates/byteplus-light/` or `templates/ai-tech-light/` (set `TEMPLATE_DIR`): helpers `feature() cover() part() closing() frame(plate=) diagram() video() video_placeholder() mcell() mrow() pills() points()`; copies the brand images |
| `scripts/make_byteplus_light.py` | Regenerates `templates/byteplus-light/template.html` from `templates/byteplus/` — re-run after any byteplus change |
| `scripts/make_ai_tech_light.py` | Regenerates `templates/ai-tech-light/template.html` from `templates/byteplus/` + the light CSS (`--images` rebuilds the AI-icon cover background) — re-run after any byteplus or byteplus-light change |
| `scripts/validate_deck.js` | Static checks: JS syntax, duplicate IDs, missing local assets, slide IDs, tiny fonts, `object-fit: cover` |
| `scripts/screenshot_deck.py` | Playwright: PNG of every slide at chosen sizes with transitions off + overflow-vs-footer report |
| `scripts/export_pdf.py` | Playwright: one PDF page per slide (screenshot-based, works for every template) |
| `scripts/title_case.py` | Applies Title Case to every heading/label in a deck (minor words, hyphens, brand spellings kept); `--dry-run` lists changes |
| `scripts/pptx_extract.py` | python-pptx text/notes dump + PNG of every slide via PowerPoint COM (Windows with PowerPoint installed) |
| `scripts/make_logo.py` | Cut a logo out of brand art into a transparent PNG by channel threshold |
| `scripts/match_background.py` | Shift a generated image's dark background to the deck's exact background colour |
