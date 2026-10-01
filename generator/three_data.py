D = "https://threejs.org/docs/#"
M = "https://threejs.org/manual/#en/"

def C(t, d, k, a, e, l, demo=None, labels=None):
    c = dict(t=t, d=d, k=k.strip("\n"), a=(a.strip("\n") if a else None), e=e, l=l, demo=demo)
    if labels: c["labels"] = labels
    return c

HINT = '<span class="note">3D-Szene startet per Klick auf „Abspielen“.</span>'

def demo(js, h=220):
    return dict(html=HINT, js=js, h=h, flush=True)

SECTIONS = []

SECTIONS.append(("grundlagen", "Grundlagen", "basics", "Jede Three.js-Szene braucht dieselben drei Bausteine und eine Schleife, die sie zeichnet.", [
C("Szene, Kamera, Renderer",
  "Die drei Pflichtbausteine: eine Welt mit Objekten, ein Blickwinkel und etwas, das das Bild auf ein `<canvas>` zeichnet.",
  """
import * as THREE from "three";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 4;

const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

const cube = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshNormalMaterial()
);
scene.add(cube);

renderer.render(scene, camera);
""", None,
 ("Three.js funktioniert wie ein Filmset: Die Szene ist das Studio mit allen Requisiten, die Kamera bestimmt den Bildausschnitt, und der Renderer ist der Kameramann, der auf Knopfdruck ein Bild belichtet.",
  ["`Scene` ist der Container für alles, was zu sehen sein soll: Objekte, Lichter, Hintergrund.",
   "`PerspectiveCamera(fov, aspect, near, far)`: Blickwinkel in Grad, Seitenverhältnis, und der Bereich, in dem Dinge gezeichnet werden. Was näher als 0.1 oder weiter als 100 ist, wird abgeschnitten.",
   "Die Kamera steht anfangs im Ursprung `(0, 0, 0)` und schaut in Richtung minus z. Darum wird sie mit `position.z = 4` nach hinten gesetzt, sonst steckt sie im Würfel.",
   "`WebGLRenderer` erzeugt ein `<canvas>`, das du mit `appendChild` in die Seite einhängst.",
   "`renderer.render(scene, camera)` zeichnet genau ein Bild. Für Bewegung brauchst du eine Schleife, siehe nächste Karte."],
  "Einen schwarzen Bildschirm bekommen und nicht wissen warum. Die häufigsten Ursachen: Kamera steht im Objekt, Objekt liegt außerhalb von `near` und `far`, es fehlt Licht für ein `MeshStandardMaterial`, oder `render()` wird nie aufgerufen.",
  "`MeshNormalMaterial` ist zum Lernen ideal, weil es ohne Licht funktioniert und die Flächen nach ihrer Ausrichtung einfärbt. So siehst du sofort, ob Geometrie und Kamera stimmen.",
  "Warum ist der Würfel nicht zu sehen, wenn `camera.position.z` 0 bleibt?",
  "Weil die Kamera dann genau in der Mitte des Würfels steht. Von innen sind die Flächen unsichtbar, denn standardmäßig wird nur die Außenseite gezeichnet."),
 [("Grundlagen (Manual)", M+"fundamentals"), ("PerspectiveCamera", D+"PerspectiveCamera"), ("WebGLRenderer", D+"WebGLRenderer")],
 demo=demo("""const { scene, camera } = mini(stage);
const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
cube.rotation.set(0.5, 0.6, 0);
scene.add(cube);""")),

C("Die Render-Schleife mit `Timer`",
  "Für Bewegung muss die Szene 60-mal pro Sekunde neu gezeichnet werden. Seit r183 ist `Clock` veraltet, der Nachfolger heißt `Timer`.",
  """
const timer = new THREE.Timer();
timer.connect(document);   // pausiert, wenn der Tab im Hintergrund ist

renderer.setAnimationLoop((timestamp) => {
  timer.update(timestamp);
  const delta = timer.getDelta();     // Sekunden seit dem letzten Bild

  cube.rotation.y += delta * 1.5;     // 1,5 Radiant pro Sekunde
  renderer.render(scene, camera);
});
""", """
const clock = new THREE.Clock();      // veraltet seit r183

function animate() {
  requestAnimationFrame(animate);
  const delta = clock.getDelta();

  cube.rotation.y += delta * 1.5;
  renderer.render(scene, camera);
}
animate();
""",
 ("Delta-Zeit ist wie Tempo statt Schrittzahl. Sagst du „pro Bild 0,01 drehen“, dreht sich der Würfel auf einem 120-Hz-Monitor doppelt so schnell wie auf einem 60-Hz-Monitor. Mit „1,5 pro Sekunde mal vergangene Zeit“ ist er überall gleich schnell.",
  ["`setAnimationLoop` ruft die Funktion vor jedem Bild auf, so oft der Bildschirm aktualisiert. Es ist der Three.js-Ersatz für `requestAnimationFrame` und funktioniert auch in VR.",
   "`timer.update(timestamp)` merkt sich die aktuelle Zeit. Danach liefert `getDelta()` die Sekunden seit dem letzten Bild und `getElapsed()` die Gesamtzeit.",
   "`timer.connect(document)` sorgt dafür, dass nach einem Tab-Wechsel kein riesiger Zeitsprung entsteht. Ohne das springt die Animation beim Zurückkommen.",
   "Die rechte Variante mit `Clock` funktioniert noch, gilt aber seit Version r183 als veraltet. Du findest sie in fast allen älteren Tutorials."],
  "Pro Bild einen festen Wert addieren, z.B. `rotation.y += 0.01`. Dann hängt die Geschwindigkeit von der Bildrate ab: auf schnellen Monitoren zu schnell, auf langsamen Geräten zu langsam.",
  "Neuer Code nimmt `Timer` und `setAnimationLoop`. `Clock` und `requestAnimationFrame` musst du lesen können, weil sie in vielen Beispielen noch stehen.",
  "Wie stoppst du die Render-Schleife, z.B. beim Verlassen der Seite?",
  "Mit `renderer.setAnimationLoop(null)`."),
 [("Timer", D+"Timer"), ("Migration Guide (EN)", "https://github.com/mrdoob/three.js/wiki/Migration-Guide")],
 demo=demo("""const { scene, onTick } = mini(stage);
const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
scene.add(cube);
onTick((delta) => { cube.rotation.y += delta * 1.5; cube.rotation.x += delta * 0.5; });"""),
 labels=("Aktuell: Timer", "Veraltet: Clock")),

C("Responsiv: Größe und Pixeldichte",
  "Das Canvas muss mitwachsen, wenn sich sein Container ändert, und auf hochauflösenden Displays scharf bleiben.",
  """
const container = document.querySelector("#scene");

function resize() {
  const { clientWidth: w, clientHeight: h } = container;
  camera.aspect = w / h;
  camera.updateProjectionMatrix();
  renderer.setSize(w, h);
}
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
new ResizeObserver(resize).observe(container);
""", """
renderer.setPixelRatio(devicePixelRatio);

window.addEventListener("resize", () => {
  camera.aspect = innerWidth / innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(innerWidth, innerHeight);
});
""",
 ("Das Canvas ist eine Leinwand mit einer festen Anzahl Pixel. Wird der Rahmen größer, ohne dass die Leinwand mitwächst, wird das Bild unscharf oder verzerrt. Das Seitenverhältnis der Kamera ist das Format des Fotos, das zur Leinwand passen muss.",
  ["`camera.aspect` muss dem Seitenverhältnis des Canvas entsprechen, sonst wirkt alles gestaucht.",
   "Nach jeder Änderung an der Kamera muss `updateProjectionMatrix()` aufgerufen werden. Sonst gilt die alte Einstellung weiter.",
   "`renderer.setSize()` ändert die echte Pixelzahl des Canvas.",
   "`setPixelRatio` berücksichtigt Retina-Displays. Die Begrenzung auf 2 ist wichtig: Handys mit Faktor 3 oder 4 müssten sonst bis zu viermal so viele Pixel berechnen, ohne sichtbaren Gewinn.",
   "`ResizeObserver` reagiert auf Größenänderungen des Containers, also auch wenn sich das Layout ändert, ohne dass das Fenster seine Größe ändert. Das `resize`-Event des Fensters bekommt das nicht mit."],
  "`updateProjectionMatrix()` vergessen. Das Canvas hat dann die richtige Größe, aber die Szene ist verzerrt, weil die Kamera noch mit dem alten Seitenverhältnis rechnet.",
  "`ResizeObserver` für Szenen in einem Bereich der Seite, z.B. einer Karte oder einem Hero. Das Fenster-Event reicht nur für Vollbild-Szenen.",
  "Warum ist `Math.min(devicePixelRatio, 2)` besser als `devicePixelRatio` allein?",
  "Weil es Geräte mit sehr hoher Pixeldichte begrenzt. Ab Faktor 2 sieht man kaum noch einen Unterschied, aber die Grafikkarte muss bei Faktor 3 mehr als doppelt so viele Pixel berechnen."),
 [("Responsive (Manual)", M+"responsive"), ("ResizeObserver (MDN)", "https://developer.mozilla.org/de/docs/Web/API/ResizeObserver")],
 labels=("Container", "Ganzes Fenster")),
]))

