#!/usr/bin/env python3
"""
render_svgs.py

Generates the hand-designed SVG assets used in the README:
  - research-cards.svg
  - tech-stack.svg
  - security-dashboard.svg
  - roadmap.svg

Run manually whenever content changes:
    python3 scripts/render_svgs.py
"""

import html
import os

BG = "#0D1117"
PANEL = "#161B22"
BORDER = "#30363D"
TEXT = "#F0F6FC"
MUTED = "#8B949E"
BLUE = "#58A6FF"
GREEN = "#7EE787"
PURPLE = "#BC8CFF"

FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "svg")


def wrap(width, height, body, extra_style=""):
    return f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <style>
    .card-bg  {{ fill: {PANEL}; stroke: {BORDER}; stroke-width: 1; }}
    .title    {{ font-family: {FONT}; font-size: 15px; font-weight: 600; fill: {TEXT}; }}
    .subtitle {{ font-family: {FONT}; font-size: 11.5px; fill: {MUTED}; }}
    .tag      {{ font-family: {MONO}; font-size: 10.5px; fill: {MUTED}; }}
    .label    {{ font-family: {MONO}; font-size: 12px; fill: {TEXT}; }}
    .small    {{ font-family: {MONO}; font-size: 11px; fill: {MUTED}; }}
    {extra_style}
  </style>
  {body}
