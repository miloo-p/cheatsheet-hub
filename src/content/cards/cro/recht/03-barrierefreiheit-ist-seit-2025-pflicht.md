---
title: "Barrierefreiheit ist seit 2025 Pflicht"
description: "Seit dem 28. Juni 2025 müssen viele Onlineshops und digitale Dienste für Verbraucher nach dem BFSG barrierefrei sein."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <div class="btn" onclick="addToCart()">
      <img src="cart.svg">
    </div>
    <input placeholder="E-Mail">
    <span style="color:#bbb">Nur noch heute!</span>
  long: |-
    <button type="button" onclick="addToCart()">
      <img src="cart.svg" alt=""> In den Warenkorb
    </button>
    <label for="email">E-Mail</label>
    <input id="email" type="email" autocomplete="email">
    <p class="notice">Angebot gilt bis 31.10.2026</p>   <!-- ausreichender Kontrast -->
explain:
  picture: "Barrierefreiheit ist eine Rampe neben der Treppe. Gebaut wird sie für Rollstuhlfahrer, aber sie hilft auch allen mit Kinderwagen oder Koffer. Genauso helfen klare Labels und Tastaturbedienung allen Besuchern."
  steps:
    - "Das Barrierefreiheitsstärkungsgesetz (BFSG) gilt u.a. für Dienstleistungen im elektronischen Geschäftsverkehr mit Verbrauchern, also typische Onlineshops."
    - "Ausgenommen sind Kleinstunternehmen, die Dienstleistungen erbringen: weniger als 10 Beschäftigte und höchstens 2 Mio. € Jahresumsatz."
    - "Maßstab ist die Norm EN 301 549, die auf die WCAG 2.1 in Stufe AA verweist."
    - "Verstöße können mit Bußgeldern bis 100.000 € geahndet werden."
    - "Fast alles, was dafür nötig ist, steht im HTML-Spickzettel: echte Buttons, Labels, Alternativtexte, Tastaturbedienung, sichtbarer Fokus und ausreichender Kontrast."
  mistake: "Barrierefreiheit als nachträgliches Projekt behandeln oder mit einem Overlay-Plugin „nachrüsten“. Solche Overlays beheben die Ursachen nicht. Barrierefreiheit entsteht im HTML und CSS, beim Bauen."
  when: "Lighthouse und axe DevTools für automatische Prüfungen, dazu einmal die ganze Bestellung nur mit der Tastatur und einmal mit einem Screenreader durchspielen. Automatische Tests finden nur einen Teil der Probleme."
  question: "Ein Shop eines Ein-Personen-Unternehmens mit 300.000 € Umsatz: Gilt das BFSG?"
  answer: "Für die Dienstleistung Onlineshop greift die Ausnahme für Kleinstunternehmen. Barrierefreiheit lohnt sich trotzdem, weil sie für alle die Bedienung verbessert."
links:
  - text: "BFSG (IHK Stuttgart)"
    url: "https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/it-recht/barrierefreie-webseiten-6200594"
  - text: "HTML-Spickzettel: Barrierefreiheit"
    url: "/html/#a11y"
  - text: "WCAG 2.1 (W3C, EN)"
    url: "https://www.w3.org/TR/WCAG21/"
---
