"""Shift a generated image's background colour to the deck's exact background (slides-design skill).

Usage:
    python match_background.py in.png out.png --target 1c2644 [--source auto|r,g,b] [--mode dark|light]

Image models never hit a hex exactly (Seedream returned ~(19,22,53) for a requested #1c2644). Pixels are
shifted by (target - source), weighted by how close they are to the background's brightness, so cards,
text and highlights are left alone while the background, shadows and outlines move together.
--source auto samples the median of the four corners. Run it ONCE per fresh image — it shifts colours,
so running it again on its own output drifts further.
"""
import argparse

import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("dst")
ap.add_argument("--target", required=True, help="hex like 1c2644")
ap.add_argument("--source", default="auto")
ap.add_argument("--mode", default="dark", choices=["dark", "light"])
a = ap.parse_args()

arr = np.array(Image.open(a.src).convert("RGB")).astype(float)
target = np.array([int(a.target.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4)], float)
if a.source == "auto":
    k = max(8, min(arr.shape[:2]) // 40)
    corners = np.concatenate([c.reshape(-1, 3) for c in (arr[:k, :k], arr[:k, -k:], arr[-k:, :k], arr[-k:, -k:])])
    source = np.median(corners, axis=0)
else:
    source = np.array([float(v) for v in a.source.split(",")])

lum = arr.mean(axis=2)
base = source.mean()
if a.mode == "dark":
    w = np.clip(1 - (lum - base - 6) / 45, 0, 1)    # 1 at/below the background, 0 for bright pixels
else:
    w = np.clip(1 - (base + 6 - lum) / 45, 0, 1)    # 1 at/above the background, 0 for dark pixels
out = np.clip(arr + w[..., None] * (target - source), 0, 255).astype(np.uint8)
Image.fromarray(out).save(a.dst)
print("source", source.round(1), "-> target", target, "saved", a.dst)
