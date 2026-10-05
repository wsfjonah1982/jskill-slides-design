---
version: alpha
name: Bible Study
description: "An \"Ivory & Gold Scripture\" teaching-deck system in the register of an illuminated manuscript: ivory paper with soft radial glows, one classical serif (Noto Serif SC), gold titles between fading gold rules with diamond ends, teal scripture-reference pills, copper-ringed number badges and olive-branch corner ornaments. The slide carries the title, structure and short headings; full passages, notes and comparison tables open in click-to-enlarge popups at 48px. Fixed 1920×1080 canvas scaled to the window, so every element is positioned in canvas pixels and can line up with generated illustrations."

colors:
  ivory: "#F6EEE1"
  ivory-deep: "#EFE3CF"
  gold: "#B98A4E"
  gold-dark: "#8A5F1F"
  gold-light: "#D8B88A"
  gold-line: "#D9BD8F"
  teal: "#24565B"
  teal-soft: "#4C7B7F"
  copper: "#C0703F"
  peach: "#F3D9BF"
  crimson: "#9A3F33"
  ink: "#2F3B3C"
  ink-soft: "#5B6768"
  card: "rgba(255,255,255,0.62)"
  letterbox: "#E6DCCB"

color-roles:
  title: gold
  ornament: gold
  structure: teal
  reference-pill: teal
  positive-column: teal
  badge-ring: copper
  badge-fill: peach
  warning: crimson
  negative-column: crimson
  body: ink
  secondary: ink-soft
  highlight-text: gold-dark

typography:
  cover:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, STSong, SimSun, serif"
    fontSize: 112px
    fontWeight: 700
    letterSpacing: 0.06em
    color: gold
  title:
    fontSize: 64px
    fontWeight: 700
    letterSpacing: 0.04em
    color: gold
  subtitle:
    fontSize: 28px
    fontWeight: 400
    color: teal
  column-heading:
    fontSize: 36px
    fontWeight: 700
    color: teal
  question:
    fontSize: 36px
    fontWeight: 700
    color: teal
  body-note:
    fontSize: 25px
    lineHeight: 1.62
  verse-card:
    fontSize: 23px
    lineHeight: 1.62
  verse-card-large:
    fontSize: 29px
    lineHeight: 1.86
  verse-list:
    fontSize: 32px
    lineHeight: 1.55
  table-cell:
    fontSize: 32px
    lineHeight: 1.5
  table-header:
    fontSize: 38px
    fontWeight: 700
    color: "#ffffff"
  reference-pill:
    fontSize: 19-24px
    fontWeight: 500
    letterSpacing: 0.14-0.18em
    color: "#ffffff on teal"
  memory-verse:
    fontSize: 54px
    lineHeight: 1.75
  popup-text:
    fontSize: 48px
    lineHeight: 1.8
  popup-note:
    fontSize: 38px
    lineHeight: 1.6

canvas:
  width: 1920px
  height: 1080px
  scaling: "transform: scale(min(vw/1920, vh/1080)), letterboxed"
  header-zone: "y 24–150"
  content-zone: "y 150–1000"
  nav-clearance: "bottom 60px"

components:
  head:
    description: "Centred title between two 2px gold rules that fade outward, each ending in a 9px gold diamond at the title; subtitle directly below in teal with key words in bold gold (or crimson)."
  olive:
    description: "SVG symbol #olive (gold stem, teal + gold leaves). 190px top-left and mirrored top-right on every slide; .sm = 140px for dense slides; .bl/.br bottom corners for cover-like closing slides."
  verse:
    description: "The one scripture component. Translucent white card, 6px gold left bar, 6/18px radius, soft shadow; teal reference pill on top, justified serif text below; expand icon top-right. Click/Enter opens the popup. .verse.lg for a key passage."
  vchip:
    description: "Reference chip: only the teal pill + white expand icon shows; hidden .text and .pop-extra open in the same verse popup. Use where there is no room for a card."
  pop-extra:
    description: "Notes attached to a verse/chip, hidden on the slide, shown in the popup under a dashed gold divider with gold diamond bullets. A verse quoted inside a note starts with a bold teal .vref label."
  hl:
    description: "Highlight marker: bold dark-gold text with a gold highlighter stripe on the lower 40%. .hl.warn = crimson text with a thin crimson underline. Max 1–2 per passage."
  badge:
    description: "46–64px circle, peach radial fill, 2.5px copper ring, copper numeral."
  band:
    description: "Full-width 1920px strip showing a crop of a generated 16:9 illustration (img moved with a negative top); top/bottom edges masked so it melts into the paper. .band.radial adds an elliptical fade."
  cols:
    description: "Three 570px columns at left 89 / 675 / 1270px, centred under the three circles (x≈374 / 960 / 1555) of a 3-part picture band."
  banner:
    description: "Notched ribbon (clip-path), gold border, ivory gradient, one centred sentence with key words coloured. With data-pop it becomes a popup trigger with an expand icon."
  stage-chips:
    description: "Pills with a coloured dot + label + muted sub-label, joined by gold › arrows. For 3-step progressions."
  vlist:
    description: "Numbered verse list: badges joined by a thin vertical gold thread, each beside a compact verse card at 32px."
  cmp:
    description: "Comparison table with spaced rounded cells (border-spacing 12/14px): gold dimension column with badge labels, teal positive column, crimson negative column; gradient header cells with white text and a small sub-label."
  qcard:
    description: "Discussion-question card: badge, 36px teal question + 25px muted hint line, a reference chip at the right."
  memory:
    description: "Closing memory verse: large ref pill, 54px centred text with one highlight, application banner below."
  popup:
    description: "Overlay mounted inside the active slide (teal wash, 7px blur). Ivory panel 1560px (1740px .wide for tables), 14px gold left border, 14/36px radius, big shadow, round × top-right. Esc / click outside / × closes; keys blocked while open; changing slide closes it."
  placeholder:
    description: ".ph — dashed gold, diagonal-striped box with a label, standing in for a generated image until it exists. Delete it when the img goes in."
