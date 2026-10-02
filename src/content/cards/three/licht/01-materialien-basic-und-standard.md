---
title: "Materialien: Basic und Standard"
description: "`MeshBasicMaterial` ignoriert Licht. `MeshStandardMaterial` reagiert physikalisch plausibel darauf."
code:
  short: |-
    const flat = new THREE.MeshBasicMaterial({ color: "#3b82f6" });

    const shiny = new THREE.MeshStandardMaterial({
      color: "#3b82f6",
      roughness: 0.3,   // 0 = spiegelglatt, 1 = matt
      metalness: 0.0,   // 0 = Kunststoff, 1 = Metall
    });
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage, { z: 4 });
    const col = accent(stage);
    const a = new THREE.Mesh(new THREE.SphereGeometry(0.7, 48, 24), new THREE.MeshBasicMaterial({ color: col }));
    const b = new THREE.Mesh(new THREE.SphereGeometry(0.7, 48, 24), new THREE.MeshStandardMaterial({ color: col, roughness: 0.3 }));
    a.position.x = -0.9; b.position.x = 0.9;
    scene.add(a, b, new THREE.AmbientLight(0xffffff, 0.4));
    const light = new THREE.DirectionalLight(0xffffff, 2.5);
    scene.add(light);
    onTick((dt, t) => light.position.set(Math.cos(t) * 3, 2, Math.sin(t) * 3 + 1));
explain:
  picture: "`MeshBasicMaterial` ist ein Aufkleber: überall gleich bunt, egal wie das Licht fällt. `MeshStandardMaterial` ist echte Farbe auf einem Gegenstand, die Glanzlichter und Schatten zeigt."
  steps:
    - "`MeshBasicMaterial` färbt jedes Pixel in derselben Farbe. Ohne Schattierung wirkt eine Kugel wie ein flacher Kreis."
    - "`MeshStandardMaterial` berechnet Helligkeit aus Lichtrichtung, Blickwinkel und Oberfläche (PBR, physikalisch basiertes Rendering)."
    - "`roughness` steuert, wie scharf Glanzlichter sind. `metalness` lässt die Oberfläche die Umgebung spiegeln, statt eine eigene Farbe zu haben."
    - "`MeshPhysicalMaterial` erweitert das um Effekte wie Klarlack oder Glas. Es braucht dafür mehr Rechenleistung."
  mistake: "`metalness: 1` ohne Umgebungsbild setzen. Metall spiegelt seine Umgebung, und ohne Umgebung bleibt es fast schwarz. Für Metall brauchst du eine `scene.environment`, z.B. aus `RoomEnvironment`."
  when: "`MeshBasicMaterial` für Linien, Hilfsobjekte und bewusst flache Stile. `MeshStandardMaterial` als Standard für alles, was realistisch wirken soll."
  question: "Warum bleibt ein Würfel mit `MeshStandardMaterial` schwarz?"
  answer: "Weil kein Licht in der Szene ist. Ohne Licht gibt es nichts, was die Oberfläche zurückwerfen könnte."
links:
  - text: "Materials (Manual)"
    url: "https://threejs.org/manual/#en/materials"
  - text: "MeshStandardMaterial"
    url: "https://threejs.org/docs/#MeshStandardMaterial"
---
