#!/usr/bin/env python3
"""Resize an image to specified dimensions or by a scale factor.

Usage:
    python resize.py INPUT OUTPUT [--width W] [--height H] [--scale S] [--stretch]

Examples:
    # Scale to half size
    python resize.py player.png player_small.png --scale 0.5

    # Resize to a fixed width, height adjusts to keep aspect ratio
    python resize.py player.png player_w64.png --width 64

    # Resize to a fixed height, width adjusts to keep aspect ratio
    python resize.py player.png player_h64.png --height 64

    # Force exact dimensions, ignoring aspect ratio (may distort)
    python resize.py player.png player_64x32.png --width 64 --height 32 --stretch

Notes:
    - Provide at least one of --width, --height, or --scale.
    - Without --stretch, aspect ratio is preserved.
    - Requires Pillow (pip install Pillow).
"""

import argparse
from PIL import Image


def resize_image(input_path, output_path, width=None, height=None, scale=None, keep_aspect=True):
    img = Image.open(input_path)
    orig_w, orig_h = img.size

    if scale is not None:
        new_w, new_h = int(orig_w * scale), int(orig_h * scale)
    elif width and height and not keep_aspect:
        new_w, new_h = width, height
    elif width:
        ratio = width / orig_w
        new_w, new_h = width, int(orig_h * ratio)
    elif height:
        ratio = height / orig_h
        new_w, new_h = int(orig_w * ratio), height
    else:
        raise ValueError("Must provide --width, --height, or --scale")

    resized = img.resize((new_w, new_h), Image.LANCZOS)
    resized.save(output_path)
    print(f"Resized {orig_w}x{orig_h} → {new_w}x{new_h}, saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image.")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path")
    parser.add_argument("--width", type=int, help="Target width in pixels")
    parser.add_argument("--height", type=int, help="Target height in pixels")
    parser.add_argument("--scale", type=float, help="Scale factor (e.g. 0.5 for half size)")
    parser.add_argument("--stretch", action="store_true", help="Allow stretching (ignore aspect ratio)")
    args = parser.parse_args()

    resize_image(args.input, args.output, args.width, args.height, args.scale,
                 keep_aspect=not args.stretch)
