---
title: "Verstecken: `hidden`, `aria-hidden`, `inert`"
description: "Drei Arten, etwas zu verstecken: vor allen, nur vor Screenreadern oder nur vor der Bedienung."
code:
  short: |-
    <div hidden>Nirgends sichtbar</div>

    <svg aria-hidden="true">...</svg>

    <main inert>...</main>
  long: |-
    <div style="display: none">Nirgends sichtbar</div>

    <svg role="presentation" focusable="false">...</svg>

    <main aria-hidden="true">
      <!-- zusätzlich jedes fokussierbare Element darin sperren: -->
      <button tabindex="-1">...</button>
      <a href="/" tabindex="-1">...</a>
    </main>
explain:
  picture: "`hidden` ist ein abgeschlossener Raum, den niemand betritt. `aria-hidden` ist ein Raum, den Sehende sehen, der aber im Lageplan für Blinde fehlt. `inert` ist ein Raum hinter Glas: sichtbar, aber nichts darin lässt sich anfassen."
  steps:
    - "`hidden` versteckt ein Element vollständig, wie `display: none`. Es ist weder sichtbar noch für Screenreader vorhanden."
    - "`aria-hidden=\"true\"` entfernt ein Element nur aus der Ansage für Screenreader. Sichtbar bleibt es. Gut für dekorative Icons."
    - "`inert` macht einen ganzen Bereich unbedienbar: kein Klick, kein Tab, keine Ansage. Praktisch für den Hintergrund hinter einem eigenen Overlay."
    - "Ohne `inert` musst du wie in der ausführlichen Variante jedes fokussierbare Element einzeln mit `tabindex=\"-1\"` sperren."
  mistake: "`aria-hidden=\"true\"` auf ein fokussierbares Element setzen, z.B. einen Button. Dann landet man per Tab darauf, aber der Screenreader schweigt. Für solche Bereiche ist `inert` richtig."
  when: "`hidden` für Inhalte, die erst später erscheinen. `aria-hidden` für reine Deko. `inert` für vorübergehend gesperrte Bereiche. `<dialog>` mit `showModal()` erledigt das sogar automatisch."
  question: "Ein Element mit `hidden` bekommt per CSS `display: block`. Was passiert?"
  answer: "Es wird sichtbar. `hidden` ist nur ein Standard-Style mit `display: none`, und CSS kann ihn überschreiben. Deshalb setzen viele Resets `[hidden] { display: none !important; }`."
links:
  - text: "hidden"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Global_attributes/hidden"
  - text: "inert"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Global_attributes/inert"
  - text: "aria-hidden"
    url: "https://developer.mozilla.org/de/docs/Web/Accessibility/ARIA/Attributes/aria-hidden"
---
