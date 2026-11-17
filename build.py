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
    "chips": ["Developer", "Full-Stack", "Open Source", "Always Learning"],
    "quote": ("Software is eating the world.", "MARC ANDREESSEN"),
    "stack": {
        "Languages": ["Python", "JavaScript", "TypeScript", "C++", "SQL"],
        "AI / ML":   ["PyTorch", "TensorFlow", "scikit-learn", "LangChain", "OpenCV"],
        "Web":       ["React", "Node.js", "Express", "Next.js", "Tailwind"],
        "Data & Ops":["MongoDB", "PostgreSQL", "Docker", "Git", "Linux"],
    },
    "projects": [
        {"name": "ai-code-review-tool", "desc": "Paste code, get instant AI review feedback powered by an LLM API.",
         "tags": ["React", "Node.js", "Groq"], "lang": "JavaScript", "color": "#facc15", "url": "https://github.com/DeepakGupta2006"},
        {"name": "land-cover-unet", "desc": "Land-use classification on satellite imagery using a U-Net model.",
         "tags": ["Python", "U-Net", "Remote Sensing"], "lang": "Python", "color": "#38bdf8", "url": "https://github.com/DeepakGupta2006"},
        {"name": "time-capsule", "desc": "Write messages to your future self and unlock them on a chosen date.",
         "tags": ["Next.js", "MongoDB"], "lang": "TypeScript", "color": "#818cf8", "url": "https://github.com/DeepakGupta2006"},
        {"name": "your-next-idea", "desc": "A placeholder for the project you're about to ship. Edit me in build.py.",
         "tags": ["Idea", "Soon"], "lang": "Python", "color": "#e879f9", "url": "https://github.com/DeepakGupta2006"},
    ],
    "sections": ["About Me", "Tech Stack", "Featured Projects", "GitHub Stats", "Contribution Snake"],
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
    W = 1000; y = 24; body = f"<defs>{GRAD}</defs>"; cols = [C1, C2, C3, "#34d399"]; n = 0
    for ci, (cat, items) in enumerate(c["stack"].items()):
        col = cols[ci % 4]
        body += f'<text x="60" y="{y+22}" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="2" fill="{col}">{esc(cat.upper())}</text>'
        x = 230
        for t in items:
            w = len(t)*8.6 + 36
            body += f'''<g transform="translate({x:.0f} {y})"><rect width="{w:.0f}" height="34" rx="10" fill="{col}" fill-opacity=".09" stroke="{col}" stroke-opacity=".55"/><circle cx="16" cy="17" r="3.2" fill="{col}"/><text x="28" y="21.5" font-family="{SANS}" font-size="13.5" font-weight="600" fill="#e2e8f0">{esc(t)}</text><animate attributeName="opacity" from="0" to="1" dur=".5s" begin="{n*.07:.2f}s" fill="freeze"/></g>'''
            x += w + 12; n += 1
        y += 52
    save("stack.svg", W, y + 6, body)

def cards(c):
    for i, p in enumerate(c["projects"], 1):
        W, H = 480, 178
        lines = textwrap.wrap(p["desc"], 56)[:2]
        desc = "".join(f'<text x="26" y="{84+i2*20}" font-family="{SANS}" font-size="13.5" fill="#94a3b8">{esc(l)}</text>' for i2, l in enumerate(lines))
        tx = 26; tg = ""
        for t in p["tags"][:4]:
            w = len(t)*7.2 + 22
            tg += f'<g transform="translate({tx:.0f} 112)"><rect width="{w:.0f}" height="24" rx="12" fill="{C2}" fill-opacity=".14" stroke="{C2}" stroke-opacity=".5"/><text x="{w/2:.0f}" y="16" text-anchor="middle" font-family="{MONO}" font-size="11" fill="#c7d2fe">{esc(t)}</text></g>'
            tx += w + 8
        body = f'''<defs>{GRAD}<linearGradient id="g{i}" gradientUnits="userSpaceOnUse" x1="-480" x2="0" y1="0" y2="0" spreadMethod="repeat"><stop offset="0" stop-color="{C1}"/><stop offset=".5" stop-color="{C2}"/><stop offset="1" stop-color="{C3}"/><animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="480 0" dur="5s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="bg{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#131a2e"/><stop offset="1" stop-color="#0c1020"/></linearGradient></defs>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="url(#bg{i})" stroke="url(#g{i})" stroke-width="1.6"/>
<circle cx="{W-30}" cy="30" r="46" fill="{p['color']}" opacity=".08"/>
<text x="26" y="46" font-family="{MONO}" font-size="17" font-weight="700" fill="{C1}">{esc(p["name"])}</text>
<path d="M{W-42} 34l8-8m0 0h-6m6 0v6" stroke="#94a3b8" stroke-width="1.8" fill="none" stroke-linecap="round"/>
{desc}{tg}
<circle cx="32" cy="156" r="5" fill="{p['color']}"/><text x="44" y="160" font-family="{SANS}" font-size="12.5" fill="#cbd5e1">{esc(p["lang"])}</text>
<text x="{W-26}" y="160" text-anchor="end" font-family="{MONO}" font-size="11.5" font-weight="700" letter-spacing="1" fill="{C3}">VIEW PROJECT →</text>'''
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

def quote(c):
    q, a = c["quote"]; W, H = 1000, 120
    body = f'''<defs>{GRAD}</defs><text x="500" y="56" text-anchor="middle" font-family="Georgia,'Times New Roman',serif" font-style="italic" font-size="26" fill="#e2e8f0">“{esc(q)}”</text>
<text x="500" y="90" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="4" fill="url(#aur)">— {esc(a)}</text>'''
    save("quote.svg", W, H, body)

def readme(c):
    u = c["username"]
    stats_q = f"username={u}&show_icons=true&hide_border=true&bg_color=0a0c14&title_color=22d3ee&icon_color=e879f9&text_color=cbd5e1&ring_color=818cf8"
    streak = f"user={u}&theme=dark&hide_border=true&background=0a0c14&ring=818cf8&fire=e879f9&currStreakNum=22d3ee&sideNums=c7d2fe&currStreakLabel=818cf8&sideLabels=94a3b8&dates=64748b"
    langs = f"username={u}&layout=compact&hide_border=true&bg_color=0a0c14&title_color=22d3ee&text_color=cbd5e1"
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

<img height="170" src="https://github-readme-stats.vercel.app/api?{stats_q}" alt="stats"/>
<img height="170" src="https://github-readme-stats.vercel.app/api/top-langs/?{langs}" alt="languages"/>

<img src="https://streak-stats.demolab.com?{streak}" width="97%" alt="streak"/>

<img src="assets/divider.svg" width="100%" alt=""/>

<img src="assets/h5.svg" width="100%" alt="Contribution Snake"/>

<img src="https://raw.githubusercontent.com/{u}/{u}/output/github-snake-dark.svg" width="100%" alt="snake"/>

<img src="assets/quote.svg" width="100%" alt="quote"/>

<img src="assets/footer.svg" width="100%" alt="Thanks for visiting"/>

</div>
'''
    (pathlib.Path(__file__).parent / "README.md").write_text(md, encoding="utf-8")

if __name__ == "__main__":
    c = CONFIG
    banner(c); banner(c, footer=True); divider(); chips(c); about(c); stack(c); cards(c); quote(c)
    for i, s in enumerate(c["sections"], 1): header(s, i)
    readme(c); print("built:", sorted(p.name for p in OUT.iterdir()))
