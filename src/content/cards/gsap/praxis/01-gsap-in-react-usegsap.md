---
title: "GSAP in React: `useGSAP`"
description: "Der offizielle Hook räumt Animationen automatisch auf und begrenzt Selektoren auf deine Komponente."
labels:
  - "Mit useGSAP"
  - "Mit useLayoutEffect"
code:
  short: |-
    import { useRef } from "react";
    import gsap from "gsap";
    import { useGSAP } from "@gsap/react";
    gsap.registerPlugin(useGSAP);

    function Hero() {
      const container = useRef(null);
      useGSAP(() => {
        gsap.from(".title", { y: 40, autoAlpha: 0 });
      }, { scope: container });

      return <section ref={container}><h1 className="title">Hallo</h1></section>;
    }
  long: |-
    import { useRef, useLayoutEffect } from "react";
    import gsap from "gsap";

    function Hero() {
      const container = useRef(null);
      useLayoutEffect(() => {
        const ctx = gsap.context(() => {
          gsap.from(".title", { y: 40, autoAlpha: 0 });
        }, container);
        return () => ctx.revert();   // Aufräumen beim Unmount
      }, []);

      return <section ref={container}><h1 className="title">Hallo</h1></section>;
    }
lang:
  short: "jsx"
  long: "jsx"
explain:
  picture: "`useGSAP` ist ein Hausmeister für deine Komponente: Er merkt sich jede Animation, die darin entsteht, und räumt sie weg, sobald die Komponente verschwindet."
  steps:
    - "`scope: container` sorgt dafür, dass `\".title\"` nur innerhalb dieser Komponente gesucht wird, nicht auf der ganzen Seite."
    - "Beim Unmount werden alle Animationen und ScrollTrigger aus dem Hook automatisch zurückgesetzt."
    - "Im Strict Mode führt React Effekte in der Entwicklung doppelt aus. Ohne Aufräumen laufen dann zwei Animationen gleichzeitig. `useGSAP` verhindert das."
    - "Animationen, die später entstehen, z.B. in einem `onClick`, wickelst du in `contextSafe()`, damit auch sie aufgeräumt werden."
    - "Die ausführliche Variante zeigt, was der Hook intern tut: `gsap.context()` plus `revert()` im Cleanup."
  mistake: "GSAP in einem normalen `useEffect` ohne Aufräumen benutzen. Im Strict Mode verdoppeln sich dann `from()`-Animationen, und Elemente bleiben unsichtbar, weil die zweite Animation den halb animierten Zustand als Ziel nimmt."
  when: "`useGSAP` in jedem React-Projekt mit GSAP. Die manuelle Variante nur, wenn du das Paket `@gsap/react` nicht installieren kannst."
  question: "Eine Animation soll bei Klick starten. Wie bindest du sie sauber ein?"
  answer: "Mit `const { contextSafe } = useGSAP({ scope: container });` und `const onClick = contextSafe(() => gsap.to(...));`. So wird auch sie beim Unmount aufgeräumt."
links:
  - text: "GSAP mit React"
    url: "https://gsap.com/resources/React/"
  - text: "gsap.context()"
    url: "https://gsap.com/docs/v3/GSAP/gsap.context()"
---
