---
title: "Farben und Texturen: `colorSpace`"
description: "Farbige Bildtexturen müssen als sRGB markiert werden, sonst wirken sie blass. Datentexturen wie Normal Maps dagegen nicht."
code:
  short: |-
    const texture = new THREE.TextureLoader().load("holz.jpg");
    texture.colorSpace = THREE.SRGBColorSpace;   // Farbbild

    const material = new THREE.MeshStandardMaterial({
      map: texture,              // sRGB
      normalMap: normalTexture,  // bleibt linear: Daten, keine Farbe
    });
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage, { z: 3.6 });
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
    stage.insertAdjacentHTML("beforeend", '<span class="note" style="background:var(--surface);padding:2px 6px;border-radius:4px">links: ohne colorSpace · rechts: SRGBColorSpace</span>');
explain:
  picture: "Ein Bild ist wie ein Rezept in einer fremden Maßeinheit. Sagst du Three.js nicht, dass die Zahlen in sRGB angegeben sind, rechnet es mit den falschen Mengen, und das Ergebnis schmeckt fad: Die Farben wirken ausgewaschen."
  steps:
    - "Bilddateien wie JPG und PNG speichern Farben in sRGB, einem Farbraum, der an das menschliche Sehen angepasst ist."
    - "Three.js rechnet Licht intern linear und wandelt am Ende zurück in sRGB (`renderer.outputColorSpace` ist standardmäßig sRGB)."
    - "`texture.colorSpace = THREE.SRGBColorSpace` sagt: Diese Textur ist ein Farbbild und muss erst umgerechnet werden."
    - "Normal-, Roughness- oder Metalness-Maps enthalten Messwerte, keine Farben. Sie bleiben ohne Angabe linear."
    - "Der GLTFLoader setzt den Farbraum automatisch richtig. Von Hand musst du ihn nur bei selbst geladenen Texturen setzen."
  mistake: "Den Farbraum bei Farbtexturen vergessen: Holz, Fotos und Logos wirken blass und kontrastarm. Oder umgekehrt eine Normal Map als sRGB markieren, dann stimmt die Beleuchtung nicht mehr."
  when: "Farbbilder (`map`, `emissiveMap`) als sRGB, alles andere linear lassen. Farben, die du im Code als Hex oder CSS-String angibst, wandelt Three.js automatisch um."
  question: "Muss eine `roughnessMap` auf `SRGBColorSpace` gesetzt werden?"
  answer: "Nein. Sie enthält Messwerte für die Rauheit, keine Farben, und bleibt linear."
links:
  - text: "Color Management (Manual)"
    url: "https://threejs.org/manual/#en/color-management"
  - text: "Textures (Manual)"
    url: "https://threejs.org/manual/#en/textures"
  - text: "CanvasTexture"
    url: "https://threejs.org/docs/#CanvasTexture"
---
