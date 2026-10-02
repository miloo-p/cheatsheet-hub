---
title: "Dark Patterns vermeiden"
description: "Tricks, die Nutzer zu ungewollten Entscheidungen drängen, kosten Vertrauen und sind in vielen Fällen unzulässig."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <label>
      <input type="checkbox" name="insurance" checked>
      Versicherung für 4,99 €/Monat
    </label>

    <button>Ja, ich will sparen!</button>
    <a class="tiny">Nein danke, ich zahle lieber den vollen Preis</a>
  long: |-
    <label>
      <input type="checkbox" name="insurance">
      Versicherung für 4,99 €/Monat hinzufügen
    </label>

    <button>Gutschein einlösen</button>
    <button class="btn-ghost">Ohne Gutschein fortfahren</button>

    <!-- Abos: Kündigen so leicht wie Abschließen -->
    <a href="/vertraege/kuendigen">Verträge hier kündigen</a>
explain:
  picture: "Dark Patterns sind wie ein Verkäufer, der dir unauffällig etwas zusätzlich in die Tüte legt. Kurzfristig steigt der Umsatz, langfristig kommt niemand wieder."
  steps:
    - "Vorausgewählte kostenpflichtige Zusatzleistungen sind in der EU unzulässig. Ein Häkchen für einen Aufpreis muss der Kunde selbst setzen."
    - "Confirmshaming macht die Ablehnung lächerlich („Nein, ich zahle lieber mehr“). Neutrale Texte für beide Optionen sind fair."
    - "Seit Juli 2022 schreibt § 312k BGB für online abschließbare Abos einen Kündigungsbutton vor, z.B. beschriftet mit „Verträge hier kündigen“."
    - "Weitere Muster: versteckte Kosten, erzwungene Konten, falsche Dringlichkeit und Abos, die sich nur per Brief kündigen lassen."
    - "Der Digital Services Act der EU verbietet Online-Plattformen ausdrücklich, ihre Oberflächen so zu gestalten, dass Nutzer getäuscht oder manipuliert werden."
  mistake: "Den Erfolg eines Dark Patterns an der kurzfristigen Conversion messen. Mehr Zusatzverkäufe sehen gut aus, bis Rücksendungen, Rückbuchungen und Beschwerden dazukommen."
  when: "Nicht nur Conversions messen, sondern auch Rückgaben, Kündigungen, Support-Anfragen und wiederkehrende Kunden. Faire Muster zeigen sich in diesen Zahlen langfristig besser."
  question: "Ist eine bereits angehakte Checkbox für den Newsletter erlaubt?"
  answer: "Nein. Eine Einwilligung muss aktiv erteilt werden, ein vorausgefülltes Häkchen reicht nach der DSGVO nicht."
links:
  - text: "§ 312k BGB (gesetze-im-internet.de)"
    url: "https://www.gesetze-im-internet.de/bgb/__312k.html"
  - text: "Deceptive Patterns (EN)"
    url: "https://www.deceptive.design/"
---