SECTIONS.append(("objekte", "Objekte", "objects", "Was du siehst, ist immer ein Mesh: eine Form plus eine Oberfläche, platziert im Raum.", [
C("Mesh = Geometrie + Material",
  "Die Geometrie legt die Form fest, das Material das Aussehen. Erst zusammen ergeben sie ein sichtbares Objekt.",
  """
const geometry = new THREE.TorusKnotGeometry(0.6, 0.2, 128, 16);
const material = new THREE.MeshNormalMaterial();
const knot = new THREE.Mesh(geometry, material);
scene.add(knot);

// eingebaute Formen, u.a.:
// BoxGeometry, SphereGeometry, PlaneGeometry,
// CylinderGeometry, ConeGeometry, TorusGeometry
""", None,
 ("Die Geometrie ist das Drahtgestell einer Figur, das Material der Stoff, der darübergespannt wird. Dasselbe Gestell kann mit verschiedenen Stoffen bezogen werden, und derselbe Stoff passt auf verschiedene Gestelle.",
  ["Eine Geometrie besteht aus Eckpunkten (Vertices), die zu Dreiecken verbunden sind. Auch eine Kugel ist nur aus vielen Dreiecken zusammengesetzt.",
   "Die Zahlenparameter bestimmen Größe und Detailgrad. Bei `SphereGeometry(1, 32, 16)` sind 32 und 16 die Segmente: mehr Segmente, rundere Kugel, mehr Rechenaufwand.",
   "Ein Material beschreibt, wie die Oberfläche auf Licht reagiert, siehe Abschnitt Licht.",
   "Geometrie und Material lassen sich zwischen mehreren Meshes teilen. Das spart Speicher."],
  "Für jeden von 100 gleichen Würfeln eine eigene Geometrie und ein eigenes Material erzeugen. Das kostet unnötig Speicher. Einmal erzeugen und an alle Meshes übergeben reicht, und bei sehr vielen Objekten ist `InstancedMesh` noch besser.",
  "Eingebaute Geometrien für Prototypen und einfache Formen. Für echte Modelle exportierst du aus Blender und lädst sie als GLTF.",
  "Was passiert mit einer Kugel, wenn du `SphereGeometry(1, 6, 4)` statt `(1, 32, 16)` nimmst?",
  "Sie wird sichtbar eckig, weil sie nur aus wenigen Dreiecken besteht. Für Low-Poly-Stil ist das sogar gewollt."),
 [("Primitives (Manual)", M+"primitives"), ("Mesh", D+"Mesh"), ("BufferGeometry", D+"BufferGeometry")],
 demo=demo("""const { scene, onTick } = mini(stage, { z: 5 });
const mat = new THREE.MeshNormalMaterial();
const shapes = [new THREE.BoxGeometry(0.9, 0.9, 0.9), new THREE.TorusKnotGeometry(0.4, 0.14, 128, 16), new THREE.SphereGeometry(0.55, 8, 6)]
  .map((g, i) => { const m = new THREE.Mesh(g, mat); m.position.x = (i - 1) * 1.6; scene.add(m); return m; });
onTick((dt) => shapes.forEach(m => { m.rotation.x += dt * 0.6; m.rotation.y += dt; }));""")),

C("Position, Drehung, Größe",
  "Jedes Objekt hat `position`, `rotation` und `scale`. Drehungen werden in Radiant angegeben, nicht in Grad.",
  """
cube.position.set(1, 0.5, 0);
cube.rotation.y = THREE.MathUtils.degToRad(45);
cube.scale.setScalar(1.5);

cube.lookAt(0, 0, 0);   // zum Ursprung ausrichten
""", """
cube.position.x = 1;
cube.position.y = 0.5;
cube.position.z = 0;
cube.rotation.y = 45 * Math.PI / 180;   // Grad in Radiant
cube.scale.x = 1.5;
cube.scale.y = 1.5;
cube.scale.z = 1.5;
""",
 ("Radiant misst den Winkel über die Länge des Bogens: Eine volle Umdrehung ist 2π, also etwa 6,28. Eine halbe Drehung ist π, eine Vierteldrehung π/2.",
  ["Das Koordinatensystem: x nach rechts, y nach oben, z zur Kamera hin.",
   "`position`, `rotation` und `scale` sind Objekte mit `x`, `y` und `z`. `set()` setzt alle drei auf einmal.",
   "`MathUtils.degToRad(45)` rechnet Grad in Radiant um. Das ist lesbarer als `Math.PI / 4`.",
   "`scale.setScalar(1.5)` skaliert gleichmäßig in alle Richtungen.",
   "`lookAt()` dreht ein Objekt so, dass es auf einen Punkt zeigt. Das funktioniert auch mit Kameras."],
  "Grad direkt eintragen: `rotation.y = 90` sind über 14 volle Umdrehungen und ergeben eine scheinbar zufällige Ausrichtung. Drehungen immer in Radiant.",
  "`set()`, `setScalar()` und `degToRad()` sind kürzer und weniger fehleranfällig. Einzelne Achsen setzt du direkt, wenn sich nur eine ändert.",
  "Wie viel Radiant ist eine Vierteldrehung?",
  "π/2, also `Math.PI / 2`, etwa 1,57."),
 [("Object3D", D+"Object3D"), ("MathUtils", D+"MathUtils")],
 demo=demo("""const { scene } = mini(stage, { z: 5 });
scene.add(new THREE.AxesHelper(2));
const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
cube.position.set(1, 0.5, 0);
cube.rotation.y = THREE.MathUtils.degToRad(45);
cube.scale.setScalar(0.8);
scene.add(cube);
scene.rotation.set(0.35, -0.5, 0);"""),
 labels=("Mit Hilfsfunktionen", "Von Hand")),

C("Gruppen und Hierarchie",
  "Objekte lassen sich verschachteln. Kinder bewegen sich mit ihrem Elternobjekt mit.",
  """
const sun = new THREE.Mesh(new THREE.SphereGeometry(0.6), sunMaterial);
const orbit = new THREE.Group();
const earth = new THREE.Mesh(new THREE.SphereGeometry(0.25), earthMaterial);

earth.position.x = 2;       // Abstand relativ zur Gruppe
orbit.add(earth);
scene.add(sun, orbit);

// im Loop: nur die Gruppe drehen, die Erde kreist mit
orbit.rotation.y += delta;
""", None,
 ("Eine Gruppe ist ein Karussell: Setzt du ein Pferd zwei Meter vom Mittelpunkt entfernt darauf und drehst das Karussell, fährt das Pferd im Kreis, ohne dass du seine Bahn berechnen musst.",
  ["Jedes Object3D kann Kinder haben. `add()` hängt sie an.",
   "Position, Drehung und Größe eines Kindes gelten relativ zu seinem Elternobjekt.",
   "`Group` ist ein unsichtbares Object3D, das nur als Halter dient.",
   "Dreht sich die Gruppe, kreist alles darin um ihren Mittelpunkt. So entstehen Umlaufbahnen, Roboterarme oder Modelle mit beweglichen Teilen.",
   "`getWorldPosition()` liefert die Position eines Kindes in Weltkoordinaten, falls du sie brauchst."],
  "Ein Objekt per `add()` in eine skalierte Gruppe hängen und sich wundern, dass es plötzlich viel größer ist. Kinder erben `scale` vom Elternobjekt.",
  "Gruppen, sobald sich mehrere Objekte gemeinsam bewegen sollen. Die Bahn von Hand mit `Math.sin` und `Math.cos` zu berechnen geht auch, wird aber bei mehreren Ebenen schnell unübersichtlich.",
  "Wie lässt du zusätzlich einen Mond um die Erde kreisen?",
  "Eine zweite Gruppe an die Erde hängen, den Mond darin mit Abstand platzieren und diese Gruppe ebenfalls drehen."),
 [("Scene Graph (Manual)", M+"scenegraph"), ("Group", D+"Group")],
 demo=demo("""const { scene, onTick } = mini(stage, { z: 6 });
const sun = new THREE.Mesh(new THREE.SphereGeometry(0.6, 32, 16), new THREE.MeshBasicMaterial({ color: accent(stage) }));
const orbit = new THREE.Group();
const earth = new THREE.Mesh(new THREE.SphereGeometry(0.25, 24, 12), new THREE.MeshNormalMaterial());
earth.position.x = 2;
const moonOrbit = new THREE.Group();
const moon = new THREE.Mesh(new THREE.SphereGeometry(0.1, 16, 8), new THREE.MeshNormalMaterial());
moon.position.x = 0.5;
moonOrbit.add(moon); earth.add(moonOrbit); orbit.add(earth);
scene.add(sun, orbit);
scene.rotation.x = 0.4;
onTick((dt) => { orbit.rotation.y += dt * 0.8; moonOrbit.rotation.y += dt * 3; })""")),
]))

