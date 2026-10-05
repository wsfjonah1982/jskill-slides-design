# Components and Slide Layouts

Each component is a helper function in the build script that returns HTML. Reuse the helper; don't hand-write
variants — that is how one deck ends up with three title sizes.

## Components (navy/gold template names; adapt tokens for other systems)

| Component | Class / helper | Look / behaviour |
|---|---|---|
| Bullet list | `.bullet-list > li > span` (`bullets()`) | gold mono em-dash marker, 2-col grid. **Wrap all `<li>` text in one `<span>`** or inline `.hl` spans become separate grid cells |
| Field kicker | `.label.accent.label-lg` | gold mono caps label above a field ("Solutions", "Customer Cases") |
| Header bar | `.bar` | full-width, 18 % gold fill + 3 px gold left edge, serif panel title 1.875u |
| Highlight box | `.hl-box` | 1 px gold border, 8 % gold fill; value line + optional sub-line |
| Clickable highlight box | `<button class="hl-box hl-box--link" data-popup-open="id">` | same + gold `→`; opens a popup |
| Subtitle band | `.sub-band` | 18 % gold fill, 3 px gold edge, one sentence; may be an external link (new tab) |
| Chip row | `.chip` (`chips()`) | serif gold text, gold 1 px border, faint fill — product/solution names |
| Value pills | `.pill` | numbered pill with a bold gold keyword; size with `auto auto auto` columns + `space-between` + `nowrap` to keep one line |
| Score / metric | big gold serif number + short label | units and comparison base explicit; `.na` muted variant |
| Goal row | name · % · thin bar (capped 100 %) · `done / target` | dashboard slides |
| Hub list | `.hub-item` rows: big gold `01`, title + one-line teaser, `→` | each row opens a popup |
| Image grid hub | 2×2 `.frame` tiles + numbered captions | click-to-zoom |
| Numbered target boxes | badge + label; one `--hl` solid-gold hero | under a framed diagram |
| Framed diagram | `.frame.plate` | light diagrams on a white plate, hairline border, `contain`, never cropped |
| Feathered crop | `.crop` + CSS mask | a generated picture cropped to its useful band with masked edges so it melts into the background — **force `width:100%; height:auto`** on the crop box in narrow columns |
| Timeline | explicit `grid-column`/`grid-row` on every item | logos + names + dots + dates in era bands; a highlight box spanning rows needs every other item placed explicitly or auto-placement shifts them all |
| Tabs | `.cap-tabs > button.cap[data-tab]` + `.cap-panel[data-panel]` | swaps a before/after pair in place; add `.cap-panel[hidden]{display:none}` when panels are `display:flex` |
| Points list | `.pts > .pt` (number · title · optional desc); `.pts.plain` when no item has a description | agent/product explainer slides |
| Verse / quote card (ivory) | `.verse`, `.verse.lg` | gold left bar, teal reference pill, serif text, click → popup |
| Reference chip (ivory) | `.vchip[data-pop]` | only the pill shows; hidden `.text` + `.pop-extra` open in the popup |
| Comparison table | `.cmp` | spaced rounded cells: dimension column + positive (teal/gold) + negative (crimson) columns |
| Closing banner | `.banner` | notched ribbon, one centred sentence; can be a popup trigger |
| Stage chips | pill + dot + label joined by arrows | short progressions (3 stages) |

## Slide layout archetypes

| Layout | Structure | Use for |
|---|---|---|
| Cover | kicker band → (rule) → title → lead (name, role) → meta; logo top-right | title slide |
| Part opener | big chapter number, title with gold-italic half, subtitle, 1–2 product cards | section map |
| Statement | one claim + 1–3 value pills or metrics | "what we offer" |
| Timeline | era bands + logo/date nodes, one highlighted | company intro |
| Dashboard (two periods) | two panels: header bar, big score, goal rows, deal list | results vs targets |
| Two-panel case | full-width requirement band → **row-per-field grid** (header / solutions / products / case box) | two themes, each with a case |
| Two-column bullets | two panels, header bars, kickers + bullets | reflections, challenges |
| Media grid | title + lede → `.mrow.c2/.c3` of `mcell(label, frame()/video())` | proof: ads, outputs, before/after |
| Text card + media pair | text card left, original vs altered media right | edit/variation demos |
| Agent explainer | flow bar (Goal → Assets → Skill → Review) + numbered points left, one video right | product walkthrough |
| Hub list | title → optional teaser image → 3–5 hub rows, each opening a popup | index of solutions |
| Diagram + numbered boxes | framed diagram ≈80 % width → row of target boxes, one hero | architecture + segments |
| Picture band + three columns (ivory) | 3-circle illustration band → three columns centred under the circles (left 89/675/1270 px on 1920) → banner | three parallel points |
| Numbered list (ivory) | badges joined by a vertical gold line, each with a compact card | 4–6 supporting items |
| Comparison table | full-width `.cmp`, 3 cols × 4–5 rows | two things side by side |
| Closing | thank-you + contact, large logo | end |

## Layout mechanics that held up

- Slide = grid `auto 1fr auto` (chrome · body · footer). Body is a flex column; media rows get `flex:1; min-height:0`.
- **Fit media to remaining height:** wrapper `container-type: size`, media box
  `width: min(100cqw, calc(100cqh * var(--r))); aspect-ratio: var(--r)` where `--r` is the media's own w/h.
  Box ratio = media ratio, so even `cover` inside it crops nothing.
- **Fit an image in a fixed panel with no scroll:** panel has a definite `height` and is a flex column; header
  `flex-shrink:0`; frame `flex:1; min-height:0`; img `max-width:100%; max-height:100%; width:auto; height:auto;
  object-fit:contain`. `max-height` + `overflow:auto` only adds a scrollbar.
- Rows that must align across two panels: one grid, each field a row of left/right cells; draw the centre divider
  once with `::before` on the grid, not per-cell borders.
- A title's global negative `margin-bottom` collides with an immediate flex sibling (e.g. a subtitle band in a
  `gap` column) — override locally and check the gap.
- Equal frames may hold differently sized media; don't stretch two screenshots to equal sizes.
