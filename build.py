#!/usr/bin/env python3
"""Generates the animated SVG assets + README.md. Edit CONFIG, run: python build.py"""
import random, textwrap, pathlib
from xml.sax.saxutils import escape as esc

CONFIG = {
    "name": "Deepak R Gupta",
    "username": "DeepakGupta2006",
    "role": "AI/ML  ·  FULL STACK  ·  DSA",
    "pill": "BUILD · SHIP · REPEAT",
    "site_label": "deepakgupta.vercel.app",
    "site_url": "https://deepak-portfolio-deepak-gupta-s-project.vercel.app/",
    "bio": "I turn messy data and half-formed ideas into products that work, from React front-ends to ML pipelines.",
    "motto": "Build simple. Make it work. Then scale.",
    "photo": "photo.jpg",
    "gitfut_url": "https://gitfut.com/DeepakGupta2006?country=in",
    "card": {"overall": 64, "pos": "RW", "name": "D GUPTA", "pac": 67, "sho": 64, "pas": 54, "dri": 75, "def": 40, "phy": 63},
    "chips": ["Developer", "Full-Stack", "Open Source", "Always Learning"],
    "quote": ("Software is eating the world.", "MARC ANDREESSEN"),
    "stack_rows": [
        [("C++","cplusplus"),("React","react"),("Next.js","nextdotjs"),("Tailwind","tailwindcss"),("HTML","html5"),("CSS","css3"),("JavaScript","javascript"),("TypeScript","typescript"),("Python","python"),("Node.js","nodedotjs")],
        [("FastAPI","fastapi"),("VS Code","vscode"),("MongoDB","mongodb"),("PostgreSQL","postgresql"),("MySQL","mysql"),("Docker","docker"),("Git","git"),("GitHub","github"),("Flutter","flutter"),("Flask","flask")],
        [("Hugging Face","huggingface"),("Firebase","firebase"),("Vercel","vercel"),("Netlify","netlify"),("Linux","linux"),("Postman","postman"),("TensorFlow","tensorflow"),("PyTorch","pytorch"),("Pandas","pandas"),("NumPy","numpy")],
    ],
    # Optional: type your numbers here to show them before the workflow has run. Leave None to use live data.
    # Example: {"contributions": 120, "stars": 3, "prs": 5, "issues": 1, "repos": 9, "followers": 4}
    "stats_manual": None,
    "projects": [
        {"name": "Zero Spoof", "desc": "Anti-spoofing system that detects fake faces, photos and replay attacks before they get access.",
         "tags": ["Python", "OpenCV", "Deep Learning"], "lang": "Python", "color": "#34d399",
         "url": "https://github.com/DeepakGupta2006?tab=repositories"},
        {"name": "Fake News Detector", "desc": "NLP model that reads a news headline or article and tells you if it is real or fake.",
         "tags": ["Python", "NLP", "scikit-learn", "Flask"], "lang": "Python", "color": "#38bdf8",
         "url": "https://github.com/DeepakGupta2006?tab=repositories"},
        {"name": "NextCart", "desc": "Full-stack shopping website with product pages, live cart, checkout and an admin panel.",
         "tags": ["Next.js", "React", "MongoDB", "Tailwind"], "lang": "JavaScript", "color": "#818cf8",
         "url": "https://github.com/DeepakGupta2006?tab=repositories"},
        {"name": "Food Delivery", "desc": "Food ordering app with menu browsing, cart, order placing and order tracking.",
         "tags": ["React", "Node.js", "Express", "MongoDB"], "lang": "JavaScript", "color": "#fb923c",
         "url": "https://github.com/DeepakGupta2006?tab=repositories"},
    ],
    "sections": ["About Me", "Tech Stack", "Featured Projects", "GitHub Stats", "Contribution Graph"],
}

C1, C2, C3 = "#22d3ee", "#818cf8", "#e879f9"
BG = "#0a0c14"
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code',Consolas,'Courier New',monospace"
OUT = pathlib.Path(__file__).parent / "assets"
OUT.mkdir(exist_ok=True)

def save(name, w, h, body):
    (OUT / name).write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>',
        encoding="utf-8")

GRAD = f'''<linearGradient id="aur" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C3}"/></linearGradient>
<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C2}" stop-opacity="0"/><stop offset=".5" stop-color="{C1}"/><stop offset="1" stop-color="{C3}" stop-opacity="0"/></linearGradient>
<filter id="glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'''

def stars(n, w, h, seed, ymax=None):
    r = random.Random(seed); s = ""
    for _ in range(n):
        x, y, rad = r.uniform(8, w-8), r.uniform(8, (ymax or h)-8), r.choice([.7, 1, 1.3, 1.8])
        d, b = r.uniform(2, 5), r.uniform(0, 4)
        s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad}" fill="#fff" opacity=".6"><animate attributeName="opacity" values=".15;.9;.15" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/></circle>'
    return s

