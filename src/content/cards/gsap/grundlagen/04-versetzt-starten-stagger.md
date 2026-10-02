---
title: "Versetzt starten: `stagger`"
description: "Viele Elemente nacheinander statt gleichzeitig animieren, mit einer einzigen Zeile."
code:
  short: |-
    gsap.from(".item", {
      y: 20,
      autoAlpha: 0,
      stagger: 0.1,
    });
  long: |-
    document.querySelectorAll(".item").forEach((el, i) => {
      el.animate(
        [
          { transform: "translateY(20px)", opacity: 0 },
          { transform: "translateY(0)", opacity: 1 },
        ],
        { duration: 500, delay: i * 100, easing: "ease-out", fill: "backwards" }
      );
    });
demo:
  height: 90
  html: "<div class=\"row\" style=\"flex-wrap:wrap\"><div class=\"box item\"></div><div class=\"box item\"></div><div class=\"box item\"></div><div class=\"box item\"></div><div class=\"box item\"></div><div class=\"box item\"></div></div>"
  js: "gsap.from(\".item\", { y: 20, autoAlpha: 0, stagger: 0.1 });"
explain:
  picture: "`stagger` ist eine La-Ola-Welle im Stadion: Jeder macht dieselbe Bewegung, aber einen Augenblick nach dem Nachbarn."
  steps:
    - "`stagger: 0.1` startet jedes Element 0,1 Sekunden nach dem vorherigen."
    - "Die Gesamtdauer wächst mit der Anzahl: Bei 20 Elementen startet das letzte erst nach 1,9 Sekunden."
    - "Als Objekt lässt sich mehr steuern: `stagger: { each: 0.1, from: \"center\" }` startet in der Mitte und läuft nach außen. `amount: 1` verteilt alle Starts auf genau eine Sekunde, egal wie viele Elemente es sind."
    - "Ohne GSAP berechnest du die Verzögerung pro Element selbst aus dem Index."
  mistake: "`each` bei langen Listen verwenden. Bei 100 Einträgen dauert die Animation dann über 10 Sekunden, und Nutzer warten auf Inhalte. Für variable Listen ist `amount` sicherer."
  when: "GSAP, sobald du mit `from`, `amount` oder Raster-Staggers arbeiten willst. Für drei feste Elemente geht es auch mit CSS und `animation-delay`."
  question: "Wie animierst du ein Raster von innen nach außen?"
  answer: "Mit `stagger: { each: 0.05, grid: \"auto\", from: \"center\" }`. GSAP berechnet die Abstände im Raster selbst."
links:
  - text: "Staggers"
    url: "https://gsap.com/resources/getting-started/Staggers"
---