SECTIONS.append(("licht", "Licht und Oberflächen", "light", "Realistische Materialien brauchen Licht. Ohne Licht bleibt ein MeshStandardMaterial schwarz.", [
C("Materialien: Basic und Standard",
  "`MeshBasicMaterial` ignoriert Licht. `MeshStandardMaterial` reagiert physikalisch plausibel darauf.",
  """
const flat = new THREE.MeshBasicMaterial({ color: "#3b82f6" });

const shiny = new THREE.MeshStandardMaterial({
  color: "#3b82f6",
  roughness: 0.3,   // 0 = spiegelglatt, 1 = matt
  metalness: 0.0,   // 0 = Kunststoff, 1 = Metall
});
""", None,
 ("`MeshBasicMaterial` ist ein Aufkleber: überall gleich bunt, egal wie das Licht fällt. `MeshStandardMaterial` ist echte Farbe auf einem Gegenstand, die Glanzlichter und Schatten zeigt.",
  ["`MeshBasicMaterial` färbt jedes Pixel in derselben Farbe. Ohne Schattierung wirkt eine Kugel wie ein flacher Kreis.",
   "`MeshStandardMaterial` berechnet Helligkeit aus Lichtrichtung, Blickwinkel und Oberfläche (PBR, physikalisch basiertes Rendering).",
   "`roughness` steuert, wie scharf Glanzlichter sind. `metalness` lässt die Oberfläche die Umgebung spiegeln, statt eine eigene Farbe zu haben.",
   "`MeshPhysicalMaterial` erweitert das um Effekte wie Klarlack oder Glas. Es braucht dafür mehr Rechenleistung."],
  "`metalness: 1` ohne Umgebungsbild setzen. Metall spiegelt seine Umgebung, und ohne Umgebung bleibt es fast schwarz. Für Metall brauchst du eine `scene.environment`, z.B. aus `RoomEnvironment`.",
  "`MeshBasicMaterial` für Linien, Hilfsobjekte und bewusst flache Stile. `MeshStandardMaterial` als Standard für alles, was realistisch wirken soll.",
  "Warum bleibt ein Würfel mit `MeshStandardMaterial` schwarz?",
  "Weil kein Licht in der Szene ist. Ohne Licht gibt es nichts, was die Oberfläche zurückwerfen könnte."),
 [("Materials (Manual)", M+"materials"), ("MeshStandardMaterial", D+"MeshStandardMaterial")],
 demo=demo("""const { scene, onTick } = mini(stage, { z: 4 });
const col = accent(stage);
const a = new THREE.Mesh(new THREE.SphereGeometry(0.7, 48, 24), new THREE.MeshBasicMaterial({ color: col }));
const b = new THREE.Mesh(new THREE.SphereGeometry(0.7, 48, 24), new THREE.MeshStandardMaterial({ color: col, roughness: 0.3 }));
a.position.x = -0.9; b.position.x = 0.9;
scene.add(a, b, new THREE.AmbientLight(0xffffff, 0.4));
const light = new THREE.DirectionalLight(0xffffff, 2.5);
scene.add(light);
onTick((dt, t) => light.position.set(Math.cos(t) * 3, 2, Math.sin(t) * 3 + 1));""")),

C("Lichtarten",
  "Grundlicht für alles, gerichtetes Licht wie Sonne, Punktlicht wie Glühbirne. Meist kombiniert man zwei bis drei.",
  """
// sanftes Grundlicht, Himmel oben, Boden unten
scene.add(new THREE.HemisphereLight("#ffffff", "#445566", 1));

// Sonne: parallele Strahlen aus einer Richtung
const sun = new THREE.DirectionalLight("#ffffff", 2);
sun.position.set(3, 4, 2);
scene.add(sun);

// Glühbirne: strahlt in alle Richtungen, wird schwächer mit Abstand
const bulb = new THREE.PointLight("#ff8844", 8, 0, 2);
bulb.position.set(-1, 1, 1);
scene.add(bulb);
""", None,
 ("Ein Fotostudio: Das Grundlicht hellt alles gleichmäßig auf, damit keine Seite ganz schwarz ist. Das Hauptlicht kommt von schräg oben und erzeugt Form. Ein farbiges Effektlicht setzt Akzente.",
  ["`AmbientLight` hellt alles gleich stark auf und hat keine Richtung. `HemisphereLight` mischt eine Himmels- und eine Bodenfarbe und wirkt dadurch natürlicher.",
   "`DirectionalLight` hat parallele Strahlen, wie die Sonne. Nur die Richtung zählt, nicht der Abstand.",
   "`PointLight` strahlt von einem Punkt in alle Richtungen und wird mit Abstand schwächer (`decay` 2 entspricht der Physik).",
   "`SpotLight` ist ein Kegel, z.B. für Taschenlampen oder Bühnenlicht.",
   "Seit Version r155 rechnet Three.js Lichtstärken physikalisch. Werte aus alten Tutorials wirken deshalb oft zu dunkel oder zu hell."],
  "Nur ein `AmbientLight` verwenden. Dann ist jede Fläche gleich hell, und 3D-Objekte wirken flach wie Scherenschnitte. Form entsteht erst durch Licht aus einer Richtung.",
  "Ein weiches Grundlicht plus ein gerichtetes Hauptlicht ist der übliche Start. Für realistische Szenen ersetzt eine Umgebungs-Map (`scene.environment`) oft das Grundlicht.",
  "Welches Licht nimmst du für Tageslicht im Freien?",
  "Ein `DirectionalLight` als Sonne plus ein `HemisphereLight` für das Himmelslicht."),
 [("Lights (Manual)", M+"lights"), ("DirectionalLight", D+"DirectionalLight"), ("PointLight", D+"PointLight")],
 demo=demo("""const { scene, onTick } = mini(stage, { z: 4.5 });
const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.7, 0.25, 160, 24), new THREE.MeshStandardMaterial({ color: "#d9dde6", roughness: 0.4 }));
scene.add(knot);
scene.add(new THREE.HemisphereLight("#ffffff", "#445566", 0.6));
const sun = new THREE.DirectionalLight("#ffffff", 1.6); sun.position.set(3, 4, 2); scene.add(sun);
const bulb = new THREE.PointLight("#ff6a2a", 12, 0, 2); scene.add(bulb);
bulb.add(new THREE.Mesh(new THREE.SphereGeometry(0.05), new THREE.MeshBasicMaterial({ color: "#ff6a2a" })));
onTick((dt, t) => { knot.rotation.y += dt * 0.4; bulb.position.set(Math.cos(t * 1.5) * 1.6, Math.sin(t) * 0.8, Math.sin(t * 1.5) * 1.6); });""")),

C("Schatten",
  "Schatten sind standardmäßig aus. Drei Stellen müssen sie erlauben: Renderer, Licht und jedes beteiligte Objekt.",
  """
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;   // seit r182 weich

sun.castShadow = true;
sun.shadow.mapSize.set(1024, 1024);

cube.castShadow = true;       // wirft Schatten
floor.receiveShadow = true;   // fängt Schatten auf
""", None,
 ("Schatten in Three.js sind wie ein zweites Foto aus der Sicht der Lampe: Alles, was die Lampe sehen kann, ist beleuchtet. Was dahinter liegt, liegt im Schatten. Dieses Foto ist die Shadow Map.",
  ["`renderer.shadowMap.enabled` schaltet Schatten global ein.",
   "`castShadow` beim Licht: Dieses Licht berechnet Schatten. Nicht alle Lichter müssen das, und jedes kostet Leistung.",
   "`castShadow` beim Objekt: Es wirft Schatten. `receiveShadow`: Auf ihm erscheinen Schatten anderer Objekte.",
   "`shadow.mapSize` ist die Auflösung der Shadow Map. Größer bedeutet schärfer, aber teurer.",
   "Seit Version r182 ist `PCFShadowMap` standardmäßig weich, `PCFSoftShadowMap` gilt als veraltet."],
  "Eine der drei Stellen vergessen, meist `receiveShadow` am Boden. Dann wird der Schatten zwar berechnet, aber nirgends angezeigt. Bei großen Szenen ist außerdem der Bereich der Schattenkamera (`sun.shadow.camera`) oft zu klein, und Schatten werden abgeschnitten.",
  "Echte Schatten für bewegte Objekte. Für statische Szenen sind vorberechnete Schatten aus Blender (Baking) viel günstiger.",
  "Wie prüfst du, welchen Bereich die Schattenkamera abdeckt?",
  "Mit `scene.add(new THREE.CameraHelper(sun.shadow.camera))`. Der Helfer zeigt den Bereich als Drahtgitter."),
 [("Shadows (Manual)", M+"shadows"), ("DirectionalLightShadow", D+"DirectionalLightShadow")],
 demo=demo("""const { scene, camera, renderer, onTick } = mini(stage, { z: 5 });
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;
camera.position.set(0, 2.2, 4.5); camera.lookAt(0, 0, 0);
const floor = new THREE.Mesh(new THREE.PlaneGeometry(8, 8), new THREE.MeshStandardMaterial({ color: "#c9ced8" }));
floor.rotation.x = -Math.PI / 2; floor.position.y = -0.6; floor.receiveShadow = true;
const cube = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.8, 0.8), new THREE.MeshStandardMaterial({ color: accent(stage) }));
cube.castShadow = true;
scene.add(floor, cube, new THREE.HemisphereLight("#ffffff", "#667788", 0.8));
const sun = new THREE.DirectionalLight("#ffffff", 2); sun.position.set(2, 4, 1); sun.castShadow = true; sun.shadow.mapSize.set(1024, 1024); scene.add(sun);
onTick((dt, t) => { cube.rotation.y += dt; cube.position.y = Math.abs(Math.sin(t * 2)) * 0.6; });""")),

C("Farben und Texturen: `colorSpace`",
  "Farbige Bildtexturen müssen als sRGB markiert werden, sonst wirken sie blass. Datentexturen wie Normal Maps dagegen nicht.",
  """
const texture = new THREE.TextureLoader().load("holz.jpg");
texture.colorSpace = THREE.SRGBColorSpace;   // Farbbild

const material = new THREE.MeshStandardMaterial({
  map: texture,              // sRGB
  normalMap: normalTexture,  // bleibt linear: Daten, keine Farbe
});
""", None,
 ("Ein Bild ist wie ein Rezept in einer fremden Maßeinheit. Sagst du Three.js nicht, dass die Zahlen in sRGB angegeben sind, rechnet es mit den falschen Mengen, und das Ergebnis schmeckt fad: Die Farben wirken ausgewaschen.",
  ["Bilddateien wie JPG und PNG speichern Farben in sRGB, einem Farbraum, der an das menschliche Sehen angepasst ist.",
   "Three.js rechnet Licht intern linear und wandelt am Ende zurück in sRGB (`renderer.outputColorSpace` ist standardmäßig sRGB).",
   "`texture.colorSpace = THREE.SRGBColorSpace` sagt: Diese Textur ist ein Farbbild und muss erst umgerechnet werden.",
   "Normal-, Roughness- oder Metalness-Maps enthalten Messwerte, keine Farben. Sie bleiben ohne Angabe linear.",
   "Der GLTFLoader setzt den Farbraum automatisch richtig. Von Hand musst du ihn nur bei selbst geladenen Texturen setzen."],
  "Den Farbraum bei Farbtexturen vergessen: Holz, Fotos und Logos wirken blass und kontrastarm. Oder umgekehrt eine Normal Map als sRGB markieren, dann stimmt die Beleuchtung nicht mehr.",
  "Farbbilder (`map`, `emissiveMap`) als sRGB, alles andere linear lassen. Farben, die du im Code als Hex oder CSS-String angibst, wandelt Three.js automatisch um.",
  "Muss eine `roughnessMap` auf `SRGBColorSpace` gesetzt werden?",
  "Nein. Sie enthält Messwerte für die Rauheit, keine Farben, und bleibt linear."),
 [("Color Management (Manual)", M+"color-management"), ("Textures (Manual)", M+"textures"), ("CanvasTexture", D+"CanvasTexture")],
 demo=demo("""const { scene, onTick } = mini(stage, { z: 3.6 });
function checker() {
  const c = document.createElement("canvas"); c.width = c.height = 128;
  const g = c.getContext("2d");
  for (let y = 0; y < 8; y++) for (let x = 0; x < 8; x++) { g.fillStyle = (x + y) % 2 ? "#e24a33" : "#f2c14e"; g.fillRect(x * 16, y * 16, 16, 16); }
  return new THREE.CanvasTexture(c);
}
const wrong = checker();
const right = checker(); right.colorSpace = THREE.SRGBColorSpace;
const a = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshBasicMaterial({ map: wrong }));
const b = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshBasicMaterial({ map: right }));
a.position.x = -0.8; b.position.x = 0.8;
scene.add(a, b);
onTick((dt) => { a.rotation.y += dt * 0.5; b.rotation.y += dt * 0.5; });
stage.insertAdjacentHTML("beforeend", '<span class="note" style="background:var(--surface);padding:2px 6px;border-radius:4px">links: ohne colorSpace · rechts: SRGBColorSpace</span>');""")),
]))

