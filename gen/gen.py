#!/usr/bin/env python3
"""Generates the profile's SVG artwork (dark = Almanak Nocturne, light = Almanak Paper) and the latest-posts block.

Run daily by .github/workflows/daily.yml: the hero carries today's moon and Montréal's sun.
Fonts are subset per SVG and embedded, because GitHub serves SVGs as images (no external loads).
Requires fonttools and brotli.
"""
import base64, datetime as dt, html, io, math, random, re, sys, urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from zoneinfo import ZoneInfo

from fontTools import subset
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
FONTS, SRC, OUT = ROOT / "gen/fonts", ROOT / "gen/src", ROOT / "assets"
TZ, LAT, LON = ZoneInfo("America/Montreal"), 45.5017, -73.5673
FEED = "https://blok.storagebits.workers.dev/atom.xml"

THEMES = {
    "dark": dict(bg="#0E0D0B", sky="#141A20", card="#16140F", fg="#F2EDE4", accent="#E89E5C",
                 light="#F2B35B", hot="#FFE2B0", rim="#6E8BC2", ground="#0A1020", muted=0.70, faint=0.45, line=0.12),
    "light": dict(bg="#EFE8DA", sky="#E8DFCC", card="#F6F1E7", fg="#1F1B16", accent="#B4532A",
                  light="#B4532A", hot="#D9783F", rim="#B4532A", ground="#E4D9C3", muted=0.72, faint=0.50, line=0.14),
}
FACES = {  # css family -> file
    "Fraunces": "fraunces-300.ttf", "FrauncesBook": "fraunces-400.ttf", "Inter": "inter-400.ttf",
    "InterMedium": "inter-500.ttf", "Instrument": "instrument-serif.ttf", "InstrumentItalic": "instrument-serif-italic.ttf",
}
_ttf = {k: TTFont(FONTS / v) for k, v in FACES.items()}


def width(face, size, text, tracking=0.0):
    """Advance width in px (no kerning), with letter-spacing in em."""
    f = _ttf[face]; cmap, hmtx, upm = f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    w = sum(hmtx[cmap.get(ord(c), cmap[32])][0] for c in text) * size / upm
    return w + tracking * size * len(text)


class Svg:
    def __init__(self, w, h, theme, title):
        self.w, self.h, self.t, self.title = w, h, THEMES[theme], title
        self.parts, self.used, self.css = [], {}, []

    def text(self, x, y, s, face, size, color=None, opacity=1.0, tracking=0.0, anchor="start", features=None):
        self.used.setdefault(face, set()).update(s)
        st = f"font-family:{face};font-size:{size}px"
        if tracking: st += f";letter-spacing:{tracking}em"
        if features: st += f";font-feature-settings:{features}"
        op = f' fill-opacity="{opacity}"' if opacity < 1 else ""
        self.parts.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" fill="{color or self.t["fg"]}"{op} style="{st}">{html.escape(s)}</text>')

    def add(self, s): self.parts.append(s)

    def render(self):
        faces = []
        for face, chars in self.used.items():
            o = subset.Options(); o.flavor = "woff2"; o.layout_features = ["kern", "tnum", "lnum"]
            f = TTFont(FONTS / FACES[face]); s = subset.Subsetter(o); s.populate(text="".join(chars) + " "); s.subset(f)
            b = io.BytesIO(); f.flavor = "woff2"; f.save(b)
            faces.append(f"@font-face{{font-family:{face};src:url(data:font/woff2;base64,{base64.b64encode(b.getvalue()).decode()}) format('woff2')}}")
        css = "".join(faces) + "".join(self.css) + "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
        return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {self.w} {self.h}" '
                f'width="{self.w}" height="{self.h}" role="img"><title>{html.escape(self.title)}</title><style>{css}</style>'
                + "".join(self.parts) + "</svg>")


def img(path):
    return "data:image/jpeg;base64," + base64.b64encode(path.read_bytes()).decode()


# ---------- sky facts ----------

SYNODIC = 29.530588853

def moon(now):
    jd = now.timestamp() / 86400 + 2440587.5
    age = (jd - 2451550.1) % SYNODIC
    k = (1 - math.cos(2 * math.pi * age / SYNODIC)) / 2
    waxing = age < SYNODIC / 2
    if k < .03: name = "New moon"
    elif k > .97: name = "Full moon"
    elif .45 <= k <= .55: name = "First quarter" if waxing else "Last quarter"
    else: name = ("Waxing " if waxing else "Waning ") + ("crescent" if k < .5 else "gibbous")
    return age, k, name, next_full(jd).astimezone(TZ).date()


