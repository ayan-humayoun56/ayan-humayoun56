#!/usr/bin/env python3
"""
txt_to_svg.py

Renders a plain-text ASCII art file into a themed, terminal-style SVG
that matches the GitHub-Dark palette used across this profile.

Usage:
    python3 scripts/txt_to_svg.py <input.txt> <output.svg> [--title "ayan@github:~/portrait"] [--color green]
"""

import argparse
import html

PALETTE = {
    "bg": "#0D1117",
    "panel": "#161B22",
    "border": "#30363D",
    "text": "#F0F6FC",
    "muted": "#8B949E",
    "blue": "#58A6FF",
    "green": "#7EE787",
    "purple": "#BC8CFF",
}

CHAR_W = 8.4       # approx monospace advance width at font-size 12.5
LINE_H = 15.5
PAD_X = 24
PAD_TOP = 44        # room for title bar
PAD_BOTTOM = 20


def load_lines(path: str):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        raw = f.read().rstrip("\n").split("\n")
    lines = [line.replace("\t", "    ") for line in raw]
    while lines and not lines[-1].strip():
        lines.pop()
    return lines


def build_svg(lines, title: str, color_key: str) -> str:
    max_len = max((len(l) for l in lines), default=1)
    width = int(max(max_len * CHAR_W, len(title) * 7.2) + PAD_X * 2)
    width = max(width, 360)
    height = int(len(lines) * LINE_H + PAD_TOP + PAD_BOTTOM)
    fg = PALETTE.get(color_key, PALETTE["green"])

    text_rows = []
    for i, line in enumerate(lines):
        y = PAD_TOP + i * LINE_H
        escaped = html.escape(line) if line.strip() else "&#160;"
        text_rows.append(f'<text x="{PAD_X}" y="{y}" class="ascii">{escaped}</text>')

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{html.escape(title)}">
  <style>
    .frame  {{ fill: {PALETTE['bg']}; stroke: {PALETTE['border']}; stroke-width: 1; }}
    .bar    {{ fill: {PALETTE['panel']}; }}
    .title  {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 12px; fill: {PALETTE['muted']}; }}
    .ascii  {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 12.5px; fill: {fg}; white-space: pre; }}
  </style>

  <rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="10" class="frame" />
  <path d="M 0.5 10.5 A 10 10 0 0 1 10.5 0.5 L {width - 10.5} 0.5 A 10 10 0 0 1 {width - 0.5} 10.5 L {width - 0.5} 32 L 0.5 32 Z" class="bar" />
  <circle cx="22" cy="16" r="5" fill="#FF5F56" />
  <circle cx="40" cy="16" r="5" fill="#FFBD2E" />
  <circle cx="58" cy="16" r="5" fill="#27C93F" />
  <text x="{width / 2}" y="20" text-anchor="middle" class="title">{html.escape(title)}</text>

  {''.join(text_rows)}
</svg>'''
    return svg


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--title", default="ayan@github:~$")
    parser.add_argument("--color", default="green", choices=list(PALETTE.keys()))
    args = parser.parse_args()

    lines = load_lines(args.input)
    svg = build_svg(lines, args.title, args.color)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"Wrote {args.output} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
