---
title: "A/B-Tests technisch sauber"
description: "Jeder Besucher muss dauerhaft dieselbe Variante sehen, und die Zuteilung darf die Seite nicht flackern lassen."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <script>
      // bei jedem Seitenaufruf neu würfeln
      if (Math.random() < 0.5) {
        document.querySelector(".cta").textContent = "Jetzt starten";
      }
    </script>
  long: |-
    // Server (Express): einmal zuteilen, im Cookie merken
    app.use((req, res, next) => {
      let variant = req.cookies.exp_cta;
      if (!variant) {
        variant = Math.random() < 0.5 ? "A" : "B";
        res.cookie("exp_cta", variant, { maxAge: 30 * 864e5, sameSite: "lax" });
      }
      res.locals.variant = variant;   // Template rendert direkt die richtige Variante
      next();
    });

    // Client: Zuteilung als Event melden, wenn die Variante sichtbar ist
    track("experiment_view", { experiment: "cta_text", variant });
lang:
  long: "js"
explain:
  picture: "Ein A/B-Test ist ein Experiment mit zwei Gruppen. Wechselt ein Teilnehmer bei jedem Besuch die Gruppe, weißt du am Ende nicht mehr, welche Variante gewirkt hat. Die Zuteilung muss so fest sein wie eine Namensliste."
  steps:
    - "Bei `Math.random()` pro Seitenaufruf sieht dieselbe Person mal A, mal B. Die Ergebnisse vermischen sich."
    - "Die Zuteilung wird einmal getroffen und gespeichert, z.B. im Cookie oder anhand einer gehashten Nutzer-ID."
    - "Serverseitig ausgeliefert gibt es kein Flackern. Clientseitige Tests tauschen Inhalte erst nach dem Laden aus, und Besucher sehen kurz die Originalvariante."
    - "Das `experiment_view`-Event zählt nur Besucher, die die Variante wirklich gesehen haben. Wer nie bis zum Button scrollt, gehört nicht in die Auswertung."
    - "Auch das Test-Cookie braucht eine rechtliche Grundlage. Kläre mit dem Datenschutz, ob dafür eine Einwilligung nötig ist."
  mistake: "Den Test mitten im Lauf ändern, z.B. die Variante B nachbessern. Dann vergleichst du ab da etwas anderes, und die gesammelten Daten passen nicht mehr zusammen."
  when: "Wenige, gut begründete Tests mit großer Änderung bringen mehr als viele kleine. Für einen A/A-Test (zweimal dieselbe Variante) lohnt sich ein Probelauf: Zeigt er einen „Gewinner“, stimmt etwas am Aufbau nicht."
  question: "Warum misst du `experiment_view` und nicht einfach alle Seitenaufrufe?"
  answer: "Weil nur Besucher, die die Variante gesehen haben, von ihr beeinflusst werden konnten. Alle anderen verwässern das Ergebnis."
links:
  - text: "res.cookie (Express, EN)"
    url: "https://expressjs.com/en/api.html#res.cookie"
---
