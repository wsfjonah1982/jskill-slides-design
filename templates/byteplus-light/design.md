---
version: alpha
name: BytePlus Light
description: "The BytePlus deck system in the light look of the official BytePlus PowerPoint master. Same slides, layout engine and media runtime as the byteplus template (click-to-zoom images, ratio-locked frames that never crop, a video model that auto-plays once and never loops); the look changes to the pptx master's pale blue gradient backgrounds, the dark-text BytePlus wordmark, bold DM Sans titles with a BytePlus-blue second half, and white cards and plates."

colors:
  paper: "#F5F8FF"
  text: "#1D2028"
  text-2: "#4E5969"
  text-3: "#86909C"
  blue: "#0068FF"
  hairline: "#C6D6EF"
  header-gradient: "#0092FF → #006CFF"
  blue-tint-band: "rgba(0,104,255,0.09)"
  blue-tint-soft: "rgba(0,104,255,0.06)"
  card: "rgba(255,255,255,0.8)"

color-aliases:
  c-bg: paper
  c-fg: text
  c-fg-2: text-2
  c-fg-3: text-3
  c-accent: blue
  c-border: hairline

typography:
  scale-unit: "--u: min(1vw, 1.7778vh)  (16px at 1600×900)"
  display:
    fontFamily: "DM Sans, Noto Sans SC, system-ui, sans-serif"
    fontWeight: 700
    use: "cover title — the <em> half drops to its own line in blue"
  h1:
    fontFamily: "DM Sans"
    fontWeight: 700
    use: "part-opener title"
  h2:
    fontFamily: "DM Sans"
    fontWeight: 700
    fontSize: 3u
    use: "every feature-slide title; second half in <em> = BytePlus blue, upright"
  lead:
    fontFamily: "DM Sans"
    fontSize: 1.4u
  label:
    fontFamily: "IBM Plex Mono"
    fontSize: 0.7u
    textTransform: uppercase
    use: "chrome, footer, tags, kickers"

components:
  backgrounds:
    description: "assets/img/bg-light-cover.jpg (concentric circles + the BytePlus 'M' icon, from the pptx title layout) on cover, part openers and the end slide; assets/img/bg-light-content.jpg (white-to-blue gradient, from the pptx content layout) on every other slide. Both 1920×1080, background-size: cover."
  logo:
    description: "assets/img/byteplus_logo_light.png — dark-text wordmark + blue mark, transparent, 1071×194 (the byteplus logo with its white text recoloured #1D2028). Never on a dark field."
  part-mark:
    description: "Hidden: the cover background already carries the 'M' icon."
  lede:
    description: "One-sentence band under the title (blue tint, blue left edge)."
  frame:
    description: "Content image box with --r = width/height; white surface. .frame.plate = a light diagram on a white plate with a hairline border and a soft blue shadow (use scripts/build_deck.py diagram())."
  vid:
    description: "Video box on white; light 'Click to play' hint and play button."
  placeholder:
    description: ".ph — blue-striped placeholder; replace with real media."
---

## Overview

BytePlus Light is the **byteplus** template restyled to match the official BytePlus PowerPoint master, so an HTML deck sits next to the company's pptx decks without looking like a different brand. Every slide, class and runtime behaviour is the same as `byteplus`; read `../byteplus/design.md` for the slide catalogue, story spine, media rules and do's and don'ts. This file lists only what differs.

## How it is made

`template.html` is generated: `python scripts/make_byteplus_light.py` reads `templates/byteplus/template.html`, swaps the logo to `byteplus_logo_light.png`, and appends one light-theme CSS block. **Don't hand-edit `template.html`** — change the CSS in the script (or fix the shared slides in `byteplus`) and re-run it, so both templates stay in sync.

## Look

- Backgrounds are the pptx master's own images: circles + "M" icon on cover / part / end, a soft white-to-blue gradient elsewhere. The cover title's blue half wraps to its own line so it never runs over the icon.
- Near-black text `#1D2028`; one accent, BytePlus blue `#0068FF` — title halves, numbers, pills, tags, active tab, nav dot. Gold is gone entirely.
- Bold DM Sans for every title (the pptx uses a bold sans); body DM Sans; chrome IBM Plex Mono.
- Cards, edit card, part cards and plates are white with a hairline `#C6D6EF` border and a soft blue shadow. Header bars in deck-specific layouts use the pptx's blue gradient `#0092FF → #006CFF` with white text.
- Lightbox and speaker-notes panel are light too.

## Using the template

1. Copy `templates/byteplus-light/` (template.html + assets/) into the project; rename the HTML. Or set `TEMPLATE_DIR` in `scripts/build_deck.py` to this folder — the script picks the light logo and backgrounds automatically.
2. Everything else as in `../byteplus/design.md` → "Using the template".
3. Light diagrams (architecture slides from a pptx) go on `.frame.plate`; dark screenshots and videos sit fine on the white frames.

## Known Gaps

- Same as byteplus: Google Fonts online; the small `n / N` counter duplicates the footer counter; timeline content as of Oct 2026.
- The background JPEGs are 1920×1080; on a 4K screen they are upscaled (they are soft gradients, so this is barely visible).