# ---------------- banner ----------------
def banner(c, footer=False):
    W, H = 1000, (150 if footer else 320)
    name = c["name"].upper()
    size = max(34, min(70, int(900 / (len(name) * 0.78))))
    grid = ""
    hz = H - 105 if not footer else 0
    if not footer:
        for t in range(8):
            y = hz + 105 * (t/7)**2
            grid += f'<line x1="0" x2="{W}" y1="{y:.1f}" y2="{y:.1f}"/>'
        for x in range(-700, 1701, 110):
            grid += f'<line x1="500" y1="{hz}" x2="{x}" y2="{H}"/>'
    blobs = f'''
<circle r="140" fill="#1f8a58" opacity=".60" filter="url(#blur)"><animate attributeName="cx" values="180;360;180" dur="14s" repeatCount="indefinite"/><animate attributeName="cy" values="90;200;90" dur="11s" repeatCount="indefinite"/></circle>
<circle r="150" fill="#d4a62a" opacity=".42" filter="url(#blur)"><animate attributeName="cx" values="520;640;520" dur="16s" repeatCount="indefinite"/><animate attributeName="cy" values="60;{H-40};60" dur="13s" repeatCount="indefinite"/></circle>
<circle r="130" fill="#8a7a1e" opacity=".50" filter="url(#blur)"><animate attributeName="cx" values="860;700;860" dur="15s" repeatCount="indefinite"/><animate attributeName="cy" values="220;80;220" dur="12s" repeatCount="indefinite"/></circle>'''
    corners = f'''<g fill="none" stroke="url(#aur)" stroke-width="2.5" stroke-linecap="round" filter="url(#glow)">
<path d="M26 56V28a2 2 0 0 1 2-2h28"/><path d="M974 56V28a2 2 0 0 0-2-2h-28"/>
<path d="M26 {H-56}v28a2 2 0 0 0 2 2h28"/><path d="M974 {H-56}v28a2 2 0 0 1-2 2h-28"/></g>'''
    if footer:
        body = f'''<defs>{GRAD}<filter id="blur" filterUnits="userSpaceOnUse" x="-400" y="-400" width="1800" height="1000"><feGaussianBlur stdDeviation="45"/></filter>
<clipPath id="c"><rect width="{W}" height="{H}" rx="22"/></clipPath>
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="0" x2="500" y1="0" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="#e0f2fe"/><stop offset=".33" stop-color="{C1}"/><stop offset=".66" stop-color="{C2}"/><stop offset="1" stop-color="#e0f2fe"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="500 0" dur="7s" repeatCount="indefinite"/></linearGradient></defs>
<g clip-path="url(#c)"><rect width="{W}" height="{H}" fill="#07120d"/>{blobs}{stars(30,W,H,7)}</g>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="21" fill="none" stroke="url(#aur)" stroke-opacity=".55" stroke-width="1.5"/>
{corners}
<text x="500" y="68" text-anchor="middle" font-family="{MONO}" font-size="20" font-weight="700" letter-spacing="10" fill="url(#nm)">THANKS FOR VISITING</text>
<text x="500" y="100" text-anchor="middle" font-family="{SANS}" font-size="13" letter-spacing="2" fill="#94a3b8">made with curiosity · coffee · {esc(name)}</text>'''
        save("footer.svg", W, H, body); return
    body = f'''<defs>{GRAD}<filter id="blur" filterUnits="userSpaceOnUse" x="-400" y="-400" width="1800" height="1000"><feGaussianBlur stdDeviation="50"/></filter>
<clipPath id="c"><rect width="{W}" height="{H}" rx="22"/></clipPath>
<linearGradient id="gm" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff"/></linearGradient>
<mask id="gmask"><rect y="{hz}" width="{W}" height="105" fill="url(#gm)"/></mask>
<linearGradient id="nm" gradientUnits="userSpaceOnUse" x1="0" x2="500" y1="0" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="#e0f2fe"/><stop offset=".33" stop-color="{C1}"/><stop offset=".66" stop-color="{C2}"/><stop offset="1" stop-color="#e0f2fe"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="500 0" dur="7s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="sweep" gradientUnits="userSpaceOnUse" x1="-300" x2="-100" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".10"/><stop offset="1" stop-color="#fff" stop-opacity="0"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1400 0" dur="6s" repeatCount="indefinite"/></linearGradient></defs>
<g clip-path="url(#c)"><rect width="{W}" height="{H}" fill="#07120d"/>{blobs}
<g mask="url(#gmask)" stroke="#e0b94a" stroke-opacity=".45" stroke-width="1">{grid}</g><circle cx="500" cy="150" r="125" fill="none" stroke="#e0b94a" stroke-opacity=".14" stroke-dasharray="2 6"/><circle cx="500" cy="150" r="170" fill="none" stroke="#e0b94a" stroke-opacity=".07"/>
{stars(46,W,H,11,hz)}<rect width="{W}" height="{H}" fill="url(#sweep)" transform="skewX(-18)"/></g>
<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="21" fill="none" stroke="url(#aur)" stroke-opacity=".6" stroke-width="1.5"/>
{corners}
<g transform="translate(500 66)"><rect x="-150" y="-17" width="300" height="34" rx="17" fill="#0f172a" fill-opacity=".7" stroke="url(#aur)" stroke-width="1.3"/>
<circle cx="-128" r="3.5" fill="{C1}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>
<text x="10" y="4.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" font-weight="700" letter-spacing="3" fill="#e2e8f0">{esc(c["pill"])}</text></g>
<text x="500" y="{148}" text-anchor="middle" font-family="{SANS}" font-size="{size}" font-weight="800" letter-spacing="7" fill="url(#nm)" filter="url(#glow)">{esc(name)}</text>
<text x="500" y="188" text-anchor="middle" font-family="{SANS}" font-size="15" letter-spacing="5" fill="#cbd5e1">{esc(c["role"])}</text>
<g transform="translate(500 244)"><rect x="-160" y="-19" width="320" height="38" rx="19" fill="#0f172a" fill-opacity=".8" stroke="url(#aur)" stroke-width="1.3"/>
<path d="M-34-19H141a19 19 0 0 1 0 38H-34z" fill="url(#aur)"/>
<text x="-97" y="4.5" text-anchor="middle" font-family="{MONO}" font-size="11.5" font-weight="700" letter-spacing="2" fill="#e2e8f0">PORTFOLIO</text>
<text x="53" y="4.5" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="800" fill="#0a0c14">{esc(c["site_label"])}</text></g>'''
    save("banner.svg", W, H, body)

