"""Generator for a BytePlus-style HTML deck (slides-design skill).

Copy this file into <project>/tools/, edit CONFIG and SLIDES, then run:
    python tools/build_deck.py
It reads templates/byteplus/template.html (CSS, navigation engine and media runtime), drops the template's
sample slides, inserts the slides defined below, writes OUT, and copies the brand images the deck uses into
OUT's assets/img/. Every later change = edit this script + rebuild, so the HTML is always reproducible.

Slide text lives in the slide functions below; keep it in sync with the md / pptx source of truth.
Media rules (ratio-locked frames, no-loop video model, lightbox, tabs, notes) come with the template —
see templates/byteplus/design.md.
"""
import html
import re
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---- CONFIG ------------------------------------------------------------------------------------
# Folder holding template.html + assets/img/. After copying this script into a project, point it at
# the skill's templates/byteplus/ (navy & gold), templates/byteplus-light/ (light pptx-master look) or
# templates/ai-tech-light/ (the same light look, brand-free: no logo, AI icon on cover / part / end) folder.
TEMPLATE_DIR = HERE.parent / "templates" / "byteplus"
OUT = HERE.parent / "deck.html"             # the generated deck
TITLE = "Deck Title"
FOOT_LEFT = "Deck Title · Oct 2026"         # footer left text on every content slide
PRESENTER = "Presenter Name · Role"
DATE = "Oct 2026"
KICKER = "Industry Solution"                # cover / end kicker on ai-tech-light (BytePlus templates keep theirs)
I = "assets/img/"                           # image folder, relative to OUT
V = "assets/video/"                         # video folder, relative to OUT
# ------------------------------------------------------------------------------------------------

GENERIC = (TEMPLATE_DIR / "assets" / "img" / "ai-mark.png").exists()             # ai-tech-light: no brand
LIGHT = (TEMPLATE_DIR / "assets" / "img" / "byteplus_logo_light.png").exists()   # byteplus-light template
if GENERIC:
    LOGO = LOGO_COVER = PART_MARK = ""
    KICKER_TEXT = KICKER
    BRAND_FILES = ["bg-cover.jpg", "bg-content.jpg"]
else:
    LOGO_FILE = "byteplus_logo_light.png" if LIGHT else "byteplus_logo_dark.png"
    LOGO = f'<img class="bp-logo" src="{I}{LOGO_FILE}" alt="BytePlus" />'
    LOGO_COVER = f'<img class="bp-logo bp-logo-cover" src="{I}{LOGO_FILE}" alt="BytePlus" />'
    PART_MARK = f'<img class="part-mark" src="{I}bp-mark.png" alt="" />'
    KICKER_TEXT = "BytePlus Industry Solution"
    BRAND_FILES = [LOGO_FILE, "bp-mark.png"] + (["bg-light-cover.jpg", "bg-light-content.jpg"] if LIGHT else [])


def esc(t):
    """Escape plain text. Slide strings may contain deliberate inline HTML (<em>, <strong>) — only pass
    user-supplied plain text through esc()."""
    return html.escape(t, quote=True)


# ---- helpers -----------------------------------------------------------------------------------
def chrome(label):
    return f'''        <div class="slide-chrome">
          <span class="label muted" data-anim="fade-in" data-delay="0">{label}</span>
          {LOGO}
        </div>'''


def foot(n, total):
    return f'''        <div class="slide-foot">
          <span class="label muted">{FOOT_LEFT}</span>
          <span class="label muted">{n:02d} / {total:02d}</span>
        </div>'''


def feature(n, total, label, title_html, lede, inner, tag=None, notes=None):
    """Ordinary content slide: chrome, title (second half in <em> = gold italic / blue on light), optional
    product tag, one-sentence lede band (pass None when the source has none), then the content."""
    nt = f' data-notes="{esc(notes)}"' if notes else ""
    t = f'<span class="tag">{tag}</span>' if tag else ""
    ld = f'\n          <p class="lead lede" data-anim="fade-up" data-delay="2">{lede}</p>' if lede else ""
    return f'''
      <!-- ═══════ SLIDE {n} ═══════════════════════════════════════════════════ -->
      <section class="slide dark slide--feature" id="s{n:02d}"{nt}>
{chrome(label)}

        <div class="slide-body">
          <div class="feat-head" data-anim="fade-up" data-delay="1">
            <h2 class="h2">{title_html}</h2>
            {t}
          </div>{ld}
{inner}
        </div>

{foot(n, total)}
      </section>
'''


