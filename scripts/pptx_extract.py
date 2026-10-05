"""Extract a .pptx for conversion into an HTML deck (slides-design skill).

Usage:
    python pptx_extract.py deck.pptx out_dir [--size 1600x900] [--no-png]

Writes:
    out_dir/slides.md       text of every slide, shape by shape (top-to-bottom, left-to-right), tables,
                            picture/media names, and speaker notes — the wording source
    out_dir/png/slide-NN.png every slide rendered by PowerPoint itself (COM automation, Windows only) —
                            the layout source. Use --size 2880x1620 for diagrams you will embed.
Needs: pip install python-pptx pywin32. No LibreOffice required.
Large video-heavy decks are fine: python-pptx reads the XML; media bytes are not loaded.
"""
import argparse
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu


def shape_lines(shape, depth=0):
    pad = "  " * depth
    out = []
    kind = shape.shape_type
    if shape.has_text_frame and shape.text_frame.text.strip():
        for p in shape.text_frame.paragraphs:
            t = "".join(r.text for r in p.runs).strip()
            if t:
                bold = any(r.font.bold for r in p.runs)
                out.append(f"{pad}{'  ' * p.level}- {'**' + t + '**' if bold else t}")
    if getattr(shape, "has_table", False) and shape.has_table:
        for row in shape.table.rows:
            out.append(pad + "| " + " | ".join(c.text.strip().replace("\n", " ") for c in row.cells) + " |")
    if kind == 13:  # picture
        out.append(f"{pad}- [image: {shape.name} {Emu(shape.width).inches:.1f}x{Emu(shape.height).inches:.1f}in]")
    if kind == 16 or shape.element.xpath(".//p:videoFile|.//a:videoFile"):  # media
        out.append(f"{pad}- [media: {shape.name}]")
    if kind == 6:  # group
        for s in sorted(shape.shapes, key=lambda s: (s.top or 0, s.left or 0)):
            out += shape_lines(s, depth + 1)
    return out


def dump_text(pptx, out_dir):
    prs = Presentation(pptx)
    md = [f"# {Path(pptx).name}", "", f"{len(prs.slides)} slides", ""]
    for i, slide in enumerate(prs.slides, 1):
        md.append(f"## Slide {i}")
        for s in sorted(slide.shapes, key=lambda s: (s.top or 0, s.left or 0)):
            md += shape_lines(s)
        if slide.has_notes_slide:
            n = slide.notes_slide.notes_text_frame.text.strip()
            if n:
                md += ["", "> Notes: " + n.replace("\n", "\n> ")]
        md.append("")
    (out_dir / "slides.md").write_text("\n".join(md), encoding="utf-8")
    print("wrote", out_dir / "slides.md")


def export_png(pptx, out_dir, w, h):
    import win32com.client  # pywin32

    png = out_dir / "png"
    png.mkdir(exist_ok=True)
    app = win32com.client.Dispatch("PowerPoint.Application")
    pres = app.Presentations.Open(str(Path(pptx).resolve()), ReadOnly=True, WithWindow=False)
    try:
        for i in range(1, pres.Slides.Count + 1):
            pres.Slides(i).Export(str(png / f"slide-{i:02d}.png"), "PNG", w, h)
        print("exported", pres.Slides.Count, "PNGs to", png)
    finally:
        pres.Close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pptx")
    ap.add_argument("out_dir")
    ap.add_argument("--size", default="1600x900")
    ap.add_argument("--no-png", action="store_true")
    a = ap.parse_args()
    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    dump_text(a.pptx, out)
    if not a.no_png:
        w, h = (int(v) for v in a.size.split("x"))
        export_png(a.pptx, out, w, h)


if __name__ == "__main__":
    main()
