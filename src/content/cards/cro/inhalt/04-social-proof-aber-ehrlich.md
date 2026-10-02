---
title: "Social Proof, aber ehrlich"
description: "Echte Bewertungen helfen bei der Entscheidung. Erfundene Zähler und gefälschte Knappheit sind Täuschung."
labels:
  - "Vorher"
  - "Nachher"
code:
  short: |-
    <p class="fomo">
      🔥 <span id="viewers"></span> Personen sehen sich das gerade an!
    </p>
    <script>
      // Zufallszahl, hat nichts mit echten Besuchern zu tun
      viewers.textContent = 12 + Math.floor(Math.random() * 30);
    </script>
  long: |-
    <section class="reviews" aria-labelledby="reviews-h">
      <h2 id="reviews-h">4,6 von 5 Sternen aus 312 Bewertungen</h2>
      <!-- Daten aus der eigenen Datenbank bzw. Bewertungsplattform -->
      <blockquote>
        „Nach zwei Wochen im Einsatz: leise und schnell.“
        <footer>Anna, verifizierter Kauf, 12.09.2026</footer>
      </blockquote>
      <a href="/bewertungen">Alle Bewertungen ansehen, auch die kritischen</a>
    </section>
explain:
  picture: "Social Proof funktioniert wie eine Schlange vor einem Restaurant: Andere vertrauen dem Laden, also kann er nicht schlecht sein. Stellt der Wirt Pappaufsteller in die Schlange, ist das Betrug, und wer es merkt, kommt nie wieder."
  steps:
    - "Menschen orientieren sich an den Entscheidungen anderer, besonders bei Unsicherheit."
    - "Echte Bewertungen mit Datum, Kontext und auch kritischen Stimmen wirken glaubwürdiger als ausschließlich Fünf-Sterne-Bewertungen."
    - "Erfundene Besucherzähler, falsche Countdowns oder „nur noch 2 Stück“ ohne echten Bestand sind Irreführung im Sinne des Wettbewerbsrechts (UWG)."
    - "Shops müssen in Deutschland angeben, ob und wie sie prüfen, dass Bewertungen von echten Käufern stammen."
  mistake: "Als Entwickler einen Fake-Zähler einbauen, weil das Marketing es so will. Das ist der Moment, um nachzufragen. Technisch ist es eine Zeile, rechtlich und für die Marke kann es teuer werden."
  when: "Conversion von Besuchern, die den Bewertungsbereich gesehen haben, gegenüber denen, die ihn nicht gesehen haben. Dafür brauchst du ein Sichtbarkeits-Event, z.B. per Intersection Observer."
  question: "Ein Countdown zeigt „Angebot endet in 10 Minuten“ und startet bei jedem Neuladen neu. Ist das in Ordnung?"
  answer: "Nein. Das erzeugt falsche Dringlichkeit und ist eine Irreführung. Ein Countdown muss ein echtes Ende haben."
links:
  - text: "Social Proof (NN/g, EN)"
    url: "https://www.nngroup.com/articles/social-proof-ux/"
  - text: "§ 5b UWG, Abs. 3 zu Bewertungen (gesetze-im-internet.de)"
    url: "https://www.gesetze-im-internet.de/uwg_2004/__5b.html"
---
