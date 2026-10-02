---
title: "Gruppen und Hierarchie"
description: "Objekte lassen sich verschachteln. Kinder bewegen sich mit ihrem Elternobjekt mit."
code:
  short: |-
    const sun = new THREE.Mesh(new THREE.SphereGeometry(0.6), sunMaterial);
    const orbit = new THREE.Group();
    const earth = new THREE.Mesh(new THREE.SphereGeometry(0.25), earthMaterial);

    earth.position.x = 2;       // Abstand relativ zur Gruppe
    orbit.add(earth);
    scene.add(sun, orbit);

    // im Loop: nur die Gruppe drehen, die Erde kreist mit
    orbit.rotation.y += delta;
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage, { z: 6 });
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
    onTick((dt) => { orbit.rotation.y += dt * 0.8; moonOrbit.rotation.y += dt * 3; })
explain:
  picture: "Eine Gruppe ist ein Karussell: Setzt du ein Pferd zwei Meter vom Mittelpunkt entfernt darauf und drehst das Karussell, fährt das Pferd im Kreis, ohne dass du seine Bahn berechnen musst."
  steps:
    - "Jedes Object3D kann Kinder haben. `add()` hängt sie an."
    - "Position, Drehung und Größe eines Kindes gelten relativ zu seinem Elternobjekt."
    - "`Group` ist ein unsichtbares Object3D, das nur als Halter dient."
    - "Dreht sich die Gruppe, kreist alles darin um ihren Mittelpunkt. So entstehen Umlaufbahnen, Roboterarme oder Modelle mit beweglichen Teilen."
    - "`getWorldPosition()` liefert die Position eines Kindes in Weltkoordinaten, falls du sie brauchst."
  mistake: "Ein Objekt per `add()` in eine skalierte Gruppe hängen und sich wundern, dass es plötzlich viel größer ist. Kinder erben `scale` vom Elternobjekt."
  when: "Gruppen, sobald sich mehrere Objekte gemeinsam bewegen sollen. Die Bahn von Hand mit `Math.sin` und `Math.cos` zu berechnen geht auch, wird aber bei mehreren Ebenen schnell unübersichtlich."
  question: "Wie lässt du zusätzlich einen Mond um die Erde kreisen?"
  answer: "Eine zweite Gruppe an die Erde hängen, den Mond darin mit Abstand platzieren und diese Gruppe ebenfalls drehen."
links:
  - text: "Scene Graph (Manual)"
    url: "https://threejs.org/manual/#en/scenegraph"
  - text: "Group"
    url: "https://threejs.org/docs/#Group"
---