---

## Overview

Bible Study is a **teaching deck that reads like an illuminated manuscript page**. Everything sits on warm ivory paper lit by three soft radial glows; the only ornaments are thin gold rules with diamond ends and an olive branch in each top corner. One classical serif carries every word, so the deck feels like a printed study Bible rather than a corporate template.

The governing principle is **keep the slide light and put the detail in popups**. A slide shows a title, a subtitle, perhaps one illustration, and short headings or labels. Long text — full passages, study notes, comparison tables — is one click away in a popup that renders the passage at 48px, readable from the back of a room. This lets a leader walk a group through the structure first and open the text exactly when it is read aloud.

The canvas is **fixed at 1920×1080** and scaled to fit the window. Elements are absolutely positioned in canvas pixels. That trade-off (less fluid than a vw-based system) is deliberate: generated illustrations have fixed geometry, and the three-column layout must sit precisely under the three circles of a picture band.

**Key characteristics**
- Ivory paper + gold titles + teal structure; copper/peach badges; crimson reserved for warning wording ("slave", "sin", the negative column).
- One serif family (Noto Serif SC) at every size; titles 64px on every slide, subtitles 28px.
- One verse component everywhere — card or chip — and one popup system.
- Popups live inside the active slide so they scale with the canvas.
- Illustrations are AI-generated in the same ivory/gold/teal style and cropped into the page with feathered edges.

## Colors

- **Ivory** `#F6EEE1` — the paper. **Ivory Deep** `#EFE3CF` — deeper paper tone. A slide built around a picture may override its background to match the picture's paper where the crop fades out.
- **Gold** `#B98A4E` — titles, card bars, diamonds, popup border. **Gold Dark** `#8A5F1F` — highlighted words. **Gold Light / Gold Line** `#D8B88A` / `#D9BD8F` — borders, rules, dashed dividers.
- **Teal** `#24565B` — subtitles, column headings, questions, reference pills, the positive table column. **Teal Soft** `#4C7B7F` — secondary teal, background glow.
- **Copper** `#C0703F` + **Peach** `#F3D9BF` — number badges and the table's dimension column.
- **Crimson** `#9A3F33` — warning/negative wording only.
- **Ink** `#2F3B3C` / **Ink Soft** `#5B6768` — body and secondary text.

Rules: gold means title or ornament, teal means structure or label, crimson means warning. Don't add other hues. Coloured dots in stage chips may take the illustration's own colours.

## Typography

| Use | Size | Weight / colour |
|---|---|---|
| Cover title | 112px | 700, gold, 0.06em |
| Slide title | **64px, every slide** | 700, gold, 0.04em |
| Subtitle | **28px, every slide** | 400, teal; key phrase bold gold or crimson |
| Column / question heading | 36px | 700, teal |
| Body note | 25px | 400, ink, line-height 1.62 |
| Verse card / large card | 23px / 29px | ink, justified |
| Numbered verse list | 32px | ink |
| Table cell / header | 32px / 38px | ink / 700 white |
| Reference pill | 19–24px | 500, white on teal, 0.14–0.18em |
| Memory verse | 54px | ink, one highlight |
| Popup text / notes | 48px / 38px | ink |

Use `text-wrap: balance` on headings and `pretty` on body so no line ends with a single character. Put `&nbsp;` inside short references (book + number) if they wrap. Nothing on a slide below 19px.

