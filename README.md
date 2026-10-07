# Slides Design skill

The skill is `SKILL.md` (name `slides-design`). This README is for maintainers only.

## Layout

```
SKILL.md        routing, workflow, non-negotiables, templates + resources tables
references/     intake & story, design systems, components, media/popups, images, QA/export
scripts/        build_deck.py · layer_slide.py · make_byteplus_light.py · make_ai_tech_light.py · validate_deck.js · screenshot_deck.py · export_pdf.py · title_case.py
                pptx_extract.py · make_logo.py · match_background.py
templates/      byteplus · byteplus-light · ai-tech-light · work-review · bible-study · studio (each: template.html + template.json + design.md)
```

Requirements: Python 3 with `playwright`, `pillow`, `numpy`, `opencv-python` (ai-tech-light images only), `python-pptx`, `pywin32` (pptx PNG export only);
Node for the validator.

## Maintenance rules

- New templates go in `templates/<slug>/` and must be added to `templates/index.json`, the templates table in
  `SKILL.md`, and the layout above.
- `byteplus-light/template.html` is generated: after changing `byteplus/template.html`, run
  `python scripts/make_byteplus_light.py` and `python scripts/make_ai_tech_light.py`. Never hand-edit either
  light template. `ai-tech-light` stays brand-free (the script asserts no BytePlus / Seed names remain) and
  drops byteplus's layer-playground slide 7.
- The layer playground's CSS / JS live in `scripts/layer_slide.py`. After changing them run
  `python scripts/layer_slide.py sync templates/byteplus/template.html`, then both make scripts; a deck that carries its
  own copy of `layer_slide.py` needs the new file copied over and a rebuild.
  The templates ship the slide as a placeholder (`layer_wrap(None)`), with no sample images: layer images belong
  to the deck that uses them.
- Templates carry `[bracketed]` placeholders, never a real person, company, customer or topic.
- `byteplus` and `work-review` are maintained here directly (they were first derived from real decks; the
  derivation scripts are not part of the skill).

## Known issues

- `byteplus` and `work-review` keep a small `n / N` counter bottom-right that duplicates the footer counter.
- `design-systems.md` §C (light corporate) is a written spec with no template.
