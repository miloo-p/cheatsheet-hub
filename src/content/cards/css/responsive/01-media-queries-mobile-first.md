---
title: "Media Queries, mobile-first"
description: "Erst die Handy-Version schreiben, dann für größere Bildschirme erweitern."
code:
  short: |-
    .nav { flex-direction: column; }

    @media (width >= 48rem) {
      .nav { flex-direction: row; }
    }
  long: |-
    .nav {
      flex-direction: column;
    }

    @media screen and (min-width: 48rem) {
      .nav {
        flex-direction: row;
      }
    }
preview:
  height: 170
  sizes: [375, 900]
  html: |-
    <nav class="nav"><a href="#">Start</a><a href="#">Kurse</a><a href="#">Termine</a><a href="#">Kontakt</a></nav>
    <p class="hint">Schmal untereinander, ab 48rem nebeneinander.</p>
  css: |-
    .nav { flex-direction: column; }

    @media (width >= 48rem) {
      .nav { flex-direction: row; }
    }

    .nav { display: flex; gap: 6px; }
    .nav a { background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 6px 12px; color: var(--fg); text-decoration: none; font-weight: 600; }
explain:
  picture: "Mobile-first ist wie Kofferpacken: Erst das Nötigste ins Handgepäck, und wenn mehr Platz da ist, kommt Zusätzliches dazu."
  steps:
    - "Die Regeln außerhalb der Media Query gelten für alle Bildschirme, also auch fürs Handy."
    - "Die Media Query ergänzt Regeln ab einer Mindestbreite."
    - "`width >= 48rem` ist die neue Bereichsschreibweise und bedeutet dasselbe wie `min-width: 48rem`."
    - "`screen` beschränkt auf Bildschirme. Weil `all` der Standard ist, lässt man es meist weg."
  mistake: "Das Viewport-Meta-Tag im HTML vergessen: `<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">`. Ohne es tut das Handy so, als sei es etwa 980px breit, und deine Media Queries für kleine Bildschirme greifen nicht."
  when: "Die Bereichsschreibweise ist kürzer und bei Spannen wie `(30rem <= width < 60rem)` viel lesbarer. Alle aktuellen Browser können sie. `min-width` steht in fast jedem älteren Projekt."
  question: "Warum ist es sinnvoll, Breakpoints in `rem` oder `em` statt in `px` anzugeben?"
  answer: "Wenn jemand die Schrift im Browser vergrößert, greifen die Breakpoints entsprechend früher. Das Layout bricht dann um, bevor der Text gequetscht wird."
links:
  - text: "@media"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/@media"
  - text: "Media Queries verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_media_queries/Using_media_queries"
---
