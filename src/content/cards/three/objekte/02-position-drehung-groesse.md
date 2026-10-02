---
title: "Position, Drehung, Größe"
description: "Jedes Objekt hat `position`, `rotation` und `scale`. Drehungen werden in Radiant angegeben, nicht in Grad."
labels:
  - "Mit Hilfsfunktionen"
  - "Von Hand"
code:
  short: |-
    cube.position.set(1, 0.5, 0);
    cube.rotation.y = THREE.MathUtils.degToRad(45);
    cube.scale.setScalar(1.5);

    cube.lookAt(0, 0, 0);   // zum Ursprung ausrichten
  long: |-
    cube.position.x = 1;
    cube.position.y = 0.5;
    cube.position.z = 0;
    cube.rotation.y = 45 * Math.PI / 180;   // Grad in Radiant
    cube.scale.x = 1.5;
    cube.scale.y = 1.5;
    cube.scale.z = 1.5;
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene } = mini(stage, { z: 5 });
    scene.add(new THREE.AxesHelper(2));
    const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
    cube.position.set(1, 0.5, 0);
    cube.rotation.y = THREE.MathUtils.degToRad(45);
    cube.scale.setScalar(0.8);
    scene.add(cube);
    scene.rotation.set(0.35, -0.5, 0);
explain:
  picture: "Radiant misst den Winkel über die Länge des Bogens: Eine volle Umdrehung ist 2π, also etwa 6,28. Eine halbe Drehung ist π, eine Vierteldrehung π/2."
  steps:
    - "Das Koordinatensystem: x nach rechts, y nach oben, z zur Kamera hin."
    - "`position`, `rotation` und `scale` sind Objekte mit `x`, `y` und `z`. `set()` setzt alle drei auf einmal."
    - "`MathUtils.degToRad(45)` rechnet Grad in Radiant um. Das ist lesbarer als `Math.PI / 4`."
    - "`scale.setScalar(1.5)` skaliert gleichmäßig in alle Richtungen."
    - "`lookAt()` dreht ein Objekt so, dass es auf einen Punkt zeigt. Das funktioniert auch mit Kameras."
  mistake: "Grad direkt eintragen: `rotation.y = 90` sind über 14 volle Umdrehungen und ergeben eine scheinbar zufällige Ausrichtung. Drehungen immer in Radiant."
  when: "`set()`, `setScalar()` und `degToRad()` sind kürzer und weniger fehleranfällig. Einzelne Achsen setzt du direkt, wenn sich nur eine ändert."
  question: "Wie viel Radiant ist eine Vierteldrehung?"
  answer: "π/2, also `Math.PI / 2`, etwa 1,57."
links:
  - text: "Object3D"
    url: "https://threejs.org/docs/#Object3D"
  - text: "MathUtils"
    url: "https://threejs.org/docs/#MathUtils"
---