def next_full(jd):
    """Next full moon, Meeus (Astronomical Algorithms, ch. 49), main periodic terms: within minutes."""
    n = math.floor((jd - 2451550.09766) / 29.530588861) - 1
    while True:
        k = n + 0.5; t = k / 1236.85; e = 1 - 0.002516 * t
        m, mp, f, om = (math.radians(v % 360) for v in (2.5534 + 29.1053567 * k, 201.5643 + 385.81693528 * k,
                                                          160.7108 + 390.67050284 * k, 124.7746 - 1.56375588 * k))
        jde = (2451550.09766 + 29.530588861 * k + 0.00015437 * t * t
               - 0.40614 * math.sin(mp) + 0.17302 * e * math.sin(m) + 0.01614 * math.sin(2 * mp) + 0.01043 * math.sin(2 * f)
               + 0.00734 * e * math.sin(mp - m) - 0.00515 * e * math.sin(mp + m) + 0.00209 * e * e * math.sin(2 * m)
               - 0.00111 * math.sin(mp - 2 * f) - 0.00057 * math.sin(mp + 2 * f) + 0.00056 * e * math.sin(2 * mp + m)
               - 0.00042 * math.sin(3 * mp) + 0.00042 * e * math.sin(m + 2 * f) + 0.00038 * e * math.sin(m - 2 * f)
               - 0.00024 * e * math.sin(2 * mp - m) - 0.00017 * math.sin(om))
        if jde > jd: return dt.datetime.fromtimestamp((jde - 2440587.5) * 86400, dt.timezone.utc)
        n += 1


