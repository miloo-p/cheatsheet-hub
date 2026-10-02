---
title: "Springende Seiten vermeiden (CLS)"
description: "Wenn Inhalte beim Laden verrutschen, klicken Besucher daneben. Platz für spät ladende Elemente wird vorher reserviert."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <div id="banner"></div>   <!-- wird per JS mit 120px Inhalt gefüllt -->
    <img src="produkt.jpg" alt="...">
    <button>In den Warenkorb</button>
  long: |-
    <div id="banner" style="min-height: 120px"></div>
    <img src="produkt.jpg" alt="..." width="800" height="800">
    <button>In den Warenkorb</button>

    <style>
      /* Webfont mit ähnlicher Ersatzschrift, damit Text nicht springt */
      @font-face {
        font-family: "Brand";
        src: url("brand.woff2") format("woff2");
        font-display: swap;
      }
    </style>
explain:
  picture: "Ein Layout Shift ist wie ein Tisch, an den sich plötzlich jemand dazwischen setzt: Alle rutschen, und dein Teller landet beim Nachbarn. Wer vorher einen Stuhl freihält, verhindert das Rutschen."
  steps:
    - "CLS misst, wie stark sichtbare Elemente sich unerwartet verschieben. Gut ist ein Wert bis 0,1."
    - "Typische Ursachen: Bilder ohne Maße, nachgeladene Banner und Werbung, Webfonts mit anderer Breite, eingeblendete Hinweise oben auf der Seite."
    - "`width` und `height` an Bildern und `min-height` für nachgeladene Bereiche reservieren den Platz vorab."
    - "Cookie-Banner und Hinweise als Overlay unten einblenden statt oben in den Inhalt einzuschieben."
    - "Verschiebungen direkt nach einer Nutzeraktion, z.B. beim Aufklappen, zählen nicht als CLS."
  mistake: "Ein Banner „Kostenloser Versand ab 50 €“ nachträglich oben einfügen. Genau dann rutscht der „In den Warenkorb“-Button weg, während jemand darauf tippen will."
  when: "CLS im Feld mit `web-vitals` messen. Im Chrome-Performance-Panel zeigt die Spur „Layout Shifts“, welches Element sich verschoben hat und warum."
  question: "Ein Bild hat `width=\"800\" height=\"800\"`, wird aber per CSS mit `width: 100%` angezeigt. Springt es trotzdem?"
  answer: "Nein, solange im CSS auch `height: auto` gilt. Der Browser berechnet aus den Attributen das Seitenverhältnis und reserviert den passenden Platz."
links:
  - text: "CLS optimieren (web.dev, EN)"
    url: "https://web.dev/articles/optimize-cls"
  - text: "CSS-Spickzettel: aspect-ratio"
    url: "/css/#responsive"
---
