---
title: "Das Hauptbild schnell laden (LCP)"
description: "Das größte Element im sichtbaren Bereich, meist ein Hero-Bild, bestimmt den LCP. Es braucht Vorrang statt Verzögerung."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: "<img src=\"hero-2400.jpg\" alt=\"...\" loading=\"lazy\">"
  long: |-
    <link rel="preload" as="image" href="hero-1200.avif"
          imagesrcset="hero-800.avif 800w, hero-1200.avif 1200w"
          imagesizes="100vw">

    <img src="hero-1200.avif"
         srcset="hero-800.avif 800w, hero-1200.avif 1200w"
         sizes="100vw"
         width="1200" height="600"
         fetchpriority="high"
         alt="...">
explain:
  picture: "Der Browser lädt Dinge in einer Warteschlange. Das Hauptbild ist der wichtigste Gast, und `fetchpriority=\"high\"` ist der VIP-Eingang. `loading=\"lazy\"` schickt ihn dagegen ans Ende der Schlange."
  steps:
    - "`loading=\"lazy\"` beim Hauptbild verzögert genau das Element, das den LCP bestimmt."
    - "`fetchpriority=\"high\"` sagt dem Browser, dass dieses Bild vor anderen Ressourcen geladen werden soll."
    - "`<link rel=\"preload\">` im `<head>` startet den Download, bevor der Browser das `<img>` im HTML erreicht. Das hilft vor allem bei Bildern, die per CSS oder JavaScript eingebunden werden."
    - "Moderne Formate wie AVIF oder WebP und eine passende Größe per `srcset` sparen oft mehr als die Hälfte der Datenmenge."
    - "`width` und `height` reservieren den Platz und verhindern einen Layout Shift."
  mistake: "Das Hauptbild per JavaScript nachladen, z.B. in einem Slider, der erst nach dem Framework-Start initialisiert wird. Dann wartet der LCP auf das ganze JavaScript."
  when: "LCP-Wert und LCP-Element im Performance-Panel der Chrome-Entwicklertools prüfen. Dort steht, welches Element als größtes gilt und wie lange es gedauert hat."
  question: "Ein Hero hat ein Hintergrundbild per CSS `background-image`. Wie beschleunigst du es?"
  answer: "Mit `<link rel=\"preload\" as=\"image\" href=\"…\" fetchpriority=\"high\">` im `<head>`. Sonst entdeckt der Browser das Bild erst, nachdem er das CSS geladen und ausgewertet hat."
links:
  - text: "LCP optimieren (web.dev, EN)"
    url: "https://web.dev/articles/optimize-lcp"
  - text: "fetchpriority (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/img#fetchpriority"
---
