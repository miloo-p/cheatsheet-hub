---
title: "Statistikfallen: Stichprobengröße und Peeking"
description: "Wer täglich auf das Dashboard schaut und bei „signifikant“ stoppt, findet fast immer einen Gewinner, auch wenn es keinen gibt."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: "// Tag 3: \"B liegt 18 % vorne, p < 0.05 – fertig, B gewinnt!\""
  long: |-
    // Vorher festlegen: Wie viele Besucher pro Variante?
    // Faustregel (Signifikanz 5 %, Power 80 %):
    //   n ≈ 16 · p · (1 − p) / δ²
    function sampleSize(baseRate, minEffect) {
      const delta = baseRate * minEffect;          // absoluter Unterschied
      return Math.ceil(16 * baseRate * (1 - baseRate) / delta ** 2);
    }

    sampleSize(0.03, 0.10);   // 3 % Basis, +10 % relativ
    // -> 51.734 Besucher pro Variante
    // Test erst danach auswerten, mindestens volle Wochen laufen lassen
lang:
  short: "js"
  long: "js"
explain:
  picture: "Peeking ist wie ein Münzwurf-Wettbewerb, bei dem du aufhörst, sobald Kopf zufällig vorne liegt. Wenn du nur oft genug nachschaust, liegt irgendwann jede Seite einmal vorn."
  steps:
    - "Ein p-Wert unter 0,05 bedeutet nur dann 5 % Irrtumswahrscheinlichkeit, wenn du genau einmal am geplanten Ende auswertest."
    - "Wer zwischendurch immer wieder prüft und beim ersten „signifikanten“ Ergebnis stoppt, erhöht die Fehlerquote stark. Evan Miller zeigt, dass aus 5 % so schnell über 25 % werden."
    - "Die Faustregel berechnet, wie viele Besucher pro Variante nötig sind, um einen bestimmten Unterschied zuverlässig zu erkennen."
    - "Kleine Effekte brauchen riesige Stichproben. Bei 3 % Conversion und +10 % relativem Effekt sind es über 50.000 Besucher pro Variante."
    - "Tests sollten volle Wochen laufen, weil sich Besucher am Wochenende anders verhalten als unter der Woche."
  mistake: "Auf einer Seite mit 500 Besuchern pro Woche A/B-Tests für kleine Textänderungen fahren. Das Ergebnis ist fast immer Zufall. Mit wenig Traffic lernst du mehr aus Nutzertests mit fünf Personen."
  when: "Stichprobe und Laufzeit vor dem Start festlegen und im Hypothesen-Dokument notieren. Für genaue Werte einen Rechner wie den von Evan Miller benutzen, die Faustregel dient nur zur Abschätzung."
  question: "Dein Test hat nach zwei Tagen ein signifikantes Ergebnis, geplant waren vier Wochen. Was tust du?"
  answer: "Weiterlaufen lassen. Ein frühes signifikantes Ergebnis ist bei häufigem Nachsehen sehr oft Zufall."
links:
  - text: "How Not To Run an A/B Test (Evan Miller, EN)"
    url: "https://www.evanmiller.org/how-not-to-run-an-ab-test.html"
  - text: "Stichprobenrechner (Evan Miller, EN)"
    url: "https://www.evanmiller.org/ab-testing/sample-size.html"
---