SECTIONS.append(("interaktion", "Interaktion", "input", "Kamera steuern und Objekte anklicken.", [
C("Kamera steuern: OrbitControls",
  "Mit Maus oder Finger um ein Objekt kreisen, zoomen und verschieben. Ein Addon, das in fast jedem Projekt steckt.",
  """
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;     // weiches Ausrollen
controls.minDistance = 2;
controls.maxDistance = 10;

renderer.setAnimationLoop(() => {
  controls.update();               // nötig für enableDamping
  renderer.render(scene, camera);
});
""", None,
 ("OrbitControls machen die Kamera zu einem Satelliten: Sie kreist auf einer Kugelbahn um einen Mittelpunkt, kann näher heranfliegen oder weiter weg, schaut aber immer auf die Mitte.",
  ["Addons wie OrbitControls liegen nicht im Kern von Three.js, sondern unter `three/addons/`. Mit Vite oder einer Import Map ist dieser Pfad direkt verfügbar.",
   "Der zweite Parameter ist das Element, das Maus- und Touch-Events empfängt, meist das Canvas.",
   "Linke Maustaste dreht, Mausrad zoomt, rechte Maustaste verschiebt. Auf Touch-Geräten geht dasselbe mit einem und zwei Fingern.",
   "`enableDamping` lässt die Bewegung nach dem Loslassen auslaufen. Dafür muss `controls.update()` in jedem Bild aufgerufen werden.",
   "`controls.target` ist der Punkt, um den die Kamera kreist. Standard ist der Ursprung."],
  "`enableDamping` einschalten, aber `controls.update()` nicht im Loop aufrufen. Dann reagiert die Steuerung nur ruckartig oder gar nicht. Und: `controls.dispose()` beim Aufräumen vergessen, dann bleiben die Event-Listener am Canvas hängen.",
  "OrbitControls für Produktansichten, Modelle und Szenen zum Erkunden. Für eine feste Kamerafahrt, z.B. beim Scrollen, steuerst du die Kamera besser per GSAP.",
  "Wie verhinderst du, dass man unter den Boden schauen kann?",
  "Mit `controls.maxPolarAngle = Math.PI / 2`. Dann kann die Kamera höchstens bis zur Horizontalen hinunterschwenken."),
 [("OrbitControls", D+"OrbitControls"), ("Installation und Addons (Manual)", M+"installation")],
 demo=demo("""const { scene, camera, renderer, onTick, track } = mini(stage, { z: 4 });
const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.7, 0.25, 160, 24), new THREE.MeshNormalMaterial());
scene.add(knot);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true; controls.minDistance = 2; controls.maxDistance = 10;
track(controls);
onTick(() => controls.update());
stage.insertAdjacentHTML("beforeend", '<span class="note">Ziehen zum Drehen, Mausrad zum Zoomen</span>');""")),

C("Objekte anklicken: Raycaster",
  "Herausfinden, welches Objekt unter dem Mauszeiger liegt, z.B. um es auszuwählen.",
  """
const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();

renderer.domElement.addEventListener("click", (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

  raycaster.setFromCamera(pointer, camera);
  const hits = raycaster.intersectObjects(clickables);
  if (hits.length) hits[0].object.material.color.set("#e24a33");
});
""", None,
 ("Ein Raycaster ist ein Laserpointer: Vom Auge der Kamera aus wird ein Strahl durch den angeklickten Bildpunkt in die Szene geschossen. Das erste Objekt, das er trifft, ist das angeklickte.",
  ["Die Mausposition wird in Koordinaten von -1 bis 1 umgerechnet (Normalized Device Coordinates). Links ist -1, rechts 1, unten -1, oben 1.",
   "Darum das Minus bei y: Im Browser zählt y nach unten, in Three.js nach oben.",
   "`setFromCamera` erzeugt den Strahl von der Kamera durch diesen Punkt.",
   "`intersectObjects` liefert alle Treffer, sortiert nach Entfernung. `hits[0]` ist das vorderste Objekt.",
   "Jeder Treffer enthält u.a. `object`, `point` (Treffpunkt im Raum) und `distance`."],
  "Mit `window.innerWidth` rechnen, obwohl das Canvas nur einen Teil der Seite einnimmt. Dann sind alle Klicks verschoben. Immer `getBoundingClientRect()` des Canvas verwenden. Ebenfalls häufig: Alle Objekte teilen ein Material, und beim Einfärben eines Treffers ändern sich alle.",
  "Den Raycaster nur bei Klicks oder Mausbewegung ausführen, nicht in jedem Bild. Bei sehr vielen Objekten nur die anklickbaren in `intersectObjects` übergeben.",
  "Wie zeigst du einen Hover-Effekt statt eines Klicks?",
  "Den Strahl im `pointermove`-Event berechnen, das getroffene Objekt merken und hervorheben. Beim Verlassen die Hervorhebung wieder zurücksetzen."),
 [("Picking (Manual)", M+"picking"), ("Raycaster", D+"Raycaster")],
 demo=demo("""const { scene, camera, renderer, track } = mini(stage, { z: 5 });
scene.add(new THREE.HemisphereLight("#ffffff", "#556677", 1.2));
const sun = new THREE.DirectionalLight("#ffffff", 1.5); sun.position.set(2, 3, 4); scene.add(sun);
const clickables = [-1.6, 0, 1.6].map(x => { const m = new THREE.Mesh(new THREE.SphereGeometry(0.6, 32, 16), new THREE.MeshStandardMaterial({ color: "#c9ced8" })); m.position.x = x; scene.add(m); return m; });
const raycaster = new THREE.Raycaster(), pointer = new THREE.Vector2();
const onClick = (event) => {
  const rect = renderer.domElement.getBoundingClientRect();
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
  raycaster.setFromCamera(pointer, camera);
  const hits = raycaster.intersectObjects(clickables);
  if (hits.length) { const c = hits[0].object.material.color; c.set(c.getHexString() === "c9ced8" ? accent(stage) : "#c9ced8"); }
};
renderer.domElement.addEventListener("click", onClick);
track({ dispose: () => renderer.domElement.removeEventListener("click", onClick) });
stage.insertAdjacentHTML("beforeend", '<span class="note">Kugeln anklicken</span>');""")),
]))

