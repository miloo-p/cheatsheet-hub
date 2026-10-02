---
title: "Schatten"
description: "Schatten sind standardmäßig aus. Drei Stellen müssen sie erlauben: Renderer, Licht und jedes beteiligte Objekt."
code:
  short: |-
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;   // seit r182 weich

    sun.castShadow = true;
    sun.shadow.mapSize.set(1024, 1024);

    cube.castShadow = true;       // wirft Schatten
    floor.receiveShadow = true;   // fängt Schatten auf
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, camera, renderer, onTick } = mini(stage, { z: 5 });
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFShadowMap;
    camera.position.set(0, 2.2, 4.5); camera.lookAt(0, 0, 0);
    const floor = new THREE.Mesh(new THREE.PlaneGeometry(8, 8), new THREE.MeshStandardMaterial({ color: "#c9ced8" }));
    floor.rotation.x = -Math.PI / 2; floor.position.y = -0.6; floor.receiveShadow = true;
    const cube = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.8, 0.8), new THREE.MeshStandardMaterial({ color: accent(stage) }));
    cube.castShadow = true;
    scene.add(floor, cube, new THREE.HemisphereLight("#ffffff", "#667788", 0.8));
    const sun = new THREE.DirectionalLight("#ffffff", 2); sun.position.set(2, 4, 1); sun.castShadow = true; sun.shadow.mapSize.set(1024, 1024); scene.add(sun);
    onTick((dt, t) => { cube.rotation.y += dt; cube.position.y = Math.abs(Math.sin(t * 2)) * 0.6; });
explain:
  picture: "Schatten in Three.js sind wie ein zweites Foto aus der Sicht der Lampe: Alles, was die Lampe sehen kann, ist beleuchtet. Was dahinter liegt, liegt im Schatten. Dieses Foto ist die Shadow Map."
  steps:
    - "`renderer.shadowMap.enabled` schaltet Schatten global ein."
    - "`castShadow` beim Licht: Dieses Licht berechnet Schatten. Nicht alle Lichter müssen das, und jedes kostet Leistung."
    - "`castShadow` beim Objekt: Es wirft Schatten. `receiveShadow`: Auf ihm erscheinen Schatten anderer Objekte."
    - "`shadow.mapSize` ist die Auflösung der Shadow Map. Größer bedeutet schärfer, aber teurer."
    - "Seit Version r182 ist `PCFShadowMap` standardmäßig weich, `PCFSoftShadowMap` gilt als veraltet."
  mistake: "Eine der drei Stellen vergessen, meist `receiveShadow` am Boden. Dann wird der Schatten zwar berechnet, aber nirgends angezeigt. Bei großen Szenen ist außerdem der Bereich der Schattenkamera (`sun.shadow.camera`) oft zu klein, und Schatten werden abgeschnitten."
  when: "Echte Schatten für bewegte Objekte. Für statische Szenen sind vorberechnete Schatten aus Blender (Baking) viel günstiger."
  question: "Wie prüfst du, welchen Bereich die Schattenkamera abdeckt?"
  answer: "Mit `scene.add(new THREE.CameraHelper(sun.shadow.camera))`. Der Helfer zeigt den Bereich als Drahtgitter."
links:
  - text: "Shadows (Manual)"
    url: "https://threejs.org/manual/#en/shadows"
  - text: "DirectionalLightShadow"
    url: "https://threejs.org/docs/#DirectionalLightShadow"
---