def frame(src, alt, ratio, plate=False):
    """Content image: never cropped (box ratio = image ratio), click-to-zoom. ratio = width / height.
    plate=True puts a light diagram on a plate (white on byteplus-light)."""
    cls = "frame plate" if plate else "frame"
    return f'<div class="{cls}" style="--r: {ratio}"><img src="{I}{src}" alt="{esc(alt)}" /></div>'


def diagram(src, alt, ratio):
    """A framed diagram that fills the rest of a feature slide: feature(..., inner=diagram(...))."""
    return f'          <div class="dg" data-anim="fade-up" data-delay="3">{frame(src, alt, ratio, plate=True)}</div>'


def video(name, ratio, poster=None, fullscreen=False):
    """Auto-plays once on first view, never loops; a slide's only video plays with sound.
    fullscreen=True never auto-plays — a click plays it full screen with sound.
    poster defaults to poster-<name>.jpg in the image folder."""
    poster = poster or f"poster-{Path(name).stem}.jpg"
    cls, lab = ("vid vid--fs", "Click to play full screen") if fullscreen else ("vid not-played", "Click to play")
    return f'''<div class="{cls}" style="--r: {ratio}" role="button" aria-label="Play video">
                  <video src="{V}{name}" poster="{I}{poster}" muted playsinline preload="none"></video>
                  <span class="play-btn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
                  <span class="snd">{lab}</span>
                </div>'''


def video_placeholder(ratio, label, fullscreen=False):
    """Striped stand-in until the real clip exists; swap for video(...) later."""
    cls = "vid vid--fs ph" if fullscreen else "vid not-played ph"
    return f'''<div class="{cls}" style="--r: {ratio}" role="button" aria-label="Play video">
                  <video muted playsinline preload="none"></video>
                  <span class="ph-label">{label}</span>
                  <span class="play-btn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
                  <span class="snd">Click to play</span>
                </div>'''


def mcell(label, inner):
    return f'''            <div class="mcell">
              <div class="mlabel center">{label}</div>
              <div class="mwrap">{inner}</div>
            </div>'''


def mrow(cells):
    return f'          <div class="mrow c{len(cells)}" data-anim="fade-up" data-delay="3">\n' + "\n".join(cells) + "\n          </div>"


def pills(items):
    """items: ["Reduce <strong>Time</strong> to Market", ...] — the <strong> word turns gold."""
    return ('          <div class="pills" data-anim="fade-up" data-delay="3">'
            + "".join(f'<div class="pill pill--x2"><b>{i:02d}</b><span>{t}</span></div>' for i, t in enumerate(items, 1))
            + "</div>")


def points(items, plain=False):
    """Numbered points: [(title, description or None), ...]."""
    rows = "".join(f'<div class="pt"><b>{i:02d}</b><h3>{t}</h3>{f"<p>{d}</p>" if d else ""}</div>'
                   for i, (t, d) in enumerate(items, 1))
    return f'<div class="pts{" plain" if plain else ""}">{rows}</div>'


# ---- slides ------------------------------------------------------------------------------------
# Each function takes (n, total) and returns one <section>. One job per slide; title states the takeaway.
def cover(n, total):
    return f'''
      <!-- ═══════ SLIDE {n} · COVER ═══════════════════════════════════════════ -->
      <section class="slide dark slide--cover" id="s{n:02d}">
        {LOGO_COVER}
        <div class="cover-body">
          <div class="label muted cover-kicker" data-anim="fade-in" data-delay="0">{KICKER_TEXT}</div>
          <div class="rule" data-anim="reveal-right" data-delay="1"></div>
          <h1 class="display cover-title" data-anim="fade-up" data-delay="2">{TITLE.split(" ", 1)[0]} <em>{TITLE.split(" ", 1)[-1]}</em></h1>
          <p class="cover-sub" data-anim="fade-up" data-delay="3">From <em>Before</em> to <em>After</em></p>
          <div class="cover-meta" data-anim="fade-in" data-delay="4">
            <span class="label muted">{PRESENTER}</span>
            <span class="label muted">{DATE}</span>
          </div>
        </div>
      </section>
'''