SECTIONS.append(("animation", "Modelle und Animation", "assets", "Echte Modelle laden und Bewegung steuern.", [
C("3D-Modelle laden: GLTF",
  "GLTF bzw. GLB ist das Standardformat fürs Web, quasi das JPG für 3D. Blender exportiert es direkt.",
  """
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";

const loader = new GLTFLoader();
const gltf = await loader.loadAsync("/models/robot.glb");

scene.add(gltf.scene);

// enthaltene Animationen abspielen
const mixer = new THREE.AnimationMixer(gltf.scene);
mixer.clipAction(gltf.animations[0]).play();
// im Loop: mixer.update(delta);
""", None,
 ("Eine GLB-Datei ist ein Umzugskarton mit allem drin: Formen, Materialien, Texturen, Knochen und Animationen. Der Loader packt ihn aus und stellt alles fertig in die Szene.",
  ["`.gltf` ist ein JSON mit separaten Dateien für Texturen und Daten, `.glb` packt alles in eine einzige Binärdatei. Fürs Web ist `.glb` meist praktischer.",
   "`loadAsync` gibt ein Promise zurück und funktioniert mit `await`.",
   "`gltf.scene` ist eine Gruppe mit dem ganzen Modell, die du direkt in deine Szene hängst.",
   "Animationen aus Blender stecken in `gltf.animations`. Der `AnimationMixer` spielt sie ab und braucht in jedem Bild `mixer.update(delta)`.",
   "Große Modelle lassen sich mit Draco oder Meshopt komprimieren. Dafür gibt es passende Decoder für den Loader."],
  "Die Datei mit einem relativen Pfad laden, der im Build nicht mehr stimmt. In Vite gehören Modelle in den Ordner `public/` und werden mit `/models/…` geladen. Und: Riesige, unkomprimierte Modelle ausliefern. Ein 50-MB-Modell ist auf dem Handy eine Minute Ladezeit.",
  "GLB für alles, was aus einem 3D-Programm kommt. Eingebaute Geometrien nur für einfache Formen und Prototypen. Prüfen und optimieren kannst du Modelle vorab im Browser-Tool gltf.report.",
  "Warum gibt es zu dieser Karte keine Live-Demo?",
  "Weil die Spickzettel-Seite aus Sicherheitsgründen keine externen Dateien nachladen darf. Ein Modell müsste von einem fremden Server kommen. In deinem eigenen Projekt funktioniert der Code genau so."),
 [("Load a .GLTF (Manual)", M+"load-gltf"), ("GLTFLoader", D+"GLTFLoader"), ("AnimationMixer", D+"AnimationMixer"), ("gltf.report (EN)", "https://gltf.report/")]),

C("Animieren mit GSAP",
  "Kamerafahrten und Übergänge mit GSAP-Tweens statt mit eigener Rechnung im Render-Loop.",
  """
gsap.to(cube.position, { y: 1, duration: 1, ease: "back.out(2)" });
gsap.to(cube.rotation, { y: Math.PI * 2, duration: 2, ease: "power2.inOut" });

// Kamerafahrt
gsap.to(camera.position, {
  x: 3, z: 3, duration: 2,
  onUpdate: () => camera.lookAt(0, 0, 0),
});
""", """
let t = 0;
renderer.setAnimationLoop(() => {
  t = Math.min(t + timer.getDelta() / 1, 1);   // 0 bis 1 in 1 Sekunde
  const eased = 1 - Math.pow(1 - t, 3);         // ease-out von Hand
  cube.position.y = eased * 1;
  renderer.render(scene, camera);
});
""",
 ("GSAP kann jede Zahl in jedem Objekt animieren, nicht nur CSS. Für GSAP ist `cube.position` einfach ein Objekt mit den Zahlen `x`, `y` und `z`, und genau die schiebt es über die Zeit.",
  ["`gsap.to(cube.position, { y: 1 })` animiert die Eigenschaft `y` des Positionsobjekts.",
   "Für Drehungen animierst du `cube.rotation`, für Größe `cube.scale`.",
   "Die Render-Schleife läuft weiter wie gewohnt und zeichnet in jedem Bild den aktuellen Zwischenstand.",
   "`onUpdate` wird in jedem Animationsschritt aufgerufen. Bei Kamerafahrten hält `lookAt` den Blick auf das Ziel.",
   "Mit ScrollTrigger kombiniert entstehen so die typischen 3D-Scroll-Seiten."],
  "Die Kamera per GSAP bewegen, während OrbitControls aktiv sind. Die Controls überschreiben die Position im nächsten Bild wieder. Entweder die Controls während der Fahrt abschalten (`controls.enabled = false`) oder `controls.target` mit animieren.",
  "GSAP für Übergänge mit klarem Anfang und Ende. Dauerhafte Bewegungen wie ein rotierender Planet gehören in die Render-Schleife mit Delta-Zeit.",
  "Wie animierst du die Farbe eines Materials mit GSAP?",
  "Über die Zahlen des Farbobjekts, z.B. `gsap.to(material.color, { r: 1, g: 0.3, b: 0.2 })`. Die Werte liegen zwischen 0 und 1."),
 [("GSAP-Spickzettel", "https://claude.ai/artifact/DVpdoSZy1Zrmuy21bkjg4a"), ("gsap.to()", "https://gsap.com/docs/v3/GSAP/gsap.to()")],
 demo=demo("""const { scene, camera } = mini(stage, { z: 5 });
camera.position.set(0, 1, 5); camera.lookAt(0, 0, 0);
scene.add(new THREE.GridHelper(6, 12, 0x888888, 0xcccccc));
const cube = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.8, 0.8), new THREE.MeshNormalMaterial());
cube.position.y = 0.4; scene.add(cube);
const tl = gsap.timeline();
tl.to(cube.position, { y: 1.4, duration: 0.8, ease: "back.out(2)" })
  .to(cube.rotation, { y: Math.PI * 2, duration: 1.4, ease: "power2.inOut" }, "<")
  .to(camera.position, { x: 3.5, y: 2.5, z: 3.5, duration: 1.6, ease: "power2.inOut", onUpdate: () => camera.lookAt(0, 0.6, 0) }, "-=0.6")
  .to(cube.position, { y: 0.4, duration: 0.6, ease: "bounce.out" });
return () => tl.kill();"""),
 labels=("Mit GSAP", "Von Hand im Loop")),
]))

