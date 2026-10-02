---
title: "Ebenen ordnen: `z-index` und `isolation`"
description: "Ebenen ordnen, ohne dass sich `z-index`-Werte quer durch die Seite ins Gehege kommen."
code:
  short: |-
    .card {
      isolation: isolate;
    }
    .card .badge {
      position: absolute;
      z-index: 1;
    }
  long: |-
    .card {
      position: relative;
      z-index: 0;
    }
    .card .badge {
      position: absolute;
      z-index: 1;
    }
preview:
  height: 200
  html: |-
    <div class="menu">Dropdown-Menü (z-index: 1)</div>
    <div class="grid">
      <div class="card plain"><span class="badge">Neu</span>ohne isolation</div>
      <div class="card"><span class="badge">Neu</span>mit isolation</div>
    </div>
    <p class="hint">Links drängelt sich das Badge über das Menü, rechts bleibt es in seiner Karte.</p>
  css: |-
    .card {
      isolation: isolate;
    }
    .card .badge {
      position: absolute;
      z-index: 1;
    }

    .card.plain { isolation: auto; }

    .menu { position: absolute; z-index: 1; top: 30px; left: 12px; right: 12px; padding: 20px 12px; border-radius: 8px;
            background: var(--surface); border: 1px solid var(--line); box-shadow: 0 8px 24px rgb(0 0 0 / .2); font-weight: 600; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-top: 12px; }
    .card { position: relative; background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 70px 10px 10px; font-size: 12px; color: var(--muted); }
    .badge { top: 26px; right: 10px; background: crimson; color: #fff; font-size: 12px; font-weight: 700; padding: 2px 8px; border-radius: 999px; }
explain:
  picture: "Ein Stapelkontext ist wie ein Ordner auf dem Schreibtisch. Die Blätter im Ordner kannst du beliebig sortieren, aber der Ordner liegt als Ganzes im Stapel. Ein Blatt mit `z-index: 9999` kommt nicht aus seinem Ordner heraus."
  steps:
    - "`z-index` wirkt nur bei positionierten Elementen sowie bei Flex- und Grid-Items."
    - "Bestimmte Eigenschaften erzeugen einen neuen Stapelkontext, z.B. `position` mit `z-index`, `opacity` unter 1, `transform` oder `isolation: isolate`."
    - "Alle `z-index`-Werte innerhalb eines Kontexts gelten nur dort."
    - "`isolation: isolate` erzeugt diesen Kontext ohne Nebenwirkungen. Die ausführliche Variante braucht dafür `position` und `z-index`."
  mistake: "`z-index` immer weiter erhöhen (`999`, `99999`), weil ein Element nicht nach vorne kommt. Meist liegt es in einem Stapelkontext, der als Ganzes weiter hinten liegt. Dann helfen höhere Zahlen nie."
  when: "`isolation: isolate` für Komponenten, deren interne Ebenen nicht mit dem Rest der Seite kollidieren sollen. Kleine Werte wie 1, 2, 3 reichen fast immer, am besten zentral als Custom Properties."
  question: "Ein Dropdown mit `z-index: 100` liegt hinter einem Element mit `z-index: 2`. Woran liegt das wahrscheinlich?"
  answer: "Ein Vorfahre des Dropdowns bildet einen eigenen Stapelkontext mit niedrigerem `z-index` als 2. Das Dropdown kann diesen Kontext nicht verlassen."
links:
  - text: "z-index"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/z-index"
  - text: "isolation"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/isolation"
  - text: "Stapelkontext"
    url: "https://developer.mozilla.org/de/docs/Web/CSS/CSS_positioned_layout/Stacking_context"
---
