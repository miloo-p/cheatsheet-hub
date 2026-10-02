---
title: "Beim Hineinscrollen abspielen"
description: "Eine Animation starten, sobald ein Element in den sichtbaren Bereich kommt."
code:
  short: |-
    gsap.registerPlugin(ScrollTrigger);

    gsap.from(".target", {
      x: -100,
      autoAlpha: 0,
      scrollTrigger: {
        trigger: ".target",
        start: "top 80%",
        toggleActions: "play none none reverse",
      },
    });
  long: |-
    const target = document.querySelector(".target");

    const observer = new IntersectionObserver(([entry]) => {
      target.classList.toggle("visible", entry.isIntersecting);
    }, { rootMargin: "0px 0px -20% 0px" });

    observer.observe(target);

    /* CSS */
    .target { opacity: 0; transform: translateX(-100px); transition: .5s; }
    .target.visible { opacity: 1; transform: none; }
demo:
  height: 200
  html: "<div class=\"scroller\"><div class=\"spacer\">↓ hier scrollen</div><div class=\"box target\"></div><div class=\"spacer\"></div></div>"
  js: |-
    const scroller = stage.querySelector(".scroller");
    gsap.from(".target", { x: -100, autoAlpha: 0, scrollTrigger: { trigger: ".target", scroller, start: "top 80%", toggleActions: "play none none reverse", markers: true } });
explain:
  picture: "Ein ScrollTrigger ist eine Lichtschranke im Flur: Wenn das Element eine bestimmte Linie im Fenster überquert, wird die Animation ausgelöst."
  steps:
    - "`trigger` ist das Element, dessen Position beobachtet wird."
    - "`start: \"top 80%\"` heißt: wenn die Oberkante des Elements die Linie bei 80% der Fensterhöhe erreicht."
    - "`toggleActions` legt vier Aktionen fest: beim Hineinscrollen, beim Verlassen nach unten, beim Zurückkommen von unten und beim Verlassen nach oben. Hier: abspielen, nichts, nichts, rückwärts."
    - "`markers: true` zeigt die Start- und End-Linien beim Entwickeln an."
    - "Ohne GSAP übernimmt ein `IntersectionObserver` die Lichtschranke, und eine CSS-Transition die Animation."
  mistake: "`markers: true` im fertigen Projekt vergessen. Und: ScrollTrigger in einem eigenen Scroll-Container benutzen, ohne `scroller` anzugeben. Dann beobachtet er das Fenster, und nichts passiert."
  when: "Für einfache Einblendungen reicht der `IntersectionObserver` mit CSS völlig. ScrollTrigger lohnt sich, sobald Timelines, `scrub` oder `pin` ins Spiel kommen."
  question: "Was bedeutet `start: \"center center\"`?"
  answer: "Die Animation startet, wenn die Mitte des Elements die Mitte des Fensters erreicht."
links:
  - text: "ScrollTrigger"
    url: "https://gsap.com/docs/v3/Plugins/ScrollTrigger/"
  - text: "IntersectionObserver (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/API/Intersection_Observer_API"
---
