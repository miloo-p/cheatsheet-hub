---
title: "Custom Properties"
description: "Werte einmal definieren und überall verwenden. Ändern musst du sie dann nur noch an einer Stelle."
code:
  short: |-
    :root {
      --brand: #2b5fae;
      --radius: 8px;
    }

    .button { background: var(--brand); border-radius: var(--radius); }
    .link   { color: var(--brand); }
  long: |-
    .button {
      background: #2b5fae;
      border-radius: 8px;
    }

    .link {
      color: #2b5fae;
    }
explain:
  picture: "Custom Properties sind wie Farbtöpfe mit Etikett. Statt jedes Mal den Farbton neu anzumischen, greifst du zum Topf „brand“. Tauschst du den Inhalt des Topfs, ändert sich die Farbe überall."
  steps:
    - "Eigenschaften, die mit `--` beginnen, sind selbst definierte Variablen."
    - "Auf `:root` (dem `<html>`-Element) definiert, gelten sie im ganzen Dokument, weil sie vererbt werden."
    - "`var(--brand)` setzt den Wert ein. Ein zweiter Wert dient als Ersatz: `var(--brand, blue)`."
    - "Variablen lassen sich für Bereiche überschreiben, z.B. `.dark { --brand: #8db4f2; }`. Alles darin nimmt dann automatisch den neuen Wert."
  mistake: "Variablen in der Bedingung einer Media Query benutzen: `@media (width >= var(--bp))` funktioniert nicht. In den Regeln innerhalb der Media Query darfst du sie aber ganz normal verwenden."
  when: "Custom Properties für alles, was mehrfach vorkommt: Farben, Abstände, Radien, Schriften. So funktionieren Dark Mode und Themes, auch auf diesen Spickzetteln."
  question: "Welche Farbe hat ein `.link` innerhalb von `.dark`, wenn dort `--brand: white` gesetzt ist?"
  answer: "Weiß. Die Variable wird vererbt, und innerhalb von `.dark` gilt der überschriebene Wert."
links:
  - text: "Custom Properties verwenden"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/Using_CSS_custom_properties"
  - text: "var()"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/var"
---
