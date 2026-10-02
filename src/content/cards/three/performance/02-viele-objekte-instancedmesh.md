---
title: "Viele Objekte: `InstancedMesh`"
description: "Tausende gleiche Objekte in einem einzigen Zeichenaufruf statt tausend einzelnen."
labels:
  - "InstancedMesh"
  - "Einzelne Meshes"
code:
  short: |-
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
  long: |-
    for (let i = 0; i < 1000; i++) {
      const cube = new THREE.Mesh(geometry, material);
      cube.position.set(rand(), rand(), rand());
      cube.rotation.set(rand(), rand(), 0);
      scene.add(cube);
    }
    // 1000 Objekte = 1000 Zeichenaufrufe pro Bild
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, renderer, onTick } = mini(stage, { z: 9 });
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
    onTick((dt) => { mesh.rotation.y += dt * 0.2; info.textContent = count + " Würfel · " + renderer.info.render.calls + " Zeichenaufruf"; });
explain:
  picture: "Einzelne Meshes sind wie 1000 Briefe, die du einzeln zur Post bringst. `InstancedMesh` ist ein Paket mit 1000 Adressaufklebern: ein Weg, und die Grafikkarte verteilt den Inhalt selbst."
  steps:
    - "Jedes Mesh erzeugt pro Bild einen eigenen Zeichenaufruf (Draw Call). Ab einigen hundert wird das zum Engpass."
    - "`InstancedMesh` zeichnet dieselbe Geometrie mit demselben Material beliebig oft in einem Aufruf."
    - "Jede Instanz hat nur eine eigene Transformationsmatrix. Das `dummy`-Objekt hilft, sie bequem aus Position, Drehung und Größe zu berechnen."
    - "Nach Änderungen muss `instanceMatrix.needsUpdate = true` gesetzt werden, sonst sieht die Grafikkarte die neuen Werte nicht."
    - "Mit `setColorAt` bekommt jede Instanz eine eigene Farbe."
  mistake: "`needsUpdate` vergessen. Dann bleiben alle Instanzen im Ursprung übereinander liegen, und man sieht nur einen einzigen Würfel."
  when: "`InstancedMesh` für Partikel, Bäume, Gras, Sterne und alles, was oft vorkommt. Einzelne Meshes, solange es um wenige Objekte geht, die sich unterschiedlich verhalten. `renderer.info.render.calls` zeigt die Zahl der Zeichenaufrufe."
  question: "Kann eine Instanz eine andere Geometrie haben als die anderen?"
  answer: "Nein. Alle Instanzen teilen Geometrie und Material. Für verschiedene Formen brauchst du mehrere `InstancedMesh` oder `BatchedMesh`."
links:
  - text: "InstancedMesh"
    url: "https://threejs.org/docs/#InstancedMesh"
  - text: "Optimize lots of objects (Manual)"
    url: "https://threejs.org/manual/#en/optimize-lots-of-objects"
---
