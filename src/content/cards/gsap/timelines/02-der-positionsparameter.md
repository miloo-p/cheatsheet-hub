---
title: "Der Positionsparameter"
description: "Das dritte Argument bestimmt, wo ein Tween in der Timeline startet: überlappend, gleichzeitig oder mit Pause."
labels:
  - "Relativ"
  - "Absolut"
code:
  short: |-
    tl.to(".a", { x: 220, duration: 1 })
      .to(".b", { x: 220 }, "<")        // gleichzeitig mit dem vorigen
      .to(".c", { x: 220 }, "-=0.3")    // 0,3 s vor dem Ende
      .add("ende", "+=0.5")             // Label nach 0,5 s Pause
      .to(".a", { rotation: 90 }, "ende");
  long: |-
    // Startzeiten in Sekunden, von Hand berechnet:
    tl.to(".a", { x: 220, duration: 1 }, 0)
      .to(".b", { x: 220 }, 0)            // gleichzeitig mit .a
      .to(".c", { x: 220 }, 0.7)          // Ende bei 1 s, minus 0,3 s
      .to(".a", { rotation: 90 }, 1.7);   // Ende von .c (1,2 s) + 0,5 s Pause
demo:
  height: 180
  html: "<div class=\"col\"><div class=\"box a\"></div><div class=\"box alt b\"></div><div class=\"box warn c\"></div></div>"
  js: |-
    const tl = gsap.timeline();
    tl.to(".a", { x: 220, duration: 1 })
      .to(".b", { x: 220 }, "<")
      .to(".c", { x: 220 }, "-=0.3")
      .add("ende", "+=0.5")
      .to(".a", { rotation: 90 }, "ende");
explain:
  picture: "Der Positionsparameter ist wie Regieanweisungen im Drehbuch: „gleichzeitig mit der letzten Szene“, „kurz bevor sie endet“, „nach einer Pause“. Relative Angaben bleiben richtig, auch wenn sich Szenen ändern."
  steps:
    - "Ohne Angabe wird ans Ende der Timeline angehängt."
    - "`\"<\"` startet gleichzeitig mit dem Start des vorigen Tweens, `\">\"` an dessen Ende."
    - "`\"-=0.3\"` startet 0,3 Sekunden vor dem Ende der Timeline, also überlappend. `\"+=0.5\"` lässt eine Pause."
    - "Eine Zahl wie `1.2` ist eine absolute Zeit ab Timeline-Beginn."
    - "Labels wie `\"ende\"` sind benannte Sprungmarken. Tweens können dort starten, und `tl.play(\"ende\")` springt direkt hin."
  mistake: "Absolute Zeiten benutzen wie in der rechten Variante. Ändert sich eine einzige Dauer, stimmen alle Zeiten danach nicht mehr und müssen neu gerechnet werden. Relative Angaben wie `\"<\"` und `\"-=0.3\"` passen sich automatisch an."
  when: "Relative Positionen für fast alles. Absolute Zahlen nur, wenn ein Tween genau zu einem festen Zeitpunkt starten muss, z.B. synchron zu Audio."
  question: "Was bedeutet `\"<0.2\"`?"
  answer: "0,2 Sekunden nach dem Start des vorigen Tweens. So entsteht ein leichter Versatz, ähnlich wie bei `stagger`."
links:
  - text: "Positionsparameter"
    url: "https://gsap.com/resources/position-parameter"
---
