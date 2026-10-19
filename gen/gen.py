#!/usr/bin/env python3
"""Generates the profile's SVG artwork (dark = Almanak Nocturne, light = Almanak Paper) and the latest-posts block.

Run daily by .github/workflows/daily.yml: the hero carries real repo numbers and today's moon.
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
FONTS, OUT = ROOT / "gen/fonts", ROOT / "assets"
TZ = ZoneInfo("America/Montreal")
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
    "Mono": "mono-400.ttf", "MonoMedium": "mono-500.ttf",
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


# ---------- pieces ----------

MOTTO = ("Create. Share. Explore. Love.", "NOT NECESSARILY IN THAT ORDER")
LIGHTS = [(45.5, -73.6), (50.7, 3.2), (41.4, 2.2), (-23.5, -46.6), (40.7, -74.0), (48.9, 2.4), (51.5, -0.1), (37.8, -122.4),
          (-22.9, -43.2), (52.5, 13.4), (19.4, -99.1), (64.1, -21.9), (38.7, -9.1), (14.7, -17.4), (33.6, -7.6)]
SKIP_LANGS = {"HTML", "CSS", "CMake", "Makefile", "Dockerfile", "Batchfile", "Procfile", "Jupyter Notebook"}


def stats(now):
    """Real numbers for the hero, from the public repos of storagebits and algotitanhq."""
    repos = gh("/users/storagebits/repos?type=owner&per_page=100") + gh("/orgs/algotitanhq/repos?type=public&per_page=100")
    repos = [r for r in repos if not r["private"] and not r["fork"] and not r["archived"] and r["name"] != "storagebits"]
    since = (now - dt.timedelta(days=30)).astimezone(dt.timezone.utc)
    commits, langs, release = 0, {}, None
    for r in repos:
        for k, v in gh(f"/repos/{r['full_name']}/languages").items():
            if k not in SKIP_LANGS: langs[k] = langs.get(k, 0) + v
        if dt.datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00")) > since:
            for page in (1, 2, 3):
                got = gh(f"/repos/{r['full_name']}/commits?since={since:%Y-%m-%dT%H:%M:%SZ}&per_page=100&page={page}")
                commits += len(got)
                if len(got) < 100: break
    for r in sorted(repos, key=lambda r: r["pushed_at"], reverse=True):
        rel = gh(f"/repos/{r['full_name']}/releases?per_page=1")
        if rel: release = f"{r['name']} {rel[0]['tag_name']}"; break
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:6]
    return dict(repos=len(repos), commits=commits, release=release, langs=[(k, v / total) for k, v in top])


def globe(svg, t, cx, cy, r, rnd, lat0=24, lon0=-38):
    """Lukarne's night globe as a dot grid, with warm city lights."""
    def proj(lat, lon):
        la, lo, l0 = math.radians(lat), math.radians(lon - lon0), math.radians(lat0)
        cosc = math.sin(l0) * math.sin(la) + math.cos(l0) * math.cos(la) * math.cos(lo)
        x = cx + r * math.cos(la) * math.sin(lo)
        y = cy - r * (math.cos(l0) * math.sin(la) - math.sin(l0) * math.cos(la) * math.cos(lo))
        return x, y, cosc
    svg.add(f'<defs><radialGradient id="gl" cx=".38" cy=".32" r=".75"><stop offset="0" stop-color="{t["rim"]}" stop-opacity=".22"/>'
            f'<stop offset="1" stop-color="{t["ground"]}" stop-opacity=".9"/></radialGradient></defs>')
    svg.add(f'<circle cx="{cx}" cy="{cy}" r="{r + 16}" fill="{t["rim"]}" fill-opacity=".05"/>')
    svg.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#gl)" stroke="{t["rim"]}" stroke-opacity=".45"/>')
    for lat in range(-75, 90, 9):
        step = max(6, int(9 / max(math.cos(math.radians(lat)), .2)))
        for lon in range(-180, 180, step):
            x, y, c = proj(lat, lon)
            if c > 0: svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{.6 + .9 * c:.2f}" fill="{t["fg"]}" fill-opacity="{.08 + .32 * c:.2f}"/>')
    svg.css.append("@keyframes pl{0%,100%{opacity:.35}50%{opacity:1}}.pl{animation:pl 4.5s ease-in-out infinite}")
    for lat, lon in LIGHTS:
        x, y, c = proj(lat, lon)
        if c <= 0.05: continue
        d = f"-{rnd.uniform(0, 4.5):.1f}s"
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{t["light"]}" fill-opacity=".16" class="pl" style="animation-delay:{d}"/>')
        svg.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.3" fill="{t["hot"]}" class="pl" style="animation-delay:{d}"/>')


