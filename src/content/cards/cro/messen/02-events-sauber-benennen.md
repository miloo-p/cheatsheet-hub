---
title: "Events sauber benennen"
description: "Ein kleiner Tracking-Wrapper mit klaren Namen und Parametern macht Daten auswertbar und das Tool austauschbar."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <button onclick="gtag('event', 'click')">Jetzt testen</button>
    <button onclick="gtag('event', 'Click Button 2')">Preise</button>
    <button onclick="plausible('cta')">Kontakt</button>
  long: |-
    <button data-track="cta_click" data-track-location="hero">Jetzt testen</button>

    <script>
      // Ein Wrapper für alle Tools, mit Consent-Prüfung
      export function track(name, params = {}) {
        if (!hasConsent("analytics")) return;
        window.gtag?.("event", name, params);
      }

      document.addEventListener("click", (e) => {
        const el = e.target.closest("[data-track]");
        if (el) track(el.dataset.track, { location: el.dataset.trackLocation });
      });
    </script>
explain:
  picture: "Events sind wie Ordner in einem Archiv. Heißt jeder Ordner anders oder „Sonstiges“, findet später niemand etwas. Mit festen Namen und Etiketten lässt sich jede Frage beantworten."
  steps:
    - "Event-Namen in einem festen Schema, z.B. `objekt_aktion` in snake_case: `cta_click`, `form_submit`, `video_play`."
    - "Details gehören in Parameter, nicht in den Namen. Statt `hero_cta_click` und `footer_cta_click` ein Event `cta_click` mit `location`."
    - "Ein eigener `track()`-Wrapper kapselt das Tool. Ein Wechsel von Google Analytics zu Plausible oder Matomo ändert nur eine Funktion."
    - "Die Consent-Prüfung im Wrapper sorgt dafür, dass ohne Einwilligung nichts gesendet wird."
    - "`data-track`-Attribute halten das Tracking aus der Komponentenlogik heraus, ähnlich wie bei Event Delegation."
  mistake: "Personenbezogene Daten in Events schicken, z.B. E-Mail-Adressen als Parameter oder in der URL. Das ist datenschutzrechtlich heikel und bei Google Analytics ausdrücklich verboten."
  when: "Ein Tracking-Plan als Tabelle mit Event-Name, Parametern, Auslöser und Zweck, bevor du Code schreibst. Prüfen kannst du die Events im Netzwerk-Tab der Entwicklertools oder in der Debug-Ansicht des Tools."
  question: "Wie trackst du, dass jemand ein Formularfeld mit Fehler verlassen hat, ohne den eingegebenen Wert zu senden?"
  answer: "Mit einem Event wie `form_error` und Parametern für Feldname und Fehlerart, z.B. `{ field: \"email\", error: \"typeMismatch\" }`. Der Wert selbst bleibt im Browser."
links:
  - text: "Event Delegation (JS-Spickzettel)"
    url: "/js/#muster"
  - text: "dataset (MDN)"
    url: "https://developer.mozilla.org/de/docs/Web/API/HTMLElement/dataset"
---
