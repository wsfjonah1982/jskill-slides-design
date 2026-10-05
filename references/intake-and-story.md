# Intake, Sources and Story

## 1. What to collect

- Audience, setting (live talk / sent as file / both), and the action wanted at the end.
- Source content: a markdown/txt file, a `.pptx`, an older HTML deck, or loose notes.
- Brand cues: logo files (light **and** dark variants), palette, reference slides or images.
- Asset folder: images, screenshots, videos, posters, fonts, data.
- Output: standalone HTML, PDF, zip, or a `.pptx` too.

Don't block on gaps — state assumptions and use clearly marked placeholders. Never invent a logo, a client result,
a metric or evidence.

## 2. Source of truth

Pick one and write it in the project README:

| Pattern | When | How it worked |
|---|---|---|
| **One md for the whole deck** | corporate / review decks (`<deck>_slides.md`) | `## Slide N — Title` per slide; popups listed under the slide that opens them; a deck-overview table + conventions section at the top |
| **One md per slide** | teaching decks built slide by slide (`<deck>_slideNN.md`) | `Title:` on line 1, subtitle paragraph, then a bullet tree (point → quote → notes) |
| **The build script itself** | converting a pptx where the pptx stays master | slide text lives in the slide functions; the pptx is re-diffed when it changes |

Markers in an md map to components — agree them once and reuse:
"(bold, tinted background)" → header bar · "(highlighted)" → gold highlight box · "(different background)" →
subtitle band · `[popup: …]` → popup trigger.

There is no automatic md → HTML parser: an md change means a matching edit in the build script, then rebuild.

**Content hygiene** (apply consistently, record exceptions in the README): drop trailing `;`/`.` on bullets,
straight → curly quotes, never change wording, keep the user's spellings ("Painpoints"), Chinese text uses
full-width punctuation and no stray (full-width) spaces, verse/inline numbers dropped from quoted passages.
Numbers: compute percentages yourself (2 dp) and check parts sum to totals; bars cap at 100 % width while the
printed value stays real.

## 3. Converting a `.pptx`

Run `python scripts/pptx_extract.py deck.pptx out_dir/` — it writes `slides.md` (text per slide, shape by shape,
plus speaker notes) and `png/slide-NN.png` via PowerPoint COM at 1600×900.

- **Use the PNG export for layout**, the XML/python-pptx text for wording. Inferring layout from XML is unreliable.
- Without LibreOffice, use PowerPoint COM: `Slide.Export(path, "PNG", w, h)` per slide (use 2880×1620 for diagrams you
  will embed), or `Presentation.SaveAs(dir, 18)` for a quick ~1280×720 dump.
- Huge pptx (hundreds of MB of video): never read it whole. Unzip and read `ppt/slides/slideN.xml`; pull media from
  `ppt/media/`. Embedded media get renumbered on every save — match clips by **duration** (`ffprobe`), not filename.
- Dense native diagrams (boxes, arrows, icons): export as an image and frame it whole on a white plate; don't
  redraw in HTML and don't repeat the diagram's baked-in title as HTML text.
- Make a poster for every video from frame 0 (`ffmpeg -i in.mp4 -frames:v 1 poster.jpg`), remux with
  `-movflags +faststart` for quick start, and `ffprobe` that an audio stream exists before debugging "no sound".
- Record an **HTML ↔ pptx slide-number map** in the README when slides are merged or dropped.

**"pptx is updated" later:** re-extract, then classify each slide: deliberate edit (new text shapes, a blanked-out
row, a new overlaid picture) vs stale mirror (the user sometimes pastes screenshots of the current deck as
redlines). Update the md, then the script. Ask before building anything that changes the interaction model.

## 4. Story map before HTML

Complete: *This deck shows **[audience]** how **[offer]** creates **[outcome]**, supported by **[proof]**, and
leads to **[next action]**.*

Then a table:

| # | Job (establish / quantify / prove / explain / compare / demonstrate / ask) | Takeaway title | Content / proof | Asset |
|---|---|---|---|---|

Client-facing spine that worked: cover → who we are (timeline) → what we offer (value pills) →
Part 01/02/03 openers each followed by proof slides (media grids, before/after, case) → closing. Part openers with a
big chapter number give the audience a map. Every asset must support a claim; drop orphan assets.

Weak → better titles: "Creative Workflow" → "Every Test Makes the Next Creative Smarter".

## 5. Project shape

```
project/
├── README.md              ← read-first notes; replaces conversation history
├── <deck>.html            ← generated
├── <deck>_slides.md       ← source of truth (if md-driven)
├── assets/ (or img/)      ← img/, video/ — relative paths only
└── tools/
    ├── build_deck.py      ← copied from this skill's scripts/, then filled in
    └── prompts/           ← prompts that produced each generated image
```

## 6. Iterating with the user

- "md updated" / "pptx is updated" → read, diff against the deck, update, verify, **open the HTML**, give the path.
- Keep md, pptx and HTML consistent.
- Short, concrete replies: what changed, what to check, the file path.
- Pixel- and size-level feedback comes in rounds ("2x font", "a bit smaller", "move left") — apply exactly,
  re-measure at 1600×900 / 1280×900 / 1920×1080, and log each round in the README change log with the date.
