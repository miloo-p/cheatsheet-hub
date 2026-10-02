---
title: "Aufräumen: `dispose()`"
description: "Geometrien, Materialien und Texturen belegen Speicher auf der Grafikkarte. Der wird nicht automatisch freigegeben, wenn du ein Objekt entfernst."
code:
  short: |-
    function removeObject(obj) {
      scene.remove(obj);
      obj.traverse((child) => {
        child.geometry?.dispose();
        for (const mat of [].concat(child.material ?? [])) {
          for (const value of Object.values(mat)) {
            if (value?.isTexture) value.dispose();
          }
          mat.dispose();
        }
      });
    }

    // beim Verlassen der Seite / Unmount:
    renderer.setAnimationLoop(null);
    controls.dispose();
    renderer.dispose();
explain:
  picture: "Die Grafikkarte ist ein Lager mit begrenzten Regalen. `scene.remove()` nimmt nur das Etikett von der Liste, die Kiste bleibt im Regal stehen. Erst `dispose()` räumt sie wirklich aus."
  steps:
    - "Beim ersten Zeichnen lädt Three.js Geometrien und Texturen in den Grafikspeicher."
    - "`scene.remove(obj)` entfernt das Objekt nur aus der Szene. Die Daten auf der Grafikkarte bleiben."
    - "`geometry.dispose()`, `material.dispose()` und `texture.dispose()` geben den Speicher frei."
    - "`traverse` geht rekursiv durch alle Kinder, wichtig bei geladenen Modellen mit vielen Teilen."
    - "Seit Version r186 haben auch Object3D-Objekte selbst eine `dispose()`-Methode. Eigene Klassen, die davon erben, müssen dann `super.dispose()` aufrufen."
  mistake: "In einer Single-Page-App zwischen Seiten wechseln, ohne aufzuräumen. Jeder Besuch der 3D-Seite legt neue Daten auf die Grafikkarte, bis der Browser langsam wird oder den WebGL-Kontext verliert."
  when: "Immer aufräumen, wenn Objekte dauerhaft verschwinden oder eine Komponente unmountet. Mit `renderer.info.memory` siehst du, wie viele Geometrien und Texturen gerade belegt sind."
  question: "Wie prüfst du, ob dein Aufräumen funktioniert?"
  answer: "`console.log(renderer.info.memory)` vor und nach dem Entfernen. Die Zahlen für `geometries` und `textures` müssen sinken."
links:
  - text: "Cleanup (Manual)"
    url: "https://threejs.org/manual/#en/cleanup"
  - text: "WebGLRenderer.info"
    url: "https://threejs.org/docs/#WebGLRenderer"
---
