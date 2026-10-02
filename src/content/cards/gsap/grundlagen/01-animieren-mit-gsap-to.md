---
title: "Animieren mit `gsap.to()`"
description: "Ein Element vom aktuellen Zustand zu neuen Werten animieren."
code:
  short: |-
    gsap.to(".box", {
      x: 220,
      rotation: 360,
      duration: 1,
    });
  long: |-
    document.querySelector(".box").animate(
      [
        { transform: "translateX(0) rotate(0deg)" },
        { transform: "translateX(220px) rotate(360deg)" },
      ],
      { duration: 1000, easing: "ease-out", fill: "forwards" }
    );
demo:
  height: 90
  html: "<div class=\"box\"></div>"
  js: "gsap.to(\".box\", { x: 220, rotation: 360, duration: 1 });"
explain:
  picture: "Ein Tween ist wie ein Navi-Auftrag: Du sagst nur, wo es hingehen soll und wie lange die Fahrt dauern darf. Den Weg dazwischen berechnet GSAP Bild für Bild."
  steps:
    - "`gsap.to()` nimmt ein Ziel (Selektor, Element oder Array) und ein Objekt mit Zielwerten."
    - "`x` und `rotation` sind GSAP-Kurzformen für Transforms. GSAP setzt daraus den `transform`-String zusammen."
    - "`duration` ist in Sekunden angegeben, nicht in Millisekunden wie bei CSS oder der Web Animations API."
    - "Der Standard-Ease ist `power1.out`: schneller Start, sanftes Ende."
    - "Die Variante ohne GSAP nutzt die Web Animations API (`element.animate`). Dort musst du Start- und Endzustand komplett angeben und mit `fill: \"forwards\"` festhalten."
  mistake: "Die Dauer in Millisekunden angeben: `duration: 1000` dauert bei GSAP über 16 Minuten. Und bei `element.animate` ohne `fill: \"forwards\"` springt das Element nach dem Ende zurück an den Start."
  when: "GSAP, sobald mehrere Animationen zusammenspielen, Scrollen beteiligt ist oder du Werte während der Animation ändern willst. Für einen einzelnen Hover-Effekt reicht eine CSS-Transition."
  question: "Wie lange dauert `gsap.to(\".box\", { x: 100 })` ohne Angabe von `duration`?"
  answer: "0,5 Sekunden. Das ist die Standarddauer in GSAP."
links:
  - text: "gsap.to()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.to()"
  - text: "Transforms (CSSPlugin)"
    url: "https://gsap.com/docs/v3/GSAP/CorePlugins/CSS"
  - text: "Web Animations API (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/API/Web_Animations_API"
---
