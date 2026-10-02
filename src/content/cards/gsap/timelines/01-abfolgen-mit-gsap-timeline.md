---
title: "Abfolgen mit `gsap.timeline()`"
description: "Animationen nacheinander abspielen, ohne Verzögerungen von Hand auszurechnen."
code:
  short: |-
    const tl = gsap.timeline();
    tl.to(".a", { x: 220 })
      .to(".b", { x: 220 })
      .to(".c", { x: 220 });
  long: |-
    const opts = { duration: 500, fill: "forwards", easing: "ease-out" };
    const move = [{ transform: "translateX(0)" }, { transform: "translateX(220px)" }];

    document.querySelector(".a").animate(move, { ...opts, delay: 0 });
    document.querySelector(".b").animate(move, { ...opts, delay: 500 });
    document.querySelector(".c").animate(move, { ...opts, delay: 1000 });
demo:
  height: 180
  html: "<div class=\"col\"><div class=\"box a\"></div><div class=\"box alt b\"></div><div class=\"box warn c\"></div></div>"
  js: |-
    const tl = gsap.timeline();
    tl.to(".a", { x: 220 }).to(".b", { x: 220 }).to(".c", { x: 220 });
explain:
  picture: "Eine Timeline ist ein Drehbuch: Szene folgt auf Szene. Willst du eine Szene verlängern, rutschen alle folgenden automatisch nach hinten, ohne dass du jede Uhrzeit neu ausrechnest."
  steps:
    - "`gsap.timeline()` erzeugt einen Container für Tweens."
    - "Jedes `.to()` auf der Timeline wird standardmäßig ans Ende angehängt."
    - "Änderst du die Dauer eines Tweens, verschieben sich alle späteren automatisch."
    - "Die ganze Timeline lässt sich wie ein einzelner Tween steuern: `tl.pause()`, `tl.reverse()`, `tl.progress(0.5)`."
    - "Ohne Timeline musst du jede Verzögerung selbst ausrechnen und bei jeder Änderung alle nachfolgenden anpassen."
  mistake: "Abfolgen mit `delay` in einzelnen Tweens bauen. Das funktioniert, bis du die erste Dauer änderst und alle Verzögerungen danach falsch sind. Und `reverse()` geht nur für die ganze Timeline, nicht für lose Tweens."
  when: "Eine Timeline, sobald zwei oder mehr Schritte voneinander abhängen. Einzelne `delay`-Werte nur für wirklich unabhängige Animationen."
  question: "Wie lange dauert die Timeline im Beispiel ohne Angabe von `duration`?"
  answer: "1,5 Sekunden: drei Tweens mit der Standarddauer von 0,5 Sekunden hintereinander."
links:
  - text: "Timeline"
    url: "https://gsap.com/docs/v3/GSAP/Timeline"
  - text: "gsap.timeline()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.timeline()"
---
