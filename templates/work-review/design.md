---
version: alpha
name: Work Review
description: "A generic executive review deck for project progress or work performance. Navy field with a faint 80px grid, warm off-white text, one antique-gold accent, Source Serif 4 / DM Sans / IBM Plex Mono. The slide carries the headline, structure and numbers — attainment, goal bars, labelled workstream fields — and the detail (initiative write-ups, diagrams, outcome evidence) opens in full-slide popups, small image popups or the lightbox. Two-panel slides are one CSS grid with a row per field, so left and right always align. Unbranded: an [Organisation] text slot sits where a logo would go."

colors:
  navy: "#1C2644"
  text: "#E2DCD0"
  text-2: "#8A96A8"
  text-3: "#4E5A6E"
  gold: "#C8A870"
  hairline: "#2E3D5C"
  plate: "#FFFFFF"
  gold-fill-soft: "rgba(200,168,112,0.06-0.08)"
  gold-fill-band: "rgba(200,168,112,0.18)"

typography:
  scale-unit: "--u: min(1vw, 1.7778vh)  (16px at 1600×900)"
  display: { fontFamily: "Source Serif 4", fontSize: 9.5u, fontWeight: 600 }
  h2: { fontFamily: "Source Serif 4", fontSize: "3u (48px) on every slide", decoration: "1px gold underline; second half in <em> = gold italic" }
  h3-panel: { fontFamily: "Source Serif 4", fontSize: "1.875u (30px)" }
  lead: { fontFamily: "DM Sans", fontSize: 1.4u }
  score: { fontFamily: "Source Serif 4", fontSize: 4.4u, color: gold }
  kicker-lg: { fontFamily: "IBM Plex Mono", fontSize: "label + 4px", color: gold, textTransform: uppercase }
  label: { fontFamily: "IBM Plex Mono", fontSize: "1.125u (18px) — the floor for all text" }

components:
  chrome: "Top bar: mono '§ NN · Section' left, [Organisation] slot right. Footer: hairline, '[Review Title] · [Mon YYYY]' left, 'NN / TT' right."
  header-bar: "Panel title bar (.case-col .h3, .ach-period): 18% gold fill + 3px gold left edge, 30px serif."
  field-kicker: ".label.accent.label-lg — gold mono caps above a field (Approach, Outcome, Status…)."
  bullets: ".bullet-list > li > span — gold em-dash marker; wrap the whole li text in one span so inline .hl spans don't split into grid cells."
  highlight-box: ".case-hl — 1px gold border, 8% gold fill, value line + sub line; .case-hl--link (button) adds → and opens a popup."
  score: ".ach-score-val — big gold serif percentage; .na = muted grey for 'not yet available'."
  goal-row: ".ach-goal — name · % · bar (gold fill = % width, capped at 100%) · done / target with done in bold; optional note."
  deliverables: ".ach-deals > .ach-deal — two-column rows (item · status), hairline between rows."
  hub-list: ".hub-item — big gold number, title + one-line summary, gold →; opens a full-slide popup."
  priority-boxes: ".tc-card / .tc-card--hl — numbered box; --hl = solid gold with navy text for the single top priority."
  image-grid: ".hub-grid > .hub-tile — 2×2 framed diagrams with numbered captions, click to enlarge."
  framed-diagram: ".tc-frame, .mini-frame, .pp-diagram, .hub-tile-frame — white plate, hairline border, object-fit: contain, never cropped."
  full-popup: "section.slide.dark.popup[data-popup] — a whole slide with chrome + ×, subtitle band, chips, two-column split; footer counts within its group (1 / 2)."
  small-popup: ".mini-overlay[data-popup] > .mini-panel — dimmed + blurred backdrop, navy card with gold left edge, title, description, numbered highlights, image that shrinks to fit."
  placeholder: ".ph / .ph.on-plate — striped stand-in for a diagram; replace with an <img>."
---

## Overview

Work Review is a **calm, executive review deck**: a well-set report printed on dark navy. It answers four questions in order — *what did we commit to and how did we do* (results vs goals), *what happened in each workstream* (highlights, progress), *what did we learn* (reflections), and *what happens next* (priorities, plan). Use it for a project's progress review, a team or quarterly review, or an individual's performance review; only the labels change.

