#!/usr/bin/env python3
"""Film-pass and resize the Codex popup images to 480x768 JPGs next to the PNGs."""
import subprocess, sys
from pathlib import Path
from PIL import Image
D = Path(__file__).resolve().parent.parent / "design" / "popup-img"
FP = Path.home() / ".claude/skills/image-generation/filmpass.py"
for png in sorted(D.glob("*.png")):
    jpg = png.with_suffix(".jpg")
    if jpg.exists() and jpg.stat().st_mtime > png.stat().st_mtime:
        continue
    subprocess.run([sys.executable, str(FP), str(png), str(jpg), "0.5"], check=True, capture_output=True)
    im = Image.open(jpg)
    w, h = im.size
    # crop to 5:8 portrait centre then resize
    target = 5 / 8
    if w / h > target:
        nw = int(h * target); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
    else:
        nh = int(w / target); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    im = im.resize((480, 768), Image.LANCZOS)
    im.save(jpg, quality=80, optimize=True)
    print(jpg.name, jpg.stat().st_size // 1024, "KB")
