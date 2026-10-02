---
title: "Kleben bleiben: `sticky`"
description: "Ein Header, der beim Scrollen oben stehen bleibt."
code:
  short: |-
    .site-header {
      position: sticky;
      top: 0;
    }
  long: |-
    .site-header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
    }
    body {
      padding-top: 4rem; /* Höhe des Headers */
    }
preview:
  height: 200
  html: |-
    <header class="site-header">Header bleibt oben kleben</header>
    <p class="hint">In der Vorschau scrollen.</p>
    <p>Absatz 1</p><p>Absatz 2</p><p>Absatz 3</p><p>Absatz 4</p><p>Absatz 5</p><p>Absatz 6</p><p>Absatz 7</p><p>Absatz 8</p><p>Absatz 9</p><p>Absatz 10</p>
  css: |-
    .site-header {
      position: sticky;
      top: 0;
    }

    body { padding-top: 0; }
    .site-header { background: var(--brand); color: var(--on-brand); font-weight: 600; padding: 10px 12px; margin: 0 -12px; }
    p { background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 8px; margin: 8px 0; }
explain:
  picture: "Ein Sticky-Element ist wie ein Post-it, das normal mitläuft, bis es oben am Bildschirmrand ankommt. Dort bleibt es kleben, solange sein Elternelement sichtbar ist."
  steps:
    - "`position: sticky` verhält sich zunächst wie ein normales Element im Fluss."
    - "Erreicht es beim Scrollen die Schwelle aus `top: 0`, bleibt es dort haften."
    - "Es klebt nur innerhalb seines Elternelements. Scrollt das Elternelement aus dem Bild, nimmt es den Header mit."
    - "`position: fixed` klebt dagegen immer am Fenster und nimmt keinen Platz im Fluss ein. Darum braucht die ausführliche Variante das `padding-top` auf `body`, sonst verschwindet der Seitenanfang unter dem Header."
  mistake: "Sticky scheint nicht zu funktionieren, weil ein Vorfahre `overflow: hidden` oder `overflow: auto` hat. Dann klebt das Element an diesem Container statt am Fenster. Ebenfalls häufig: Der Schwellenwert `top` fehlt."
  when: "`sticky` für Header, Tabellenköpfe und Inhaltsverzeichnisse. `fixed` für Elemente, die unabhängig vom Layout immer sichtbar sein sollen, z.B. einen Chat-Button unten rechts."
  question: "Warum bleibt ein Sticky-Header nicht stehen, wenn er das einzige Kind eines niedrigen `<div>` ist?"
  answer: "Weil er nur innerhalb seines Elternelements kleben kann. Ist das Elternelement nicht höher als der Header, hat er keinen Weg, den er zurücklegen könnte."
links:
  - text: "position"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/position"
---
