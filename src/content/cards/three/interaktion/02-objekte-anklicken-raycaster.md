---
title: "Objekte anklicken: Raycaster"
description: "Herausfinden, welches Objekt unter dem Mauszeiger liegt, z.B. um es auszuwählen."
code:
  short: |-
    const raycaster = new THREE.Raycaster();
    const pointer = new THREE.Vector2();

    renderer.domElement.addEventListener("click", (event) => {
      const rect = renderer.domElement.getBoundingClientRect();
      pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;

      raycaster.setFromCamera(pointer, camera);
      const hits = raycaster.intersectObjects(clickables);
      if (hits.length) hits[0].object.material.color.set("#e24a33");
    });
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, camera, renderer, track } = mini(stage, { z: 5 });
    scene.add(new THREE.HemisphereLight("#ffffff", "#556677", 1.2));
    const sun = new THREE.DirectionalLight("#ffffff", 1.5); sun.position.set(2, 3, 4); scene.add(sun);
    const clickables = [-1.6, 0, 1.6].map(x => { const m = new THREE.Mesh(new THREE.SphereGeometry(0.6, 32, 16), new THREE.MeshStandardMaterial({ color: "#c9ced8" })); m.position.x = x; scene.add(m); return m; });
    const raycaster = new THREE.Raycaster(), pointer = new THREE.Vector2();
    const onClick = (event) => {
      const rect = renderer.domElement.getBoundingClientRect();
      pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1;
      pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1;
      raycaster.setFromCamera(pointer, camera);
      const hits = raycaster.intersectObjects(clickables);
      if (hits.length) { const c = hits[0].object.material.color; c.set(c.getHexString() === "c9ced8" ? accent(stage) : "#c9ced8"); }
    };
    renderer.domElement.addEventListener("click", onClick);
    track({ dispose: () => renderer.domElement.removeEventListener("click", onClick) });
    stage.insertAdjacentHTML("beforeend", '<span class="note">Kugeln anklicken</span>');
explain:
  picture: "Ein Raycaster ist ein Laserpointer: Vom Auge der Kamera aus wird ein Strahl durch den angeklickten Bildpunkt in die Szene geschossen. Das erste Objekt, das er trifft, ist das angeklickte."
  steps:
    - "Die Mausposition wird in Koordinaten von -1 bis 1 umgerechnet (Normalized Device Coordinates). Links ist -1, rechts 1, unten -1, oben 1."
    - "Darum das Minus bei y: Im Browser zählt y nach unten, in Three.js nach oben."
    - "`setFromCamera` erzeugt den Strahl von der Kamera durch diesen Punkt."
    - "`intersectObjects` liefert alle Treffer, sortiert nach Entfernung. `hits[0]` ist das vorderste Objekt."
    - "Jeder Treffer enthält u.a. `object`, `point` (Treffpunkt im Raum) und `distance`."
  mistake: "Mit `window.innerWidth` rechnen, obwohl das Canvas nur einen Teil der Seite einnimmt. Dann sind alle Klicks verschoben. Immer `getBoundingClientRect()` des Canvas verwenden. Ebenfalls häufig: Alle Objekte teilen ein Material, und beim Einfärben eines Treffers ändern sich alle."
  when: "Den Raycaster nur bei Klicks oder Mausbewegung ausführen, nicht in jedem Bild. Bei sehr vielen Objekten nur die anklickbaren in `intersectObjects` übergeben."
  question: "Wie zeigst du einen Hover-Effekt statt eines Klicks?"
  answer: "Den Strahl im `pointermove`-Event berechnen, das getroffene Objekt merken und hervorheben. Beim Verlassen die Hervorhebung wieder zurücksetzen."
links:
  - text: "Picking (Manual)"
    url: "https://threejs.org/manual/#en/picking"
  - text: "Raycaster"
    url: "https://threejs.org/docs/#Raycaster"
---
