---
title: "Festhalten: `pin`"
description: "Ein Element bleibt stehen, während daneben weitergescrollt wird, und läuft danach normal weiter."
labels:
  - "Mit GSAP"
  - "Ohne GSAP (nur sticky)"
code:
  short: |-
    gsap.to(".panel", {
      rotation: 360,
      scrollTrigger: {
        trigger: ".panel",
        start: "top 20%",
        end: "+=300",
        pin: true,
        scrub: true,
      },
    });
  long: |-
    /* CSS: Festhalten geht ohne GSAP mit sticky */
    .panel-wrap { height: 600px; }       /* Strecke, auf der es klebt */
    .panel { position: sticky; top: 20%; }

    /* Die Drehung muss JavaScript im Scroll-Event berechnen,
       wie in der Karte zu scrub. */
lang:
  long: "css"
demo:
  height: 220
  html: "<div class=\"scroller\"><div class=\"spacer\">↓ scrollen</div><div class=\"box panel\" style=\"margin-inline:auto\"></div><div class=\"spacer\"></div><div class=\"spacer\">Ende</div></div>"
  js: |-
    const scroller = stage.querySelector(".scroller");
    gsap.to(".panel", { rotation: 360, scrollTrigger: { trigger: ".panel", scroller, start: "top 30%", end: "+=200", pin: true, scrub: true } });
explain:
  picture: "`pin` ist ein Magnet an der Scheibe: Das Element bleibt an einer Stelle im Fenster haften, während die Seite für eine festgelegte Strecke darunter weiterläuft. Danach löst sich der Magnet."
  steps:
    - "`pin: true` hält den Trigger zwischen `start` und `end` fest."
    - "`end: \"+=300\"` heißt: 300 Pixel Scrollstrecke nach dem Start."
    - "ScrollTrigger fügt dafür automatisch Abstand ein (`pinSpacing`), damit der folgende Inhalt nicht darunter verschwindet."
    - "Kombiniert mit `scrub` entsteht das typische Muster „Element bleibt stehen und animiert, während man scrollt“."
    - "Das reine Festhalten kann CSS mit `position: sticky`. Nur die Kopplung an eine Animation braucht JavaScript."
  mistake: "Ein Element pinnen, das selbst animiert wird, und dann das Pin-Element auch per `transform` bewegen. Das kann sich beißen. Besser einen Wrapper pinnen und das innere Element animieren."
  when: "`position: sticky`, wenn ein Element nur kleben soll. ScrollTrigger mit `pin`, wenn während des Klebens etwas passiert, z.B. eine Folge von Bildern oder ein horizontales Scrollen."
  question: "Wofür ist `pinSpacing: false` gut?"
  answer: "Wenn das nachfolgende Element über das gepinnte Element hinweggleiten soll, z.B. für gestapelte Karten. Ohne Abstand rückt der Inhalt nicht nach unten."
links:
  - text: "ScrollTrigger: pin"
    url: "https://gsap.com/docs/v3/Plugins/ScrollTrigger/"
  - text: "position: sticky (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/position"
---
