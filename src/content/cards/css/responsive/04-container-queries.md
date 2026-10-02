---
title: "Container Queries"
description: "Eine Komponente reagiert auf den Platz ihres Containers statt auf die Bildschirmbreite."
code:
  short: |-
    .card-list { container-type: inline-size; }

    @container (width >= 30rem) {
      .card { flex-direction: row; }
    }
  long: |-
    /* Pro Einsatzort eine eigene Regel */
    .main .card {
      flex-direction: row;
    }

    @media (width < 64rem) {
      .main .card {
        flex-direction: column;
      }
    }

    .sidebar .card {
      flex-direction: column;
    }
preview:
  height: 230
  sizes: [760, 460]
  html: |-
    <div class="page">
      <section class="card-list"><div class="card"><div class="img"></div><p>Hauptspalte: breit genug, Bild neben Text</p></div></section>
      <aside class="card-list"><div class="card"><div class="img"></div><p>Sidebar: schmal, Bild über Text</p></div></aside>
    </div>
    <p class="hint">Dieselbe Karte, zwei Container. Jede Karte richtet sich nach ihrem Platz.</p>
  css: |-
    .page { display: grid; grid-template-columns: 1fr 12rem; gap: 12px; }
    .card { display: flex; flex-direction: column; gap: 10px; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 10px; }

    .card-list { container-type: inline-size; }

    @container (width >= 30rem) {
      .card { flex-direction: row; }
    }

    .img { flex: 0 0 auto; width: 100%; max-width: 160px; aspect-ratio: 4 / 3; border-radius: 6px; background: linear-gradient(135deg, var(--brand), #f0c35a); }
    .card p { margin: 0; font-size: 13px; }
explain:
  picture: "Eine Media Query fragt: Wie groß ist das Zimmer? Eine Container Query fragt: Wie groß ist der Tisch, auf dem ich stehe? Für eine Karte ist der Tisch die wichtigere Frage."
  steps:
    - "`container-type: inline-size` macht ein Element zum Container, dessen Breite abgefragt werden kann."
    - "`@container (width >= 30rem)` greift, wenn dieser Container mindestens 30rem breit ist, egal wie breit der Bildschirm ist."
    - "Dieselbe Karte sieht in der schmalen Sidebar anders aus als im breiten Hauptbereich, ganz ohne Zusatzregeln."
    - "Die ausführliche Variante muss jeden Einsatzort einzeln kennen und mit eigenen Selektoren oder Media Queries behandeln."
  mistake: "Den Container selbst in seiner Container Query stylen wollen. Eine Container Query kann nur die Elemente darin verändern. Außerdem braucht die Abfrage `container-type` auf einem Vorfahren, sonst greift sie nie."
  when: "Container Queries für wiederverwendbare Komponenten wie Karten oder Widgets. Media Queries für das Seitenlayout als Ganzes."
  question: "Warum passen Container Queries so gut zu React-Komponenten?"
  answer: "Weil eine Komponente nicht wissen muss, wo sie eingebaut wird. Sie passt sich dem verfügbaren Platz an, ob in Sidebar, Modal oder Hauptbereich."
links:
  - text: "Container Queries"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_containment/Container_queries"
  - text: "container-type"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/container-type"
---
