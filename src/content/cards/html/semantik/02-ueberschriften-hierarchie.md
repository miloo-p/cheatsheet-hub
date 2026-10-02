---
title: "Überschriften-Hierarchie"
description: "Überschriften bilden das Inhaltsverzeichnis der Seite. Die Ebene richtet sich nach der Struktur, nicht nach der Schriftgröße."
code:
  short: |-
    <h1>Meine Todos</h1>
    <h2>Heute</h2>
    <h3>Arbeit</h3>
    <h3>Privat</h3>
    <h2>Diese Woche</h2>
  long: |-
    <div class="title-xl" role="heading" aria-level="1">Meine Todos</div>
    <div class="title-l" role="heading" aria-level="2">Heute</div>
    <div class="title-m" role="heading" aria-level="3">Arbeit</div>
    <div class="title-m" role="heading" aria-level="3">Privat</div>
    <div class="title-l" role="heading" aria-level="2">Diese Woche</div>
explain:
  picture: "Die Überschriften sind die Gliederung eines Buches: Kapitel, Unterkapitel, Abschnitte. Screenreader-Nutzer springen durch diese Gliederung wie durch ein Inhaltsverzeichnis."
  steps:
    - "`<h1>` ist der Titel der Seite, meist genau einer."
    - "Darunter folgen `<h2>` für Hauptabschnitte, `<h3>` für Unterabschnitte und so weiter."
    - "Ebenen sollten nicht übersprungen werden: Auf `<h2>` folgt `<h3>`, nicht `<h5>`."
    - "Wie groß eine Überschrift aussieht, regelst du mit CSS, nicht mit der Ebene."
  mistake: "Die Ebene nach der gewünschten Größe wählen, z.B. `<h4>`, weil es kleiner aussieht. Dann stimmt die Gliederung nicht mehr, und Screenreader-Nutzer verlieren die Orientierung."
  when: "Immer echte `<h1>` bis `<h6>`. Die Variante mit `role=\"heading\"` zeigt nur, wie viel Aufwand der Nachbau eines nativen Elements kostet."
  question: "Eine Karte unter einem `<h2>` soll eine kleine Überschrift bekommen. Welche Ebene nimmst du?"
  answer: "`<h3>`, weil sie inhaltlich unter dem `<h2>` liegt. Die kleine Darstellung erledigt CSS."
links:
  - text: "<h1> bis <h6>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/Heading_Elements"
  - text: "HTML und Barrierefreiheit"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Accessibility/HTML"
---
