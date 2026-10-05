# Images and Assets

## Sources, in order of preference

1. **The user's own assets** (pptx media, screenshots, product photos, logos) — evidence; never alter, crop or
   recolour without approval.
2. **PowerPoint-rendered exports** of native diagrams — `scripts/pptx_extract.py --size 2880x1620`; frame whole.
3. **Generated illustrations** (any image model) — for concept slides that have no picture: infographics, vignettes,
   metaphors (two crossing paths, nested circles, three-question vignettes).

Store each image once (`assets/img/` or `img/`), descriptive stable filenames, keep masters when you make
derivatives, and don't package unused files.

## Generating illustrations

Use whatever image-generation tool is available (an image skill, API or app). Ask for 16:9 at about 2K
(e.g. 2688×1536) and, once one image is approved, pass it as the style reference for the rest so the set
matches. API keys and config stay outside the deck folder.

Rename each output to the slide's name (`slide05.png`,
`<deck>_slide06_infographic.png`). Save every prompt that produced a kept image in `tools/prompts/` with
the pass history and lessons.

**Prompt recipe that worked**

- Open with the medium and style: *"A 16:9 presentation infographic in exactly the same visual style as the
  reference image: ivory paper texture, thin gold linework, circular painted vignettes with teal rims, numbered
  copper badges, olive-branch corners…"* or *"solid muted deep navy background #1c2644 with an extremely faint
  square grid, warm cream #f0ece3 cards, antique gold #c8a870 icons…"*.
- *"Ignore and discard all text and numbers of the reference image; only reuse its style and layout language."*
- Describe the composition concretely (three evenly spaced circles; two diagonal paths crossing in an X meeting
  at a gold star; nested circles).
- Quote every in-image string exactly, and for paragraphs give **explicit per-line text** — otherwise the model
  hyphenates or repeats fragments ("hyper-localiz-/ation").
- End with *"All text must be spelled exactly as quoted, crisp and legible, with no extra text, no logos and no
  watermark."*
- Keep `--ref` on the latest good image so palette and layout stay consistent across a deck; the first image in a
  series sets the house style.
- Edit-style prompts ("change only the colours") can corrupt text; a full redraw with the text quoted line by line
  was more reliable.
- Chinese in-image text: keep it very short and exact; long scripture/notes go in HTML.

**After generating**

1. **Proofread at full resolution** — crop and zoom every text region (Read the PNG crops). Wrong characters or
   stray marks → regenerate; you can't edit baked-in text.
2. Dark deck: `python scripts/match_background.py img.png img.png --target 1c2644` once per fresh image so it
   blends seamlessly (no visible plate).
3. Lay HTML over/under it deliberately: for a 3-circle illustration on the 1920 canvas the circle centres were
   x≈374/960/1555, so text columns sat at left 89/675/1270 px, width 570.
4. Crop away the image's own title band if the slide has a real HTML title, and feather the edges with a CSS
   mask (`.crop`) so it melts into the background.
5. Record open issues you notice (odd sleeve, oversized hands, title word differs from the md) in the README.

## Logos

- Find the real variants: wordmark on light, wordmark on dark, compact mark. Logo colour decides the deck field:
  a white wordmark ⇒ all-dark slides.
- If only artwork exists (logo on a gradient), cut it out: `python scripts/make_logo.py art.webp logo_dark.png
  --box x0,y0,x1,y1 --channel G --lo 60 --hi 230 --color 255,255,255`; multi-colour marks need one pass per part.
- Render at a fixed height with `width:auto`; chrome ≈1.55u, cover ≈2.6u.

## PowerPoint (.pptx) output when it is also wanted

`pptxgenjs` (Node, `npm i pptxgenjs`), `pres.layout = "LAYOUT_WIDE"` (13.33×7.5 in). Build tables from rounded
rectangles + text boxes (header row in solid brand colours with white text, tinted body cells, numbered circle
badges in the label column) rather than native tables when the look matters; mixed runs
(`[{text, options:{bold,color,italic}}]`) carry highlights. A generated infographic can simply be placed
full-bleed on a slide. For exact HTML → pptx fidelity, export slide PNGs (`screenshot_deck.py`) and place them as
full-slide pictures, noting that text then isn't editable.
