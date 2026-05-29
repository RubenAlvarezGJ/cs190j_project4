#!/usr/bin/env python3
"""Remove the background from an image.

Usage:
    python remove_background.py <input> <output> [--model MODEL] [--alpha-matting]

Examples:
    # Basic: produces a transparent PNG
    python remove_background.py photo.jpg photo_nobg.png

    # People, with finer edges (slower, better for hair/fur)
    python remove_background.py portrait.jpg out.png --model u2net_human_seg --alpha-matting

    # Highest-quality general model
    python remove_background.py product.png cutout.png --model birefnet-general

Notes:
    - Output is forced to .png if you give a non-transparent extension.
    - Models: u2net (default), u2netp (lighter), u2net_human_seg (people),
      isnet-general-use, birefnet-general (highest quality).
    - The first run with a given model downloads its weights.
    - Requires: pip install rembg pillow
"""

import argparse
from pathlib import Path
from rembg import remove, new_session
from PIL import Image


def remove_background(input_path, output_path, model="u2net", alpha_matting=False):
    session = new_session(model)
    input_img = Image.open(input_path)

    output_img = remove(
        input_img,
        session=session,
        alpha_matting=alpha_matting,
        alpha_matting_foreground_threshold=240,
        alpha_matting_background_threshold=10,
        alpha_matting_erode_size=10,
    )

    # Ensure output has alpha channel — force PNG if user gave a non-transparent format
    out_path = Path(output_path)
    if out_path.suffix.lower() not in (".png", ".webp"):
        out_path = out_path.with_suffix(".png")
        print(f"Switched output to {out_path} (needs transparency support)")

    output_img.save(out_path)
    print(f"Saved background-removed image to {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove the background from an image.")
    parser.add_argument("input", help="Input image path")
    parser.add_argument("output", help="Output image path (will be forced to .png if not transparent)")
    parser.add_argument(
        "--model",
        default="u2net",
        choices=["u2net", "u2netp", "u2net_human_seg", "isnet-general-use", "birefnet-general"],
        help="Segmentation model (u2net=default, u2netp=lighter, u2net_human_seg=people, birefnet-general=highest quality)",
    )
    parser.add_argument(
        "--alpha-matting",
        action="store_true",
        help="Use alpha matting for finer edges (slower, better for hair/fur)",
    )
    args = parser.parse_args()

    remove_background(args.input, args.output, args.model, args.alpha_matting)
