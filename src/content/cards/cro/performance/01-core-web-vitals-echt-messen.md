---
title: "Core Web Vitals echt messen"
description: "Lighthouse auf dem eigenen Laptop ist ein Labortest. Entscheidend ist, wie schnell die Seite bei echten Besuchern ist."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    // Nur lokal: Lighthouse im schnellen Entwickler-Laptop
    // "Performance 98 – passt!"
  long: |-
    import { onLCP, onINP, onCLS } from "web-vitals";

    function send(metric) {
      navigator.sendBeacon("/api/vitals", JSON.stringify({
        name: metric.name,          // "LCP" | "INP" | "CLS"
        value: metric.value,
        rating: metric.rating,      // "good" | "needs-improvement" | "poor"
        page: location.pathname,
      }));
    }

    onLCP(send);
    onINP(send);
    onCLS(send);
lang:
  short: "js"
  long: "js"
explain:
  picture: "Lighthouse ist ein Probelauf im Trainingsraum. Echte Besucher laufen draußen, bei Regen, mit altem Handy und schlechtem Netz. Erst die Messung im Feld zeigt, wie es ihnen wirklich geht."
  steps:
    - "Die drei Core Web Vitals: LCP (Ladezeit des größten Inhalts, gut bis 2,5 s), INP (Reaktionszeit auf Eingaben, gut bis 200 ms) und CLS (Layoutverschiebungen, gut bis 0,1)."
    - "Bewertet wird das 75. Perzentil aller Seitenaufrufe, getrennt nach Mobil und Desktop. Drei von vier Besuchern sollen also eine gute Erfahrung haben."
    - "Die Bibliothek `web-vitals` misst die Werte im Browser echter Besucher (Real User Monitoring)."
    - "`sendBeacon` schickt die Daten auch dann zuverlässig, wenn die Seite gerade verlassen wird."
    - "Im Backend speicherst du die Werte und wertest das 75. Perzentil pro Seite aus."
  mistake: "Nur am eigenen Rechner mit Glasfaser testen. Für einen realistischen Labortest in den Chrome-Entwicklertools die Netzwerk- und CPU-Drosselung einschalten."
  when: "Pro Seitentyp (Startseite, Produktseite, Checkout) das 75. Perzentil von LCP, INP und CLS beobachten. Öffentliche Felddaten für größere Seiten liefert PageSpeed Insights aus dem Chrome UX Report."
  question: "Warum zählt das 75. Perzentil und nicht der Durchschnitt?"
  answer: "Weil ein Durchschnitt gute Werte vieler schneller Besuche mit sehr schlechten Werten weniger Besuche verrechnet. Das 75. Perzentil stellt sicher, dass die große Mehrheit eine gute Erfahrung hat."
links:
  - text: "Core Web Vitals (web.dev, EN)"
    url: "https://web.dev/articles/vitals"
  - text: "web-vitals (GitHub, EN)"
    url: "https://github.com/GoogleChrome/web-vitals"
  - text: "sendBeacon (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/API/Navigator/sendBeacon"
---
