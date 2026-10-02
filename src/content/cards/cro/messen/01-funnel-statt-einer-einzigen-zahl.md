---
title: "Funnel statt einer einzigen Zahl"
description: "Die Conversion Rate sagt, wie viele kaufen. Der Funnel sagt, wo die anderen aussteigen."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    // Nur das Endergebnis messen
    track("purchase");

    // Auswertung: 2 % Conversion Rate.
    // Aber warum nicht mehr? Keine Ahnung.
  long: |-
    // Jeden Schritt messen
    track("view_product",   { id });
    track("add_to_cart",    { id, value });
    track("begin_checkout", { value });
    track("add_shipping");
    track("add_payment");
    track("purchase",       { value, orderId });

    // Auswertung: 40 % springen bei add_shipping ab
    // -> Versandkosten früher zeigen?
lang:
  short: "js"
  long: "js"
explain:
  picture: "Ein Funnel ist ein Trichter mit Löchern. Nur zu zählen, was unten herauskommt, hilft wenig. Erst wenn du an jeder Stufe misst, siehst du, wo das größte Loch ist."
  steps:
    - "Conversion Rate = Conversions ÷ Besuche. Was als Conversion zählt, legst du fest: Kauf, Anmeldung, Anfrage."
    - "Makro-Conversions sind die Hauptziele (Kauf). Mikro-Conversions sind Zwischenschritte (in den Warenkorb, Newsletter, Video angesehen)."
    - "Ein Funnel misst jeden Schritt einzeln. Die Abbruchrate pro Schritt zeigt, wo du ansetzen solltest."
    - "Die Event-Namen im Beispiel folgen den empfohlenen E-Commerce-Events von Google Analytics 4. Einheitliche Namen machen Auswertungen und Toolwechsel einfacher."
  mistake: "Nur Seitenaufrufe messen. Ein Aufruf der Checkout-Seite sagt nicht, ob jemand das Formular ausgefüllt, einen Fehler bekommen oder abgebrochen hat. Wichtige Schritte brauchen eigene Events."
  when: "Im Analytics-Tool einen Trichter aus den Events anlegen und die Abbruchrate je Schritt vergleichen, getrennt nach Mobil und Desktop. Oft unterscheiden sich die Probleme stark."
  question: "Wo setzt du an, wenn 1000 Leute in den Warenkorb legen, 900 den Checkout starten und 300 kaufen?"
  answer: "Im Checkout. Zwischen Start und Kauf gehen zwei Drittel verloren, das ist das größte Loch."
links:
  - text: "GA4: empfohlene Events (EN)"
    url: "https://developers.google.com/analytics/devguides/collection/ga4/reference/events"
  - text: "Kaufabbrüche (Baymard, EN)"
    url: "https://baymard.com/lists/cart-abandonment-rate"
---