SECTIONS.append(("performance", "Performance und React", "perf", "Speicher freigeben, viele Objekte effizient zeichnen und Three.js in React einsetzen.", [
C("Aufräumen: `dispose()`",
  "Geometrien, Materialien und Texturen belegen Speicher auf der Grafikkarte. Der wird nicht automatisch freigegeben, wenn du ein Objekt entfernst.",
  """
function removeObject(obj) {
  scene.remove(obj);
  obj.traverse((child) => {
    child.geometry?.dispose();
    for (const mat of [].concat(child.material ?? [])) {
      for (const value of Object.values(mat)) {
        if (value?.isTexture) value.dispose();
      }
      mat.dispose();
    }
  });
}

// beim Verlassen der Seite / Unmount:
renderer.setAnimationLoop(null);
controls.dispose();
renderer.dispose();
""", None,
 ("Die Grafikkarte ist ein Lager mit begrenzten Regalen. `scene.remove()` nimmt nur das Etikett von der Liste, die Kiste bleibt im Regal stehen. Erst `dispose()` räumt sie wirklich aus.",
  ["Beim ersten Zeichnen lädt Three.js Geometrien und Texturen in den Grafikspeicher.",
   "`scene.remove(obj)` entfernt das Objekt nur aus der Szene. Die Daten auf der Grafikkarte bleiben.",
   "`geometry.dispose()`, `material.dispose()` und `texture.dispose()` geben den Speicher frei.",
   "`traverse` geht rekursiv durch alle Kinder, wichtig bei geladenen Modellen mit vielen Teilen.",
   "Seit Version r186 haben auch Object3D-Objekte selbst eine `dispose()`-Methode. Eigene Klassen, die davon erben, müssen dann `super.dispose()` aufrufen."],
  "In einer Single-Page-App zwischen Seiten wechseln, ohne aufzuräumen. Jeder Besuch der 3D-Seite legt neue Daten auf die Grafikkarte, bis der Browser langsam wird oder den WebGL-Kontext verliert.",
  "Immer aufräumen, wenn Objekte dauerhaft verschwinden oder eine Komponente unmountet. Mit `renderer.info.memory` siehst du, wie viele Geometrien und Texturen gerade belegt sind.",
  "Wie prüfst du, ob dein Aufräumen funktioniert?",
  "`console.log(renderer.info.memory)` vor und nach dem Entfernen. Die Zahlen für `geometries` und `textures` müssen sinken."),
 [("Cleanup (Manual)", M+"cleanup"), ("WebGLRenderer.info", D+"WebGLRenderer")]),

C("Viele Objekte: `InstancedMesh`",
  "Tausende gleiche Objekte in einem einzigen Zeichenaufruf statt tausend einzelnen.",
  """
const count = 1000;
const mesh = new THREE.InstancedMesh(geometry, material, count);
const dummy = new THREE.Object3D();

for (let i = 0; i < count; i++) {
  dummy.position.set(rand(), rand(), rand());
  dummy.rotation.set(rand(), rand(), 0);
  dummy.updateMatrix();
  mesh.setMatrixAt(i, dummy.matrix);
}
mesh.instanceMatrix.needsUpdate = true;
scene.add(mesh);
""", """
for (let i = 0; i < 1000; i++) {
  const cube = new THREE.Mesh(geometry, material);
  cube.position.set(rand(), rand(), rand());
  cube.rotation.set(rand(), rand(), 0);
  scene.add(cube);
}
// 1000 Objekte = 1000 Zeichenaufrufe pro Bild
""",
 ("Einzelne Meshes sind wie 1000 Briefe, die du einzeln zur Post bringst. `InstancedMesh` ist ein Paket mit 1000 Adressaufklebern: ein Weg, und die Grafikkarte verteilt den Inhalt selbst.",
  ["Jedes Mesh erzeugt pro Bild einen eigenen Zeichenaufruf (Draw Call). Ab einigen hundert wird das zum Engpass.",
   "`InstancedMesh` zeichnet dieselbe Geometrie mit demselben Material beliebig oft in einem Aufruf.",
   "Jede Instanz hat nur eine eigene Transformationsmatrix. Das `dummy`-Objekt hilft, sie bequem aus Position, Drehung und Größe zu berechnen.",
   "Nach Änderungen muss `instanceMatrix.needsUpdate = true` gesetzt werden, sonst sieht die Grafikkarte die neuen Werte nicht.",
   "Mit `setColorAt` bekommt jede Instanz eine eigene Farbe."],
  "`needsUpdate` vergessen. Dann bleiben alle Instanzen im Ursprung übereinander liegen, und man sieht nur einen einzigen Würfel.",
  "`InstancedMesh` für Partikel, Bäume, Gras, Sterne und alles, was oft vorkommt. Einzelne Meshes, solange es um wenige Objekte geht, die sich unterschiedlich verhalten. `renderer.info.render.calls` zeigt die Zahl der Zeichenaufrufe.",
  "Kann eine Instanz eine andere Geometrie haben als die anderen?",
  "Nein. Alle Instanzen teilen Geometrie und Material. Für verschiedene Formen brauchst du mehrere `InstancedMesh` oder `BatchedMesh`."),
 [("InstancedMesh", D+"InstancedMesh"), ("Optimize lots of objects (Manual)", M+"optimize-lots-of-objects")],
 demo=demo("""const { scene, renderer, onTick } = mini(stage, { z: 9 });
scene.add(new THREE.HemisphereLight("#ffffff", "#445566", 1.4));
const count = 1500;
const mesh = new THREE.InstancedMesh(new THREE.BoxGeometry(0.15, 0.15, 0.15), new THREE.MeshStandardMaterial(), count);
const dummy = new THREE.Object3D(), color = new THREE.Color();
const r = () => (Math.random() - 0.5) * 8;
for (let i = 0; i < count; i++) {
  dummy.position.set(r(), r() * 0.6, r()); dummy.rotation.set(r(), r(), 0); dummy.updateMatrix();
  mesh.setMatrixAt(i, dummy.matrix);
  mesh.setColorAt(i, color.setHSL(0.55 + Math.random() * 0.15, 0.6, 0.55));
}
mesh.instanceMatrix.needsUpdate = true;
scene.add(mesh);
const info = document.createElement("span"); info.className = "note"; stage.appendChild(info);
onTick((dt) => { mesh.rotation.y += dt * 0.2; info.textContent = count + " Würfel · " + renderer.info.render.calls + " Zeichenaufruf"; });"""),
 labels=("InstancedMesh", "Einzelne Meshes")),

C("Three.js in React: React Three Fiber",
  "React Three Fiber beschreibt Szenen als JSX-Komponenten. Darunter läuft ganz normales Three.js.",
  """
import { Canvas, useFrame } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import { useRef } from "react";

function Box() {
  const ref = useRef();
  useFrame((state, delta) => { ref.current.rotation.y += delta; });
  return (
    <mesh ref={ref}>
      <boxGeometry args={[1, 1, 1]} />
      <meshStandardMaterial color="hotpink" />
    </mesh>
  );
}

export default function App() {
  return (
    <Canvas camera={{ position: [0, 0, 4] }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[3, 3, 3]} />
      <Box />
      <OrbitControls />
    </Canvas>
  );
}
""", """
import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(50, innerWidth / innerHeight, 0.1, 100);
camera.position.z = 4;
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(innerWidth, innerHeight);
document.body.appendChild(renderer.domElement);

scene.add(new THREE.AmbientLight(0xffffff, 0.5));
const light = new THREE.DirectionalLight(0xffffff);
light.position.set(3, 3, 3);
scene.add(light);

const box = new THREE.Mesh(
  new THREE.BoxGeometry(1, 1, 1),
  new THREE.MeshStandardMaterial({ color: "hotpink" })
);
scene.add(box);
const controls = new OrbitControls(camera, renderer.domElement);

const timer = new THREE.Timer();
renderer.setAnimationLoop((t) => {
  timer.update(t);
  box.rotation.y += timer.getDelta();
  renderer.render(scene, camera);
});
// + Resize und Aufräumen von Hand
""",
 ("React Three Fiber ist eine Übersetzung: Jedes JSX-Element entspricht einer Three.js-Klasse. `<mesh>` wird zu `new THREE.Mesh()`, `<boxGeometry args={[1, 1, 1]}>` zu `new THREE.BoxGeometry(1, 1, 1)`.",
  ["`<Canvas>` erzeugt Szene, Kamera, Renderer und Render-Schleife und kümmert sich um Resize und Pixeldichte.",
   "Elementnamen sind die Klassennamen in camelCase. `args` sind die Konstruktor-Parameter, andere Props werden als Eigenschaften gesetzt, z.B. `position={[1, 0, 0]}`.",
   "`useFrame` läuft in jedem Bild und bekommt die Delta-Zeit. Dort gehören laufende Animationen hin, nicht in `useState`, denn ein Re-Render pro Bild wäre viel zu langsam.",
   "Beim Unmount räumt Fiber Geometrien und Materialien automatisch auf.",
   "Die Bibliothek `@react-three/drei` liefert fertige Helfer wie OrbitControls, Umgebungslicht oder einen GLTF-Hook."],
  "Animationen über React-State steuern, z.B. `setRotation(r => r + 0.01)` in jedem Bild. Das löst 60 Re-Renders pro Sekunde aus. Werte im `useFrame` direkt über `ref.current` ändern.",
  "React Three Fiber, wenn dein Projekt ohnehin React ist und die 3D-Szene mit dem Rest der App zusammenspielen soll. Vanilla Three.js für eigenständige Szenen und um zu verstehen, was darunter passiert. Die Konzepte dieses Zettels gelten in beiden Fällen.",
  "Wie schreibst du `new THREE.SphereGeometry(1, 32, 16)` in React Three Fiber?",
  "`<sphereGeometry args={[1, 32, 16]} />` innerhalb eines `<mesh>`."),
 [("React Three Fiber (EN)", "https://r3f.docs.pmnd.rs/getting-started/introduction"), ("drei (EN)", "https://drei.docs.pmnd.rs/")],
 labels=("React Three Fiber", "Vanilla Three.js")),
]))