**Principle: the slide carries the headline, structure and numbers; detail lives behind a click.** A slide shows a title, short labelled fields, bullets, chips and at most one picture. Write-ups, evidence and dense diagrams open in a popup or the lightbox.

**All slides are dark.** If you add a logo, use a light (white) version; don't add light slides without a dark logo variant.

## Slides in the template

| # | Slide | Use for |
|---|---|---|
| 1 | Cover | review type and period, title, name/team and role/project |
| 2 | Results vs Goals | two periods side by side: overall attainment, contributors, goal rows with bars, deliverables / status |
| 3 | Key Highlights | a context band across both panels, then two workstreams: Approach · Tools / Resources · Outcome (one outcome opens the small popup) |
| 4 | Progress by Workstream | two workstreams, a row per field: Goal · What Was Done · Status |
| 5 | Key Initiatives | overview diagram + numbered rows, each opening a full-slide popup (Scope chips, Objectives, Risks & Dependencies) |
| 6 | Reflections | What Went Well / What to Improve: Insights, Keep Doing, Change |
| 7 | Next Steps | plan or roadmap diagram + four numbered priorities, the top one in solid gold |
| 8 | Plan in Detail | subtitle band + 2×2 grid of diagrams, click to enlarge |

**Adapting the labels.** Project progress: Workstream / Milestones / Risks. Performance review: Goals / Key results / Development areas. Quarterly business review: Objectives / KPIs / Next-quarter priorities. Keep the structure; rename the kickers.

## Colors

Navy `#1C2644` field with a faint white 80px grid (3% opacity), warm off-white text `#E2DCD0`, secondary `#8A96A8`, disabled `#4E5A6E`, gold `#C8A870` for title halves, kickers, numbers, bullet dashes, chip borders, highlight boxes and bars, hairline `#2E3D5C`. Gold tints: 6–8% for boxes and chips, 18% for header bars and the subtitle band (always with a 3px gold left edge). Solid gold with navy text marks the single hero item. `.hl` = gold, weight 600, at most 1–3 terms per bullet. No other hues; colour beyond this comes only from diagrams and screenshots.

## Typography

Source Serif 4 for titles, panel titles and big numbers; DM Sans for body; IBM Plex Mono uppercase for chrome, kickers and counters. Every slide title is 3u (48px at 1600×900) with a gold underline; panel titles 30px; bullets ~22px; nothing anywhere below 18px. Keep the source wording and spelling; normalise only punctuation (no trailing `;`/`.` on bullets, curly quotes).

## Numbers

Compute percentages yourself (done ÷ target, 2 decimals) and check that parts sum to totals. Bars are capped at 100% width while the printed value stays real (e.g. 150.00% with a full bar). Use `NA` (muted) for a period that hasn't closed, plus a status line such as "In progress · period ends [date]".

## Using the template

1. Copy `templates/work-review/template.html` into the project and rename it.
2. Keep the slides you need, delete the rest; give each section a unique `id`; update every footer `NN / TT`.
3. Replace `[bracketed]` text and the `[Organisation]` slot (keep it as text, or put a light logo `<img class="org-logo">` there at ~1.55u high).
4. Replace each `.ph` placeholder with an `<img>`; diagrams on `.on-plate` white plates are framed whole, never cropped.
5. Popups: a trigger has `data-popup-open="id"`; the popup sits after `#deck` with `data-popup="id"` — a full slide (`section.slide.dark.popup`) or a small card (`.mini-overlay`). Text inside a small popup needs explicit colours.
6. For a deck that will change many times, keep one markdown file as the source of truth and generate the HTML with a build script.
7. Check: `scripts/validate_deck.js`, `scripts/screenshot_deck.py` at 1600×900 and 1280×720, open every popup, and compare every source line with the slides. Measure overflow against the footer's top edge, not `scrollHeight`.

## Known Gaps

- Fonts load from Google Fonts; offline fallbacks are Georgia / system-ui / monospace.
- No video handling — if a review needs clips, follow the video rules in `references/media-popups-runtime.md`.
- The small `n / N` counter bottom-right duplicates the footer counter.
