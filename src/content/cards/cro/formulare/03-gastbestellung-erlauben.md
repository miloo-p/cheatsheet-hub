---
title: "Gastbestellung erlauben"
description: "Eine Pflicht zur Kontoerstellung nennen in Baymards Befragung 18 % als Abbruchgrund. Das Konto kann nach der Bestellung angeboten werden."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <!-- Checkout-Schritt 1 -->
    <h2>Bitte melde dich an oder registriere dich</h2>
    <form action="/login">...</form>
    <form action="/register">...</form>
  long: |-
    <!-- Checkout-Schritt 1 -->
    <h2>Wie möchtest du bestellen?</h2>
    <a class="btn btn-primary" href="/checkout/guest">Als Gast bestellen</a>
    <a class="btn btn-ghost" href="/login?next=/checkout">Anmelden</a>

    <!-- Bestätigungsseite: E-Mail und Adresse liegen schon vor -->
    <form action="/account/create" method="post">
      <label>Passwort für dein Kundenkonto (optional)
        <input type="password" name="password" autocomplete="new-password">
      </label>
      <button>Konto anlegen</button>
    </form>
explain:
  picture: "Eine Kontopflicht vor dem Kauf ist wie ein Laden, in dem man erst eine Kundenkarte beantragen muss, bevor man an die Kasse darf. Ein Konto nach dem Kauf ist die freundliche Frage an der Kasse: „Möchten Sie Punkte sammeln?“"
  steps:
    - "Gastbestellung als gleichwertige oder hervorgehobene Option anbieten."
    - "Für Bestandskunden bleibt die Anmeldung einen Klick entfernt."
    - "Nach der Bestellung liegen Name, E-Mail und Adresse bereits vor. Für ein Konto fehlt nur noch ein Passwort."
    - "Im Backend muss eine Bestellung ohne `userId` möglich sein. Die E-Mail-Adresse wird dann zum Schlüssel, um eine spätere Kontoerstellung mit der Bestellung zu verknüpfen."
  mistake: "Die Gastoption verstecken, z.B. als kleinen grauen Link unter einem großen Registrierungsformular. Wer sie nicht findet, bricht genauso ab wie ohne Gastoption."
  when: "Abbruchrate auf dem ersten Checkout-Schritt und Anteil der Gastbestellungen. Zusätzlich: Wie viele Gäste legen nach der Bestellung ein Konto an?"
  question: "Welche Daten brauchst du, um eine Gastbestellung später einem neuen Konto zuzuordnen?"
  answer: "Die E-Mail-Adresse. Nach Bestätigung der Adresse kann das Backend frühere Gastbestellungen mit derselben E-Mail dem Konto zuordnen."
links:
  - text: "Kaufabbrüche und Gründe (Baymard, EN)"
    url: "https://baymard.com/lists/cart-abandonment-rate"
---
