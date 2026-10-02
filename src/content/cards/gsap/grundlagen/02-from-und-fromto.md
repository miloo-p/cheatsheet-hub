---
title: "`from()` und `fromTo()`"
description: "Vom Ziel aus zurück animieren, ideal für Einblend-Effekte. Oder Start und Ende komplett festlegen."
code:
  short: |-
    gsap.from(".card", { y: 40, autoAlpha: 0, duration: 0.6 });

    gsap.fromTo(".bar",
      { scaleX: 0 },
      { scaleX: 1, duration: 1, transformOrigin: "left center" }
    );
  long: |-
    document.querySelector(".card").animate(
      [
        { transform: "translateY(40px)", opacity: 0, visibility: "hidden" },
        { transform: "translateY(0)", opacity: 1, visibility: "visible" },
      ],
      { duration: 600, easing: "ease-out" }
    );

    const bar = document.querySelector(".bar");
    bar.style.transformOrigin = "left center";
    bar.animate([{ transform: "scaleX(0)" }, { transform: "scaleX(1)" }],
      { duration: 1000, fill: "forwards" });
demo:
  height: 100
  html: "<div class=\"col\"><div class=\"chip card\">Karte erscheint</div><div class=\"box bar\" style=\"width:100%;height:10px\"></div></div>"
  js: |-
    gsap.from(".card", { y: 40, autoAlpha: 0, duration: 0.6 });
    gsap.fromTo(".bar", { scaleX: 0 }, { scaleX: 1, duration: 1, transformOrigin: "left center" });
explain:
  picture: "`from()` ist wie ein Film, der rückwärts gedreht und vorwärts abgespielt wird: Das Element steht schon an seinem Platz, GSAP schiebt es kurz weg und lässt es dorthin zurückfliegen."
  steps:
    - "`gsap.from()` nimmt die angegebenen Werte als Start und den aktuellen Zustand aus dem CSS als Ziel."
    - "`autoAlpha` ist eine GSAP-Kurzform: Es animiert `opacity` und setzt `visibility: hidden`, sobald der Wert 0 ist. Unsichtbare Elemente sind dann auch nicht mehr klickbar."
    - "`fromTo()` legt Start und Ziel ausdrücklich fest und ist damit unabhängig vom aktuellen Zustand."
    - "`transformOrigin` bestimmt den Fixpunkt für `scale` und `rotation`. Mit `left center` wächst der Balken von links."
  mistake: "Ein `from()` mehrfach hintereinander auslösen, z.B. bei jedem Klick. Startet die zweite Animation, während die erste noch läuft, liest GSAP den halb animierten Zustand als neues Ziel, und das Element bleibt irgendwo in der Mitte hängen. Für wiederholbare Animationen ist `fromTo()` sicher."
  when: "`from()` für Einblendungen beim Laden. `fromTo()`, wenn eine Animation mehrfach abgespielt wird oder der Ausgangszustand nicht sicher ist."
  question: "Warum flackert ein Element manchmal kurz sichtbar auf, bevor `gsap.from(…, { autoAlpha: 0 })` startet?"
  answer: "Weil das Element schon gerendert wird, bevor das Skript läuft. Abhilfe: im CSS `visibility: hidden` setzen und mit `autoAlpha` einblenden, oder das Skript früher laden."
links:
  - text: "gsap.from()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.from()"
  - text: "gsap.fromTo()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.fromTo()"
---
