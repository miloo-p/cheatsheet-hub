---
title: "An den Scroll koppeln: `scrub`"
description: "Die Animation läuft genau so weit, wie gescrollt wurde, vor und zurück."
code:
  short: |-
    gsap.to(".progress", {
      scaleX: 1,
      ease: "none",
      scrollTrigger: {
        trigger: "article",
        start: "top top",
        end: "bottom bottom",
        scrub: true,
      },
    });
  long: |-
    const bar = document.querySelector(".progress");
    const article = document.querySelector("article");

    window.addEventListener("scroll", () => {
      const rect = article.getBoundingClientRect();
      const total = rect.height - window.innerHeight;
      const progress = Math.min(Math.max(-rect.top / total, 0), 1);
      bar.style.transform = `scaleX(${progress})`;
    }, { passive: true });
demo:
  height: 200
  html: "<div class=\"scroller\"><div class=\"box progress\" style=\"position:sticky;top:0;width:100%;height:8px;transform:scaleX(0);transform-origin:left;z-index:1\"></div><div class=\"spacer\">↓ scrollen</div><div class=\"spacer\">weiter …</div><div class=\"spacer\">fast geschafft</div></div>"
  js: |-
    const scroller = stage.querySelector(".scroller");
    gsap.to(".progress", { scaleX: 1, ease: "none", scrollTrigger: { trigger: scroller.firstElementChild.nextElementSibling, scroller, start: "top top", end: () => "+=" + (scroller.scrollHeight - scroller.clientHeight), scrub: true } });
explain:
  picture: "Mit `scrub` wird die Scrollleiste zum Abspielregler eines Videos. Scrollst du ein Stück nach unten, läuft das Video ein Stück weiter. Scrollst du zurück, spult es zurück."
  steps:
    - "`scrub: true` verbindet den Fortschritt der Animation direkt mit der Scrollposition zwischen `start` und `end`."
    - "`scrub: 1` glättet die Kopplung: Die Animation braucht eine Sekunde, um zur Scrollposition aufzuholen. Das wirkt weicher."
    - "`ease: \"none\"` ist hier wichtig, sonst läuft die Animation an manchen Scrollstellen schneller als an anderen."
    - "Ohne GSAP rechnest du den Fortschritt im Scroll-Event selbst aus. Modernes CSS kann das auch mit `animation-timeline: scroll()`, das wird aber noch nicht in allen Browsern unterstützt."
  mistake: "Bei `scrub` ein Easing wie `power2.out` stehen lassen. Dann passt der Fortschritt nicht mehr gleichmäßig zum Scrollen, und es fühlt sich an, als würde die Seite haken."
  when: "`scrub` für Fortschrittsbalken, Parallax und Scroll-Geschichten. Für einen einfachen Lesefortschritt lohnt sich ein Blick auf CSS Scroll-Driven Animations."
  question: "Was ist der Unterschied zwischen `scrub: true` und `scrub: 0.5`?"
  answer: "Bei `true` folgt die Animation exakt und sofort. Bei `0.5` braucht sie eine halbe Sekunde zum Aufholen und wirkt dadurch gedämpft."
links:
  - text: "ScrollTrigger: scrub"
    url: "https://gsap.com/docs/v3/Plugins/ScrollTrigger/"
  - text: "Scroll-Driven Animations (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_scroll-driven_animations"
---
