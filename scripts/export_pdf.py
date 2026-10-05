"""Export an HTML deck to PDF, one 16:9 page per slide (slides-design skill).

Usage:
    python export_pdf.py deck.html [out.pdf] [--size 1920x1080] [--popups]

Screenshot-based, so it works for any engine (slide-strip templates or deck-stage fixed canvas) and keeps
the look exactly as presented. Text is not selectable; for a selectable-text PDF of a deck-stage deck use
the browser's Print → Save as PDF instead (deck-stage ships print CSS).
--popups: after each slide, also add a page per popup opened from it: every distinct [data-popup-open="id"]
trigger on the slide is clicked, captured, then closed with Esc (work-review full-slide and small popups),
so detail hidden behind clicks still reaches the PDF.
Needs: pip install playwright pillow  (uses the installed Chrome: channel="chrome").
"""
import argparse
import io
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

from screenshot_deck import COUNT, GOTO, NO_MOTION

POPUP_IDS = """([kind, i]) => {
  const slide = kind === 'strip'
    ? document.querySelectorAll('#deck > .slide')[i]
    : document.querySelectorAll('deck-stage > section')[i];
  return [...new Set([...slide.querySelectorAll('[data-popup-open]')].map(t => t.getAttribute('data-popup-open')))];
}"""



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("out", nargs="?")
    ap.add_argument("--size", default="1920x1080")
    ap.add_argument("--popups", action="store_true")
    a = ap.parse_args()

    deck = Path(a.deck).resolve()
    out = Path(a.out) if a.out else deck.with_suffix(".pdf")
    w, h = (int(v) for v in a.size.split("x"))
    pages = []
    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(deck.as_uri(), wait_until="load")
        pg.add_style_tag(content=NO_MOTION + " #nav-dots,#slide-counter{display:none!important}")
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(1000)
        info = pg.evaluate(COUNT)
        for i in range(info["n"]):
            pg.evaluate(GOTO, [info["kind"], i])
            pg.wait_for_timeout(500)
            pages.append(Image.open(io.BytesIO(pg.screenshot())).convert("RGB"))
            if a.popups:
                for pid in pg.evaluate(POPUP_IDS, [info["kind"], i]):
                    pg.locator(f'[data-popup-open="{pid}"]').first.click()
                    pg.wait_for_timeout(600)
                    pages.append(Image.open(io.BytesIO(pg.screenshot())).convert("RGB"))
                    print(f"slide {i + 1:02d} popup {pid}")
                    pg.keyboard.press("Escape")
                    pg.wait_for_timeout(400)
        b.close()
    pages[0].save(out, save_all=True, append_images=pages[1:], resolution=w / 13.333)
    print("saved", out, len(pages), "pages")


if __name__ == "__main__":
    main()
