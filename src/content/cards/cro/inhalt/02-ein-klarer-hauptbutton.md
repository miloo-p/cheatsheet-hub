---
title: "Ein klarer Hauptbutton"
description: "Mehrere gleich starke Buttons nebeneinander zwingen zum Nachdenken. Visuelle Hierarchie zeigt, was der nächste Schritt ist."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <div class="actions">
      <button class="btn">Jetzt kaufen</button>
      <button class="btn">Merken</button>
      <button class="btn">Teilen</button>
      <button class="btn">Vergleichen</button>
    </div>
  long: |-
    <div class="actions">
      <button class="btn btn-primary">In den Warenkorb</button>
      <button class="btn btn-ghost">Merken</button>
    </div>

    <style>
      .btn-primary { background: var(--brand); color: white; font-weight: 600; }
      .btn-ghost   { background: transparent; border: 1px solid currentColor; }
    </style>
explain:
  picture: "Ein Hauptbutton ist ein Wegweiser mit einem großen Schild für den Hauptweg und kleinen Schildern für Nebenwege. Stehen vier gleich große Schilder da, bleibt man stehen und liest."
  steps:
    - "Pro Bildschirmbereich gibt es einen primären Button, der sich durch Farbe, Füllung und Gewicht abhebt."
    - "Nebenaktionen werden zurückhaltend gestaltet: als Rahmen-Button, Textlink oder Icon mit Beschriftung."
    - "Die Reihenfolge folgt der Leserichtung. Der Hauptbutton steht dort, wo der Blick zuerst landet."
    - "Sehr seltene Aktionen wandern in ein Menü, statt Platz zu belegen."
  mistake: "Zwei Hauptbuttons mit unterschiedlichen Zielen nebeneinander, z.B. „Jetzt kaufen“ und „Newsletter abonnieren“. Sie konkurrieren um dieselbe Aufmerksamkeit."
  when: "Klickverteilung auf die Buttons, z.B. per Event mit `location`-Parameter, und die Rate des Hauptziels. Eine Heatmap zeigt zusätzlich, ob Leute auf Dinge klicken, die nicht klickbar sind."
  question: "Wie gestaltest du einen Löschen-Button in einem Bestätigungsdialog?"
  answer: "Als klar erkennbaren Button mit Warnfarbe und eindeutigem Text wie „Konto löschen“. „Abbrechen“ steht daneben als ruhigere Option."
links:
  - text: "Visual Hierarchy (NN/g, EN)"
    url: "https://www.nngroup.com/articles/visual-hierarchy-ux-definition/"
---
