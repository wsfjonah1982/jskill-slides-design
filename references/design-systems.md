# Design Systems

Three systems have held up in real decks. Reuse one; only build a new one when the user asks. A new system
needs: semantic colour tokens, a type scale, a 2–3 mode background vocabulary, deterministic logo rules, chrome,
and a written spec (`Slides.md`) another agent can follow without reverse-engineering the HTML.

---

## A. Navy & gold, executive → ready templates: `templates/byteplus/`, `templates/work-review/`

**Good for:** project-progress and performance reviews, QBRs, customer cases, solution architecture, GTM/sales decks.
**Engine:** built into both templates — every slide is `100vw × 100vh`, `#deck` is a horizontal strip moved by `transform`, nav dots, keys, wheel, swipe, 0.85 s transition, `data-anim="fade-up|fade-in|reveal-right|scale-in"` + `data-delay="0…4"`.

**Mood:** an annual report printed on dark navy — serif headlines, one warm gold accent, hairline rules, mono
labels, generous whitespace. **Principle:** the slide carries headline, structure and numbers; detail lives behind
a click.

| Token | Hex | Role |
|---|---|---|
| `--c-bg` | `#1c2644` | slide + popup background |
| `--c-fg` | `#e2dcd0` | main text (warm off-white) |
| `--c-fg-2` | `#8a96a8` | secondary text, chrome labels |
| `--c-fg-3` | `#4e5a6e` | disabled / "NA" |
| `--c-accent` | `#c8a870` | gold: title underline, kickers, numbers, bullet dashes, chip borders, highlights |
| `--c-border` | `#2e3d5c` | hairlines, card borders |
| cream | `#f0ece3` | light slides — only if a light-background logo exists |

- Gold tint fills: `rgba(200,168,112,.06–.08)` boxes/chips; `.18` header bars & subtitle band, always with a 3 px
  gold left edge. **Solid gold + navy text = the one hero item** on a slide.
- `.hl` = gold, weight 600, 1–3 key terms per bullet max. Second half of a title may be `<em>` gold italic.
- **All slides dark** when the logo is a white wordmark. Don't add cream slides without a dark logo variant.

**Type** (Google Fonts): Source Serif 4 (headings, numbers) · DM Sans (body) · IBM Plex Mono (labels, uppercase,
tracked) · Noto Serif/Sans SC fallback for Chinese.

| Use | Size (u = 16 px at 1600×900) |
|---|---|
| Cover title `--sz-display` | 9.5u (≈152 px; 6.6u if it must stay one line) |
| Slide title `--sz-h2` | **3u (48 px) on every slide**, gold 1 px underline |
| Panel title `--sz-h3` | 1.875u (30 px) — every tier-2 heading the same |
| Lead / bullets `--sz-lead` | 1.4u (≈22 px) |
| Big score | 4.4u gold serif |
| Field kicker `.label-lg` | label + 4 px, gold mono |
| Chrome / footer `--sz-label` | **1.125u (18 px) — the floor for all text** |

**Chrome:** top bar `§ NN · Section` (mono, muted) left + logo (≈1.55u high) right; footer with hairline:
`Deck name · Mon YYYY` left, `NN / TT` right. Cover/part/end slides: larger logo top-right (≈2.6u).
Cover: kicker band → title → lead (name · role) → meta; title block vertically centred, **left-aligned** flush with
`--pad-x`.

---

## B. "Ivory & Gold Scripture" — warm teaching deck → ready template: `templates/bible-study/`

**Good for:** Bible study, sermons, classroom lessons, workshops.
**Engine:** inline in `templates/bible-study/template.html` (no dependencies) — each `<section class="slide sNN"
data-label="…">` inside `#deck` is a slide on a fixed 1920×1080 canvas scaled to the window, elements **absolutely
positioned in px**, keys + nav dots + URL hash, browser Print → one PDF page per slide.

| Token | Hex | Role |
|---|---|---|
| `--ivory` / `--ivory-deep` | `#f6eee1` / `#efe3cf` | paper |
| `--gold` / `--gold-light` / `--gold-line` | `#b98a4e` / `#d8b88a` / `#d9bd8f` | titles, ornaments, rules |
| `--teal` / `--teal-soft` | `#24565b` / `#4c7b7f` | structure, subtitles, reference pills, positive column |
| `--copper` / `--peach` | `#c0703f` / `#f3d9bf` | number badges |
| `--crimson` | `#9a3f33` | warning / negative wording only |
| `--ink` / `--ink-soft` | `#2f3b3c` / `#5b6768` | text |

Gold = title/ornament, teal = structure, crimson = warning; no other hues. Background: ivory + three soft radial
glows. Highlight: dark-gold bold text with a gold highlighter stripe on the lower 40 %.
**Type:** one serif (Noto Serif SC → Source Han Serif SC → Songti → SimSun). Title 64 px, subtitle 28 px teal,
column heading 35–36 px, body 23–32 px, popup main text 48 px, popup notes 38 px. `text-wrap: balance` on headings,
`pretty` on body; `&nbsp;` inside short references so they don't split.
**Chrome:** centred title between two fading gold rules ending in diamonds; olive-branch SVG in top corners;
content y≈150–1000; keep bottom 60 px clear for the nav bar.
For a `.pptx` version of this look, `pptxgenjs` with `LAYOUT_WIDE` and navy `1E2761` / gold `C9962C` / crimson
`990011` with tints worked (see root `build_slide02.js`).

---

## C. Light corporate (BytePlus Ads Minimal, html-slides best practices)

**Good for:** client pitches, product overviews, case-study decks on white.
Tokens: `--ink #0c1020 · --body #566071 · --muted #8c95a5 · --line #e3e7ee · --accent #2458e8 (or #0865f7) ·
--paper #fff · --wash #f4f6fa · --dark #071027`. Reference canvas 1500×844, padding 48–58 px; eyebrow 9–11 px
tracked caps above a 34–46 px title; card headline 17–24 px; body 12–16 px. Dark cover/chapter field, light body
field, optional evidence field — never a new background per slide. Use the dark-field logo on the cover and the
light-field logo elsewhere.

---

## Shared rules for any system

- **Scaling unit** for fluid decks: `--u: min(1vw, 1.7778vh)`; override the template's `--sz-*` tokens with it
  (see `scripts/build_deck.py` `ROOT_OVERRIDE`).
- **Spacing scale** 4/8/12/16/24/32/48; eyebrow→title 8–10 px, title→content 16–24 px, sibling gap 12–16 px.
- **Vertical budget:** content should use ~85–94 % of usable height; don't leave one large empty band.
- **Title Case, always:** every English title and heading (slide titles, card/step/panel/popup headings,
  sub-headings, labels) capitalises first/last and major words and the first word after a colon; minor words
  (a, an, the, and, but, or, nor, for, of, on, in, to, at, by, with, as, per, via, vs) stay lower-case mid-title;
  hyphenated parts each capitalised. Applies even when the source uses sentence case — change case only, never
  wording; words already containing capitals (NextAPI, OCI, SaaS) stay as written. `scripts/title_case.py` does it.
  Body text, notes and bullets stay sentence case. Never shrink a title below the shared size to fit — rephrase
  or allow one wrap; re-screenshot after title-casing (capitals widen lines).
- **Equal meaning, equal look:** sibling cards/chips share border, radius, fill, padding and type; a coloured
  state must mean something (active, recommended, hero).
- **Logo:** real asset only, `height` fixed + `width:auto`, correct variant for the field; never stretched,
  recoloured or faked with text.
