---
title: "Animieren mit GSAP"
description: "Kamerafahrten und Übergänge mit GSAP-Tweens statt mit eigener Rechnung im Render-Loop."
labels:
  - "Mit GSAP"
  - "Von Hand im Loop"
code:
  short: |-
    gsap.to(cube.position, { y: 1, duration: 1, ease: "back.out(2)" });
    gsap.to(cube.rotation, { y: Math.PI * 2, duration: 2, ease: "power2.inOut" });

    // Kamerafahrt
    gsap.to(camera.position, {
      x: 3, z: 3, duration: 2,
      onUpdate: () => camera.lookAt(0, 0, 0),
    });
  long: |-
    let t = 0;
    renderer.setAnimationLoop(() => {
      t = Math.min(t + timer.getDelta() / 1, 1);   // 0 bis 1 in 1 Sekunde
      const eased = 1 - Math.pow(1 - t, 3);         // ease-out von Hand
      cube.position.y = eased * 1;
      renderer.render(scene, camera);
    });
demo:
  height: 220
  flush: true
  html: "<span class=\"note\">3D-Szene startet per Klick auf „Abspielen“.</span>"
  js: |-
    const { scene, camera } = mini(stage, { z: 5 });
    camera.position.set(0, 1, 5); camera.lookAt(0, 0, 0);
    scene.add(new THREE.GridHelper(6, 12, 0x888888, 0xcccccc));
    const cube = new THREE.Mesh(new THREE.BoxGeometry(0.8, 0.8, 0.8), new THREE.MeshNormalMaterial());
    cube.position.y = 0.4; scene.add(cube);
    const tl = gsap.timeline();
    tl.to(cube.position, { y: 1.4, duration: 0.8, ease: "back.out(2)" })
      .to(cube.rotation, { y: Math.PI * 2, duration: 1.4, ease: "power2.inOut" }, "<")
      .to(camera.position, { x: 3.5, y: 2.5, z: 3.5, duration: 1.6, ease: "power2.inOut", onUpdate: () => camera.lookAt(0, 0.6, 0) }, "-=0.6")
      .to(cube.position, { y: 0.4, duration: 0.6, ease: "bounce.out" });
    return () => tl.kill();
explain:
  picture: "GSAP kann jede Zahl in jedem Objekt animieren, nicht nur CSS. Für GSAP ist `cube.position` einfach ein Objekt mit den Zahlen `x`, `y` und `z`, und genau die schiebt es über die Zeit."
  steps:
    - "`gsap.to(cube.position, { y: 1 })` animiert die Eigenschaft `y` des Positionsobjekts."
    - "Für Drehungen animierst du `cube.rotation`, für Größe `cube.scale`."
    - "Die Render-Schleife läuft weiter wie gewohnt und zeichnet in jedem Bild den aktuellen Zwischenstand."
    - "`onUpdate` wird in jedem Animationsschritt aufgerufen. Bei Kamerafahrten hält `lookAt` den Blick auf das Ziel."
    - "Mit ScrollTrigger kombiniert entstehen so die typischen 3D-Scroll-Seiten."
  mistake: "Die Kamera per GSAP bewegen, während OrbitControls aktiv sind. Die Controls überschreiben die Position im nächsten Bild wieder. Entweder die Controls während der Fahrt abschalten (`controls.enabled = false`) oder `controls.target` mit animieren."
  when: "GSAP für Übergänge mit klarem Anfang und Ende. Dauerhafte Bewegungen wie ein rotierender Planet gehören in die Render-Schleife mit Delta-Zeit."
  question: "Wie animierst du die Farbe eines Materials mit GSAP?"
  answer: "Über die Zahlen des Farbobjekts, z.B. `gsap.to(material.color, { r: 1, g: 0.3, b: 0.2 })`. Die Werte liegen zwischen 0 und 1."
links:
  - text: "GSAP-Spickzettel"
    url: "/gsap/"
  - text: "gsap.to()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.to()"
---
