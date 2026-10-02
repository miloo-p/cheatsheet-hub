---
title: "Layout-Wechsel animieren: Flip"
description: "Elemente springen bei einer Layout-Änderung nicht, sondern gleiten an ihre neue Position."
code:
  short: |-
    gsap.registerPlugin(Flip);

    const state = Flip.getState(".item");
    container.classList.toggle("grid");   // Layout ändern
    Flip.from(state, { duration: 0.6, ease: "power2.inOut" });
  long: |-
    const items = [...document.querySelectorAll(".item")];
    const first = items.map(el => el.getBoundingClientRect());   // F: First

    container.classList.toggle("grid");                           // Layout ändern
    items.forEach((el, i) => {
      const last = el.getBoundingClientRect();                    // L: Last
      const dx = first[i].left - last.left;                       // I: Invert
      const dy = first[i].top - last.top;
      el.animate(                                                 // P: Play
        [{ transform: `translate(${dx}px, ${dy}px)` }, { transform: "none" }],
        { duration: 600, easing: "ease-in-out" }
      );
    });
demo:
  height: 250
  html: "<div class=\"col\"><div class=\"row flipwrap\"><div class=\"box item\"></div><div class=\"box alt item\"></div><div class=\"box warn item\"></div><div class=\"box item\" style=\"opacity:.5\"></div></div><button type=\"button\" class=\"chip shuffle\" style=\"justify-self:start\">Mischen</button></div>"
  js: |-
    const wrap = stage.querySelector(".flipwrap");
    const shuffle = () => {
      const state = Flip.getState(wrap.children);
      [...wrap.children].sort(() => Math.random() - 0.5).forEach(el => wrap.appendChild(el));
      wrap.style.flexDirection = wrap.style.flexDirection === "column" ? "row" : "column";
      Flip.from(state, { duration: 0.6, ease: "power2.inOut" });
    };
    stage.querySelector(".shuffle").onclick = shuffle;
    shuffle();
explain:
  picture: "Flip ist ein Zaubertrick: Das Element springt sofort an seinen neuen Platz, wird aber optisch an den alten zurückversetzt und gleitet dann sichtbar hinüber. Die Zuschauer sehen nur das Gleiten."
  steps:
    - "FLIP steht für First, Last, Invert, Play."
    - "First: `Flip.getState()` merkt sich Position und Größe aller Elemente."
    - "Last: Du änderst das Layout ganz normal, per Klasse, Umsortieren oder Verschieben im DOM."
    - "Invert und Play: `Flip.from()` versetzt die Elemente per Transform an die alte Position und animiert sie zur neuen."
    - "Die ausführliche Variante zeigt genau diese vier Schritte von Hand. Flip kümmert sich zusätzlich um Größenänderungen, verschachtelte Elemente und unterbrochene Animationen."
  mistake: "Den Zustand erst nach der Layout-Änderung erfassen. Dann sind First und Last identisch, und es passiert nichts. `getState()` muss immer vor der Änderung stehen."
  when: "Flip für Filter, Sortierungen, Raster-Wechsel und Elemente, die den Container wechseln. Für ein einzelnes Element reicht oft die ausführliche Variante."
  question: "Wofür steht das I in FLIP?"
  answer: "Für Invert: Das Element wird per Transform optisch an seine alte Position zurückgesetzt, bevor es animiert wird."
links:
  - text: "Flip"
    url: "https://gsap.com/docs/v3/Plugins/Flip/"
---
