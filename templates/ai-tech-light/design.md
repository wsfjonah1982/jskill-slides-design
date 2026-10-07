---
version: alpha
name: AI Tech Light
description: "A brand-free light AI deck. Same slides, layout engine and media runtime as the byteplus template (click-to-zoom images, ratio-locked frames that never crop, a video model that auto-plays once and never loops) in the byteplus-light look: pale blue gradient backgrounds, bold DM Sans titles with a blue second half, white cards and plates. No logo anywhere; the title pages carry an AI icon in concentric circles."

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
    use: "every feature-slide title; second half in <em> = blue, upright"
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
    description: "assets/img/bg-cover.jpg (concentric circles with the AI icon in the middle circle, right of centre) on cover, part openers and the end slide; assets/img/bg-content.jpg (white-to-blue gradient) on every other slide. Both 1920×1080, background-size: cover."
  ai-mark:
    description: "assets/img/ai-mark.png — the AI icon alone, #0068FF on transparent. Source for bg-cover.jpg; also usable as a small mark on a slide."
  logo:
    description: "None. The chrome bar shows only the section label. Add a client logo by hand if a deck needs one (an <img> in .slide-chrome, height ≈ 1.55u)."
  about-timeline:
    description: "Slide 2: 6 columns (eras → logo box → milestone → dot → date), one highlighted column. Replace each .tl-logo.ph with a .tl-logo holding an <img>, or delete the logo row."
  lede:
    description: "One-sentence band under the title (blue tint, blue left edge)."
  frame:
    description: "Content image box with --r = width/height; white surface. .frame.plate = a light diagram on a white plate with a hairline border and a soft blue shadow (scripts/build_deck.py diagram())."
  vid:
    description: "Video box on white; light 'Click to play' hint and play button."
  placeholder:
    description: ".ph — blue-striped placeholder; replace with real media."
---

## Overview

AI Tech Light is the **byteplus-light** look without the BytePlus brand: no wordmark, no product logos, no
BytePlus copy. Every slide, class and runtime behaviour is the same as `byteplus`; read `../byteplus/design.md`
for the slide catalogue, story spine, media rules and do's and don'ts. This file lists only what differs.

## How it is made

`template.html` is generated: `python scripts/make_ai_tech_light.py` reads `templates/byteplus/template.html`,
removes every logo and the part watermark, swaps slide 2 for a generic About-[Organisation] timeline, turns
product names into `[Model A]` / `[Model B]`, and appends the byteplus-light CSS (imported from
`make_byteplus_light.py`) with its own background file names. **Don't hand-edit `template.html`** — change the
script and re-run it. `--images` also rebuilds `bg-cover.jpg` (the light circles, centre mark painted out,
`ai-mark.png` placed with a soft white halo) and `bg-content.jpg`; it needs `numpy` and `opencv-python`.

## Look

- Cover, part openers and the end slide: concentric circles with the AI icon in the middle circle on the right;
  the title block sits on the left. The cover title's blue half wraps to its own line so it stays clear of the icon.
- Content slides: the soft white-to-blue gradient, no logo in the chrome bar.
- Near-black text `#1D2028`; one accent, blue `#0068FF` — title halves, numbers, pills, tags, active tab, nav dot.
- Bold DM Sans for every title; body DM Sans; chrome IBM Plex Mono.
- Cards, edit card, part cards and plates are white with a hairline `#C6D6EF` border and a soft blue shadow.

## Using the template

1. Copy `templates/ai-tech-light/` (template.html + assets/) into the project; rename the HTML. Or set
   `TEMPLATE_DIR` in `scripts/build_deck.py` to this folder — the script drops the logo, uses `KICKER` for the
   cover / end kicker and copies `bg-cover.jpg` + `bg-content.jpg`.
2. Everything else as in `../byteplus/design.md` → "Using the template".
3. Light diagrams go on `.frame.plate`; dark screenshots and videos sit fine on the white frames.

## Known Gaps

- Same as byteplus: Google Fonts online; the small `n / N` counter duplicates the footer counter.
- The background JPEGs are 1920×1080; on a 4K screen they are upscaled (soft gradients, barely visible).
