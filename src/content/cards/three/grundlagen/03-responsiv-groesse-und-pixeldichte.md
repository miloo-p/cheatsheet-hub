---
title: "Responsiv: Größe und Pixeldichte"
description: "Das Canvas muss mitwachsen, wenn sich sein Container ändert, und auf hochauflösenden Displays scharf bleiben."
labels:
  - "Container"
  - "Ganzes Fenster"
code:
  short: |-
    const container = document.querySelector("#scene");

    function resize() {
      const { clientWidth: w, clientHeight: h } = container;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }
    renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    new ResizeObserver(resize).observe(container);
  long: |-
    renderer.setPixelRatio(devicePixelRatio);

    window.addEventListener("resize", () => {
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(innerWidth, innerHeight);
    });
explain:
  picture: "Das Canvas ist eine Leinwand mit einer festen Anzahl Pixel. Wird der Rahmen größer, ohne dass die Leinwand mitwächst, wird das Bild unscharf oder verzerrt. Das Seitenverhältnis der Kamera ist das Format des Fotos, das zur Leinwand passen muss."
  steps:
    - "`camera.aspect` muss dem Seitenverhältnis des Canvas entsprechen, sonst wirkt alles gestaucht."
    - "Nach jeder Änderung an der Kamera muss `updateProjectionMatrix()` aufgerufen werden. Sonst gilt die alte Einstellung weiter."
    - "`renderer.setSize()` ändert die echte Pixelzahl des Canvas."
    - "`setPixelRatio` berücksichtigt Retina-Displays. Die Begrenzung auf 2 ist wichtig: Handys mit Faktor 3 oder 4 müssten sonst bis zu viermal so viele Pixel berechnen, ohne sichtbaren Gewinn."
    - "`ResizeObserver` reagiert auf Größenänderungen des Containers, also auch wenn sich das Layout ändert, ohne dass das Fenster seine Größe ändert. Das `resize`-Event des Fensters bekommt das nicht mit."
  mistake: "`updateProjectionMatrix()` vergessen. Das Canvas hat dann die richtige Größe, aber die Szene ist verzerrt, weil die Kamera noch mit dem alten Seitenverhältnis rechnet."
  when: "`ResizeObserver` für Szenen in einem Bereich der Seite, z.B. einer Karte oder einem Hero. Das Fenster-Event reicht nur für Vollbild-Szenen."
  question: "Warum ist `Math.min(devicePixelRatio, 2)` besser als `devicePixelRatio` allein?"
  answer: "Weil es Geräte mit sehr hoher Pixeldichte begrenzt. Ab Faktor 2 sieht man kaum noch einen Unterschied, aber die Grafikkarte muss bei Faktor 3 mehr als doppelt so viele Pixel berechnen."
links:
  - text: "Responsive (Manual)"
    url: "https://threejs.org/manual/#en/responsive"
  - text: "ResizeObserver (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/API/ResizeObserver"
---
