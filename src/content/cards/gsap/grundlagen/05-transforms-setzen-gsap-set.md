---
title: "Transforms setzen: `gsap.set()`"
description: "Werte sofort setzen, ohne Animation. GSAP verwaltet alle Transforms einzeln, sodass sie sich nicht gegenseitig überschreiben."
code:
  short: |-
    gsap.set(".box", { xPercent: -50, rotation: 15 });

    // später, nur x ändern – rotation bleibt erhalten
    gsap.to(".box", { x: 120 });
  long: |-
    const box = document.querySelector(".box");
    box.style.transform = "translateX(-50%) rotate(15deg)";

    // später: der komplette String muss neu gebaut werden,
    // sonst geht die Drehung verloren
    box.style.transform = "translateX(-50%) translateX(120px) rotate(15deg)";
demo:
  height: 90
  html: "<div class=\"box\"></div>"
  js: |-
    gsap.set(".box", { rotation: 15 });
    gsap.to(".box", { x: 120, duration: 0.8, delay: 0.4 });
explain:
  picture: "CSS-Transforms sind ein einzelner Satz, den du immer komplett neu schreiben musst. GSAP führt stattdessen eine Liste mit einzelnen Einträgen für Verschiebung, Drehung und Skalierung und baut daraus den Satz."
  steps:
    - "`gsap.set()` ist ein Tween mit Dauer 0, also eine sofortige Zuweisung."
    - "GSAP speichert `x`, `y`, `rotation`, `scale` und `xPercent` getrennt pro Element."
    - "Animierst du danach nur `x`, bleiben die anderen Transforms unverändert."
    - "`xPercent: -50` verschiebt um die Hälfte der eigenen Breite und lässt sich mit `x` kombinieren. Das ist praktisch für zentrierte Elemente."
  mistake: "Ein Element per CSS `transform` positionieren und dann mit GSAP animieren. GSAP liest den vorhandenen Transform zwar ein, aber gemischte Quellen führen schnell zu Sprüngen. Am besten setzt du Transforms für animierte Elemente nur noch mit GSAP."
  when: "`gsap.set()` für Startzustände vor einer Animation. Für statisches Layout ohne Animation bleibt CSS der richtige Ort."
  question: "Was ist der Unterschied zwischen `x: 100` und `left: 100`?"
  answer: "`x` verschiebt per `transform` und läuft flüssig auf der Grafikkarte. `left` verändert das Layout und zwingt den Browser bei jedem Bild zum Neuberechnen. Siehe Karte „Flüssig animieren“."
links:
  - text: "gsap.set()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.set()"
  - text: "Transforms (CSSPlugin)"
    url: "https://gsap.com/docs/v3/GSAP/CorePlugins/CSS"
---