# ---------------- headers & divider ----------------
def header(title, idx):
    W, H = 1000, 84
    tw = len(title) * 17.5
    lx1, lx2 = 500 - tw/2 - 24, 500 + tw/2 + 24
    body = f'''<defs>{GRAD}<linearGradient id="lf" x1="0" x2="1"><stop offset="0" stop-color="{C1}" stop-opacity="0"/><stop offset="1" stop-color="{C2}"/></linearGradient>
<linearGradient id="rf" x1="0" x2="1"><stop offset="0" stop-color="{C3}"/><stop offset="1" stop-color="{C2}" stop-opacity="0"/></linearGradient>
<radialGradient id="halo"><stop offset="0" stop-color="{C2}" stop-opacity=".30"/><stop offset="1" stop-color="{C2}" stop-opacity="0"/></radialGradient></defs>
<ellipse cx="500" cy="42" rx="{tw/2+130:.0f}" ry="34" fill="url(#halo)"/>
<rect x="{lx1-250:.0f}" y="41" width="250" height="2" fill="url(#lf)" rx="1"/><rect x="{lx2:.0f}" y="41" width="250" height="2" fill="url(#rf)" rx="1"/>
<circle cy="42" r="3.5" fill="#fff" filter="url(#glow)"><animate attributeName="cx" values="{lx1-250:.0f};{lx1:.0f};{lx1-250:.0f}" dur="3.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/></circle>
<circle cy="42" r="3.5" fill="#fff" filter="url(#glow)"><animate attributeName="cx" values="{lx2+250:.0f};{lx2:.0f};{lx2+250:.0f}" dur="3.2s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;1;0" dur="3.2s" repeatCount="indefinite"/></circle>
<text x="500" y="52" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="800" letter-spacing="1.5" fill="url(#aur)">{esc(title)}</text>
<rect x="470" y="66" width="60" height="3" rx="1.5" fill="url(#aur)"><animate attributeName="width" values="20;60;20" dur="3s" repeatCount="indefinite"/><animate attributeName="x" values="490;470;490" dur="3s" repeatCount="indefinite"/></rect>
<text x="{lx1-262:.0f}" y="46" text-anchor="end" font-family="{MONO}" font-size="11" fill="#64748b" letter-spacing="2">0{idx}</text>'''
    save(f"h{idx}.svg", W, H, body)

def divider():
    W, H = 1000, 28
    body = f'''<defs>{GRAD}</defs><rect x="40" y="13" width="920" height="2" fill="url(#fade)" rx="1"/>
<circle cy="14" r="3" fill="#fff" filter="url(#glow)"><animate attributeName="cx" values="60;940;60" dur="7s" repeatCount="indefinite"/></circle>
<g transform="translate(500 14)"><rect x="-6" y="-6" width="12" height="12" transform="rotate(45)" fill="{BG}" stroke="url(#aur)" stroke-width="1.8" filter="url(#glow)"><animateTransform attributeName="transform" type="rotate" from="45" to="405" dur="9s" repeatCount="indefinite"/></rect></g>'''
    save("divider.svg", W, H, body)

# ---------------- chips / stack / projects ----------------
def chips(c):
    items = c["chips"]; ws = [len(t)*8.4+34 for t in items]; total = sum(ws) + 14*(len(items)-1)
    W, H = 1000, 56; x = 500 - total/2; body = f"<defs>{GRAD}</defs>"
    for i, (t, w) in enumerate(zip(items, ws)):
        body += f'''<g transform="translate({x:.0f} 10)"><rect width="{w:.0f}" height="34" rx="17" fill="#111827" stroke="url(#aur)" stroke-width="1.3"/><circle cx="16" cy="17" r="3" fill="{[C1,C2,C3][i%3]}"><animate attributeName="opacity" values="1;.3;1" dur="2.4s" begin="{i*.4}s" repeatCount="indefinite"/></circle><text x="{w/2+6:.0f}" y="21.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="#e2e8f0">{esc(t)}</text></g>'''
        x += w + 14
    save("chips.svg", W, H, body)

def stack(c):
    import json
    icons = json.loads((pathlib.Path(__file__).parent / "icons.json").read_text(encoding="utf-8"))
    icons["vscode"] = {"path": "M17.6 2.2L21.5 4.1V19.9L17.6 21.8L7.4 12.9L4.1 15.4L2.5 14.6V9.4L4.1 8.6L7.4 11.1ZM17.6 7.9L11.4 12L17.6 16.1Z", "hex": "2f9be4"}
    over = {"numpy": "#4dabcf", "pandas": "#c084fc"}
    def col(key):
        if key in over: return over[key]
        h = icons[key]["hex"]; r, g, bl = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return "#" + h if (.299*r + .587*g + .114*bl) / 255 > .32 else "#e2e8f0"
    W, PADY, ROW_H, GAP = 1000, 30, 40, 26
    rows = c["stack_rows"]; H = PADY*2 + len(rows)*ROW_H + (len(rows)-1)*GAP
    out = ""
    for r, row in enumerate(rows):
        y = PADY + r*(ROW_H + GAP)
        def make(off):
            sx = ""; x = off
            for name, key in row:
                w = 52 + len(name)*8.3
                rule = ' fill-rule="evenodd"' if key == "vscode" else ""
                sx += (f'<g transform="translate({x:.1f} {y})"><rect width="{w:.1f}" height="{ROW_H}" rx="12" fill="url(#chipbg)" stroke="#2c3a58"/>'
                       f'<g transform="translate(16 9) scale(.9167)"><path d="{icons[key]["path"]}" fill="{col(key)}"{rule}/></g>'
                       f'<text x="46" y="25.5" font-family="{SANS}" font-size="14.5" font-weight="600" fill="#e2e8f0">{esc(name)}</text></g>')
                x += w + 14
            return sx, x - off
        one, tw = make(0); two, _ = make(tw)
        frm, to = ("0 0", f"-{tw:.1f} 0") if r % 2 == 0 else (f"-{tw:.1f} 0", "0 0")
        out += f'<g><animateTransform attributeName="transform" type="translate" from="{frm}" to="{to}" dur="{tw/46:.1f}s" repeatCount="indefinite"/>{one}{two}</g>'
    body = f"""<defs>{GRAD}<linearGradient id="chipbg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#121a2c"/><stop offset="1" stop-color="#0a101d"/></linearGradient>
<linearGradient id="ef" x1="0" x2="1"><stop offset="0" stop-color="#000"/><stop offset=".07" stop-color="#fff"/><stop offset=".93" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="em"><rect width="{W}" height="{H}" fill="url(#ef)"/></mask>
<clipPath id="pc"><rect x="6" y="8" width="{W-12}" height="{H-16}" rx="16"/></clipPath>
<radialGradient id="tg" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="{C2}" stop-opacity=".16"/><stop offset="1" stop-color="{C2}" stop-opacity="0"/></radialGradient></defs>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="#0a111c" stroke="url(#aur)" stroke-width="1.6"/>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="url(#tg)"/>
<g clip-path="url(#pc)"><g mask="url(#em)">{out}</g></g>"""
    save("stack.svg", W, H, body)

