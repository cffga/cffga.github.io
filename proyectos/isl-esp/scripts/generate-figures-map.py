#!/usr/bin/env python3
"""Genera figures-map.json escaneando Figures/Chapter*/png/"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "figures-map.json"
FIGURES_DIR = ROOT / "Figures"

mapping = {}

for ch_dir in sorted(FIGURES_DIR.glob("Chapter*")):
    m = re.match(r"Chapter(\d+)$", ch_dir.name)
    if not m:
        continue
    ch_num = m.group(1)
    png_dir = ch_dir / "png"
    if not png_dir.is_dir():
        continue

    for img in sorted(png_dir.glob("*")):
        if img.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            continue
        name = img.stem  # e.g. "4_10a"
        # Split on first underscore
        parts = name.split("_", 1)
        if len(parts) < 2:
            continue
        fig_part = parts[1].rstrip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        letter_part = parts[1][len(fig_part):]
        relpath = f"Figures/Chapter{ch_num}/png/{img.name}"

        # Main label: map to first panel only (avoid overwriting with last panel)
        label = f"fig-{ch_num}-{fig_part}"
        if label not in mapping or not letter_part:
            mapping[label] = relpath

        if letter_part:
            sub_label = f"fig-{ch_num}-{fig_part}{letter_part}"
            mapping[sub_label] = relpath

OUT.write_text(json.dumps(mapping, indent=2, ensure_ascii=False) + "\n")
print(f"Generated {OUT} ({len(mapping)} entries)")
