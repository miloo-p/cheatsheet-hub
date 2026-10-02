---
title: "Die Render-Schleife mit `Timer`"
description: "Für Bewegung muss die Szene 60-mal pro Sekunde neu gezeichnet werden. Seit r183 ist `Clock` veraltet, der Nachfolger heißt `Timer`."
labels:
  - "Aktuell: Timer"
  - "Veraltet: Clock"
code:
  short: |-
    const timer = new THREE.Timer();
    timer.connect(document);   // pausiert, wenn der Tab im Hintergrund ist

    renderer.setAnimationLoop((timestamp) => {
      timer.update(timestamp);
      const delta = timer.getDelta();     // Sekunden seit dem letzten Bild

      cube.rotation.y += delta * 1.5;     // 1,5 Radiant pro Sekunde
      renderer.render(scene, camera);
    });
  long: |-
    const clock = new THREE.Clock();      // veraltet seit r183

    function animate() {
      requestAnimationFrame(animate);
      const delta = clock.getDelta();

      cube.rotation.y += delta * 1.5;
      renderer.render(scene, camera);
    }
    animate();
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, onTick } = mini(stage);
    const cube = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshNormalMaterial());
    scene.add(cube);
    onTick((delta) => { cube.rotation.y += delta * 1.5; cube.rotation.x += delta * 0.5; });
explain:
  picture: "Delta-Zeit ist wie Tempo statt Schrittzahl. Sagst du „pro Bild 0,01 drehen“, dreht sich der Würfel auf einem 120-Hz-Monitor doppelt so schnell wie auf einem 60-Hz-Monitor. Mit „1,5 pro Sekunde mal vergangene Zeit“ ist er überall gleich schnell."
  steps:
    - "`setAnimationLoop` ruft die Funktion vor jedem Bild auf, so oft der Bildschirm aktualisiert. Es ist der Three.js-Ersatz für `requestAnimationFrame` und funktioniert auch in VR."
    - "`timer.update(timestamp)` merkt sich die aktuelle Zeit. Danach liefert `getDelta()` die Sekunden seit dem letzten Bild und `getElapsed()` die Gesamtzeit."
    - "`timer.connect(document)` sorgt dafür, dass nach einem Tab-Wechsel kein riesiger Zeitsprung entsteht. Ohne das springt die Animation beim Zurückkommen."
    - "Die rechte Variante mit `Clock` funktioniert noch, gilt aber seit Version r183 als veraltet. Du findest sie in fast allen älteren Tutorials."
  mistake: "Pro Bild einen festen Wert addieren, z.B. `rotation.y += 0.01`. Dann hängt die Geschwindigkeit von der Bildrate ab: auf schnellen Monitoren zu schnell, auf langsamen Geräten zu langsam."
  when: "Neuer Code nimmt `Timer` und `setAnimationLoop`. `Clock` und `requestAnimationFrame` musst du lesen können, weil sie in vielen Beispielen noch stehen."
  question: "Wie stoppst du die Render-Schleife, z.B. beim Verlassen der Seite?"
  answer: "Mit `renderer.setAnimationLoop(null)`."
links:
  - text: "Timer"
    url: "https://threejs.org/docs/#Timer"
  - text: "Migration Guide (EN)"
    url: "https://github.com/mrdoob/three.js/wiki/Migration-Guide"
---