def cards(c):
    for i, p in enumerate(c["projects"], 1):
        W, H = 480, 216
        lines = textwrap.wrap(p["desc"], 52)[:2]
        desc = "".join(f'<text x="26" y="{88+i2*21}" font-family="{SANS}" font-size="13.5" fill="#94a3b8">{esc(l)}</text>' for i2, l in enumerate(lines))
        tx = 26; tg = ""
        for t in p["tags"]:
            w = len(t)*7.2 + 24
            if tx + w > W - 26: break
            tg += f'<g transform="translate({tx:.0f} 130)"><rect width="{w:.0f}" height="24" rx="12" fill="{p['color']}" fill-opacity=".12" stroke="{p['color']}" stroke-opacity=".55"/><text x="{w/2:.0f}" y="16" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#e2e8f0">{esc(t)}</text></g>'
            tx += w + 8
        body = f'''<defs>{GRAD}<linearGradient id="g{i}" gradientUnits="userSpaceOnUse" x1="-480" x2="0" y1="0" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C3}"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="480 0" dur="5s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="bg{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#131a2e"/><stop offset="1" stop-color="#0c1020"/></linearGradient></defs>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="url(#bg{i})" stroke="url(#g{i})" stroke-width="1.6"/>
<circle cx="{W-34}" cy="34" r="54" fill="{p['color']}" opacity=".09"/>
<clipPath id="lc{i}"><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16"/></clipPath>
<linearGradient id="ls{i}" gradientUnits="userSpaceOnUse" x1="-100" x2="-10" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".42" stop-color="{C1}" stop-opacity=".30"/><stop offset=".5" stop-color="#fff" stop-opacity=".95"/><stop offset=".58" stop-color="{C3}" stop-opacity=".30"/><stop offset="1" stop-color="#fff" stop-opacity="0"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="680 0" dur="4.2s" repeatCount="indefinite"/></linearGradient>
<g clip-path="url(#lc{i})"><rect width="{W}" height="{H}" fill="url(#ls{i})" opacity=".6" transform="skewX(-20)"/></g>
<text x="{W-26}" y="40" text-anchor="end" font-family="{MONO}" font-size="26" font-weight="800" fill="{p['color']}" opacity=".55">0{i}</text>
<text x="26" y="30" font-family="{MONO}" font-size="10.5" font-weight="700" letter-spacing="3" fill="#64748b">FEATURED PROJECT</text>
<text x="26" y="58" font-family="{SANS}" font-size="21" font-weight="800" fill="url(#aur)">{esc(p["name"])}</text>
{desc}{tg}
<rect x="26" y="170" width="{W-52}" height="1" fill="#1e293b"/>
<circle cx="32" cy="193" r="5" fill="{p['color']}"/><text x="44" y="197" font-family="{SANS}" font-size="12.5" fill="#cbd5e1">{esc(p["lang"])}</text>
<g transform="translate({W-26-150} 180)"><rect width="150" height="26" rx="13" fill="url(#aur)"/><text x="75" y="17.5" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="800" letter-spacing="1.5" fill="#0a0c14">VIEW PROJECT ↗</text></g>'''
        save(f"project{i}.svg", W, H, body)

