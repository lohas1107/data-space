"""Export the editable SVG in dataspace-services.html as the README PNG.

Requires CairoSVG==2.9.1, libcairo and the Noto Sans CJK TC font.
Run from any directory: python docs/images/render_architecture.py
"""

import argparse
from pathlib import Path
import xml.etree.ElementTree as ET

import cairosvg


def main():
    image_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=image_dir / "dataspace-architecture.png")
    parser.add_argument("--scale", type=float, default=2.0)
    args = parser.parse_args()
    if args.scale <= 0:
        parser.error("--scale must be positive")

    html = (image_dir / "dataspace-services.html").read_text(encoding="utf-8")
    start = html.index("<svg ")
    end = html.index("</svg>", start) + len("</svg>")
    svg = html[start:end]
    root = ET.fromstring(svg)
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        raise ValueError("Expected a namespaced SVG root")

    cairosvg.svg2png(bytestring=svg.encode("utf-8"), scale=args.scale, write_to=str(args.output))
    width = int(float(root.attrib["width"]) * args.scale)
    height = int(float(root.attrib["height"]) * args.scale)
    print(f"Exported {args.output} ({width} × {height})")


if __name__ == "__main__":
    main()