def part(n, total, num, title_html, sub, cards):
    cards_html = "".join(f'<div class="part-card"><h3 class="h3">{t}</h3><p>{d}</p></div>' for t, d in cards)
    return f'''
      <!-- ═══════ SLIDE {n} · PART {num:02d} ═══════════════════════════════════════ -->
      <section class="slide dark slide--chapter slide--part" id="s{n:02d}">
        {LOGO_COVER}
        {PART_MARK}
        <div class="chapter-num" data-anim="fade-in" data-delay="0">Part {num:02d}</div>
        <div class="chapter-rule" data-anim="reveal-right" data-delay="1"></div>
        <h1 class="h1 part-title" data-anim="fade-up" data-delay="2">{title_html}</h1>
        <p class="part-sub" data-anim="fade-up" data-delay="3">{sub}</p>
        <div class="part-cards" data-anim="fade-up" data-delay="4">{cards_html}</div>
      </section>
'''


def example_value(n, total):
    return feature(n, total, "01 · Value", "What You <em>Gain</em>",
                   "One sentence: what the audience gets.",
                   pills(["Reduce <strong>Time</strong> to Market", "<strong>Cost</strong>-saving", "<strong>Automated</strong> pipeline"]))


def example_agent(n, total):
    inner = f'''          <div class="agent" data-anim="fade-up" data-delay="3">
            <div class="agent-text">
              <div class="agent-goal">Goal &rarr; @ Assets &rarr; / Skill &rarr; Auto or Manual &rarr; Review</div>
              {points([("Point One", "One line."), ("Point Two", "One line."), ("Point Three", "One line.")])}
            </div>
            <div class="agent-media">
              <div class="mwrap">{video_placeholder(1.7778, "16:9 demo · click = full screen", fullscreen=True)}</div>
            </div>
          </div>'''
    return feature(n, total, "Part 01 · Example", "Product &ndash; <em>One-line Promise</em>",
                   "What goes in, what comes out.", inner, notes="Speaker notes (press N).")


def closing(n, total):
    return f'''
      <!-- ═══════ SLIDE {n} · THANK YOU ═══════════════════════════════════════ -->
      <section class="slide dark slide--end" id="s{n:02d}">
        {LOGO_COVER}
        <div class="kicker" data-anim="fade-in" data-delay="0">{KICKER_TEXT}</div>
        <div class="rule" data-anim="reveal-right" data-delay="1"></div>
        <h1 class="display" style="font-size: calc(7.6 * var(--u))" data-anim="fade-up" data-delay="2">Thank <em>You</em></h1>
        <p class="lead muted" data-anim="fade-up" data-delay="3">{TITLE} · {PRESENTER}</p>
      </section>
'''


EXAMPLE_CARDS = ([("Model A", "Image generation and editing model"), ("Model B", "Video generation model")] if GENERIC
                 else [("Seedream 5.0", "Image generation and editing model"), ("Seedance 2.5", "Video generation model")])

SLIDES = [
    cover,
    example_value,
    lambda n, t: part(n, t, 1, "Test Ideas <em>in Minutes</em>", "Reduce time to market",
                      EXAMPLE_CARDS),
    example_agent,
    closing,
]


# ---- assemble ----------------------------------------------------------------------------------
def build():
    s = (TEMPLATE_DIR / "template.html").read_text(encoding="utf-8")
    deck_open = '<div id="deck">'
    head = s[: s.index(deck_open) + len(deck_open)]
    tail = s[s.index("    </div>\n    <!-- /deck -->"):]
    head = re.sub(r"<title>[^<]*</title>", f"<title>{esc(TITLE)}</title>", head, count=1)

    total = len(SLIDES)
    out = head + "\n" + "".join(fn(i + 1, total) for i, fn in enumerate(SLIDES)) + tail
    OUT.write_text(out, encoding="utf-8")

    img_dir = OUT.parent / I
    img_dir.mkdir(parents=True, exist_ok=True)
    for f in BRAND_FILES:
        if not (img_dir / f).exists():
            shutil.copy2(TEMPLATE_DIR / "assets" / "img" / f, img_dir / f)
    print("ok", OUT, len(out), "bytes,", total, "slides")


if __name__ == "__main__":
    build()
