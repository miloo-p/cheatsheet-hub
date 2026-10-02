---
title: "Das Grundgerüst"
description: "Jede Seite braucht dieselben paar Zeilen. Heute sind sie viel kürzer als früher."
code:
  short: |-
    <!doctype html>
    <html lang="de">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>Todo-App</title>
    </head>
    <body>
      ...
    </body>
    </html>
  long: |-
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="de" lang="de">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <title>Todo-App</title>
    </head>
    <body>
      ...
    </body>
    </html>
explain:
  picture: "Das Grundgerüst ist der Briefkopf: Sprache, Zeichensatz und Titel stehen immer an derselben Stelle, damit Browser und Suchmaschinen sofort wissen, womit sie es zu tun haben."
  steps:
    - "`<!doctype html>` schaltet den Browser in den Standardmodus. Ohne ihn rendert er im Quirks-Modus mit alten Sonderregeln."
    - "`lang=\"de\"` sagt Screenreadern, Übersetzungstools und der Silbentrennung, welche Sprache die Seite hat."
    - "`<meta charset=\"utf-8\">` sorgt dafür, dass Umlaute und Emojis richtig erscheinen. Es gehört möglichst weit nach oben in den `<head>`."
    - "Das Viewport-Meta-Tag lässt Handys mit der echten Bildschirmbreite rechnen, sonst greifen keine Media Queries."
    - "Die ausführliche Variante ist der alte XHTML-Stil. Den brauchst du nicht mehr, aber du begegnest ihm in alten Projekten."
  mistake: "Das Viewport-Meta-Tag vergessen. Auf dem Handy erscheint die Seite dann winzig verkleinert, als wäre sie für den Desktop gebaut."
  when: "Immer die kurze HTML5-Variante. In VS Code erzeugen `!` und Tab dieses Gerüst automatisch."
  question: "Wo ist der Inhalt von `<title>` zu sehen?"
  answer: "Im Browser-Tab, in Lesezeichen und als Überschrift im Suchergebnis. Darum sollte jede Seite einen eigenen, aussagekräftigen Titel haben."
links:
  - text: "<html>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/html"
  - text: "<meta>"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Element/meta"
  - text: "lang"
    url: "https://developer.mozilla.org/de/docs/Web/HTML/Global_attributes/lang"
---
