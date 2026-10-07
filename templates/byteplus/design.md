---
version: alpha
name: BytePlus
description: "The BytePlus industry-solution deck system. It is a navy-and-gold slide system (navy field, warm off-white type, one antique-gold accent, Source Serif 4 / DM Sans / IBM Plex Mono) made BytePlus-specific: the white BytePlus wordmark on every slide, a bp-mark watermark on part openers, the ByteDance → BytePlus product timeline, and a media-first runtime that turns slides into proof — click-to-zoom images, ratio-locked frames that never crop, and a video model that auto-plays once, never loops and plays the single video on a slide with sound."

colors:
  navy: "#071027"
  glow-blue: "rgba(48,104,231,0.43) radial, 82% 22%"
  sweep-violet: "rgba(109,83,232,0.14) linear 120deg"
  navy-deep: "#0F1730"
  text: "#E2DCD0"
  text-2: "#8A96A8"
  text-3: "#4E5A6E"
  gold: "#C8A870"
  hairline: "#2E3D5C"
  gold-tint-soft: "rgba(200,168,112,0.08)"
  gold-tint-band: "rgba(200,168,112,0.18)"
  brand-blue: "#1259FC"

color-aliases:
  c-bg: navy
  c-fg: text
  c-fg-2: text-2
  c-fg-3: text-3
  c-accent: gold
  c-border: hairline

typography:
  scale-unit: "--u: min(1vw, 1.7778vh)  (16px at 1600×900)"
  display:
    fontFamily: "Source Serif 4, Noto Serif SC, Georgia, serif"
    fontSize: "6.6u (cover title on one line)"
    fontWeight: 600
  h1:
    fontFamily: "Source Serif 4"
    fontSize: 5.2u
    use: "part-opener title"
  h2:
    fontFamily: "Source Serif 4"
    fontSize: 3u
    use: "every feature-slide title; second half in <em> = gold italic"
  h3:
    fontSize: 1.9u
    use: "part cards, edit card, points"
  lead:
    fontFamily: "DM Sans, Noto Sans SC, system-ui"
    fontSize: 1.4u
  media-label:
    fontFamily: "Source Serif 4"
    fontSize: 1.5u
  label:
    fontFamily: "IBM Plex Mono, JetBrains Mono, monospace"
    fontSize: 0.7u
    textTransform: uppercase
    use: "chrome, footer, tags, kickers"

spacing:
  pad-x: 7.5vw
  pad-y: 5.5vh
  media-gap: 2.4u

components:
  chrome:
    description: "Top bar: mono '§ label' left, BytePlus wordmark (1.55u high) right. Footer: hairline, '[Deck] · [Mon YYYY]' left, 'NN / TT' right."
  logo:
    description: "assets/img/byteplus_logo_dark.png (white wordmark + blue mark, transparent, 1071×194). .bp-logo in chrome; .bp-logo-cover top-right on cover / part / end. Never on a light field."
  part-mark:
    description: "assets/img/bp-mark.png — the large gradient BytePlus mark as a watermark on part openers only. Decorative: not zoomable."
  lede:
    description: "One-sentence band under the title (gold-tint fill, gold left edge)."
  tag:
    description: "Mono product tag next to the title (e.g. SEEDREAM 5.0, SEEDANCE 2.5)."
  pills:
    description: "Numbered value pills; .pill--x2 at 2× size with the keyword in gold <strong>. Columns 'auto auto auto' + space-between + nowrap so all three stay on one line."
  frame:
    description: "Content image box with --r = image width/height, sized by container query to fit the remaining height. Click → lightbox. Box ratio = image ratio, so nothing crops."
  vid:
    description: "Video box with poster, play button, 'Click to play' hint; --r = video ratio. .vid--fs = never auto-plays, click plays full screen with sound."
  timeline:
    description: ".tl grid: era bands, product logos, names, dots, dates; .tl-hl box around the BytePlus column. Every item has an explicit grid-column/row."
  ec-grid:
    description: "2×2 use-case grid; each cell = label + strip of frames with fr widths matching the images."
  cap-tabs:
    description: "Three tab buttons (icon + benefit) swapping .cap-panel before/after pairs in place; the chosen tab persists."
  layers:
    description: "Layer playground (.ly-wrap, scripts/layer_slide.py): one or two images, each a background + transparent cut-out layers; drag to move, corner to resize, top handle to rotate (Shift = 15°), drop on the other image; Hide backgrounds / Hold to see originals / Reset; a thumbnail tray per image. Clicks hit only visible pixels (a 40-column alpha mask per layer). Content = the deck's assets/img/layers/layers.json + images; the template shows a striped placeholder (layer_wrap(None))."
  edit:
    description: "Text column (lead, body, edit-card with meta row + h3) beside an Original/Altered media pair."
  agent:
    description: "Gold flow bar (Goal → Assets → Skill → Auto/Manual → Review), numbered points (.pts, .pts.plain without descriptions), Auto/Manual chips; demo video right with a caption."
  placeholder:
    description: ".ph — striped placeholder inside a .frame or .vid; delete the class and add the img / video src + poster when real media exists."
---

## Overview

BytePlus is the house deck for **BytePlus industry-solution talks**: a dark navy annual-report look with one warm gold accent, built so that the proof — generated images, ad videos, product demos — does the persuading. It is a navy-and-gold slide system with three BytePlus layers on top: the brand (wordmark, watermark, product timeline), a set of media layouts proven in real pitch decks, and a runtime that makes images and videos behave well in front of an audience.

**All slides are dark** because the packaged logo is the white wordmark. Don't introduce cream slides unless a dark-on-light logo is added and documented.