## Layout

**Header zone** y 24–150: title row (rules + title) and subtitle, centred. **Content zone** y 150–1000. **Bottom 60–80px clear** for the nav dots outside the canvas and for the banner's breathing room.

| Layout | Slide | Use for |
|---|---|---|
| A. Cover | 1 | series kicker → title → rule → passage → key verse → meta |
| B. Scripture + image | 2 | key passage (large card) beside a framed illustration + stage chips |
| C. Picture band + three columns | 3 | three parallel points; columns under the picture's circles; chips open the verses |
| D. Numbered verse list | 4 | 4–6 passages in order (thread joins the badges) |
| E. Comparison table | 5 | two things side by side, 3 cols × 4–5 rows |
| F. Discussion questions | 6 | 3 question cards, each with a hint and a reference chip |
| G. Diagram + banner | 7 | summary illustration; banner and diagram open a table popup |
| H. Memory verse | 8 | closing verse + this week's application |

In layout C, when columns only hold headings, give every column one reference chip so they look the same, and put the detail in popups.

## Popups

- Triggers: `.verse`, `[data-pop="verse"]` (chips), `[data-pop="table"][data-table="id"]` (keyboard-focusable), `[data-pop-click="table"]` (mouse-only extra hit area such as a diagram).
- Verse popup = cloned ref pill + text at 48px + optional `.pop-extra` notes. Table popup = copy of the hidden `.pop-data#id > table` in a 1740px `.wide` panel.
- **Size limit: the panel must fit inside 1080px** — about 3–4 lines of main text plus 3–4 notes. More → split into a second chip.
- Esc, click outside, or × closes; arrow keys are blocked while open; changing slide closes it.

## Illustrations

Generate at 16:9 (about 2.7K × 1.5K) with any image model; once the deck has one illustration you like, pass it as the style reference for the rest. Style prompt: *ivory paper texture, thin gold linework and flourishes, circular painted vignettes with teal rims, numbered copper badges above the circles, olive-branch corners, soft warm light.* For three-point slides ask for three evenly spaced circles so they land at x≈374 / 960 / 1555 on the 1920 canvas. Keep in-image Chinese very short, spell it exactly in the prompt, and **proofread every image at full resolution** — baked-in text can't be edited. Long text belongs in HTML.

Placing it: drop the `.ph` placeholder, add `<img>` inside `.band`, and tune the image's negative `top` so the useful strip shows; match the slide background to the image's paper tone at the crop edge if they differ.

## Source → slide

One markdown file per slide (`Title:` on line 1, subtitle paragraph, then a bullet tree: point → quoted passage → notes). Title → head, subtitle → subtitle, top-level bullets → column/question headings, passage → verse card or chip, notes under the passage → that popup's `.pop-extra`.

Text hygiene: full-width Chinese punctuation, no stray or full-width spaces (e.g. the `　神` spacing in some Bible editions), drop inline verse numbers inside multi-verse passages, drop outer quotation marks on cards (the pill names the source), end notes with 。. Highlight at most 1–2 phrases per passage.

## Do's and Don'ts

**Do** keep every title 64px and every subtitle 28px; use one verse component everywhere; put long text in popups; keep columns centred under picture circles; proofread generated images; keep the bottom clear for navigation.

**Don't** shrink verse text to fit (split instead); add colours outside the palette; use crimson for anything but warning wording; mix a second font family; put essential reasoning in a picture; crop away a verse reference.

## Responsive, Print and Export

The canvas scales uniformly (letterboxed on `#e6dccb`), so 1280×720, 1920×1080 and 4K look identical. Browser **Print → Save as PDF** gives one 1920×1080 page per slide with selectable text (popups excluded). `scripts/export_pdf.py` makes a screenshot PDF; `screenshot_deck.py` renders every slide for review (both drive the nav dots).

## Iteration Guide

1. Copy `template.html` to the project as `<deck>.html`; keep images beside it.
2. Delete layouts you don't need; duplicate the ones you do. Give each `section.slide` a unique `id` and a `data-label`.
3. Replace the `[bracketed]` placeholders with the study's title, passages, points, questions and notes.
4. Replace each `.ph` with the generated image.
5. Check every slide and every popup at 1920×1080: nothing overlaps, popups fit, chips line up.

## Known Gaps

- Fonts load from Google Fonts; offline it falls back to Source Han Serif SC / Songti SC / STSong / SimSun.
- On touch screens swipe changes slides; popups need a tap on the card (works) but there's no long-press preview.
- No speaker-notes view and no video handling; if a study needs clips, follow the video rules in `references/media-popups-runtime.md`.
- No automatic md → HTML parser; slides are edited by hand from the md files.