def about(c):
    import base64
    W, H = 1000, 380
    photo = pathlib.Path(__file__).parent / c.get("photo", "photo.jpg")
    px, py, pw, ph = 676, 24, 268, 335
    lines = textwrap.wrap(c["bio"], 56)
    chips_h = 34 + 22 * ((sum(len(t)*8.4+34+12 for t in c["chips"]) > 560))
    total = len(lines)*28 + 28 + 34 + 44
    y0 = py + (ph - total)/2 + 18
    t = ""
    for i, l in enumerate(lines):
        t += f'<text x="48" y="{y0+i*28:.0f}" font-family="{SANS}" font-size="17.5" fill="#cbd5e1">{esc(l)}</text>'
    cy = y0 + len(lines)*28 + 6
    x = 48; row = 0
    for i, tx in enumerate(c["chips"]):
        w = len(tx)*8.4 + 34
        if x + w > 620: x = 48; row += 1
        t += f'''<g transform="translate({x:.0f} {cy+row*44:.0f})"><rect width="{w:.0f}" height="34" rx="17" fill="#111827" fill-opacity=".85" stroke="url(#aur)" stroke-width="1.3"/><circle cx="16" cy="17" r="3" fill="{[C1,C2,C3][i%3]}"><animate attributeName="opacity" values="1;.3;1" dur="2.4s" begin="{i*.4}s" repeatCount="indefinite"/></circle><text x="{w/2+6:.0f}" y="21.5" text-anchor="middle" font-family="{MONO}" font-size="12.5" fill="#e2e8f0">{esc(tx)}</text></g>'''
        x += w + 12
    my = cy + (row+1)*44 + 24
    t += f'<text x="48" y="{my:.0f}" font-family="Georgia,\'Times New Roman\',serif" font-style="italic" font-size="19" fill="#e2e8f0">{esc(c["motto"])}</text>'
    t += f'<rect x="48" y="{my+14:.0f}" width="70" height="3" rx="1.5" fill="url(#aur)"/>'
    img = ""
    if photo.exists():
        b64 = base64.b64encode(photo.read_bytes()).decode()
        img = f'<image href="data:image/jpeg;base64,{b64}" x="{px}" y="{py}" width="{pw}" height="{ph}" preserveAspectRatio="xMidYMin slice" clip-path="url(#pc)"/>'
    cx, cyb = px, py
    br = f'''<g fill="none" stroke="url(#aur)" stroke-width="3" stroke-linecap="round" filter="url(#glow)">
<path d="M{cx-12} {cyb+30}V{cyb-6}H{cx+24}"/><path d="M{cx+pw+12} {cyb+30}V{cyb-6}H{cx+pw-24}"/>
<path d="M{cx-12} {cyb+ph-30}V{cyb+ph+6}H{cx+24}"/><path d="M{cx+pw+12} {cyb+ph-30}V{cyb+ph+6}H{cx+pw-24}"/></g>'''
    body = f'''<defs>{GRAD}<clipPath id="pc"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16"/></clipPath>
<radialGradient id="aura" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{C2}" stop-opacity=".40"/><stop offset=".6" stop-color="#d4a62a" stop-opacity=".12"/><stop offset="1" stop-color="{C2}" stop-opacity="0"/></radialGradient>
<linearGradient id="scan" gradientUnits="userSpaceOnUse" x1="0" x2="0" y1="{py}" y2="{py+60}"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="{C1}" stop-opacity=".28"/><stop offset="1" stop-color="#fff" stop-opacity="0"/><animateTransform attributeName="gradientTransform" type="translate" from="0 -60" to="0 {ph}" dur="4.5s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="fadeb" x1="0" y1="0" x2="0" y2="1"><stop offset=".65" stop-color="#05080f" stop-opacity="0"/><stop offset="1" stop-color="#05080f" stop-opacity=".85"/></linearGradient>
<linearGradient id="pb" gradientUnits="userSpaceOnUse" x1="-268" x2="0" y1="0" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C3}"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="268 0" dur="5s" repeatCount="indefinite"/></linearGradient></defs>
<ellipse cx="{px+pw/2}" cy="{py+ph/2}" rx="230" ry="250" fill="url(#aura)"/>
{t}
<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="16" fill="#0b1020"/>
{img}
<g clip-path="url(#pc)"><rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="url(#fadeb)"/><rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="url(#scan)"/></g>
<rect x="{px+1}" y="{py+1}" width="{pw-2}" height="{ph-2}" rx="15" fill="none" stroke="url(#pb)" stroke-width="2"/>
{br}
<g transform="translate({px+pw/2} {py+ph-24})"><rect x="-96" y="-14" width="192" height="28" rx="14" fill="#0a0c14" fill-opacity=".78" stroke="url(#aur)" stroke-width="1"/><circle cx="-78" r="3.2" fill="{C1}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle><text x="6" y="4" text-anchor="middle" font-family="{MONO}" font-size="11" font-weight="700" letter-spacing="2" fill="#e2e8f0">{esc(c["name"].upper())}</text></g>'''
    save("about.svg", W, H, body)

# ---------------- scouting card + stats panels ----------------
def load_stats():
    import json
    f = pathlib.Path(__file__).parent / "data" / "stats.json"
    try: return json.loads(f.read_text(encoding="utf-8"))
    except Exception: return None

def fmt(v): return f"{v:,}" if isinstance(v, int) else "–"