</svg>'''


# ---------------------------------------------------------------------------
# 1. Research interest cards
# ---------------------------------------------------------------------------

def research_cards():
    cards = [
        {
            "title": "AI Security",
            "accent": BLUE,
            "desc": "Understanding how AI systems fail, and how to make them fail safely.",
            "tags": ["#llm-security", "#robustness", "#red-teaming"],
        },
        {
            "title": "Adversarial ML",
            "accent": PURPLE,
            "desc": "Studying inputs and attacks designed to break model behavior.",
            "tags": ["#evasion", "#poisoning", "#prompt-injection"],
        },
        {
            "title": "LLM Security",
            "accent": GREEN,
            "desc": "Vulnerability detection and secure design in LLM-integrated systems.",
            "tags": ["#code-analysis", "#llm-agents", "#eval"],
        },
        {
            "title": "Cloud Security",
            "accent": BLUE,
            "desc": "Securing cloud-native infrastructure across AWS and Azure environments.",
            "tags": ["#iam", "#aws", "#azure"],
        },
    ]

    card_w, card_h, gap, pad = 265, 132, 20, 20
    cols = 2
    width = pad * 2 + card_w * cols + gap * (cols - 1)
    rows = (len(cards) + cols - 1) // cols
    height = pad * 2 + card_h * rows + gap * (rows - 1)

    body = []
    for i, c in enumerate(cards):
        col, row = i % cols, i // cols
        x = pad + col * (card_w + gap)
        y = pad + row * (card_h + gap)
        tags_line = "  ".join(c["tags"])
        body.append(f'''
  <g transform="translate({x},{y})">
    <rect width="{card_w}" height="{card_h}" rx="10" class="card-bg" />
    <rect x="0" y="0" width="4" height="{card_h}" rx="2" fill="{c['accent']}" />
    <text x="22" y="34" class="title" style="fill:{TEXT}">{html.escape(c['title'])}</text>
    <text x="22" y="60" class="subtitle" style="fill:{MUTED}">{html.escape(c['desc'][:40])}</text>
    <text x="22" y="76" class="subtitle" style="fill:{MUTED}">{html.escape(c['desc'][40:])}</text>
    <text x="22" y="{card_h - 18}" class="tag" style="fill:{MUTED}">{html.escape(tags_line)}</text>
  </g>''')

    return wrap(width, height, "".join(body))


# ---------------------------------------------------------------------------
# 2. Tech stack — categorized
# ---------------------------------------------------------------------------

def tech_stack():
    categories = [
        ("Programming", GREEN, ["C++", "Python"]),
        ("Cybersecurity", BLUE, ["Wireshark", "Burp Suite", "Nmap", "Kali Linux"]),
        ("Cloud", PURPLE, ["AWS", "Azure"]),
        ("Networking", GREEN, ["TCP/IP", "OSI Model", "Packet Tracer"]),
        ("Operating Systems", BLUE, ["Ubuntu", "Kali Linux", "Windows"]),
        ("Frontend", PURPLE, ["React", "AI-assisted Prototyping"]),
        ("Databases", GREEN, ["PostgreSQL", "Supabase"]),
    ]

    col_w, gap, pad = 235, 18, 20
    cols = 3
    max_items = max(len(items) for _, _, items in categories)
    row_h = 50 + max_items * 18 + 12
    rows = (len(categories) + cols - 1) // cols
    width = pad * 2 + col_w * cols + gap * (cols - 1)
    height = pad * 2 + row_h * rows + gap * (rows - 1)

    body = []
    for i, (name, accent, items) in enumerate(categories):
        col, row = i % cols, i // cols
        x = pad + col * (col_w + gap)
        y = pad + row * (row_h + gap)
        item_lines = []
        for j, item in enumerate(items):
            item_lines.append(
                f'<circle cx="22" cy="{62 + j * 18}" r="2.5" fill="{accent}" />'
                f'<text x="32" y="{66 + j * 18}" class="label" style="fill:{TEXT}">{html.escape(item)}</text>'
            )
        body.append(f'''
  <g transform="translate({x},{y})">
    <rect width="{col_w}" height="{row_h}" rx="10" class="card-bg" />
    <text x="20" y="30" class="title" style="font-size:13.5px;fill:{TEXT}">{html.escape(name)}</text>
    <line x1="20" y1="40" x2="{col_w - 20}" y2="40" stroke="{BORDER}" stroke-width="1" />
    {''.join(item_lines)}
  </g>''')

    return wrap(width, height, "".join(body))


# ---------------------------------------------------------------------------
# 3. Security dashboard — progress bars
# ---------------------------------------------------------------------------

def security_dashboard():
    rows = [
        ("Research (AI / LLM Security)", 55, BLUE),
        ("Networking", 60, GREEN),
        ("Cloud Security", 45, PURPLE),
        ("Python", 65, GREEN),
        ("Linux", 70, BLUE),
        ("Technical Writing", 40, PURPLE),
    ]

    pad, row_h, label_w, bar_w, bar_h = 24, 46, 260, 220, 8
    width = pad * 2 + label_w + bar_w + 10
    height = pad * 2 + row_h * len(rows)

    body = [f'<rect width="{width}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="1" />']
    for i, (label, pct, color) in enumerate(rows):
        y = pad + i * row_h
        bar_x = pad + label_w
        filled = bar_w * pct / 100
        body.append(f'''
  <text x="{pad}" y="{y + 18}" class="label" style="fill:{TEXT}">{html.escape(label)}</text>
  <rect x="{bar_x}" y="{y + 8}" width="{bar_w}" height="{bar_h}" rx="4" fill="{PANEL}" stroke="{BORDER}" />
  <rect x="{bar_x}" y="{y + 8}" width="{filled:.1f}" height="{bar_h}" rx="4" fill="{color}" />''')

    return wrap(width, height, "".join(body))


# ---------------------------------------------------------------------------
# 4. Research roadmap — timeline
# ---------------------------------------------------------------------------

def roadmap():
    columns = [
        ("2026", GREEN, [
            ("AI Security Fundamentals", True),
            ("Cloud Security Labs", True),
            ("Networking", True),
            ("Independent Thesis Research", True),
            ("arXiv Preprint", False),
        ]),
        ("2027", BLUE, [
            ("IEEE Access Submission", False),
            ("Open Source Security Tool", False),
            ("Hackathon Participation", False),
            ("Graduate (BSCS)", False),
            ("PhD Applications", False),
        ]),
        ("Beyond", PURPLE, [
            ("PhD — AI Security", False),
            ("Published Research", False),
            ("Research Community Contributions", False),
        ]),
    ]

    col_w, gap, pad = 230, 24, 24
    item_h = 26
    header_h = 44
    width = pad * 2 + col_w * len(columns) + gap * (len(columns) - 1)
    max_items = max(len(c[2]) for c in columns)
    height = pad * 2 + header_h + max_items * item_h + 10

    body = []
    for i, (label, accent, items) in enumerate(columns):
        x = pad + i * (col_w + gap)
        body.append(f'''
  <rect x="{x}" y="{pad}" width="{col_w}" height="{height - pad * 2}" rx="10" class="card-bg" />
  <rect x="{x}" y="{pad}" width="{col_w}" height="{header_h}" rx="10" fill="{accent}" fill-opacity="0.12" />
  <text x="{x + 18}" y="{pad + 28}" class="title" fill="{accent}" style="fill:{accent}">{html.escape(label)}</text>''')
        for j, (item, done) in enumerate(items):
            iy = pad + header_h + 24 + j * item_h
            mark = f'<path d="M {x+18} {iy-4} l 4 4 l 7 -8" stroke="{GREEN}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" />' if done else \
                   f'<rect x="{x+15}" y="{iy-9}" width="10" height="10" rx="2" fill="none" stroke="{MUTED}" stroke-width="1.4" />'
            text_fill = TEXT if done else MUTED
            body.append(f'''
  {mark}
  <text x="{x + 34}" y="{iy}" class="small" style="fill:{text_fill}">{html.escape(item)}</text>''')

    return wrap(width, height, "".join(body))


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    assets = {
        "research-cards.svg": research_cards(),
        "tech-stack.svg": tech_stack(),
        "security-dashboard.svg": security_dashboard(),
        "roadmap.svg": roadmap(),
    }
    for name, svg in assets.items():
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
