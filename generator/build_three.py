import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sheetgen import build, HUB
from three_data import SECTIONS
V = "0.186.1"
HUBLINK = f'<a href="{HUB}" target="_blank" rel="noopener">Spickzettel-Hub</a>'
GSAPLINK = '<a href="https://claude.ai/artifact/DVpdoSZy1Zrmuy21bkjg4a" target="_blank" rel="noopener">GSAP Spickzettel</a>'
head = f'''<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.15.0/gsap.min.js"></script>
<script type="importmap">
{{ "imports": {{ "three": "https://cdn.jsdelivr.net/npm/three@{V}/build/three.module.js",
                "three/addons/": "https://cdn.jsdelivr.net/npm/three@{V}/examples/jsm/" }} }}
</script>'''
prelude = r'''import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
window.THREE = THREE;
const accent = (el) => getComputedStyle(el).getPropertyValue("--accent").trim() || "#3b82f6";
function mini(stage, { z = 4 } = {}) {
  const w = stage.clientWidth, h = stage.clientHeight;
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(getComputedStyle(stage).getPropertyValue("--bg").trim() || "#f5f6f8");
  const camera = new THREE.PerspectiveCamera(50, w / h, 0.1, 100);
  camera.position.z = z;
  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.setSize(w, h);
  stage.prepend(renderer.domElement);
  const timer = new THREE.Timer();
  timer.connect(document);
  let tick = null;
  const extra = [];
  renderer.setAnimationLoop((t) => {
    timer.update(t);
    if (tick) tick(timer.getDelta(), timer.getElapsed());
    renderer.render(scene, camera);
  });
  (stage._c = stage._c || []).push(() => {
    renderer.setAnimationLoop(null);
    timer.dispose();
    extra.forEach((d) => d.dispose());
    scene.traverse((o) => {
      if (o.geometry) o.geometry.dispose();
      [].concat(o.material || []).forEach((m) => { if (m.map) m.map.dispose(); m.dispose(); });
    });
    renderer.dispose();
    renderer.forceContextLoss();
    renderer.domElement.remove();
  });
  return { scene, camera, renderer, timer, onTick: (fn) => { tick = fn; }, track: (...o) => extra.push(...o) };
}'''
post = r'''for (const k of Object.keys(DEMOS)) {
  const f = DEMOS[k];
  DEMOS[k] = (stage) => {
    stage._c = [];
    const r = f(stage);
    return () => { if (typeof r === "function") r(); stage._c.forEach((fn) => fn()); stage._c = []; };
  };
}'''
cfg = dict(key="three", title="Three.js Spickzettel", eyebrow="Animation & 3D · Three.js", hl="js",
    labels=("Variante A", "Variante B"), single_label="Code",
    colors=dict(accent="#2563c9", accent_soft="#e1eafa", long="#8a4b14", long_soft="#f6e8da",
                accent_d="#7fb0ff", accent_soft_d="#17243d", long_d="#f0b07a", long_soft_d="#33241a", kw="#7fb0ff"),
    lede=f"{{n}} Konzepte für 3D im Browser mit Three.js (Version r{V.split('.')[1]}). Die meisten Karten zeigen einen Code-Block und eine <b>Live-Demo</b>, die per Klick auf „Abspielen“ startet. Es läuft immer nur eine 3D-Szene gleichzeitig. Wo es zwei sinnvolle Wege gibt, stehen sie nebeneinander, z.B. aktueller und veralteter Code oder React Three Fiber und reines Three.js. Die Doku-Links führen zur offiziellen Three.js-Doku und zum Manual auf Englisch.",
    legend=[("Code", "ein Weg, mit Live-Demo"), ("Zwei Spalten", "zwei Wege im Vergleich, Beschriftung je Karte")],
    placeholder="Filtern, z.B. Licht, Raycaster, Timer …",
    has_long=False,
    demo_mode="module", head_scripts=head, module_prelude=prelude, module_post=post,
    footer=f"Übungsidee: Baue eine Produktansicht mit einem Objekt, zwei Lichtern, Schatten und OrbitControls. Danach eine Kamerafahrt mit dem {GSAPLINK} und ScrollTrigger. Alle Zettel im {HUBLINK}.")
print("three", build(cfg, SECTIONS, "three-spickzettel.html"))
