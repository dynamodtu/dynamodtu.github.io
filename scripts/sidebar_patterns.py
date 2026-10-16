"""Draw the faint background patterns for the sidebar, as SVG files in images/patterns/.

    nodes  a "node garden": round nodes, each linked to its nearest neighbours, sparser toward the top
    dots   columns of dots that start as a neat grid and drift and wave further down (like particles in flow)
    waves  vertical lines that bulge and sway, like fluid flowing past obstacles

Both are white on transparent; the sidebar shows them at low opacity over the navy and fades them out
toward the menu (see .dyn-sidebar in _sass/_dynamo.scss; pick one with sidebar_pattern in _config.yml).
The shapes are the same on every run (fixed random seed). Change the numbers below and run again:

    python scripts/sidebar_patterns.py
"""

import math
import os
import random

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "images", "patterns")
W, H = 340, 720  # drawing size; the sidebar scales it to its width and anchors it at the bottom


def dots(path):
    rnd = random.Random(7)
    col_gap, row_gap, r = 15, 9, 1.35
    cols = int(W / col_gap) + 1
    phases = [rnd.uniform(0, 2 * math.pi) for _ in range(cols)]
    out = []
    for c in range(cols):
        x0 = (W - (cols - 1) * col_gap) / 2 + c * col_gap
        y = 6.0
        while y < H:
            t = y / H                          # 0 at the top (neat grid) .. 1 at the bottom (most drift)
            amp = 14 * t ** 1.6
            x = x0 + amp * math.sin(y / 38 + phases[c]) + 6 * t * math.sin(y / 11 + 2 * phases[c])
            if rnd.random() > 0.55 * t ** 2:   # dots thin out further down
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}"/>')
            y += row_gap * (1 + 0.5 * t)       # and spread apart
    write(path, f'<g fill="#fff">{"".join(out)}</g>')


def waves(path):
    rnd = random.Random(3)
    # uneven gaps between lines, so they don't start as a regular comb at the top
    xs, x = [], rnd.uniform(-4, 6)
    while x < W + 10:
        xs.append(x)
        x += rnd.uniform(9, 24)
    bumps = [(rnd.uniform(0, W), rnd.uniform(H * 0.1, H), rnd.uniform(35, 75), rnd.uniform(10, 24)) for _ in range(6)]
    out = []
    for x0 in xs:
        amp, freq, phase = rnd.uniform(2, 6), rnd.uniform(1 / 70, 1 / 35), rnd.uniform(0, 2 * math.pi)  # each line sways its own way
        pts = []
        for y in range(0, H + 1, 8):
            dx = amp * math.sin(y * freq + phase) * (0.6 + 0.6 * y / H)
            for bx, by, radius, push in bumps:        # lines bend around a few "obstacles"
                d = math.hypot(x0 - bx, (y - by) * 0.55)
                if d < radius * 2.5:
                    dx += math.copysign(push, x0 - bx) * math.exp(-(d / radius) ** 2)
            pts.append(f"{x0 + dx:.1f} {y:.1f}")
        out.append('<path d="M' + " L".join(pts) + '"/>')
    write(path, f'<g fill="none" stroke="#fff" stroke-width="0.8">{"".join(out)}</g>')


def nodes(path):
    # in the style of a node garden (round nodes, short links to the nearest ones), drawn at the sidebar's
    # tall shape so it never has to repeat; nodes are packed closer toward the bottom
    rnd = random.Random(11)
    h = 900
    pts = []
    for _ in range(40000):
        if len(pts) >= 420:
            break
        x, y = rnd.uniform(4, W - 4), rnd.uniform(4, h - 4)
        gap = 22 - 10 * (y / h)              # 22 apart at the top .. 12 apart at the bottom
        if all((x - px) ** 2 + (y - py) ** 2 > gap * gap for px, py in pts):
            pts.append((x, y))
    links = set()
    for i, (x, y) in enumerate(pts):
        near = sorted(range(len(pts)), key=lambda j: (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2)[1:3]
        for k, j in enumerate(near):
            if rnd.random() < (0.75 if k == 0 else 0.3):
                links.add((min(i, j), max(i, j)))
    lines = "".join(f"M{pts[i][0]:.1f} {pts[i][1]:.1f}L{pts[j][0]:.1f} {pts[j][1]:.1f}" for i, j in sorted(links))
    circles = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>' for x, y in pts)
    body = (f'<path d="{lines}" fill="none" stroke="#fff" stroke-width="0.9" stroke-linecap="round"/>'
            f'<g fill="#fff">{circles}</g>')
    write(path, body, h)


def write(path, body, h=H):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}">{body}</svg>\n')
    print(path, os.path.getsize(path) // 1024, "KB")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    nodes(os.path.join(OUT, "sidebar-nodes.svg"))
    dots(os.path.join(OUT, "sidebar-dots.svg"))
    waves(os.path.join(OUT, "sidebar-waves.svg"))
