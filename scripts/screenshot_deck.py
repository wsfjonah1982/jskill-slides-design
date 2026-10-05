"""Screenshot every slide of an HTML deck and report overflow (slides-design skill).

Usage:
    python screenshot_deck.py deck.html [--out shots/] [--sizes 1600x900,1280x720] [--slides 3,5]

Works for strip decks (#deck > .slide + .nav-dot: byteplus, work-review, bible-study) and deck-stage decks (<deck-stage>): transitions and
animations are switched off, then each slide is activated directly, so captures are never mid-pan.
For every slide it prints elements whose bottom edge passes the footer's top edge (or the slide's
bottom edge when there is no footer) — measured with getBoundingClientRect, not scrollHeight
(negative margins make scrollHeight report false overflow).
Needs: pip install playwright  (uses the installed Chrome: channel="chrome").
"""
import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright

NO_MOTION = "*{transition:none!important;animation-duration:0s!important;animation-delay:0s!important}"

COUNT = """() => {
  const stage = document.querySelector('deck-stage');
  if (stage) return {kind: 'stage', n: stage.querySelectorAll(':scope > section').length};
  return {kind: 'strip', n: document.querySelectorAll('#deck > .slide').length};
}"""

GOTO = """([kind, i]) => {
  if (kind === 'strip') { document.querySelectorAll('.nav-dot')[i].click(); return; }
  const stage = document.querySelector('deck-stage');
  stage._go(i, 'api');   // <deck-stage> web component's navigator
}"""

OVERFLOW = """([kind, i]) => {
  const slide = kind === 'strip'
    ? document.querySelectorAll('#deck > .slide')[i]
    : document.querySelectorAll('deck-stage > section')[i];
  const foot = slide.querySelector('.slide-foot');
  const sr = slide.getBoundingClientRect();
  const limit = foot ? foot.getBoundingClientRect().top : sr.bottom;
  const bad = [];
  slide.querySelectorAll('*').forEach(el => {
    if (foot && (el === foot || foot.contains(el))) return;
    const st = getComputedStyle(el);
    if (st.position === 'absolute' || st.position === 'fixed' || st.display === 'none') return;
    const r = el.getBoundingClientRect();
    if (r.width && r.height && r.bottom > limit + 1 && r.top < sr.bottom)
      bad.push((el.className || el.tagName).toString().slice(0, 40) + ' +' + Math.round(r.bottom - limit) + 'px');
  });
  return bad.slice(0, 8);
}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("--out", default=None)
    ap.add_argument("--sizes", default="1600x900,1280x720")
    ap.add_argument("--slides", default="", help="1-based list, e.g. 2,5 (default: all)")
    a = ap.parse_args()

    deck = Path(a.deck).resolve()
    out = Path(a.out) if a.out else deck.parent / "shots"
    out.mkdir(parents=True, exist_ok=True)
    sizes = [tuple(int(v) for v in s.split("x")) for s in a.sizes.split(",")]
    only = {int(x) for x in a.slides.split(",") if x.strip()}

    with sync_playwright() as pw:
        b = pw.chromium.launch(channel="chrome")
        for w, h in sizes:
            pg = b.new_page(viewport={"width": w, "height": h})
            errors = []
            pg.on("pageerror", lambda e: errors.append(str(e)))
            pg.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
            pg.goto(deck.as_uri(), wait_until="load")
            pg.add_style_tag(content=NO_MOTION)
            pg.wait_for_timeout(800)
            info = pg.evaluate(COUNT)
            for i in range(info["n"]):
                if only and i + 1 not in only:
                    continue
                pg.evaluate(GOTO, [info["kind"], i])
                pg.wait_for_timeout(500)
                path = out / f"slide{i + 1:02d}_{w}x{h}.png"
                pg.screenshot(path=str(path))
                bad = pg.evaluate(OVERFLOW, [info["kind"], i])
                print(f"{w}x{h} slide {i + 1:02d}: {'OVERFLOW ' + '; '.join(bad) if bad else 'ok'}  -> {path.name}")
            for e in errors:
                print(f"{w}x{h} console/page error: {e}")
            pg.close()
        b.close()
    print("screenshots in", out)


if __name__ == "__main__":
    main()