def sun(day, rising):
    """NOAA sunrise equation, local time in Montréal (None when the sun does not rise or set)."""
    n = day.timetuple().tm_yday; lng = LON / 15
    t = n + ((6 if rising else 18) - lng) / 24
    m = 0.9856 * t - 3.289
    l = (m + 1.916 * math.sin(math.radians(m)) + 0.020 * math.sin(math.radians(2 * m)) + 282.634) % 360
    ra = math.degrees(math.atan(0.91764 * math.tan(math.radians(l)))) % 360
    ra = (ra + (l // 90) * 90 - (ra // 90) * 90) / 15
    sd = 0.39782 * math.sin(math.radians(l)); cd = math.cos(math.asin(sd))
    ch = (math.cos(math.radians(90.833)) - sd * math.sin(math.radians(LAT))) / (cd * math.cos(math.radians(LAT)))
    if not -1 <= ch <= 1: return None
    h = (360 - math.degrees(math.acos(ch)) if rising else math.degrees(math.acos(ch))) / 15
    ut = (h + ra - 0.06571 * t - 6.622 - lng) % 24
    base = dt.datetime(day.year, day.month, day.day, tzinfo=dt.timezone.utc)
    return (base + dt.timedelta(hours=ut)).astimezone(TZ)


def moon_path(cx, cy, r, age, k):
    rx = r * abs(1 - 2 * k)
    if age < SYNODIC / 2:  # waxing: right side lit
        return f"M{cx},{cy-r} A{r},{r} 0 0 1 {cx},{cy+r} A{rx:.2f},{r} 0 0 {1 if k > .5 else 0} {cx},{cy-r}Z"
    return f"M{cx},{cy-r} A{r},{r} 0 0 0 {cx},{cy+r} A{rx:.2f},{r} 0 0 {0 if k > .5 else 1} {cx},{cy-r}Z"


def stars(svg, rnd, n, box, t):
    x0, y0, x1, y1 = box
    svg.css.append("@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}.tw{animation:tw 4s ease-in-out infinite}")
    for i in range(n):
        x, y, r = rnd.uniform(x0, x1), rnd.uniform(y0, y1), rnd.choice([.6, .7, .8, 1, 1.2])
        op = rnd.uniform(.15, .55)
        cls = f' class="tw" style="animation-delay:-{rnd.uniform(0, 4):.1f}s;animation-duration:{rnd.uniform(3, 7):.1f}s"' if i % 4 == 0 else ""
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{t["fg"]}" fill-opacity="{op:.2f}"{cls}/>')


def horizon(svg, rnd, w, h, top, t, lights=46):
    """Lukarne's night earth: a dark globe rising at the bottom, rimmed, dotted with warm city lights."""
    r = 2400; cx, cy = w * 0.55, top + r
    svg.add(f'<defs><linearGradient id="gr" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["ground"]}"/>'
            f'<stop offset="1" stop-color="{t["bg"]}"/></linearGradient></defs>')
    svg.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gr)"/>')
    svg.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{t["rim"]}" stroke-opacity=".35" stroke-width="1"/>')
    svg.css.append("@keyframes pl{0%,100%{opacity:.35}50%{opacity:1}}.pl{animation:pl 5s ease-in-out infinite}")
    for i in range(lights):
        a = rnd.uniform(-0.36, 0.42); d = rnd.uniform(6, 70)
        x = cx + (r - d) * math.sin(a); y = cy - (r - d) * math.cos(a)
        if y > h - 2 or x < 4 or x > w - 4: continue
        big = rnd.random() < .18
        cls = f' class="pl" style="animation-delay:-{rnd.uniform(0, 5):.1f}s"' if big or i % 5 == 0 else ""
        if big: svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{t["light"]}" fill-opacity=".18"{cls}/>')
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{2 if big else 1.3}" fill="{t["hot"] if big else t["light"]}"{cls}/>')


# ---------- pieces ----------

def hero(theme, now):
    w, h = 1200, 440; t = THEMES[theme]; svg = Svg(w, h, theme, "François Lesage, storagebits: I build at night, with AI agents, on real hardware.")
    rnd = random.Random(now.date().toordinal())
    svg.add(f'<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{t["sky"]}"/>'
            f'<stop offset="1" stop-color="{t["bg"]}"/></linearGradient></defs><rect width="{w}" height="{h}" rx="18" fill="url(#sk)"/>')
    stars(svg, rnd, 90, (12, 12, w - 12, 330), t)
    horizon(svg, rnd, w, h, 368, t)
    x = 64
    svg.text(x, 92, "STORAGEBITS  ·  MONTRÉAL", "InterMedium", 13, t["accent"], tracking=.2)
    svg.text(x - 3, 176, "François Lesage", "Fraunces", 78, tracking=-.02)
    svg.text(x, 226, "I build at night, with AI agents, on real hardware.", "InstrumentItalic", 31, opacity=t["muted"])
    svg.text(x, 270, "Founder of ALGOTITAN, a small company of agents.", "Inter", 16, opacity=t["faint"])
    svg.text(x, 294, "Twenty years of systems, storage and cloud before that.", "Inter", 16, opacity=t["faint"])
    # almanac column
    svg.add(f'<line x1="806" y1="70" x2="806" y2="320" stroke="{t["fg"]}" stroke-opacity="{t["line"]}"/>')
    cx = 842
    age, k, name, full = moon(now)
    svg.text(cx, 92, now.strftime("%A %-d %B").upper(), "InterMedium", 13, opacity=t["muted"], tracking=.2)
    mx, my, mr = cx + 34, 160, 34
    svg.add(f'<circle cx="{mx}" cy="{my}" r="{mr+10}" fill="{t["hot"]}" fill-opacity=".06"/>')
    svg.add(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="{t["fg"]}" fill-opacity=".07" stroke="{t["fg"]}" stroke-opacity=".15"/>')
    svg.add(f'<path d="{moon_path(mx, my, mr, age, k)}" fill="{t["hot"] if theme == "dark" else t["fg"]}" fill-opacity="{.92 if theme == "dark" else .8}"/>')
    svg.text(cx + 88, 154, name, "InstrumentItalic", 27)
    svg.text(cx + 88, 180, f"{round(k*100)}% lit · full moon {full.strftime('%b %-d')}", "Inter", 14, opacity=t["muted"])
    rise, sset = sun(now.date(), True), sun(now.date(), False)
    if rise and sset:
        day = sset - rise; hh, mm = divmod(round(day.total_seconds() / 60), 60)
        svg.text(cx, 240, "SUN OVER MONTRÉAL", "InterMedium", 13, opacity=t["muted"], tracking=.2)
        svg.text(cx - 2, 288, f"{rise:%-H:%M} → {sset:%-H:%M}", "Fraunces", 44, features="'tnum','lnum'")
        svg.text(cx, 316, f"{hh} h {mm:02d} of daylight", "Inter", 14, opacity=t["muted"])
    return svg.render()


def section(theme, num, label, aside):
    w, h = 1200, 64; t = THEMES[theme]; svg = Svg(w, h, theme, f"{num} {label}: {aside}")
    head = f"{num} — {label}"
    svg.text(0, 40, head, "InterMedium", 14, t["accent"], tracking=.22)
    x1 = width("InterMedium", 14, head, .22) + 22
    x2 = w - width("InstrumentItalic", 24, aside) - 22
    svg.add(f'<line x1="{x1:.0f}" y1="35" x2="{x2:.0f}" y2="35" stroke="{t["fg"]}" stroke-opacity="{t["line"]}"/>')
    svg.text(w, 42, aside, "InstrumentItalic", 24, opacity=t["muted"], anchor="end")
    return svg.render()


def card(theme, c):
    w, h, ih = 580, 404, 252; t = THEMES[theme]; svg = Svg(w, h, theme, f"{c['name']}: {c['line']}")
    pic = SRC / (c.get("img_" + theme) or c["img"])
    svg.add(f'<defs><clipPath id="c"><rect width="{w}" height="{h}" rx="16"/></clipPath>'
            f'<linearGradient id="fd" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#000" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="#000" stop-opacity=".45"/></linearGradient></defs>')
    svg.add(f'<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{t["card"]}"/>'
            f'<image href="{img(pic)}" x="0" y="0" width="{w}" height="{ih}" preserveAspectRatio="{c.get("align", "xMidYMid")} slice"/>'
            f'<rect width="{w}" height="{ih}" fill="url(#fd)"/></g>')
    svg.add(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="{t["fg"]}" stroke-opacity="{t["line"]}"/>')
    chip = c["status"]; cw = width("InterMedium", 11, chip, .16) + 26
    svg.add(f'<rect x="18" y="18" width="{cw:.0f}" height="26" rx="13" fill="#0E0D0B" fill-opacity=".72"/>')
    dot = "#F2B35B" if c.get("live") else "#8A8F99"
    svg.add(f'<circle cx="31" cy="31" r="3.2" fill="{dot}"/>')
    svg.text(40, 35, chip, "InterMedium", 11, "#F2EDE4", tracking=.16)
    svg.text(28, ih + 38, c["kind"], "InterMedium", 12, t["accent"], tracking=.2)
    svg.text(26, ih + 86, c["name"], "Fraunces", 44, tracking=-.02)
    svg.text(28, ih + 122, c["line"], "InstrumentItalic", 23, opacity=t["muted"])
    svg.text(w - 28, ih + 86, "→", "Inter", 26, t["accent"], anchor="end")
    assert width("InstrumentItalic", 23, c["line"]) < w - 56, c["line"]
    return svg.render()


STEPS = [
    ("01", "Idea", ["A north star and a few", "decisions. Mine."]),
    ("02", "ALGOTITAN", ["Agents run as a company", "in Paperclip, with budgets."]),
    ("03", "Forge", ["Claude Code builds and", "tests in throwaway VMs."]),
    ("04", "Gate", ["Nothing goes public", "without my approval."]),
    ("05", "Shipped", ["A repo, a release, and", "a post on the blog."]),
]

def workshop(theme):
    w, h = 1200, 250; t = THEMES[theme]; svg = Svg(w, h, theme, "How it is made: idea, ALGOTITAN, forge, gate, shipped.")
    xs = [0 + i * 246 for i in range(5)]; ly = 40
    svg.add(f'<path id="flow" d="M8,{ly} H{xs[-1]+8}" stroke="{t["fg"]}" stroke-opacity="{t["line"]*1.6:.2f}" stroke-dasharray="2 6" fill="none"/>')
    for d in (0, 2.6, 5.2):
        svg.add(f'<circle r="2.6" fill="{t["light"]}"><animateMotion dur="7.8s" begin="-{d}s" repeatCount="indefinite" '
                f'path="M8,{ly} H{xs[-1]+8}"/></circle>')
    for x, (n, title, lines) in zip(xs, STEPS):
        human = title in ("Idea", "Gate")
        c = t["accent"] if human else t["fg"]
        svg.add(f'<circle cx="{x+8}" cy="{ly}" r="8" fill="{t["bg"]}" stroke="{c}" stroke-width="1.5"/>')
        if human: svg.add(f'<circle cx="{x+8}" cy="{ly}" r="3.5" fill="{c}"/>')
        svg.text(x, ly + 50, n, "InterMedium", 12, t["accent"], tracking=.2)
        svg.text(x - 1, ly + 92, title, "Fraunces", 34, tracking=-.02)
        for i, s in enumerate(lines):
            assert width("Inter", 15, s) < 232, s
            svg.text(x, ly + 128 + i * 22, s, "Inter", 15, opacity=t["muted"])
    svg.text(0, h - 6, "Accent marks where a human decides.", "InstrumentItalic", 19, opacity=t["faint"])
    return svg.render()


def footer(theme):
    w, h = 1200, 150; t = THEMES[theme]; svg = Svg(w, h, theme, "Créer. Transmettre. Explorer. Aimer. — et pas forcément dans cet ordre.")
    stars(svg, random.Random(7), 26, (40, 10, w - 40, h - 10), t)
    svg.text(w / 2, 74, "Créer. Transmettre. Explorer. Aimer.", "InstrumentItalic", 38, anchor="middle")
    svg.text(w / 2, 108, "— ET PAS FORCÉMENT DANS CET ORDRE", "InterMedium", 12, opacity=t["faint"], tracking=.24, anchor="middle")
    return svg.render()


CARDS = {
    "kronograf": dict(name="Kronograf", kind="FIRMWARE  ·  ESP32  ·  C", status="SHIPPED  ·  v0.7 BETA", live=True, img="kronograf.jpg",
                      line="A watch you want to raise your wrist for."),
    "almanak": dict(name="Almanak", kind="ANDROID TV  ·  KOTLIN", status="SHIPPED  ·  OPEN SOURCE", live=True, img="almanak.jpg",
                    img_light="almanak-paper.jpg", align="xMidYMin", line="An almanac for the TV, made to be left on."),
    "hubris": dict(name="Hubris on F412", kind="EMBEDDED  ·  RUST", status="RUNS  ·  WRITE-UP", live=True, img="hubris.jpg",
                   line="Oxide's kernel, on a board it never met."),
    "lukarne": dict(name="Lukarne", kind="ANDROID TV  ·  OPENGL", status="ON THE BENCH", img="lukarne.jpg",
                    line="Spin a globe, dive into live webcams."),
}


def posts(n=3):
    ns = {"a": "http://www.w3.org/2005/Atom"}
    req = urllib.request.Request(FEED, headers={"User-Agent": "storagebits-profile/1.0 (+https://github.com/storagebits)"})
    with urllib.request.urlopen(req, timeout=20) as r: root = ET.parse(r).getroot()
    out = []
    for e in root.findall("a:entry", ns)[:n]:
        title, link = e.find("a:title", ns).text.strip(), e.find("a:link", ns).get("href")
        date = dt.date.fromisoformat(e.find("a:published", ns).text[:10])
        summ = e.find("a:summary", ns)
        s = re.sub(r"\s+", " ", re.sub("<[^>]+>", "", html.unescape(summ.text or ""))).strip() if summ is not None else ""
        if len(s) > 150: s = s[:s.rfind(" ", 0, 147)].rstrip(",;:") + "…"
        out.append(f"- **[{title}]({link})** <sub>{date:%b %-d, %Y}</sub><br/>{s}")
    return "\n".join(out)


def main():
    now = dt.datetime.now(TZ)
    OUT.mkdir(exist_ok=True)
    for theme in THEMES:
        (OUT / f"hero-{theme}.svg").write_text(hero(theme, now))
        if "--daily" in sys.argv: continue
        for key, c in CARDS.items(): (OUT / f"card-{key}-{theme}.svg").write_text(card(theme, c))
        for key, args in {"work": ("01", "FROM THE WORKSHOP", "things that run on real hardware"),
                          "notebook": ("02", "THE NOTEBOOK", "blok, in French, English and Spanish"),
                          "made": ("03", "HOW IT IS MADE", "a company of agents, one human")}.items():
            (OUT / f"section-{key}-{theme}.svg").write_text(section(theme, *args))
        (OUT / f"workshop-{theme}.svg").write_text(workshop(theme))
        (OUT / f"footer-{theme}.svg").write_text(footer(theme))
    readme = ROOT / "README.md"
    try:
        block = posts()
        txt = readme.read_text()
        txt = re.sub(r"(<!-- posts:start -->).*?(<!-- posts:end -->)", lambda m: f"{m[1]}\n{block}\n{m[2]}", txt, flags=re.S)
        readme.write_text(txt)
    except Exception as e:  # the feed being down must not break the hero
        print("posts: skipped:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