def hero(theme, now, st):
    w, h = 1200, 460; t = THEMES[theme]
    svg = Svg(w, h, theme, f"storagebits: {st['repos']} public repos, {st['commits']} commits in the last 30 days. {MOTTO[0]}")
    rnd = random.Random(now.date().toordinal())
    svg.add(f'<rect width="{w}" height="{h}" rx="14" fill="{t["bg"]}"/>')
    svg.add(f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{t["fg"]}" stroke-opacity="{t["line"]}"/>')
    svg.add(f'<line x1="0" y1="44" x2="{w}" y2="44" stroke="{t["fg"]}" stroke-opacity="{t["line"]}"/>')
    for i, c in enumerate((t["accent"], t["light"], t["rim"])):
        svg.add(f'<circle cx="{26 + i * 20}" cy="22" r="5.5" fill="{c}" fill-opacity=".85"/>')
    svg.text(w / 2, 27, "storagebits@workshop: ~ — neofetch", "Mono", 13, opacity=t["faint"], anchor="middle")
    stars(svg, rnd, 40, (12, 52, 440, h - 12), t)
    globe(svg, t, 240, 252, 160, rnd)
    x, y, lh, kw = 500, 96, 29, 112
    svg.text(x, y, "storagebits", "MonoMedium", 26, t["accent"])
    svg.text(x + width("MonoMedium", 26, "storagebits"), y, "@workshop", "MonoMedium", 26)
    svg.text(x, y + 22, "─" * 38, "Mono", 15, opacity=t["faint"])
    age, k, name, full = moon(now)
    rows = [
        ("role", "software engineer, builder"),
        ("repos", f"{st['repos']} public · storagebits + algotitanhq"),
        ("commits", f"{st['commits']} in the last 30 days"),
        ("release", st["release"] or "none yet"),
        ("hardware", "ESP32 · STM32 · Android TV · iPhone"),
        ("agents", "ALGOTITAN, on Claude Code"),
        ("moon", f"{name.lower()} · {round(k * 100)}% lit"),
        ("motto", MOTTO[0]),
    ]
    yy = y + 58
    for key, val in rows:
        svg.text(x, yy, key, "MonoMedium", 17, t["accent"])
        svg.text(x + kw, yy, val, "Mono", 17, opacity=.92 if key != "motto" else 1)
        yy += lh
    # language bar, like linguist
    bx, by, bw = x, yy - 4, 640
    shades = [t["accent"], t["light"], t["rim"], t["fg"], t["hot"], t["accent"]]
    ops = [1, .9, .9, .55, .7, .45]
    cur = bx
    for (lang, frac), c, op in zip(st["langs"], shades, ops):
        seg = bw * frac
        svg.add(f'<rect x="{cur:.1f}" y="{by}" width="{max(seg - 2, 1):.1f}" height="7" rx="2" fill="{c}" fill-opacity="{op}"/>')
        cur += seg
    lx = bx
    for (lang, frac), c, op in zip(st["langs"], shades, ops):
        label = f"{lang} {frac * 100:.0f}%" if frac >= .005 else lang
        svg.add(f'<circle cx="{lx + 4}" cy="{by + 25}" r="4" fill="{c}" fill-opacity="{op}"/>')
        svg.text(lx + 13, by + 30, label, "Mono", 13, opacity=t["muted"])
        lx += 13 + width("Mono", 13, label) + 20
    svg.css.append("@keyframes bl{0%,49%{opacity:1}50%,100%{opacity:0}}.bl{animation:bl 1.1s step-end infinite}")
    svg.text(x, h - 30, "$", "MonoMedium", 17, t["accent"])
    svg.add(f'<rect x="{x + 18}" y="{h - 44}" width="10" height="18" fill="{t["fg"]}" class="bl"/>')
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


def footer(theme):
    w, h = 1200, 170; t = THEMES[theme]; svg = Svg(w, h, theme, f"{MOTTO[0]} — {MOTTO[1].lower()}.")
    stars(svg, random.Random(7), 30, (40, 10, w - 40, h - 10), t)
    svg.text(w / 2, 84, MOTTO[0], "InstrumentItalic", 48, anchor="middle")
    svg.text(w / 2, 122, "— " + MOTTO[1], "InterMedium", 13, opacity=t["faint"], tracking=.26, anchor="middle")
    return svg.render()



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



STACK = [
    ("EMBEDDED", ["C on ESP32 with LVGL", "Rust on STM32 (Hubris)", "BLE, IR, I²C sensors"]),
    ("APPS", ["Kotlin, Compose for TV", "OpenGL ES on Android", "Expo, React Native"]),
    ("INFRA", ["Incus, Docker, Pangolin", "Go, Python, Terraform", "GitHub Actions, Cloudflare"]),
]

def stack(theme):
    w, h = 1200, 150; t = THEMES[theme]; svg = Svg(w, h, theme, "Stack. " + ". ".join(f"{k}: {', '.join(v)}" for k, v in STACK))
    for i, (label, lines) in enumerate(STACK):
        x = i * 410
        svg.text(x, 22, label, "InterMedium", 12, t["accent"], tracking=.22)
        for j, s in enumerate(lines):
            assert width("Instrument", 25, s) < 380, s
            svg.text(x, 62 + j * 34, s, "Instrument", 25, opacity=1 if j == 0 else t["muted"])
    return svg.render()


def gh(path):
    import json, os
    hdr = {"Accept": "application/vnd.github+json", "User-Agent": "storagebits-profile/1.0"}
    if os.environ.get("GITHUB_TOKEN"): hdr["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=hdr), timeout=20) as r:
        return json.load(r)


def ago(when, now):
    d = (now - when).days
    return "today" if d < 1 else "yesterday" if d < 2 else f"{d} days ago" if d < 30 else f"{d // 30} months ago"


def activity(n=6, scan=14):
    """Latest commits of the most recently pushed public repos, mine and ALGOTITAN's; identical messages are grouped."""
    repos = gh("/users/storagebits/repos?type=owner&sort=pushed&per_page=30") + gh("/orgs/algotitanhq/repos?type=public&sort=pushed&per_page=30")
    repos = [r for r in repos if not r["private"] and not r["fork"] and not r["archived"] and r["name"] != "storagebits"]
    repos.sort(key=lambda r: r["pushed_at"], reverse=True)
    now, groups = dt.datetime.now(dt.timezone.utc), {}
    for r in repos[:scan]:
        c = gh(f"/repos/{r['full_name']}/commits?per_page=1")[0]
        msg = c["commit"]["message"].split("\n")[0].strip()
        msg = re.sub(r"^(Merge (pull request )?#\d+\s*(\([A-Z]+-\d+\))?\s*:?\s*|[A-Z]+-\d+\s*:\s*)", "", msg).strip()
        msg = msg[:1].upper() + msg[1:]
        if len(msg) > 72: msg = msg[:msg.rfind(" ", 0, 70)] + "…"
        when = dt.datetime.fromisoformat(c["commit"]["committer"]["date"].replace("Z", "+00:00"))
        groups.setdefault(msg, []).append((r, c, when))
    out = []
    for msg, items in list(groups.items())[:n]:
        r, c, when = items[0]
        if len(items) == 1:
            out.append(f"- [`{r['full_name']}`]({r['html_url']}) · [{html.escape(msg)}]({c['html_url']}) <sub>{ago(when, now)}</sub>")
        else:
            names = ", ".join(f"[`{x[0]['name']}`]({x[0]['html_url']})" for x in items)
            out.append(f"- {html.escape(msg)}, in {len(items)} repos: {names} <sub>{ago(when, now)}</sub>")
    return "\n".join(out)


def fill(txt, name, fn):
    try:
        block = fn()
        return re.sub(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", lambda m: f"{m[1]}\n{block}\n{m[2]}", txt, flags=re.S)
    except Exception as e:  # a feed or the API being down must not break the hero
        print(f"{name}: skipped:", e, file=sys.stderr)
        return txt


def main():
    now = dt.datetime.now(TZ)
    OUT.mkdir(exist_ok=True)
    st = stats(now)
    for theme in THEMES:
        (OUT / f"hero-{theme}.svg").write_text(hero(theme, now, st))
        if "--daily" in sys.argv: continue
        for key, args in {"repos": ("01", "REPOSITORIES", "code that runs on real hardware"),
                          "stack": ("02", "STACK", "what I reach for"),
                          "lately": ("03", "LATELY", "latest commits, refreshed every morning")}.items():
            (OUT / f"section-{key}-{theme}.svg").write_text(section(theme, *args))
        (OUT / f"stack-{theme}.svg").write_text(stack(theme))
        (OUT / f"footer-{theme}.svg").write_text(footer(theme))
    readme = ROOT / "README.md"
    txt = fill(readme.read_text(), "activity", activity)
    txt = fill(txt, "posts", lambda: posts(2))
    readme.write_text(txt)


if __name__ == "__main__":
    main()
