---
title: "Flüssig animieren: Transforms statt Layout"
description: "Manche Eigenschaften kann der Browser billig animieren, andere zwingen ihn bei jedem Bild zum Neuberechnen der Seite."
labels:
  - "Flüssig"
  - "Ruckelanfällig"
code:
  short: |-
    gsap.to(".box", {
      x: 200,          // transform: translateX
      scale: 1.2,      // transform: scale
      autoAlpha: 0.5,  // opacity
    });
  long: |-
    gsap.to(".box", {
      left: 200,       // Layout: Position neu berechnen
      width: 60,       // Layout: Größe neu berechnen
      marginTop: 20,   // Layout: alles darunter verschiebt sich
    });
demo:
  height: 150
  html: "<div class=\"col\"><div class=\"box good\"></div><div class=\"box warn bad\" style=\"position:relative;left:0\"></div><span class=\"note\">oben: transform · unten: left/width</span></div>"
  js: |-
    gsap.to(".good", { x: 200, scale: 1.2, duration: 1, repeat: 1, yoyo: true });
    gsap.to(".bad", { left: 200, width: 60, duration: 1, repeat: 1, yoyo: true });
explain:
  picture: "Transforms sind wie das Verschieben eines Fotos auf einem Leuchttisch. `left` und `width` sind, als würdest du für jedes Einzelbild die ganze Seite neu setzen und drucken."
  steps:
    - "Jedes Bild durchläuft Layout (Positionen berechnen), Paint (Pixel malen) und Composite (Ebenen zusammensetzen)."
    - "`transform` und `opacity` brauchen nur den letzten, günstigen Schritt. Die Grafikkarte erledigt das."
    - "`left`, `top`, `width`, `height` und `margin` lösen bei jedem Bild ein neues Layout aus, oft für die halbe Seite."
    - "Bei 60 Bildern pro Sekunde bleiben pro Bild etwa 16 Millisekunden. Layout-Animationen sprengen das schnell, besonders auf Handys."
  mistake: "`width` und `height` animieren, um etwas wachsen zu lassen. `scale` wirkt meist gleich und bleibt flüssig. Wenn sich die Größe wirklich ändern muss, z.B. weil Text umbrechen soll, ist Flip die bessere Wahl."
  when: "Immer zuerst `x`, `y`, `scale`, `rotation` und `autoAlpha`. Layout-Eigenschaften nur, wenn es nicht anders geht, und dann bei kleinen Elementen."
  question: "Wie prüfst du, ob eine Animation ruckelt?"
  answer: "In den Chrome-Entwicklertools unter „Performance“ aufzeichnen und nach langen Frames und lila Layout-Balken suchen. Oder unter „Rendering“ die Option „Frame Rendering Stats“ einschalten."
links:
  - text: "Rendering-Performance (web.dev, EN)"
    url: "https://web.dev/articles/rendering-performance"
---
