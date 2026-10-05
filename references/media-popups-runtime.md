# Media, Popups and Runtime Behaviour

Images, video, tabs, notes and fullscreen are implemented in `templates/byteplus/` (emitted by the helpers in
`scripts/build_deck.py`); full-slide and small popups in `templates/work-review/`; in-slide verse/table
popups in `templates/bible-study/`. Emit media through the helpers (`frame()`, `video()`, `popup()`) — hand-written
`<img>`/`<video>` tags won't get these defaults.

## Images

- **Content image** = evidence → `frame(src, alt, ratio)`. The box takes the image's own ratio (`--r = w/h`) and
  fits the remaining height via container queries, so it is never cropped or stretched. Click → lightbox
  (`#lightbox`, 92 % navy wash, image at natural size capped to the viewport; click or Esc closes).
- **Decorative/chrome image** (logo, watermark, timeline icons) = plain `<img>` outside `.frame` → not zoomable,
  by construction rather than by an extra rule.
- Light diagrams on a dark deck: `frame(..., plate=True)` puts them on a white plate with a hairline border.
- Get the ratio with Pillow: `python -c "from PIL import Image; w,h=Image.open('x.png').size; print(w/h)"`.

## Video playback model (final version after many feedback rounds)

| Rule | Behaviour | Mechanism |
|---|---|---|
| Looping | never — a clip plays once, stops, resets to its poster | no `loop` attribute; `ended` → `resetVideo()` |
| First view | auto-plays **exactly once ever**, the first time its slide is active | `box.dataset.autoplayed` |
| Several videos on a slide | start **5 s apart** | `setTimeout(i * 5000)`, cancelled if you leave first |
| Only one video on a slide | plays **with sound** on that first pass | `v.muted=false; v.play()` called **synchronously** in the navigation's own task |
| Manual control | click = play with sound; click again = pause in place (resumable) | click handler |
| One sound source | starting a video fully resets the others on that slide | `resetVideo()` on siblings |
| Play button | hidden before the first play and while playing; visible after | `.vid.not-played`, `.vid.on` |
| Leaving a slide | its videos pause, mute, rewind 950 ms after the pan; the auto-played flag stays | MutationObserver on `.slide` class |
| `video(..., fullscreen=True)` | never auto-plays; click plays from the start, full screen, sound + native controls; Esc/end resets | `.vid--fs` |
| While full screen | keys/wheel/touch can't move the deck: Space play/pause, ←/→ seek 5 s, F exit | capture-phase guard |

**Why synchronous:** browsers allow *unmuted* autoplay only when `play()` runs in the same task as a real user
gesture (the key/click that changed slides). Even `setTimeout(fn, 0)` loses it. If you must delay the single
video (one user asked for a 5 s hold), set `SINGLE_VIDEO_DELAY` and accept that strict browsers fall back to muted
+ clickable. Mouse-wheel/trackpad navigation isn't a gesture in Firefox/Safari → muted fallback; one click plays.
`play()` returns a promise — always `.catch()` it and fall back to a visible play button, never a stuck state.

Video prep: poster per clip from frame 0; `+faststart`; `preload="none"` with the *next* slide's videos warmed to
`preload="auto"`; `ffprobe -show_entries stream=codec_type,codec_name` before blaming code for silence.
Upgrading a clip to a higher-res master: same footage/duration (check hash of a frame) → swap file, regenerate
poster, no build change.

## Popups — detail one click away

The slide carries headline + structure; long passages, case studies, dense diagrams open in a popup.

- Markup (work-review): `section.slide.dark.popup[data-popup="id"]` for a full-slide popup or
  `.mini-overlay[data-popup="id"] > .mini-panel` for a small one, placed **after `#deck`** (sibling). Inside `#deck` it would be positioned relative to the transformed strip and render
  off-screen on every slide but the first.
- Trigger: any element with `data-popup-open="id"` (hub row, highlight box with `→`, chip, banner, diagram).
  Use `<button>` for keyboard focus.
- Sizes: default = fixed `90vh` card for one diagram + a few lines (image `flex:1; min-height:0` shrinks to fit,
  no scroll, no crop); `auto` = text-only, content-sized; `full` = a whole slide-like layer with its own layout.
- Close: ×, Esc, backdrop click. Esc closes the top layer first (lightbox, then popup). Changing slides closes
  popups. While open, arrow keys/wheel/swipe don't move the deck (`body.popup-open` + capture guard).
- Text inside popups needs explicit colours — they sit outside `.slide.dark`, so `.dark .bullet-list li` rules
  don't reach them (bullets rendered black-on-navy once, invisible).
- Fit budget: a popup must fit 1080 px (ivory system: ~3–4 lines of 48 px main text + 3–4 notes). More → split
  into a second trigger.
- Full-slide popups in a numbered set show their own counter (`1 / 3`), not the main total.
- PDF export: `scripts/export_pdf.py --popups` adds one page per popup after its slide.

**Fixed-canvas variant (`bible-study`):** put the overlay *inside the active slide* so it scales with the canvas;
verse cards/chips hold the popup text in hidden `.text` / `.pop-extra` children that get cloned into the panel;
tables use a hidden `.pop-data > table`.

## Tabs

`<div class="tabs"><button class="tab on" data-tab="0">…</button>…</div>` + `<div class="tab-panel"
data-panel="0">…</div>` (others `hidden`). Used to merge three near-identical pptx slides (before/after pairs)
into one clickable slide. The chosen tab persists when you leave and return. Panels with `display:flex` need the
`[hidden]{display:none!important}` rule (included).

## Speaker notes and fullscreen

`slide(..., notes="…")` → `data-notes`; press **N** to toggle the notes panel (plain text). **F** toggles
browser fullscreen. For decks driven by a pptx, copy the pptx notes verbatim (`pptx_extract.py` dumps them).

## Navigation (navy/gold templates)

←/→/Space/↑/↓, Home/End, wheel (900 ms cooldown), swipe, nav dots; 0.85 s pan with an `animating` guard —
scripted key presses faster than that are dropped by design (wait ≥ 1 s between them in tests, or click
`.nav-dot` elements, which bypass the guard).
