---
title: "Szene, Kamera, Renderer"
description: "Die drei Pflichtbausteine: eine Welt mit Objekten, ein Blickwinkel und etwas, das das Bild auf ein `<canvas>` zeichnet."
code:
  short: |-
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
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, camera } = mini(stage);
    const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
    cube.rotation.set(0.5, 0.6, 0);
    scene.add(cube);
explain:
  picture: "Three.js funktioniert wie ein Filmset: Die Szene ist das Studio mit allen Requisiten, die Kamera bestimmt den Bildausschnitt, und der Renderer ist der Kameramann, der auf Knopfdruck ein Bild belichtet."
  steps:
    - "`Scene` ist der Container für alles, was zu sehen sein soll: Objekte, Lichter, Hintergrund."
    - "`PerspectiveCamera(fov, aspect, near, far)`: Blickwinkel in Grad, Seitenverhältnis, und der Bereich, in dem Dinge gezeichnet werden. Was näher als 0.1 oder weiter als 100 ist, wird abgeschnitten."
    - "Die Kamera steht anfangs im Ursprung `(0, 0, 0)` und schaut in Richtung minus z. Darum wird sie mit `position.z = 4` nach hinten gesetzt, sonst steckt sie im Würfel."
    - "`WebGLRenderer` erzeugt ein `<canvas>`, das du mit `appendChild` in die Seite einhängst."
    - "`renderer.render(scene, camera)` zeichnet genau ein Bild. Für Bewegung brauchst du eine Schleife, siehe nächste Karte."
  mistake: "Einen schwarzen Bildschirm bekommen und nicht wissen warum. Die häufigsten Ursachen: Kamera steht im Objekt, Objekt liegt außerhalb von `near` und `far`, es fehlt Licht für ein `MeshStandardMaterial`, oder `render()` wird nie aufgerufen."
  when: "`MeshNormalMaterial` ist zum Lernen ideal, weil es ohne Licht funktioniert und die Flächen nach ihrer Ausrichtung einfärbt. So siehst du sofort, ob Geometrie und Kamera stimmen."
  question: "Warum ist der Würfel nicht zu sehen, wenn `camera.position.z` 0 bleibt?"
  answer: "Weil die Kamera dann genau in der Mitte des Würfels steht. Von innen sind die Flächen unsichtbar, denn standardmäßig wird nur die Außenseite gezeichnet."
links:
  - text: "Grundlagen (Manual)"
    url: "https://threejs.org/manual/#en/fundamentals"
  - text: "PerspectiveCamera"
    url: "https://threejs.org/docs/#PerspectiveCamera"
  - text: "WebGLRenderer"
    url: "https://threejs.org/docs/#WebGLRenderer"
---
