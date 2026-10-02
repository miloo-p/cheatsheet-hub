---
title: "Container zentrieren"
description: "Ein Block mit Maximalbreite wird mit automatischem Außenabstand links und rechts mittig gesetzt."
code:
  short: |-
    .container {
      max-width: 70rem;
      margin-inline: auto;
      padding-inline: 1rem;
    }
  long: |-
    .container {
      max-width: 70rem;
      margin-left: auto;
      margin-right: auto;
      padding-left: 1rem;
      padding-right: 1rem;
    }
preview:
  height: 170
  sizes: [1440, 375]
  html: |-
    <div class="container">
      <h2>Inhalt bleibt lesbar</h2>
      <p>Höchstens 70rem breit und mittig. Auf schmalen Bildschirmen sorgt das Padding für Abstand zum Rand.</p>
    </div>
  css: |-
    .container {
      max-width: 70rem;
      margin-inline: auto;
      padding-inline: 1rem;
    }

    body { padding: 24px 0; background: repeating-linear-gradient(45deg, var(--bg) 0 10px, var(--surface) 10px 20px); }
    .container { background: var(--surface); border-inline: 2px solid var(--brand); padding-block: 1px; }
    h2 { margin: 12px 0 4px; font-size: 22px; }
    p { margin: 0 0 12px; color: var(--muted); }
explain:
  picture: "Zwei gleich starke Federn links und rechts drücken den Block in die Mitte. `auto` heißt: Nimm dir den restlichen Platz, und beide Seiten teilen ihn gerecht."
  steps:
    - "`max-width` begrenzt die Breite. Auf kleinen Bildschirmen wird der Container schmaler, auf großen nie breiter als 70rem."
    - "`margin-left: auto` und `margin-right: auto` verteilen den übrigen Platz gleichmäßig auf beide Seiten."
    - "`margin-inline` ist die logische Kurzform für beide Seiten in Schreibrichtung. In Sprachen, die von rechts nach links laufen, passt sie sich automatisch an."
    - "Das `padding-inline` sorgt dafür, dass der Text auf dem Handy nicht am Rand klebt."
  mistake: "`margin: auto` bei einem Element ohne Breitenbegrenzung benutzen und erwarten, dass es sich zentriert. Ein Block-Element ist standardmäßig so breit wie sein Elternelement, es gibt also keinen Platz zum Verteilen."
  when: "`margin-inline` und `padding-inline` sind kürzer und moderner. Die Varianten mit `left` und `right` stehen in älterem Code und funktionieren genauso."
  question: "Zentriert `margin-inline: auto` einen Block auch vertikal?"
  answer: "Nein. Im normalen Block-Layout wirkt `auto` nur horizontal. Für vertikales Zentrieren brauchst du Flexbox oder Grid."
links:
  - text: "margin-inline"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/margin-inline"
  - text: "Logische Eigenschaften"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_logical_properties_and_values"
  - text: "max-width"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/max-width"
---