## Story spine (what worked)

Cover → About BytePlus (timeline) → what we offer (value pills + product panels) → **Part 01 / 02 / 03** openers, each followed by 2–5 proof slides (image grids, tabs, video grids, text + media pairs) → product/agent explainer with a demo → Thank You. Part openers map the talk: one claim per part ("Test ideas in Minutes", "Cost-saving from Repeated Shooting", "Idea to Content Automation").

## Slides in the template

| # | Layout | Use for |
|---|---|---|
| 1 | Cover | one-line title with gold-italic keyword, "From X to Y" subtitle, presenter · date |
| 2 | About BytePlus | standard company intro + ByteDance→BytePlus timeline (real logos, BytePlus boxed) |
| 3 | Value pills + product panels | three outcomes in 2× pills, two product panel images |
| 4 | Part opener | Part NN, claim, outcome, 1–2 product cards, bp-mark watermark |
| 5 | 2×2 use-case grid | four image use cases, input → output strips |
| 6 | Tabs · before/after | merge several near-identical capability slides into one clickable slide |
| 7 | Layer playground | let the audience move, resize and rotate the objects of a layered image (ships as a striped placeholder; the deck supplies its own layered images) |
| 8 | Video grid · 3 vertical | 9:16 ad formats side by side (start 5 s apart) |
| 9 | Text card + media pair | a capability explained left, original vs altered right |
| 10 | Agent explainer | flow bar + 4 points + a click-to-full-screen demo |
| 11 | Thank You | close |

Other patterns that are in the CSS but not in the sample slides: `.sm-strip` + `.mtag` (static → motion pairs), `.mrow.c2` landscape videos, `slide--models` pills variant.

## Colors

Navy `#071027` field with a blue radial glow top-right and a faint violet sweep (on every slide; no grid texture), `#0F1730` behind media; text `#E2DCD0`, secondary `#8A96A8`; gold `#C8A870` for title halves, numbers, pills, rules, active tab, highlight box; hairline `#2E3D5C`. Gold tints: 8 % for boxes, 18 % for the lede band and kicker. The BytePlus blue lives only in the logo assets.

## Typography

Source Serif 4 for titles and media labels (second half of a title in gold italic), DM Sans for body, IBM Plex Mono uppercase for chrome, tags and kickers. Every feature-slide title is the same `--sz-h2` (3u); the cover title stays on one line. Sizes are `calc(N * var(--u))`; if you edit CSS in vw, convert it.

## Media rules (non-negotiable)

- Set `--r` on every `.frame` / `.vid` to the media's own width ÷ height; the box then fits the remaining height without cropping (the `object-fit: cover` warnings from the validator are safe inside these ratio-locked boxes).
- Videos: never loop; auto-play once on first view; several on a slide start 5 s apart; a slide's single video plays with sound (`play()` called in the navigation gesture's task); click to play/pause; leaving a slide resets them. Demo videos use `.vid--fs` (no autoplay, click = full screen with sound; keys can't move the deck while full screen).
- Every video needs a poster (frame 0) and should be remuxed `+faststart`.
- Light diagrams (e.g. architecture slides from a pptx): `.dg > .frame.plate` (`diagram()` in `scripts/build_deck.py`) fills the rest of the body on a light plate, never cropped.
- Content images are click-to-zoom; logos, watermark and timeline icons are plain `<img>` outside `.frame`, so they aren't.
- Speaker notes: `data-notes` on the section, `N` toggles; `F` toggles fullscreen.

## Do's and Don'ts

**Do** keep one claim per slide with the proof under it; use the pptx's exact wording when converting, with every title and heading in Title Case; keep all three pills on one line (measure at 1280, 1600, 1920 wide); give every timeline item explicit grid positions; check videos actually have audio (`ffprobe`) before debugging sound.

**Don't** crop customer media; add a light slide with the white logo; put a second accent colour in chrome; shrink a title to fit (rephrase); let the single-video slide's `play()` move into a `setTimeout` (sound gets blocked).

## Using the template

1. Copy `templates/byteplus/` (template.html + assets/) into the project; rename the HTML.
2. Delete or duplicate slides; give each section a unique `id`; update the footer total `NN / TT`.
3. Replace `[bracketed]` text; replace each `.ph` with real media: `<img src="assets/img/…">` inside `.frame`, or `<video src=… poster=…>` inside `.vid` (remove `ph-label`).
4. Layer playground with your own images: put a background, the original and one transparent PNG per object in
   `assets/img/layers/`, list them in `layers.json` (see the docstring of `scripts/layer_slide.py`), run
   `python scripts/layer_slide.py masks assets/img/layers/layers.json`, and swap the slide's `.ly-wrap` for
   `layer_wrap(...)` output (the build script's `layers()` helper does this). After editing `LAYER_CSS` / `LAYER_JS`,
   run `python scripts/layer_slide.py sync templates/byteplus/template.html`, then the make scripts.
5. For a larger deck, move to a build script (`scripts/build_deck.py`) instead of hand-editing.
6. Validate and screenshot (`scripts/validate_deck.js`, `scripts/screenshot_deck.py`), then open it for the user.

## Known Gaps

- Fonts load from Google Fonts; offline fallbacks are Georgia / system-ui / monospace.
- For a light deck use `templates/byteplus-light/` (generated from this template by `scripts/make_byteplus_light.py`; re-run it after editing this template).
- The template's own small `n / N` counter (bottom-right, from the slide engine) duplicates the footer counter.
- The timeline content is as of Oct 2026; update dates and products when they change.
