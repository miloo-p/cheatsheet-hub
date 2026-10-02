---
title: "Bilder richtig einbinden"
description: "Alternativtext, feste Maße und Lazy Loading sorgen dafür, dass Bilder zugänglich sind und die Seite nicht springt."
code:
  short: |-
    <img src="team.jpg" alt="Das Team beim Hackathon"
         width="800" height="450" loading="lazy">
  long: |-
    <img class="lazy" data-src="team.jpg" alt="Das Team beim Hackathon"
         style="width: 800px; height: 450px">

    <script>
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.src = entry.target.dataset.src;
            observer.unobserve(entry.target);
          }
        });
      });
      document.querySelectorAll("img.lazy").forEach(img => observer.observe(img));
    </script>
explain:
  picture: "`width` und `height` sind eine Tischreservierung im Restaurant: Der Platz ist frei gehalten, bevor der Gast kommt. Ohne Reservierung rücken alle zusammen, sobald er erscheint, und die Seite springt."
  steps:
    - "`alt` beschreibt, was das Bild zeigt. Screenreader lesen es vor, und es erscheint, wenn das Bild nicht lädt."
    - "Rein dekorative Bilder bekommen `alt=\"\"`, dann werden sie übersprungen."
    - "`width` und `height` geben das Seitenverhältnis vor. Der Browser reserviert den Platz, bevor das Bild geladen ist. Per CSS kann es trotzdem responsiv skalieren."
    - "`loading=\"lazy\"` lädt das Bild erst, wenn es in die Nähe des sichtbaren Bereichs kommt. Die ausführliche Variante baut genau das mit JavaScript nach."
  mistake: "`alt` ganz weglassen. Dann liest der Screenreader oft den Dateinamen vor, z.B. „IMG-4711.jpg“. Ebenfalls ungünstig: `loading=\"lazy\"` beim großen Bild ganz oben. Das verzögert genau das Bild, das man zuerst sieht."
  when: "Immer die native Variante. Lazy Loading nur für Bilder weiter unten auf der Seite."
  question: "Welcher `alt`-Text passt zu einem Lupen-Icon in einem Suchbutton?"
  answer: "Einer, der die Funktion beschreibt, also „Suchen“ und nicht „Lupe“. Bei Bildern in Links und Buttons zählt, was passiert."
links:
  - text: "<img>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/img"
  - text: "HTML und Barrierefreiheit"
    url: "https://developer.mozilla.org/de/docs/Learn_web_development/Core/Accessibility/HTML"
---
