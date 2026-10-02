---
title: "CSS Nesting"
description: "Regeln ineinander schreiben wie in Sass, aber direkt im Browser."
code:
  short: |-
    .card {
      padding: 1rem;

      & h2 { margin: 0; }
      &:hover { border-color: var(--brand); }

      @media (width >= 48rem) {
        padding: 2rem;
      }
    }
  long: |-
    .card {
      padding: 1rem;
    }
    .card h2 {
      margin: 0;
    }
    .card:hover {
      border-color: var(--brand);
    }
    @media (width >= 48rem) {
      .card {
        padding: 2rem;
      }
    }
preview:
  height: 150
  sizes: [375, 900]
  html: |-
    <article class="card"><h2>Verschachtelt</h2><p>Ab 48rem Breite wird das Padding größer. Mit der Maus drüberfahren färbt den Rahmen.</p></article>
  css: |-
    .card {
      padding: 1rem;

      & h2 { margin: 0; }
      &:hover { border-color: var(--brand); }

      @media (width >= 48rem) {
        padding: 2rem;
      }
    }

    .card { background: var(--surface); border: 2px solid var(--line); border-radius: 8px; }
    .card p { margin: 4px 0 0; color: var(--muted); }
explain:
  picture: "Nesting ist wie eine Ordnerstruktur: Alles, was zur Karte gehört, liegt im Ordner `.card` statt verstreut auf dem Schreibtisch."
  steps:
    - "Verschachtelte Regeln gelten nur innerhalb des äußeren Selektors."
    - "`&` steht für den äußeren Selektor. `&:hover` wird zu `.card:hover`, `& h2` zu `.card h2`."
    - "Auch Media Queries dürfen verschachtelt werden. Die Regeln darin gelten dann für `.card`."
    - "Der Browser rechnet das intern in die flache Form der ausführlichen Variante um."
  mistake: "Zu tief verschachteln. Fünf Ebenen erzeugen lange, sehr spezifische Selektoren, die später schwer zu überschreiben sind. Faustregel: höchstens zwei, drei Ebenen. Außerdem geht BEM-Verkettung wie `&__title` nur in Sass, nicht im nativen CSS."
  when: "Nesting hält Zusammengehöriges beisammen und läuft in allen aktuellen Browsern. Flaches CSS ist weiterhin völlig in Ordnung und in vielen Projekten Standard."
  question: "Was ergibt `.nav { & a { } }` als flacher Selektor?"
  answer: "`.nav a`, also alle Links innerhalb von `.nav`."
links:
  - text: "CSS Nesting verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_nesting/Using_CSS_nesting"
  - text: "Nesting-Selektor &"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Nesting_selector"
---
