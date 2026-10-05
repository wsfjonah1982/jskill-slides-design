"""Cut a logo out of brand artwork into a transparent PNG (slides-design skill).

Usage:
    python make_logo.py src.(webp|png|jpg) out.png [--box x0,y0,x1,y1] [--channel G] [--lo 60] [--hi 230]
                        [--color 255,255,255]

Alpha is derived from one colour channel: pixels at or below --lo become transparent, at or above --hi
fully opaque, linear between. Works for a light logo on a dark background (the BytePlus white wordmark on
navy used --channel G --lo 60 --hi 230). For a two-colour logo (e.g. blue mark + white wordmark) run it
twice with different --box/--lo/--hi/--color and paste the halves together, or extend this script.
The result is trimmed to its visible bounding box. Never redraw or fake a logo with text.
"""
import argparse

import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("out")
ap.add_argument("--box", default="")
ap.add_argument("--channel", default="G", choices=list("RGB"))
ap.add_argument("--lo", type=float, default=60)
ap.add_argument("--hi", type=float, default=230)
ap.add_argument("--color", default="", help="fill colour r,g,b; default keeps the source colours")
a = ap.parse_args()

im = Image.open(a.src).convert("RGB")
if a.box:
    im = im.crop(tuple(int(v) for v in a.box.split(",")))
arr = np.array(im).astype(float)
ch = arr[..., "RGB".index(a.channel)]
alpha = np.clip((ch - a.lo) / (a.hi - a.lo), 0, 1)

out = np.zeros(arr.shape[:2] + (4,), np.uint8)
out[..., :3] = [int(v) for v in a.color.split(",")] if a.color else arr.astype(np.uint8)
out[..., 3] = (alpha * 255).astype(np.uint8)
logo = Image.fromarray(out, "RGBA")
bbox = logo.getchannel("A").point(lambda v: 255 if v > 20 else 0).getbbox()
if bbox:
    logo = logo.crop(bbox)
logo.save(a.out)
print("saved", a.out, logo.size)
