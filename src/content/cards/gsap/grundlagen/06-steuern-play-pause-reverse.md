---
title: "Steuern: `play`, `pause`, `reverse`"
description: "Jede Animation ist ein Objekt mit Fernbedienung. Seit Version 3.15 gibt es dazu `easeReverse` für einen natürlichen Rückweg."
code:
  short: |-
    const tween = gsap.to(".menu", {
      x: 220,
      ease: "expo.out",
      easeReverse: true,
      paused: true,
    });

    openBtn.onclick = () => tween.play();
    closeBtn.onclick = () => tween.reverse();
  long: |-
    const anim = document.querySelector(".menu").animate(
      [{ transform: "translateX(0)" }, { transform: "translateX(220px)" }],
      { duration: 1000, easing: "cubic-bezier(0.19, 1, 0.22, 1)", fill: "both" }
    );
    anim.pause();

    openBtn.onclick = () => { anim.playbackRate = 1; anim.play(); };
    closeBtn.onclick = () => anim.reverse();
demo:
  height: 120
  html: "<div class=\"col\"><div class=\"box menu\"></div><div class=\"row\"><button type=\"button\" class=\"chip open\">Öffnen</button><button type=\"button\" class=\"chip close\">Schließen</button></div></div>"
  js: |-
    const tween = gsap.to(".menu", { x: 220, duration: 1, ease: "expo.out", easeReverse: true, paused: true });
    stage.querySelector(".open").onclick = () => tween.play();
    stage.querySelector(".close").onclick = () => tween.reverse();
explain:
  picture: "Ein Tween ist eine Videokassette im Rekorder: Du kannst abspielen, anhalten, zurückspulen oder an eine Stelle springen. `easeReverse` sorgt dafür, dass das Zurückspulen nicht wie ein rückwärts laufender Film aussieht."
  steps:
    - "`paused: true` erzeugt die Animation, ohne sie zu starten."
    - "`play()`, `pause()`, `reverse()`, `restart()` und `progress(0.5)` steuern sie jederzeit, auch mitten im Lauf."
    - "Beim normalen `reverse()` läuft auch das Easing rückwärts. Aus `expo.out` wird beim Schließen ein träger Start mit hartem Ende."
    - "`easeReverse: true` (neu in GSAP 3.15) verwendet beim Rückweg dieselbe Kurvenform in der passenden Richtung. Mit einem Ease-Namen wie `easeReverse: \"sine.in\"` bekommt der Rückweg ein ganz eigenes Gefühl."
  mistake: "Bei jedem Klick einen neuen Tween erzeugen, statt einen vorhandenen zu steuern. Bei schnellem Klicken laufen dann mehrere Animationen gegeneinander. Ein Tween mit `play()` und `reverse()` lässt sich beliebig unterbrechen."
  when: "GSAP für Menüs, Drawer und Modals, die man jederzeit umkehren kann. Die Web Animations API hat ebenfalls `reverse()`, aber kein getrenntes Easing für den Rückweg."
  question: "Welche Option hat `easeReverse` ersetzt?"
  answer: "`yoyoEase`. Es funktioniert weiterhin, wird aber intern in `easeReverse` umgewandelt und gilt als veraltet."
links:
  - text: "Tween-Methoden"
    url: "https://gsap.com/docs/v3/GSAP/Tween"
  - text: "GSAP 3.15: easeReverse"
    url: "https://gsap.com/blog/3-15/"
---
