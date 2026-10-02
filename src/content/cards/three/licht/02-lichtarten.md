---
title: "Lichtarten"
description: "Grundlicht für alles, gerichtetes Licht wie Sonne, Punktlicht wie Glühbirne. Meist kombiniert man zwei bis drei."
code:
  short: |-
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
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage, { z: 4.5 });
    const knot = new THREE.Mesh(new THREE.TorusKnotGeometry(0.7, 0.25, 160, 24), new THREE.MeshStandardMaterial({ color: "#d9dde6", roughness: 0.4 }));
    scene.add(knot);
    scene.add(new THREE.HemisphereLight("#ffffff", "#445566", 0.6));
    const sun = new THREE.DirectionalLight("#ffffff", 1.6); sun.position.set(3, 4, 2); scene.add(sun);
    const bulb = new THREE.PointLight("#ff6a2a", 12, 0, 2); scene.add(bulb);
    bulb.add(new THREE.Mesh(new THREE.SphereGeometry(0.05), new THREE.MeshBasicMaterial({ color: "#ff6a2a" })));
    onTick((dt, t) => { knot.rotation.y += dt * 0.4; bulb.position.set(Math.cos(t * 1.5) * 1.6, Math.sin(t) * 0.8, Math.sin(t * 1.5) * 1.6); });
explain:
  picture: "Ein Fotostudio: Das Grundlicht hellt alles gleichmäßig auf, damit keine Seite ganz schwarz ist. Das Hauptlicht kommt von schräg oben und erzeugt Form. Ein farbiges Effektlicht setzt Akzente."
  steps:
    - "`AmbientLight` hellt alles gleich stark auf und hat keine Richtung. `HemisphereLight` mischt eine Himmels- und eine Bodenfarbe und wirkt dadurch natürlicher."
    - "`DirectionalLight` hat parallele Strahlen, wie die Sonne. Nur die Richtung zählt, nicht der Abstand."
    - "`PointLight` strahlt von einem Punkt in alle Richtungen und wird mit Abstand schwächer (`decay` 2 entspricht der Physik)."
    - "`SpotLight` ist ein Kegel, z.B. für Taschenlampen oder Bühnenlicht."
    - "Seit Version r155 rechnet Three.js Lichtstärken physikalisch. Werte aus alten Tutorials wirken deshalb oft zu dunkel oder zu hell."
  mistake: "Nur ein `AmbientLight` verwenden. Dann ist jede Fläche gleich hell, und 3D-Objekte wirken flach wie Scherenschnitte. Form entsteht erst durch Licht aus einer Richtung."
  when: "Ein weiches Grundlicht plus ein gerichtetes Hauptlicht ist der übliche Start. Für realistische Szenen ersetzt eine Umgebungs-Map (`scene.environment`) oft das Grundlicht."
  question: "Welches Licht nimmst du für Tageslicht im Freien?"
  answer: "Ein `DirectionalLight` als Sonne plus ein `HemisphereLight` für das Himmelslicht."
links:
  - text: "Lights (Manual)"
    url: "https://threejs.org/manual/#en/lights"
  - text: "DirectionalLight"
    url: "https://threejs.org/docs/#DirectionalLight"
  - text: "PointLight"
    url: "https://threejs.org/docs/#PointLight"
---
