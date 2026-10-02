---
title: "Mesh = Geometrie + Material"
description: "Die Geometrie legt die Form fest, das Material das Aussehen. Erst zusammen ergeben sie ein sichtbares Objekt."
code:
  short: |-
    const geometry = new THREE.TorusKnotGeometry(0.6, 0.2, 128, 16);
    const material = new THREE.MeshNormalMaterial();
    const knot = new THREE.Mesh(geometry, material);
    scene.add(knot);

    // eingebaute Formen, u.a.:
    // BoxGeometry, SphereGeometry, PlaneGeometry,
    // CylinderGeometry, ConeGeometry, TorusGeometry
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage, { z: 5 });
    const mat = new THREE.MeshNormalMaterial();
    const shapes = [new THREE.BoxGeometry(0.9, 0.9, 0.9), new THREE.TorusKnotGeometry(0.4, 0.14, 128, 16), new THREE.SphereGeometry(0.55, 8, 6)]
      .map((g, i) => { const m = new THREE.Mesh(g, mat); m.position.x = (i - 1) * 1.6; scene.add(m); return m; });
    onTick((dt) => shapes.forEach(m => { m.rotation.x += dt * 0.6; m.rotation.y += dt; }));
explain:
  picture: "Die Geometrie ist das Drahtgestell einer Figur, das Material der Stoff, der darübergespannt wird. Dasselbe Gestell kann mit verschiedenen Stoffen bezogen werden, und derselbe Stoff passt auf verschiedene Gestelle."
  steps:
    - "Eine Geometrie besteht aus Eckpunkten (Vertices), die zu Dreiecken verbunden sind. Auch eine Kugel ist nur aus vielen Dreiecken zusammengesetzt."
    - "Die Zahlenparameter bestimmen Größe und Detailgrad. Bei `SphereGeometry(1, 32, 16)` sind 32 und 16 die Segmente: mehr Segmente, rundere Kugel, mehr Rechenaufwand."
    - "Ein Material beschreibt, wie die Oberfläche auf Licht reagiert, siehe Abschnitt Licht."
    - "Geometrie und Material lassen sich zwischen mehreren Meshes teilen. Das spart Speicher."
  mistake: "Für jeden von 100 gleichen Würfeln eine eigene Geometrie und ein eigenes Material erzeugen. Das kostet unnötig Speicher. Einmal erzeugen und an alle Meshes übergeben reicht, und bei sehr vielen Objekten ist `InstancedMesh` noch besser."
  when: "Eingebaute Geometrien für Prototypen und einfache Formen. Für echte Modelle exportierst du aus Blender und lädst sie als GLTF."
  question: "Was passiert mit einer Kugel, wenn du `SphereGeometry(1, 6, 4)` statt `(1, 32, 16)` nimmst?"
  answer: "Sie wird sichtbar eckig, weil sie nur aus wenigen Dreiecken besteht. Für Low-Poly-Stil ist das sogar gewollt."
links:
  - text: "Primitives (Manual)"
    url: "https://threejs.org/manual/#en/primitives"
  - text: "Mesh"
    url: "https://threejs.org/docs/#Mesh"
  - text: "BufferGeometry"
    url: "https://threejs.org/docs/#BufferGeometry"
---