def card(c):
    import base64
    k = c["card"]; W, H = 290, 400
    photo = pathlib.Path(__file__).parent / c.get("photo", "photo.jpg")
    img = ""
    if photo.exists():
        b64 = base64.b64encode(photo.read_bytes()).decode()
        img = f'<image href="data:image/jpeg;base64,{b64}" x="112" y="40" width="150" height="195" preserveAspectRatio="xMidYMin slice" clip-path="url(#ph)" mask="url(#pf)"/>'
    shape = "M145 8C175 22 215 28 262 28V300C262 340 220 372 145 394C70 372 28 340 28 300V28C75 28 115 22 145 8Z"
    def stat(v, lab, x, y):
        return (f'<text x="{x}" y="{y}" text-anchor="end" font-family="{SANS}" font-size="23" font-weight="800" fill="#f8fafc">{v}</text>'
                f'<text x="{x+6}" y="{y}" font-family="{SANS}" font-size="16" font-weight="600" fill="#a5b4fc">{lab}</text>')
    body = f'''<defs>{GRAD}
<linearGradient id="br" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2b3a8a"/><stop offset=".5" stop-color="#4a2f9a"/><stop offset="1" stop-color="#1a1048"/></linearGradient>
<linearGradient id="shine" gradientUnits="userSpaceOnUse" x1="-120" x2="-40" y1="0" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".38"/><stop offset="1" stop-color="#fff" stop-opacity="0"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="460 0" dur="5s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="pfg" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#fff"/><stop offset="1" stop-color="#000"/></linearGradient>
<mask id="pf"><rect x="100" y="30" width="170" height="215" fill="url(#pfg)"/></mask>
<clipPath id="ph"><rect x="112" y="40" width="150" height="195"/></clipPath>
<clipPath id="cs"><path d="{shape}"/></clipPath>
<radialGradient id="cg" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#818cf8" stop-opacity=".30"/><stop offset="1" stop-color="#818cf8" stop-opacity="0"/></radialGradient></defs>
<ellipse cx="145" cy="200" rx="150" ry="195" fill="url(#cg)"/>
<path d="{shape}" fill="url(#br)"/>
{img}
<g clip-path="url(#cs)"><path d="{shape}" fill="none"/><rect x="0" y="0" width="{W}" height="{H}" fill="url(#shine)" transform="skewX(-18)"/></g>
<path d="{shape}" fill="none" stroke="url(#aur)" stroke-width="3"/>
<path d="{shape}" fill="none" stroke="#22d3ee" stroke-opacity=".55" stroke-width="1.2" transform="translate(145 200) scale(.935) translate(-145 -200)"/>
<text x="68" y="104" text-anchor="middle" font-family="{SANS}" font-size="50" font-weight="800" fill="#f8fafc">{k["overall"]}</text>
<text x="68" y="130" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="700" fill="#c7d2fe" letter-spacing="1">{esc(k["pos"])}</text>
<g transform="translate(53 144)"><rect width="30" height="20" rx="2" fill="#fff"/><rect width="30" height="6.7" fill="#ff9933"/><rect y="13.3" width="30" height="6.7" fill="#138808"/><circle cx="15" cy="10" r="2.5" fill="none" stroke="#000080" stroke-width="1"/><rect width="30" height="20" rx="2" fill="none" stroke="#c7d2fe" stroke-opacity=".5"/></g>
<text x="145" y="266" text-anchor="middle" font-family="{SANS}" font-size="25" font-weight="800" letter-spacing="1" fill="#f8fafc">{esc(k["name"])}</text>
<rect x="68" y="275" width="154" height="1.5" fill="#c7d2fe" opacity=".5"/>
{stat(k["pac"],"PAC",98,306)}{stat(k["sho"],"SHO",98,332)}{stat(k["pas"],"PAS",98,358)}
<rect x="145" y="288" width="1.5" height="76" fill="#c7d2fe" opacity=".35"/>
{stat(k["dri"],"DRI",176,306)}{stat(k["def"],"DEF",176,332)}{stat(k["phy"],"PHY",176,358)}
<text x="145" y="381" text-anchor="middle" font-family="{MONO}" font-size="8.5" font-weight="700" letter-spacing="2" fill="#a5b4fc">GITFUT.COM</text>'''
    save("card.svg", W, H, body)

def panels(c, st):
    import datetime as _dt
    W, H = 700, 400; pw, ph = 345, 195
    def panel(x, y, title, right="", w=None):
        w = w or pw
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{ph}" rx="16" fill="url(#pbg)" stroke="url(#pst)" stroke-width="1.4"/>'
                f'<text x="{x+22}" y="{y+34}" font-family="{SANS}" font-size="16" font-weight="800" fill="url(#aur)">{esc(title)}</text>'
                f'<text x="{x+w-22}" y="{y+33}" text-anchor="end" font-family="{MONO}" font-size="10.5" fill="#64748b">{esc(right)}</text>'
                f'<rect x="{x+22}" y="{y+45}" width="{w-44}" height="1" fill="#1e293b"/>')
    u = "@" + c["username"]
    s = st or {}
    langs = s.get("languages")
    # 1) stats
    b = panel(0, 0, "GitHub Stats", u)
    rows = [("Contributions (year)", s.get("contributions")), ("Stars earned", s.get("stars")), ("Pull requests", s.get("prs")),
            ("Issues", s.get("issues")), ("Repositories", s.get("repos")), ("Followers", s.get("followers"))]
    for i, (lab, v) in enumerate(rows):
        y = 70 + i*20.5
        b += f'<text x="22" y="{y+4:.0f}" font-family="{SANS}" font-size="13" fill="#94a3b8">{lab}</text><text x="{pw-22}" y="{y+4:.0f}" text-anchor="end" font-family="{MONO}" font-size="13.5" font-weight="800" fill="{C1}">{fmt(v)}</text>'
    # 2) languages
    x0 = 355; b += panel(x0, 0, "Top Languages", "by code size")
    if langs:
        top = langs[:4]; other = round(100 - sum(l["pct"] for l in top), 1)
        if other > 0.1: top = top + [{"name": "Other", "pct": other, "color": "#475569"}]
        bx = x0 + 22; bw = pw - 44; cx = bx
        b += f'<clipPath id="lb"><rect x="{bx}" y="60" width="{bw}" height="9" rx="4.5"/></clipPath><g clip-path="url(#lb)">'
        tot = sum(l["pct"] for l in top) or 1
        for l in top:
            w = bw * l["pct"] / tot; b += f'<rect x="{cx:.1f}" y="60" width="{w+.5:.1f}" height="9" fill="{l["color"]}"/>'; cx += w
        b += '</g>'
        for i, l in enumerate(top):
            y = 94 + i*20
            b += f'<circle cx="{x0+28}" cy="{y}" r="4.5" fill="{l["color"]}"/><text x="{x0+42}" y="{y+4}" font-family="{SANS}" font-size="13" fill="#cbd5e1">{esc(l["name"])}</text><text x="{x0+pw-22}" y="{y+4}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="#94a3b8">{l["pct"]}%</text>'
    else:
        b += f'<text x="{x0+pw/2}" y="110" text-anchor="middle" font-family="{SANS}" font-size="13" fill="#64748b">Fills automatically after the</text><text x="{x0+pw/2}" y="130" text-anchor="middle" font-family="{SANS}" font-size="13" fill="#64748b">first "Update GitHub stats" run</text>'
    # 3) streak
    y0 = 205; b += panel(0, y0, "Contribution Streak", "past year", w=700)
    cur, lon = s.get("streak_current"), s.get("streak_longest")
    def md(d):
        try: return _dt.date.fromisoformat(d).strftime("%b %d").replace(" 0", " ")
        except Exception: return ""
    rng = f'{md(s.get("streak_start"))} – {md(s.get("streak_end"))}' if s.get("streak_start") else "–"
    for xx in (233, 467): b += f'<rect x="{xx}" y="{y0+62}" width="1" height="100" fill="#1e293b"/>'
    b += f'<text x="117" y="{y0+105}" text-anchor="middle" font-family="{SANS}" font-size="28" font-weight="800" fill="#f1f5f9">{fmt(s.get("contributions"))}</text><text x="117" y="{y0+126}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="#94a3b8">Total</text><text x="117" y="{y0+140}" text-anchor="middle" font-family="{SANS}" font-size="11" fill="#64748b">contributions</text>'
    circ = 2*3.14159*30; frac = min(1, (cur or 0) / (lon or 1)) if lon else 0
    b += f'<g transform="translate(350 {y0+98})"><circle r="30" fill="none" stroke="#1e293b" stroke-width="6"/><circle r="30" fill="none" stroke="url(#aur)" stroke-width="6" stroke-linecap="round" transform="rotate(-90)" stroke-dasharray="{frac*circ:.1f} {circ:.1f}"><animate attributeName="stroke-dasharray" from="0 {circ:.1f}" to="{frac*circ:.1f} {circ:.1f}" dur="1.4s" fill="freeze"/></circle><text y="9" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="800" fill="#f1f5f9">{fmt(cur)}</text></g>'
    b += f'<text x="350" y="{y0+150}" text-anchor="middle" font-family="{SANS}" font-size="12" font-weight="700" fill="{C1}">Current Streak</text>'
    b += f'<text x="583" y="{y0+105}" text-anchor="middle" font-family="{SANS}" font-size="28" font-weight="800" fill="#f1f5f9">{fmt(lon)}</text><text x="583" y="{y0+126}" text-anchor="middle" font-family="{SANS}" font-size="12" font-weight="700" fill="{C3}">Longest</text><text x="583" y="{y0+142}" text-anchor="middle" font-family="{SANS}" font-size="10.5" fill="#64748b">{esc(rng)}</text>'
    body = f'''<defs>{GRAD}<linearGradient id="pbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#131a2e"/><stop offset="1" stop-color="#0c1020"/></linearGradient>
<linearGradient id="pst" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C1}" stop-opacity=".55"/><stop offset=".5" stop-color="{C2}" stop-opacity=".35"/><stop offset="1" stop-color="{C3}" stop-opacity=".55"/></linearGradient></defs>{b}'''
    save("stats-panels.svg", W, H, body)


