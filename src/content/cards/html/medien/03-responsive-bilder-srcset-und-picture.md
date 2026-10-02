---
title: "Responsive Bilder: `srcset` und `<picture>`"
description: "Der Browser lädt die passende Bildgröße, statt dem Handy das riesige Desktop-Bild zu schicken."
code:
  short: |-
    <img src="hero-800.jpg"
         srcset="hero-480.jpg 480w, hero-800.jpg 800w, hero-1600.jpg 1600w"
         sizes="(width < 48rem) 100vw, 50vw"
         alt="Bergpanorama bei Sonnenaufgang">
  long: |-
    <picture>
      <source media="(width < 30rem)" srcset="hero-480.jpg">
      <source media="(width < 64rem)" srcset="hero-800.jpg">
      <img src="hero-1600.jpg" alt="Bergpanorama bei Sonnenaufgang">
    </picture>
explain:
  picture: "`srcset` ist eine Speisekarte mit Portionsgrößen: Du bietest klein, mittel und groß an, und der Browser bestellt, was zu Bildschirm und Auflösung passt."
  steps:
    - "`srcset` listet die verfügbaren Dateien mit ihrer echten Breite: `480w` heißt 480 Pixel breit."
    - "`sizes` sagt, wie breit das Bild im Layout angezeigt wird: auf kleinen Bildschirmen die volle Breite, sonst die Hälfte."
    - "Aus beidem und der Pixeldichte des Displays wählt der Browser selbst die beste Datei."
    - "`<picture>` mit `<source media>` legt dagegen fest, welches Bild bei welcher Breite kommt. Das brauchst du, wenn sich der Bildausschnitt ändern soll (Art Direction) oder für moderne Formate wie AVIF mit Fallback."
  mistake: "`sizes` vergessen. Dann geht der Browser davon aus, dass das Bild `100vw` breit ist, und lädt auf großen Bildschirmen eine viel zu große Datei, auch wenn das Bild nur in einer schmalen Spalte steht."
  when: "`srcset` und `sizes` für dasselbe Motiv in verschiedenen Größen, das ist der häufigste Fall. `<picture>` für andere Ausschnitte je Bildschirm oder für Format-Fallbacks."
  question: "Wie lieferst du ein AVIF-Bild mit JPEG als Fallback aus?"
  answer: "Mit `<picture><source type=\"image/avif\" srcset=\"bild.avif\"><img src=\"bild.jpg\" alt=\"...\"></picture>`. Browser ohne AVIF-Unterstützung nehmen das `<img>`."
links:
  - text: "Responsive Bilder"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Responsive_images"
  - text: "<picture>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/picture"
---
