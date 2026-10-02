---
title: "Weniger Bewegung respektieren: `matchMedia`"
description: "Animationen an Bildschirmgröße und Systemeinstellungen anpassen und beim Wechsel automatisch aufräumen."
labels:
  - "Mit matchMedia"
  - "Von Hand"
code:
  short: |-
    const mm = gsap.matchMedia();

    mm.add({
      isDesktop: "(min-width: 800px)",
      reduceMotion: "(prefers-reduced-motion: reduce)",
    }, (context) => {
      const { isDesktop, reduceMotion } = context.conditions;
      gsap.from(".hero", {
        y: reduceMotion ? 0 : (isDesktop ? 80 : 30),
        autoAlpha: 0,
        duration: reduceMotion ? 0.2 : 1,
      });
    });
  long: |-
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    const desktop = window.matchMedia("(min-width: 800px)");
    let tween;

    function setup() {
      if (tween) tween.revert();   // alte Animation entfernen
      tween = gsap.from(".hero", {
        y: reduce.matches ? 0 : (desktop.matches ? 80 : 30),
        autoAlpha: 0,
        duration: reduce.matches ? 0.2 : 1,
      });
    }
    reduce.addEventListener("change", setup);
    desktop.addEventListener("change", setup);
    setup();
explain:
  picture: "`gsap.matchMedia()` ist ein Thermostat mit Fühlern: Es merkt, wenn sich Bildschirmbreite oder Systemeinstellung ändern, baut die alten Animationen ab und die passenden neu auf."
  steps:
    - "`mm.add()` bekommt Bedingungen als Media Queries und eine Funktion mit den Animationen."
    - "In `context.conditions` steht für jede Bedingung `true` oder `false`."
    - "Ändert sich eine Bedingung, werden alle Animationen und ScrollTrigger aus der Funktion zurückgesetzt und die Funktion läuft neu."
    - "`prefers-reduced-motion` ist eine Systemeinstellung für Menschen, denen Bewegung Schwindel oder Übelkeit verursacht. Respektieren heißt nicht unbedingt „gar keine Animation“, sondern: keine großen Bewegungen, eher kurze Überblendungen."
  mistake: "Bei reduzierter Bewegung einfach alles abschalten, auch Animationen, die Zustände erklären. Ein kurzes Einblenden ist meist in Ordnung, große Sprünge, Parallax und Zoom-Effekte nicht."
  when: "`gsap.matchMedia()` immer dann, wenn Animationen je nach Gerät oder Einstellung anders sein sollen. Es erspart dir das komplette Aufräumen von Hand."
  question: "Wie testest du `prefers-reduced-motion`, ohne die Systemeinstellung zu ändern?"
  answer: "In den Chrome-Entwicklertools unter „Rendering“ bei „Emulate CSS media feature prefers-reduced-motion“ den Wert `reduce` wählen."
links:
  - text: "gsap.matchMedia()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.matchMedia()"
  - text: "prefers-reduced-motion (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/@media/prefers-reduced-motion"
---
