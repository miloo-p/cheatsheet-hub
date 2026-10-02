---
title: "Kamera steuern: OrbitControls"
description: "Mit Maus oder Finger um ein Objekt kreisen, zoomen und verschieben. Ein Addon, das in fast jedem Projekt steckt."
code:
  short: |-
    import { OrbitControls } from "three/addons/controls/OrbitControls.js";

    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;     // weiches Ausrollen
    controls.minDistance = 2;
    controls.maxDistance = 10;

    renderer.setAnimationLoop(() => {
      controls.update();               // nötig für enableDamping
      renderer.render(scene, camera);
    });
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, camera, renderer, onTick, track } = mini(stage, { z: 4 });
    const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.7, 0.25, 160, 24), new THREE.MeshNormalMaterial());
    scene.add(knot);
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true; controls.minDistance = 2; controls.maxDistance = 10;
    track(controls);
    onTick(() => controls.update());
    stage.insertAdjacentHTML("beforeend", '<span class="note">Ziehen zum Drehen, Mausrad zum Zoomen</span>');
explain:
  picture: "OrbitControls machen die Kamera zu einem Satelliten: Sie kreist auf einer Kugelbahn um einen Mittelpunkt, kann näher heranfliegen oder weiter weg, schaut aber immer auf die Mitte."
  steps:
    - "Addons wie OrbitControls liegen nicht im Kern von Three.js, sondern unter `three/addons/`. Mit Vite oder einer Import Map ist dieser Pfad direkt verfügbar."
    - "Der zweite Parameter ist das Element, das Maus- und Touch-Events empfängt, meist das Canvas."
    - "Linke Maustaste dreht, Mausrad zoomt, rechte Maustaste verschiebt. Auf Touch-Geräten geht dasselbe mit einem und zwei Fingern."
    - "`enableDamping` lässt die Bewegung nach dem Loslassen auslaufen. Dafür muss `controls.update()` in jedem Bild aufgerufen werden."
    - "`controls.target` ist der Punkt, um den die Kamera kreist. Standard ist der Ursprung."
  mistake: "`enableDamping` einschalten, aber `controls.update()` nicht im Loop aufrufen. Dann reagiert die Steuerung nur ruckartig oder gar nicht. Und: `controls.dispose()` beim Aufräumen vergessen, dann bleiben die Event-Listener am Canvas hängen."
  when: "OrbitControls für Produktansichten, Modelle und Szenen zum Erkunden. Für eine feste Kamerafahrt, z.B. beim Scrollen, steuerst du die Kamera besser per GSAP."
  question: "Wie verhinderst du, dass man unter den Boden schauen kann?"
  answer: "Mit `controls.maxPolarAngle = Math.PI / 2`. Dann kann die Kamera höchstens bis zur Horizontalen hinunterschwenken."
links:
  - text: "OrbitControls"
    url: "https://threejs.org/docs/#OrbitControls"
  - text: "Installation und Addons (Manual)"
    url: "https://threejs.org/manual/#en/installation"
---
