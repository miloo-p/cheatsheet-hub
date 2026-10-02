---
title: "Easing"
description: "Die Kurve bestimmt, wie sich eine Bewegung anfühlt: träge, federnd, mechanisch oder verspielt."
code:
  short: |-
    gsap.to(".a", { x: 220, ease: "power3.out" });
    gsap.to(".b", { x: 220, ease: "back.out(1.7)" });
    gsap.to(".c", { x: 220, ease: "elastic.out(1, 0.4)" });
  long: |-
    .a { transition: transform .5s cubic-bezier(0.215, 0.61, 0.355, 1); }
    .b { transition: transform .5s cubic-bezier(0.34, 1.56, 0.64, 1); }
    /* Elastisch geht nur mit vielen Stützpunkten in linear(): */
    .c { transition: transform .5s linear(0, 0.7 10%, 1.15 20%, 0.95 35%, 1.02 50%, 1); }
lang:
  long: "css"
demo:
  height: 180
  html: "<div class=\"col\"><div class=\"box a\"></div><div class=\"box alt b\"></div><div class=\"box warn c\"></div></div>"
  js: |-
    gsap.to(".a", { x: 220, ease: "power3.out", duration: 1 });
    gsap.to(".b", { x: 220, ease: "back.out(1.7)", duration: 1 });
    gsap.to(".c", { x: 220, ease: "elastic.out(1, 0.4)", duration: 1.6 });
explain:
  picture: "Easing ist der Fahrstil: Ein Taxi fährt sanft an und bremst sanft (`inOut`), ein Sportwagen zieht los und rollt aus (`out`), ein Flummi springt über das Ziel hinaus und federt zurück (`elastic`)."
  steps:
    - "`.out` heißt: schnell starten, langsam ankommen. Das passt für fast alles, was ins Bild kommt."
    - "`.in` heißt: langsam starten, schnell enden. Gut für Elemente, die das Bild verlassen."
    - "`.inOut` ist an beiden Enden weich, typisch für Bewegungen von A nach B innerhalb der Seite."
    - "Die Zahl bei `power1` bis `power4` gibt die Stärke an. `back` schießt leicht über das Ziel hinaus, `elastic` schwingt nach."
    - "In CSS gibt es `cubic-bezier()` für einfache Kurven. Federn und Abpraller lassen sich nur mit der neueren Funktion `linear()` und vielen Stützpunkten annähern."
  mistake: "Für alles dasselbe Easing nehmen, meist `linear` oder den Standardwert. Lineare Bewegungen wirken mechanisch, weil sich in der echten Welt nichts ohne Beschleunigung bewegt. `linear` passt nur für Endlosschleifen wie Ladekreisel."
  when: "GSAP, wenn du ausdrucksstarke Kurven brauchst oder sie im Ease Visualizer ausprobieren willst. Für einfache Übergänge sind `ease-out` oder ein `cubic-bezier` in CSS völlig ausreichend."
  question: "Welches Easing passt zu einem Modal, das den Bildschirm verlässt?"
  answer: "Ein `.in`-Ease wie `power2.in`. Es beschleunigt zum Ende hin, so wirkt das Wegfliegen natürlich."
links:
  - text: "Eases und Ease Visualizer"
    url: "https://gsap.com/docs/v3/Eases"
  - text: "linear() (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/easing-function/linear"
---
