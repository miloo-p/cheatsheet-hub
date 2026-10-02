---
title: "Text animieren: SplitText"
description: "Text in Zeilen, Wörter oder Buchstaben zerlegen und einzeln animieren, barrierefrei."
code:
  short: |-
    gsap.registerPlugin(SplitText);

    SplitText.create(".headline", {
      type: "words, chars",
      autoSplit: true,
      onSplit(self) {
        return gsap.from(self.chars, {
          y: 20, autoAlpha: 0, stagger: 0.03,
        });
      },
    });
  long: |-
    const el = document.querySelector(".headline");
    const text = el.textContent;
    el.setAttribute("aria-label", text);
    el.innerHTML = [...text].map(ch =>
      `<span aria-hidden="true" style="display:inline-block">${ch === " " ? "&nbsp;" : ch}</span>`
    ).join("");

    el.querySelectorAll("span").forEach((span, i) => {
      span.animate(
        [{ transform: "translateY(20px)", opacity: 0 }, { transform: "none", opacity: 1 }],
        { duration: 500, delay: i * 30, fill: "backwards" }
      );
    });
lang:
  long: "jsx"
demo:
  height: 90
  html: "<p class=\"headline\" style=\"font-family:var(--font-display);font-size:26px;font-weight:800;margin:0\">Hallo Bootcamp!</p>"
  js: "SplitText.create(\".headline\", { type: \"words, chars\", onSplit(self) { return gsap.from(self.chars, { y: 20, autoAlpha: 0, stagger: 0.03 }); } });"
explain:
  picture: "SplitText ist ein Setzkasten: Der Satz wird in einzelne Lettern zerlegt, damit jede für sich tanzen kann. Für Screenreader bleibt trotzdem der ganze Satz lesbar."
  steps:
    - "`type` legt fest, was zerlegt wird: `chars`, `words`, `lines` oder eine Kombination."
    - "Jedes Teil steckt danach in einem eigenen Element und ist über `self.chars`, `self.words` oder `self.lines` erreichbar."
    - "SplitText setzt automatisch `aria-label` auf das Original und blendet die Einzelteile für Screenreader aus."
    - "`autoSplit` zerlegt neu, wenn Schriften nachladen oder sich die Breite ändert. Dann verschieben sich nämlich Zeilenumbrüche. Die Animation aus `onSplit` wird dabei mitgeführt."
    - "Die ausführliche Variante zeigt das Prinzip mit Buchstaben. Zeilen korrekt zu erkennen ist von Hand deutlich schwieriger."
  mistake: "Text nach `lines` zerlegen, bevor die Webfont geladen ist. Dann stimmen die Zeilen nicht mehr, sobald die Schrift erscheint. `autoSplit: true` oder `document.fonts.ready` abwarten löst das."
  when: "SplitText für Überschriften und kurze Texte. Lange Fließtexte Buchstabe für Buchstabe zu animieren ist schwer lesbar und belastet die Leistung."
  question: "Was macht `split.revert()`?"
  answer: "Es stellt das ursprüngliche HTML wieder her und entfernt alle erzeugten Elemente. Wichtig beim Aufräumen, z.B. in React."
links:
  - text: "SplitText"
    url: "https://gsap.com/docs/v3/Plugins/SplitText/"
  - text: "GSAP-Lizenz"
    url: "https://gsap.com/licensing/"
---
