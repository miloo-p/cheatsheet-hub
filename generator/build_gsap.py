import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sheetgen import build, HUB
from gsap_data import SECTIONS
V = "3.15.0"
CDN = f"https://cdnjs.cloudflare.com/ajax/libs/gsap/{V}/"
HUBLINK = f'<a href="{HUB}" target="_blank" rel="noopener">Spickzettel-Hub</a>'
CSSLINK = '<a href="https://claude.ai/artifact/9i6icDS2mpDmQm3j3fzdpT#animation" target="_blank" rel="noopener">CSS Spickzettel</a>'
cfg = dict(key="gsap", title="GSAP Spickzettel", eyebrow="Animation & 3D · GSAP", hl="js",
    labels=("Mit GSAP", "Ohne GSAP"),
    colors=dict(accent="#3d7a12", accent_soft="#e4f2d6", long="#7a5a17", long_soft="#f3ead6",
                accent_d="#9be15d", accent_soft_d="#1f2e14", long_d="#e2c27a", long_soft_d="#2f2716", kw="#9be15d"),
    lede=f"{{n}} Konzepte der Animationsbibliothek GSAP (Version {V}). Links steht jeweils der GSAP-Code, rechts derselbe Effekt <b>ohne GSAP</b>, also mit CSS, der Web Animations API oder reinem JavaScript. So siehst du, was die Bibliothek dir abnimmt und wann du sie gar nicht brauchst. Die meisten Karten haben eine <b>Live-Demo</b>: einfach auf „Abspielen“ klicken. Die Doku-Links führen zur offiziellen GSAP-Doku auf Englisch.",
    legend=[("Mit GSAP", "der Code mit der Bibliothek"), ("Ohne GSAP", "CSS, Web Animations API oder Vanilla-JS")],
    placeholder="Filtern, z.B. timeline, scrub, stagger …",
    head_scripts="\n".join(f'<script src="{CDN}{f}"></script>' for f in ["gsap.min.js", "ScrollTrigger.min.js", "Flip.min.js", "SplitText.min.js"]),
    classic_prelude="gsap.registerPlugin(ScrollTrigger, Flip, SplitText);",
    footer=f"Übungsidee: Nimm die Animationskarten aus dem {CSSLINK} und baue jede einmal mit GSAP nach. Danach eine kleine Landingpage mit einer Timeline beim Laden und zwei ScrollTrigger-Effekten. Alle Zettel im {HUBLINK}.")
print("gsap", build(cfg, SECTIONS, "gsap-spickzettel.html"))