def mono_path(xs, ys):
    n = len(xs)
    if n < 2: return ""
    dx = [xs[i+1]-xs[i] for i in range(n-1)]; dy = [ys[i+1]-ys[i] for i in range(n-1)]
    m = [dy[i]/dx[i] for i in range(n-1)]
    t = [m[0]] + [(m[i-1]+m[i])/2 if m[i-1]*m[i] > 0 else 0 for i in range(1, n-1)] + [m[-1]]
    for i in range(n-1):
        if m[i] == 0: t[i] = t[i+1] = 0
        else:
            a_, b_ = t[i]/m[i], t[i+1]/m[i]; q = a_*a_ + b_*b_
            if q > 9: k = 3/q**.5; t[i] = k*a_*m[i]; t[i+1] = k*b_*m[i]
    d = f"M{xs[0]:.1f} {ys[0]:.1f}"
    for i in range(n-1):
        h = dx[i]
        d += f" C{xs[i]+h/3:.1f} {ys[i]+t[i]*h/3:.1f} {xs[i+1]-h/3:.1f} {ys[i+1]-t[i+1]*h/3:.1f} {xs[i+1]:.1f} {ys[i+1]:.1f}"
    return d

def graph(c, st):
    import datetime as _dt
    W, H = 1000, 340; L, R, T, B = 96, 944, 100, 262
    daily = (st or {}).get("daily") or []
    n = len(daily); vals = [d["count"] for d in daily]
    mx = max(vals) if vals else 0
    ymax = max(4, ((mx + 3)//4)*4)
    def fd(s_):
        d = _dt.date.fromisoformat(s_); return f"{d.strftime('%b')} {d.day}"
    xs = [L + i*(R-L)/max(1, n-1) for i in range(n)]
    ys = [B - v/ymax*(B-T) for v in vals]
    grid = ""
    for k in range(5):
        yy = B - k*(B-T)/4
        grid += f'<line x1="{L}" x2="{R}" y1="{yy:.1f}" y2="{yy:.1f}" stroke="#334155" stroke-opacity=".55" stroke-dasharray="3 6"/><text x="{L-16}" y="{yy+4:.1f}" text-anchor="end" font-family="{SANS}" font-size="12" fill="#64748b">{int(ymax*k/4)}</text>'
    if n >= 2:
        d = mono_path(xs, ys)
        area = d + f" L{xs[-1]:.1f} {B} L{xs[0]:.1f} {B} Z"
        marks = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3.6" fill="#0a0c14" stroke="#fff" stroke-width="1.6"/>' for x, y in list(zip(xs, ys))[:-1])
        pk = vals.index(mx)
        label = f"Peak · {mx} · {fd(daily[pk]['date'])}"; pw_ = len(label)*7.4 + 30
        px_ = min(max(xs[pk] - 10, L - 24), R - pw_)
        peak = (f'<g transform="translate({px_:.1f} {max(58, ys[pk]-40):.1f})"><rect width="{pw_:.1f}" height="28" rx="14" fill="url(#aur)"/>'
                f'<text x="{pw_/2:.1f}" y="18.5" text-anchor="middle" font-family="{SANS}" font-size="12.5" font-weight="800" fill="#0a0c14">{esc(label)}</text></g>') if mx > 0 else ""
        lab = ""
        for i in range(0, n, 5):
            lab += f'<text x="{xs[i]:.1f}" y="{B+22}" text-anchor="middle" font-family="{SANS}" font-size="12" fill="#64748b">{fd(daily[i]["date"])}</text>'
        if (n-1) % 5: lab += f'<text x="{xs[-1]:.1f}" y="{B+22}" text-anchor="middle" font-family="{SANS}" font-size="12" fill="#64748b">{fd(daily[-1]["date"])}</text>'
        chart = (f'<path d="{area}" fill="url(#ar)"/>'
                 f'<path d="{d}" fill="none" stroke="url(#lg)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" filter="url(#glow)" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0"><animate attributeName="stroke-dashoffset" from="1" to="0" dur="2.2s" fill="freeze"/></path>'
                 f'{marks}<circle cx="{xs[-1]:.1f}" cy="{ys[-1]:.1f}" r="9" fill="{C1}" fill-opacity=".25"><animate attributeName="r" values="7;13;7" dur="2.4s" repeatCount="indefinite"/></circle>'
                 f'<circle cx="{xs[-1]:.1f}" cy="{ys[-1]:.1f}" r="5.5" fill="#fff"/>{peak}{lab}')
        total = sum(vals); rng = f"Last {n-1} days · {fd(daily[0]['date'])} – {fd(daily[-1]['date'])} · {total} total"
    else:
        chart = (f'<line x1="{L}" x2="{R}" y1="{B}" y2="{B}" stroke="url(#lg)" stroke-width="3"/>'
                 f'<text x="500" y="{(T+B)/2:.0f}" text-anchor="middle" font-family="{SANS}" font-size="14" fill="#64748b">Fills automatically after the first "Update GitHub stats" run</text>')
        rng = "Last 30 days"
    body = f"""<defs>{GRAD}<linearGradient id="lg" gradientUnits="userSpaceOnUse" x1="{L}" x2="{R}" y1="0" y2="0"><stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C3}"/></linearGradient>
<linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{C2}" stop-opacity=".38"/><stop offset="1" stop-color="{C2}" stop-opacity="0"/></linearGradient>
<linearGradient id="gbg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#131a2e"/><stop offset="1" stop-color="#0b0f1d"/></linearGradient></defs>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="20" fill="url(#gbg)" stroke="url(#aur)" stroke-opacity=".7" stroke-width="1.6"/>
<g fill="none" stroke="url(#aur)" stroke-width="2.6" stroke-linecap="round"><path d="M24 58V30a4 4 0 0 1 4-4h28"/><path d="M{W-24} {H-58}v28a4 4 0 0 1-4 4h-28"/></g>
<circle cx="76" cy="42" r="5" fill="{C1}"/><text x="92" y="48" font-family="{SANS}" font-size="18" font-weight="800" letter-spacing="1.2" fill="url(#aur)">CONTRIBUTION ACTIVITY</text>
<text x="{W-40}" y="47" text-anchor="end" font-family="{SANS}" font-size="14" fill="#e2e8f0">{esc(rng)}</text>
{grid}{chart}"""
    save("graph.svg", W, H, body)

def quote(c):
    q, a = c["quote"]; W, H = 1000, 120
    body = f'''<defs>{GRAD}</defs><text x="500" y="56" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="26" fill="#e2e8f0">“{esc(q)}”</text>
<text x="500" y="90" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="4" fill="url(#aur)">— {esc(a)}</text>'''
    save("quote.svg", W, H, body)

def readme(c):
    u = c["username"]
    P = lambda i: f'<a href="{c["projects"][i]["url"]}"><img src="assets/project{i+1}.svg" width="49%" alt="{c["projects"][i]["name"]}"/></a>'
    n = len(c["projects"])
    proj = "\n".join(P(i) + ("\n" if i % 2 else " ") for i in range(n))
    md = f'''<div align="center">

<a href="{c["site_url"]}"><img src="assets/banner.svg" width="100%" alt="{c["name"]}"/></a>

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h1.svg" width="100%" alt="About Me"/>

<img src="assets/about.svg" width="100%" alt="About {c["name"]}"/>

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h2.svg" width="100%" alt="Tech Stack"/>

<img src="assets/stack.svg" width="100%" alt="Tech stack"/>

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h3.svg" width="100%" alt="Featured Projects"/>

{proj}

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h4.svg" width="100%" alt="GitHub Stats"/>

<a href="{c["gitfut_url"]}"><img src="assets/card.svg" width="28.8%" alt="GitFut card"/></a>
<img src="assets/stats-panels.svg" width="69.5%" alt="GitHub stats"/>

<a href="{c["gitfut_url"]}"><b>Get scouted →</b></a>

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h5.svg" width="100%" alt="Contribution Graph"/>

<img src="assets/graph.svg" width="100%" alt="Contribution graph"/>

<img src="assets/quote.svg" width="100%" alt="quote"/>

<img src="assets/footer.svg" width="100%" alt="Thanks for visiting"/>

</div>
'''
    (pathlib.Path(__file__).parent / "README.md").write_text(md, encoding="utf-8")

if __name__ == "__main__":
    c = CONFIG
    st = load_stats() or c.get("stats_manual")
    banner(c); banner(c, footer=True); divider(); chips(c); about(c); card(c); panels(c, st); graph(c, st); stack(c); cards(c); quote(c)
    for i, s in enumerate(c["sections"], 1): header(s, i)
    readme(c); print("built:", sorted(p.name for p in OUT.iterdir()))
