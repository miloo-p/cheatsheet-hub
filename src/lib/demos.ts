/*
 * Loader-Skripte für die Live-Demos.
 *
 * Jede Zettelseite mit Demos bekommt ein kleines Skript, das window.DEMO_LOADER festlegt.
 * Erst beim ersten Klick auf "Abspielen" lädt es die Bibliothek und liefert ein Objekt
 * { "<karten-id>": function (stage) { ... } } zurück. Gibt eine Demo eine Funktion zurück,
 * wird sie beim Neustart zum Aufräumen aufgerufen (siehe scripts/sheet.ts).
 */

export const GSAP_VERSION = '3.15.0';
export const THREE_VERSION = '0.186.1';

const GSAP_CDN = `https://cdnjs.cloudflare.com/ajax/libs/gsap/${GSAP_VERSION}/`;
const GSAP_FILES = ['gsap.min.js', 'ScrollTrigger.min.js', 'Flip.min.js', 'SplitText.min.js'];

export interface DemoSource {
  id: string;
  js: string;
}

/** Import Map für Three.js, muss im <head> vor allen Modulen stehen */
export const threeImportMap = JSON.stringify({
  imports: {
    three: `https://cdn.jsdelivr.net/npm/three@${THREE_VERSION}/build/three.module.js`,
    'three/addons/': `https://cdn.jsdelivr.net/npm/three@${THREE_VERSION}/examples/jsm/`,
  },
});

function defs(demos: DemoSource[]): string {
  return demos.map((d) => `DEMOS[${JSON.stringify(d.id)}] = function (stage) {\n${d.js}\n};`).join('\n\n');
}

/** Hilfsfunktionen für die Three.js-Demos: mini() baut Szene, Kamera, Renderer und Render-Loop */
const THREE_PRELUDE = String.raw`
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
}`;

/** Jede Three.js-Demo räumt zusätzlich alles auf, was mini() registriert hat */
const THREE_POST = String.raw`
for (const k of Object.keys(DEMOS)) {
  const f = DEMOS[k];
  DEMOS[k] = (stage) => {
    stage._c = [];
    const r = f(stage);
    return () => { if (typeof r === "function") r(); stage._c.forEach((fn) => fn()); stage._c = []; };
  };
}`;

export function demoLoader(mode: 'gsap' | 'three', demos: DemoSource[]): string {
  let js: string;
  if (mode === 'gsap') {
    const libs = JSON.stringify(GSAP_FILES.map((f) => GSAP_CDN + f));
    js = `window.DEMO_LOADER = async function () {
  await loadScripts(${libs});
  gsap.registerPlugin(ScrollTrigger, Flip, SplitText);
  var DEMOS = {};
${defs(demos)}
  return DEMOS;
};`;
  } else {
    js = `window.DEMO_SINGLE = true;
window.DEMO_LOADER = async function () {
  const THREE = await import("three");
  const { OrbitControls } = await import("three/addons/controls/OrbitControls.js");
  await loadScripts([${JSON.stringify(GSAP_CDN + 'gsap.min.js')}]);
${THREE_PRELUDE}
  const DEMOS = {};
${defs(demos)}
${THREE_POST}
  return DEMOS;
};`;
  }
  // Ein "</script" im Demo-Code würde das Skript-Tag vorzeitig beenden
  return js.replace(/<\/script/gi, '<\\/script');
}
