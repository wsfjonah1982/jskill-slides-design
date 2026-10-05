# QA, Export, Packaging and Gotchas

## Edit safely (existing decks)

- Read the project `README.md` and the whole build script first. Map every slide, popup, JS reordering,
  numbering (`TOTAL`), selectors, and asset folder. DOM order ≠ rendered order if JS moves things.
- Change the build script, never the generated HTML; rebuild; diff the output size/sections if unsure.
- Page-scoped selectors (`.slide--x .thing`) for per-slide fixes; don't edit shared rules like `.label` or `.h2`
  for one slide.
- Hiding/removing a slide: remove markup, dead CSS/JS that targeted it, renumber, update `TOTAL`, the README
  outline and the HTML ↔ pptx map.
- "Move by N px": move the whole related group by the same amount; re-check alignment.
- **Scripted find/replace on md/README: assert each anchor is unique** before slicing — a non-unique heading
  (`### Cards`) once deleted ~20 KB. Claude Code keeps per-edit backups of Edit/Write changes in
  `~/.claude/file-history/<session-id>/`; Bash/Python edits are not backed up.
- Close viewers on Windows before overwriting images/pptx (locked files).

## Verification loop (every change)

1. `python tools/build_deck.py`
2. `node <skill>/scripts/validate_deck.js deck.html` — JS syntax, duplicate IDs, missing assets, slide ids,
   tiny fonts, `object-fit: cover` warnings (the ratio-locked `.vid`/`.frame` boxes are fine).
3. `python <skill>/scripts/screenshot_deck.py deck.html --slides <changed>` at **1600×900 and 1280×720** (add
   1920×1080 for one-line titles/pills). **Read the PNGs** — markup review alone missed a flex-shrunk image and
   a grid auto-placement shift that screenshots caught at once.
4. Text check: compare every md/pptx line with the slide and popup text (ignore spaces/quote marks).
5. Open the HTML for the user (`start "" "deck.html"`) and give the path.

### Measuring correctly

- Overflow = content bottom vs **the footer's top edge** (`.slide-foot.getBoundingClientRect().top`), or a mini
  popup panel's own bottom — not the popup/slide box, and not an absolutely positioned close button.
- `scrollHeight > clientHeight` gives **false positives** when any descendant has a negative margin; use
  `getBoundingClientRect()` of the deepest last child.
- Wait for transitions before measuring: slide pan 0.85 s, popup open ~0.3 s (wait 400–700 ms) — or inject
  `*{transition:none!important;animation-duration:0s!important}` (the screenshot script does).
- Synthetic key presses faster than the pan are dropped by the `animating` guard; click `.nav-dot` instead.
- Headless Chrome fallback when no MCP/browser tool: `chrome.exe --headless=new --screenshot=out.png
  --window-size=1600,900 file:///…` on a temp copy with transitions disabled.

## Acceptance checklist

- Eyebrow/chrome and title on the same baseline as neighbouring slides; titles identical size; **every English
  title and heading in Title Case** (`scripts/title_case.py --dry-run` reports 0 changes), wording as in the source.
- Smallest text ≥ 18 px at 1600×900 (≥ 12 px at 1500-wide light decks); nothing essential in tiny copy.
- All media complete, proportional, uncropped; labels outside media.
- Sibling components share geometry, gaps and states; one hero at most.
- Content uses ~85–94 % of the body height; no single large empty band; no overlap with the footer.
- Two-panel rows start at the same y at both test sizes.
- Every popup/lightbox opens, fits without scroll, closes with × / Esc / backdrop; arrows blocked while open.
- Videos: auto-play once, no loop, single-video sound, stagger, reset on leave; posters present.
- No console errors, no broken images, nav dots count = main slides.
- README updated: status line, outline, decisions, gotchas, dated change log entry.

## Export

- **PDF:** `python scripts/export_pdf.py deck.html [out.pdf] --popups` (one page per slide + one per popup,
  screenshot-based, 1920×1080). Fixed-canvas decks (`bible-study`) can also use browser Print → Save as PDF for selectable text.
- **Zip package:** include the HTML + only referenced assets (extract every `src`/`poster`/`url()`), relative
  paths preserved; rebuild the zip after the final edit; `unzip -t` it and compare the packaged HTML's SHA-256
  with the working file.
- Fonts load from Google Fonts (need internet); list the local fallbacks in the README.

## Known pitfalls (each cost at least one feedback round)

| Symptom | Cause | Fix |
|---|---|---|
| Popup renders off-screen after slide 1 | popup inside the transformed `#deck` | make it a sibling of `#deck` |
| Popup bullets invisible | colour rule scoped to `.dark` ancestors | explicit colour inside popups |
| Inline `.hl` breaks a bullet into rows | `li { display:grid }` makes each child a cell | wrap `<li>` text in one `<span>` |
| Left/right panels drift apart at 1280 | two independent flex columns | one grid, row per field |
| Timeline nodes shift when a highlight is added | grid auto-placement | explicit `grid-column/row` on every item |
| Subtitle band overlaps the title underline | global negative `margin-bottom` on `.h2` + flex `gap` | local override of the margin |
| Image in narrow column shows its own baked title | `aspect-ratio` + `height:100%` + `max-width` lets the other axis drive | force `width:100%; height:auto` |
| Image won't shrink to fit popup; scrollbar | only `max-height` on the panel | definite panel height + flex column + `min-height:0` frame |
| Single video silent | `play()` inside `setTimeout` | call it synchronously in the gesture task |
| Pills wrap after 2× font | equal `1fr` columns | `auto` columns + `space-between` + `nowrap`, measure at 3 sizes |
| Points titles squeezed into middle column | 3-col grid with empty description column | `.plain` variant without the column |
| Tab panel never hides | `display:flex` beats `[hidden]` | `[hidden]{display:none!important}` |
| Title wording "fixed" by the build | script rewrote or lower-cased words | keep the source wording; only apply Title Case (`title_case.py`) |
| Headings left in sentence case from a pdf/md source | copied the source capitalisation | always Title Case titles and headings; source case does not override |
| "No sound" bug report | clip has no audio track, or wheel navigation | `ffprobe` first; explain the browser policy |
