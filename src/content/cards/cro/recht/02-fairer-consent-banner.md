---
title: "Fairer Consent-Banner"
description: "Nach § 25 TDDDG brauchen nicht notwendige Cookies und Tracking eine Einwilligung. Ablehnen muss so einfach sein wie Zustimmen."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <div class="cookie-banner">
      <button class="big-green">Alle akzeptieren</button>
      <a class="tiny-grey" href="/einstellungen">Einstellungen</a>
    </div>

    <!-- Tracking läuft schon vor der Entscheidung -->
    <script src="https://www.googletagmanager.com/gtag/js?id=G-XXXX"></script>
  long: |-
    <div class="cookie-banner" role="dialog" aria-labelledby="cb-title">
      <h2 id="cb-title">Darf ich Statistiken erheben?</h2>
      <p>Hilft mir, die Seite zu verbessern. <a href="/datenschutz">Details</a></p>
      <button data-consent="reject">Ablehnen</button>
      <button data-consent="accept">Akzeptieren</button>
    </div>

    <script>
      // Tracking erst nach Zustimmung laden
      function loadAnalytics() {
        const s = document.createElement("script");
        s.src = "https://www.googletagmanager.com/gtag/js?id=G-XXXX";
        document.head.appendChild(s);
      }
      if (localStorage.getItem("consent") === "accept") loadAnalytics();
    </script>
explain:
  picture: "Ein Consent-Banner ist eine Tür mit zwei Klinken: „Ja“ und „Nein“. Sie müssen gleich groß sein und gleich leicht zu drücken. Ein „Nein“, das man erst hinter einer zweiten Tür findet, ist keine echte Wahl."
  steps:
    - "Seit Mai 2024 heißt das TTDSG Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG). § 25 verlangt eine Einwilligung, bevor Informationen auf dem Gerät gespeichert oder ausgelesen werden, außer sie sind unbedingt erforderlich."
    - "Unbedingt erforderlich sind z.B. Warenkorb- oder Login-Cookies. Analyse- und Marketing-Tracking gehören nicht dazu."
    - "Datenschutzbehörden verlangen, dass Ablehnen und Zustimmen gleichwertig angeboten werden, ohne Extra-Klicks und ohne optische Benachteiligung."
    - "Technisch heißt das: Tracking-Skripte werden erst nach der Zustimmung geladen. Ein Skript, das schon im HTML steht, hat bereits Daten gesendet."
    - "Die Entscheidung muss sich später ändern lassen, z.B. über einen Link im Footer."
  mistake: "Das Tracking-Skript direkt im `<head>` laden und den Banner nur zur Deko anzeigen. Im Netzwerk-Tab ist sofort zu sehen, dass Anfragen an das Tracking-Tool rausgehen, bevor jemand zugestimmt hat."
  when: "Im Netzwerk-Tab prüfen, dass vor der Zustimmung keine Anfragen an Tracking-Dienste gehen. Die Zustimmungsrate selbst kannst du zählen, ohne Personen zu tracken, z.B. als serverseitigen Zähler."
  question: "Brauchst du für ein Warenkorb-Cookie eine Einwilligung?"
  answer: "Nein. Ohne das Cookie funktioniert der vom Nutzer gewünschte Dienst nicht, es ist unbedingt erforderlich."
links:
  - text: "§ 25 TDDDG (gesetze-im-internet.de)"
    url: "https://www.gesetze-im-internet.de/ttdsg/__25.html"
  - text: "TDDDG-Überblick (eRecht24)"
    url: "https://www.e-recht24.de/datenschutz/12834-tdddg.html"
---
