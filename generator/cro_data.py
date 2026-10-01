MDN = "https://developer.mozilla.org/de/docs/"
BAY = "https://baymard.com/lists/cart-abandonment-rate"
HTMLSHEET = "https://claude.ai/artifact/YPbjHyWZpJ8tEecBdsXRob"

def C(t, d, k, a, e, l, labels=None):
    c = dict(t=t, d=d, k=k.strip("\n"), a=(a.strip("\n") if a else None), e=e, l=l)
    if labels: c["labels"] = labels
    return c

SECTIONS = []

SECTIONS.append(("messen", "Messen und Testen", "data", "Ohne saubere Daten ist jede Optimierung geraten. Hier liegt der größte Hebel für Entwickler.", [
C("Funnel statt einer einzigen Zahl",
  "Die Conversion Rate sagt, wie viele kaufen. Der Funnel sagt, wo die anderen aussteigen.",
  """
// Nur das Endergebnis messen
track("purchase");

// Auswertung: 2 % Conversion Rate.
// Aber warum nicht mehr? Keine Ahnung.
""", """
// Jeden Schritt messen
track("view_product",   { id });
track("add_to_cart",    { id, value });
track("begin_checkout", { value });
track("add_shipping");
track("add_payment");
track("purchase",       { value, orderId });

// Auswertung: 40 % springen bei add_shipping ab
// -> Versandkosten früher zeigen?
""",
 ("Ein Funnel ist ein Trichter mit Löchern. Nur zu zählen, was unten herauskommt, hilft wenig. Erst wenn du an jeder Stufe misst, siehst du, wo das größte Loch ist.",
  ["Conversion Rate = Conversions ÷ Besuche. Was als Conversion zählt, legst du fest: Kauf, Anmeldung, Anfrage.",
   "Makro-Conversions sind die Hauptziele (Kauf). Mikro-Conversions sind Zwischenschritte (in den Warenkorb, Newsletter, Video angesehen).",
   "Ein Funnel misst jeden Schritt einzeln. Die Abbruchrate pro Schritt zeigt, wo du ansetzen solltest.",
   "Die Event-Namen im Beispiel folgen den empfohlenen E-Commerce-Events von Google Analytics 4. Einheitliche Namen machen Auswertungen und Toolwechsel einfacher."],
  "Nur Seitenaufrufe messen. Ein Aufruf der Checkout-Seite sagt nicht, ob jemand das Formular ausgefüllt, einen Fehler bekommen oder abgebrochen hat. Wichtige Schritte brauchen eigene Events.",
  "Im Analytics-Tool einen Trichter aus den Events anlegen und die Abbruchrate je Schritt vergleichen, getrennt nach Mobil und Desktop. Oft unterscheiden sich die Probleme stark.",
  "Wo setzt du an, wenn 1000 Leute in den Warenkorb legen, 900 den Checkout starten und 300 kaufen?",
  "Im Checkout. Zwischen Start und Kauf gehen zwei Drittel verloren, das ist das größte Loch."),
 [("GA4: empfohlene Events (EN)", "https://developers.google.com/analytics/devguides/collection/ga4/reference/events"), ("Kaufabbrüche (Baymard, EN)", BAY)],
 labels=("Vorher", "Nachher")),

C("Events sauber benennen",
  "Ein kleiner Tracking-Wrapper mit klaren Namen und Parametern macht Daten auswertbar und das Tool austauschbar.",
  """
<button onclick="gtag('event', 'click')">Jetzt testen</button>
<button onclick="gtag('event', 'Click Button 2')">Preise</button>
<button onclick="plausible('cta')">Kontakt</button>
""", """
<button data-track="cta_click" data-track-location="hero">Jetzt testen</button>

<script>
  // Ein Wrapper für alle Tools, mit Consent-Prüfung
  export function track(name, params = {}) {
    if (!hasConsent("analytics")) return;
    window.gtag?.("event", name, params);
  }

  document.addEventListener("click", (e) => {
    const el = e.target.closest("[data-track]");
    if (el) track(el.dataset.track, { location: el.dataset.trackLocation });
  });
</script>
""",
 ("Events sind wie Ordner in einem Archiv. Heißt jeder Ordner anders oder „Sonstiges“, findet später niemand etwas. Mit festen Namen und Etiketten lässt sich jede Frage beantworten.",
  ["Event-Namen in einem festen Schema, z.B. `objekt_aktion` in snake_case: `cta_click`, `form_submit`, `video_play`.",
   "Details gehören in Parameter, nicht in den Namen. Statt `hero_cta_click` und `footer_cta_click` ein Event `cta_click` mit `location`.",
   "Ein eigener `track()`-Wrapper kapselt das Tool. Ein Wechsel von Google Analytics zu Plausible oder Matomo ändert nur eine Funktion.",
   "Die Consent-Prüfung im Wrapper sorgt dafür, dass ohne Einwilligung nichts gesendet wird.",
   "`data-track`-Attribute halten das Tracking aus der Komponentenlogik heraus, ähnlich wie bei Event Delegation."],
  "Personenbezogene Daten in Events schicken, z.B. E-Mail-Adressen als Parameter oder in der URL. Das ist datenschutzrechtlich heikel und bei Google Analytics ausdrücklich verboten.",
  "Ein Tracking-Plan als Tabelle mit Event-Name, Parametern, Auslöser und Zweck, bevor du Code schreibst. Prüfen kannst du die Events im Netzwerk-Tab der Entwicklertools oder in der Debug-Ansicht des Tools.",
  "Wie trackst du, dass jemand ein Formularfeld mit Fehler verlassen hat, ohne den eingegebenen Wert zu senden?",
  "Mit einem Event wie `form_error` und Parametern für Feldname und Fehlerart, z.B. `{ field: \"email\", error: \"typeMismatch\" }`. Der Wert selbst bleibt im Browser."),
 [("Event Delegation (JS-Spickzettel)", "https://claude.ai/artifact/EgkjrRmDocu7CAwqekbRN7#muster"), ("dataset (MDN)", MDN+"Web/API/HTMLElement/dataset")],
 labels=("Vorher", "Nachher")),

C("Hypothesen statt Bauchgefühl",
  "Jede Änderung beginnt mit einer Beobachtung und einer überprüfbaren Annahme, nicht mit „mach den Button mal grün“.",
  """
"Lass uns den Button grün machen,
 das konvertiert besser."
""", """
Beobachtung:  42 % brechen auf der Versandseite ab.
              In Session-Recordings scrollen viele
              suchend nach den Versandkosten.

Hypothese:    Wenn wir die Versandkosten schon im
              Warenkorb anzeigen, sinkt die Abbruchrate
              auf der Versandseite, weil die Überraschung
              wegfällt.

Messgröße:    Abbruchrate Versandseite (primär),
              Bestellungen pro Besuch (Kontrolle)
""",
 ("Eine Hypothese ist eine Wette mit klaren Regeln: Du schreibst vorher auf, worauf du setzt, warum, und woran du erkennst, ob du gewonnen hast. Ohne diese Regeln gewinnt man jede Wette im Nachhinein.",
  ["Eine Beobachtung aus Daten oder Nutzertests ist der Ausgangspunkt, z.B. aus dem Funnel oder aus Gesprächen mit Kunden.",
   "Die Hypothese folgt dem Muster: Wenn wir X ändern, dann passiert Y, weil Z.",
   "Das „weil“ ist entscheidend. Es zwingt dich, eine Ursache zu benennen, und hilft beim Lernen, auch wenn der Test verliert.",
   "Primäre Messgröße und Kontrollgröße stehen vorher fest. Die Kontrollgröße zeigt, ob du an anderer Stelle Schaden anrichtest."],
  "Ergebnisse aus Blogposts übernehmen, z.B. „roter Button = 34 % mehr Umsatz“. Solche Zahlen gelten, wenn überhaupt, für eine bestimmte Seite mit einem bestimmten Publikum und lassen sich selten übertragen.",
  "Hypothesen in einer Liste sammeln und nach erwarteter Wirkung, Sicherheit der Annahme und Aufwand priorisieren. Nach jedem Test festhalten, was ihr gelernt habt.",
  "Was fehlt an der Hypothese „Ein größeres Produktbild erhöht die Conversion“?",
  "Das „weil“ und die Beobachtung, auf der sie beruht. Ohne Ursache lernst du nichts, wenn der Test verliert."),
 [("Kaufabbrüche und Gründe (Baymard, EN)", BAY)],
 labels=("Vorher", "Nachher")),

C("A/B-Tests technisch sauber",
  "Jeder Besucher muss dauerhaft dieselbe Variante sehen, und die Zuteilung darf die Seite nicht flackern lassen.",
  """
<script>
  // bei jedem Seitenaufruf neu würfeln
  if (Math.random() < 0.5) {
    document.querySelector(".cta").textContent = "Jetzt starten";
  }
</script>
""", """
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
""",
 ("Ein A/B-Test ist ein Experiment mit zwei Gruppen. Wechselt ein Teilnehmer bei jedem Besuch die Gruppe, weißt du am Ende nicht mehr, welche Variante gewirkt hat. Die Zuteilung muss so fest sein wie eine Namensliste.",
  ["Bei `Math.random()` pro Seitenaufruf sieht dieselbe Person mal A, mal B. Die Ergebnisse vermischen sich.",
   "Die Zuteilung wird einmal getroffen und gespeichert, z.B. im Cookie oder anhand einer gehashten Nutzer-ID.",
   "Serverseitig ausgeliefert gibt es kein Flackern. Clientseitige Tests tauschen Inhalte erst nach dem Laden aus, und Besucher sehen kurz die Originalvariante.",
   "Das `experiment_view`-Event zählt nur Besucher, die die Variante wirklich gesehen haben. Wer nie bis zum Button scrollt, gehört nicht in die Auswertung.",
   "Auch das Test-Cookie braucht eine rechtliche Grundlage. Kläre mit dem Datenschutz, ob dafür eine Einwilligung nötig ist."],
  "Den Test mitten im Lauf ändern, z.B. die Variante B nachbessern. Dann vergleichst du ab da etwas anderes, und die gesammelten Daten passen nicht mehr zusammen.",
  "Wenige, gut begründete Tests mit großer Änderung bringen mehr als viele kleine. Für einen A/A-Test (zweimal dieselbe Variante) lohnt sich ein Probelauf: Zeigt er einen „Gewinner“, stimmt etwas am Aufbau nicht.",
  "Warum misst du `experiment_view` und nicht einfach alle Seitenaufrufe?",
  "Weil nur Besucher, die die Variante gesehen haben, von ihr beeinflusst werden konnten. Alle anderen verwässern das Ergebnis."),
 [("res.cookie (Express, EN)", "https://expressjs.com/en/api.html#res.cookie")],
 labels=("Vorher", "Nachher")),

C("Statistikfallen: Stichprobengröße und Peeking",
  "Wer täglich auf das Dashboard schaut und bei „signifikant“ stoppt, findet fast immer einen Gewinner, auch wenn es keinen gibt.",
  """
// Tag 3: "B liegt 18 % vorne, p < 0.05 – fertig, B gewinnt!"
""", """
// Vorher festlegen: Wie viele Besucher pro Variante?
// Faustregel (Signifikanz 5 %, Power 80 %):
//   n ≈ 16 · p · (1 − p) / δ²
function sampleSize(baseRate, minEffect) {
  const delta = baseRate * minEffect;          // absoluter Unterschied
  return Math.ceil(16 * baseRate * (1 - baseRate) / delta ** 2);
}

sampleSize(0.03, 0.10);   // 3 % Basis, +10 % relativ
// -> 51.734 Besucher pro Variante
// Test erst danach auswerten, mindestens volle Wochen laufen lassen
""",
 ("Peeking ist wie ein Münzwurf-Wettbewerb, bei dem du aufhörst, sobald Kopf zufällig vorne liegt. Wenn du nur oft genug nachschaust, liegt irgendwann jede Seite einmal vorn.",
  ["Ein p-Wert unter 0,05 bedeutet nur dann 5 % Irrtumswahrscheinlichkeit, wenn du genau einmal am geplanten Ende auswertest.",
   "Wer zwischendurch immer wieder prüft und beim ersten „signifikanten“ Ergebnis stoppt, erhöht die Fehlerquote stark. Evan Miller zeigt, dass aus 5 % so schnell über 25 % werden.",
   "Die Faustregel berechnet, wie viele Besucher pro Variante nötig sind, um einen bestimmten Unterschied zuverlässig zu erkennen.",
   "Kleine Effekte brauchen riesige Stichproben. Bei 3 % Conversion und +10 % relativem Effekt sind es über 50.000 Besucher pro Variante.",
   "Tests sollten volle Wochen laufen, weil sich Besucher am Wochenende anders verhalten als unter der Woche."],
  "Auf einer Seite mit 500 Besuchern pro Woche A/B-Tests für kleine Textänderungen fahren. Das Ergebnis ist fast immer Zufall. Mit wenig Traffic lernst du mehr aus Nutzertests mit fünf Personen.",
  "Stichprobe und Laufzeit vor dem Start festlegen und im Hypothesen-Dokument notieren. Für genaue Werte einen Rechner wie den von Evan Miller benutzen, die Faustregel dient nur zur Abschätzung.",
  "Dein Test hat nach zwei Tagen ein signifikantes Ergebnis, geplant waren vier Wochen. Was tust du?",
  "Weiterlaufen lassen. Ein frühes signifikantes Ergebnis ist bei häufigem Nachsehen sehr oft Zufall."),
 [("How Not To Run an A/B Test (Evan Miller, EN)", "https://www.evanmiller.org/how-not-to-run-an-ab-test.html"), ("Stichprobenrechner (Evan Miller, EN)", "https://www.evanmiller.org/ab-testing/sample-size.html")],
 labels=("Vorher", "Nachher")),
]))

SECTIONS.append(("inhalt", "Seiteninhalte", "content", "Was auf der Seite steht und wo es steht. Auch hier entscheidest du als Entwickler oft mit.", [
C("Button-Texte, die sagen, was passiert",
  "Ein Button-Text sollte das Ergebnis des Klicks beschreiben, nicht die Mechanik.",
  """
<button>Absenden</button>
<button>Hier klicken</button>
<a href="/demo">Mehr</a>
""", """
<button>Kostenlos registrieren</button>
<button>Angebot anfordern</button>
<a href="/demo">Live-Demo ansehen</a>
<p class="hint">14 Tage kostenlos, keine Kreditkarte nötig.</p>
""",
 ("Ein Button ist ein Versprechen. „Absenden“ verspricht nichts, außer dass Daten irgendwohin gehen. „Angebot anfordern“ sagt, was man dafür bekommt.",
  ["Gute Button-Texte beginnen mit einem Verb und beschreiben das Ergebnis aus Sicht des Nutzers.",
   "Mehrdeutige Texte wie „Mehr“ oder „Hier klicken“ sind auch für Screenreader-Nutzer ein Problem, wenn sie sich alle Links auflisten lassen.",
   "Ein kurzer Satz direkt am Button kann die größte Sorge beantworten: Kosten, Verpflichtung, Aufwand.",
   "Texte sind leicht zu testen und haben oft mehr Wirkung als Farben oder Größen."],
  "Clevere oder lustige Texte, die niemand versteht, z.B. „Los geht's!“ auf einem Bezahl-Button. Bei Bestellungen in Deutschland ist die Beschriftung sogar gesetzlich geregelt, siehe Karte „Bestell-Button“.",
  "Klickrate auf den Button und Abschlussrate des nächsten Schritts. Steigen die Klicks, aber nicht die Abschlüsse, hat der Text mehr versprochen, als die nächste Seite hält.",
  "Welcher Text passt besser auf den Button eines Newsletter-Formulars: „Abonnieren“ oder „Wöchentliche Tipps erhalten“?",
  "„Wöchentliche Tipps erhalten“, weil er Inhalt und Häufigkeit nennt. Beides beantwortet die Frage, was man sich einhandelt."),
 [("HTML und Barrierefreiheit (MDN)", MDN+"Learn_web_development/Core/Accessibility/HTML")],
 labels=("Vorher", "Nachher")),

C("Ein klarer Hauptbutton",
  "Mehrere gleich starke Buttons nebeneinander zwingen zum Nachdenken. Visuelle Hierarchie zeigt, was der nächste Schritt ist.",
  """
<div class="actions">
  <button class="btn">Jetzt kaufen</button>
  <button class="btn">Merken</button>
  <button class="btn">Teilen</button>
  <button class="btn">Vergleichen</button>
</div>
""", """
<div class="actions">
  <button class="btn btn-primary">In den Warenkorb</button>
  <button class="btn btn-ghost">Merken</button>
</div>

<style>
  .btn-primary { background: var(--brand); color: white; font-weight: 600; }
  .btn-ghost   { background: transparent; border: 1px solid currentColor; }
</style>
""",
 ("Ein Hauptbutton ist ein Wegweiser mit einem großen Schild für den Hauptweg und kleinen Schildern für Nebenwege. Stehen vier gleich große Schilder da, bleibt man stehen und liest.",
  ["Pro Bildschirmbereich gibt es einen primären Button, der sich durch Farbe, Füllung und Gewicht abhebt.",
   "Nebenaktionen werden zurückhaltend gestaltet: als Rahmen-Button, Textlink oder Icon mit Beschriftung.",
   "Die Reihenfolge folgt der Leserichtung. Der Hauptbutton steht dort, wo der Blick zuerst landet.",
   "Sehr seltene Aktionen wandern in ein Menü, statt Platz zu belegen."],
  "Zwei Hauptbuttons mit unterschiedlichen Zielen nebeneinander, z.B. „Jetzt kaufen“ und „Newsletter abonnieren“. Sie konkurrieren um dieselbe Aufmerksamkeit.",
  "Klickverteilung auf die Buttons, z.B. per Event mit `location`-Parameter, und die Rate des Hauptziels. Eine Heatmap zeigt zusätzlich, ob Leute auf Dinge klicken, die nicht klickbar sind.",
  "Wie gestaltest du einen Löschen-Button in einem Bestätigungsdialog?",
  "Als klar erkennbaren Button mit Warnfarbe und eindeutigem Text wie „Konto löschen“. „Abbrechen“ steht daneben als ruhigere Option."),
 [("Visual Hierarchy (NN/g, EN)", "https://www.nngroup.com/articles/visual-hierarchy-ux-definition/")],
 labels=("Vorher", "Nachher")),

C("Kosten und Vertrauen früh zeigen",
  "Überraschende Zusatzkosten sind laut Baymard der häufigste Grund für Kaufabbrüche. Was Sorgen macht, gehört an den Ort der Entscheidung.",
  """
<!-- Produktseite -->
<p class="price">49,90 €</p>
<button>In den Warenkorb</button>

<!-- Versandkosten erst im 3. Checkout-Schritt -->
""", """
<p class="price">49,90 € <small>inkl. MwSt.</small></p>
<p class="shipping">Kostenloser Versand ab 50 €, sonst 4,90 €</p>
<button>In den Warenkorb</button>

<ul class="trust">
  <li>Lieferung in 1–3 Werktagen</li>
  <li>30 Tage kostenlose Rückgabe</li>
  <li>PayPal, Klarna, Kreditkarte, Rechnung</li>
</ul>
""",
 ("Vertrauen ist wie Gepäck auf einer Wanderung: Jede offene Frage wiegt etwas mehr. Was kostet der Versand? Kann ich zurückschicken? Kann ich per Rechnung zahlen? Beantwortest du sie früh, wird der Rucksack leichter.",
  ["In Baymards Befragung nennen 40 % zu hohe Zusatzkosten als Abbruchgrund, 19 % mangelndes Vertrauen beim Bezahlen und 13 % unklare Rückgaberegeln.",
   "Gesamtkosten, Lieferzeit und Rückgabe gehören auf die Produktseite und in den Warenkorb, nicht erst ans Ende des Checkouts.",
   "Bekannte Zahlungsarten schaffen Vertrauen, gerade in Deutschland, wo Rechnung und PayPal sehr verbreitet sind.",
   "In Deutschland gilt zudem die Preisangabenverordnung: Endpreise inklusive Mehrwertsteuer, Versandkosten müssen angegeben sein."],
  "Siegel, Logos und Garantien ohne echten Hintergrund einbauen. Ein erfundenes Gütesiegel schadet dem Vertrauen und ist wettbewerbswidrig.",
  "Abbruchrate zwischen Warenkorb und Checkout-Start sowie zwischen Versand- und Zahlungsschritt. Sinkt sie nach der Änderung, hat die frühe Information gewirkt.",
  "Wo zeigst du die Lieferzeit am besten an?",
  "Direkt beim Preis und beim Button auf der Produktseite und noch einmal im Warenkorb, möglichst konkret wie „Lieferung bis Freitag“."),
 [("Kaufabbrüche und Gründe (Baymard, EN)", BAY)],
 labels=("Vorher", "Nachher")),

C("Social Proof, aber ehrlich",
  "Echte Bewertungen helfen bei der Entscheidung. Erfundene Zähler und gefälschte Knappheit sind Täuschung.",
  """
<p class="fomo">
  🔥 <span id="viewers"></span> Personen sehen sich das gerade an!
</p>
<script>
  // Zufallszahl, hat nichts mit echten Besuchern zu tun
  viewers.textContent = 12 + Math.floor(Math.random() * 30);
</script>
""", """
<section class="reviews" aria-labelledby="reviews-h">
  <h2 id="reviews-h">4,6 von 5 Sternen aus 312 Bewertungen</h2>
  <!-- Daten aus der eigenen Datenbank bzw. Bewertungsplattform -->
  <blockquote>
    „Nach zwei Wochen im Einsatz: leise und schnell.“
    <footer>Anna, verifizierter Kauf, 12.09.2026</footer>
  </blockquote>
  <a href="/bewertungen">Alle Bewertungen ansehen, auch die kritischen</a>
</section>
""",
 ("Social Proof funktioniert wie eine Schlange vor einem Restaurant: Andere vertrauen dem Laden, also kann er nicht schlecht sein. Stellt der Wirt Pappaufsteller in die Schlange, ist das Betrug, und wer es merkt, kommt nie wieder.",
  ["Menschen orientieren sich an den Entscheidungen anderer, besonders bei Unsicherheit.",
   "Echte Bewertungen mit Datum, Kontext und auch kritischen Stimmen wirken glaubwürdiger als ausschließlich Fünf-Sterne-Bewertungen.",
   "Erfundene Besucherzähler, falsche Countdowns oder „nur noch 2 Stück“ ohne echten Bestand sind Irreführung im Sinne des Wettbewerbsrechts (UWG).",
   "Shops müssen in Deutschland angeben, ob und wie sie prüfen, dass Bewertungen von echten Käufern stammen."],
  "Als Entwickler einen Fake-Zähler einbauen, weil das Marketing es so will. Das ist der Moment, um nachzufragen. Technisch ist es eine Zeile, rechtlich und für die Marke kann es teuer werden.",
  "Conversion von Besuchern, die den Bewertungsbereich gesehen haben, gegenüber denen, die ihn nicht gesehen haben. Dafür brauchst du ein Sichtbarkeits-Event, z.B. per Intersection Observer.",
  "Ein Countdown zeigt „Angebot endet in 10 Minuten“ und startet bei jedem Neuladen neu. Ist das in Ordnung?",
  "Nein. Das erzeugt falsche Dringlichkeit und ist eine Irreführung. Ein Countdown muss ein echtes Ende haben."),
 [("Social Proof (NN/g, EN)", "https://www.nngroup.com/articles/social-proof-ux/"), ("§ 5b UWG, Abs. 3 zu Bewertungen (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/uwg_2004/__5b.html")],
 labels=("Vorher", "Nachher")),
]))

SECTIONS.append(("formulare", "Formulare und Checkout", "forms", "Formulare sind die Stelle, an der Interesse in Conversions umschlägt oder verpufft.", [
C("Weniger Felder",
  "Laut Baymard kommt ein guter Checkout mit 7 bis 8 Formularfeldern aus. Der Durchschnitt liegt bei fast 15.",
  """
<input name="anrede">       <input name="titel">
<input name="vorname">      <input name="nachname">
<input name="firma">        <input name="strasse">
<input name="hausnummer">   <input name="adresszusatz">
<input name="plz">          <input name="ort">
<input name="land">         <input name="telefon">
<input name="email">        <input name="email2">
<input name="geburtsdatum">
""", """
<input name="name" autocomplete="name">
<input name="email" type="email" autocomplete="email">
<input name="street" autocomplete="street-address">
<input name="zip" autocomplete="postal-code" inputmode="numeric">
<input name="city" autocomplete="address-level2">

<details>
  <summary>Firma oder Adresszusatz hinzufügen</summary>
  <input name="company" autocomplete="organization">
  <input name="addressLine2" autocomplete="address-line2">
</details>
""",
 ("Jedes Formularfeld ist eine kleine Hürde auf einem Hindernislauf. Zehn Hürden schaffen die meisten noch, aber bei jeder fällt jemand. Die beste Hürde ist die, die gar nicht erst aufgestellt wird.",
  ["Für jedes Feld fragen: Brauchen wir es wirklich für diese Bestellung? Geburtsdatum, Anrede und Telefon oft nicht.",
   "Doppelte Eingaben wie E-Mail-Wiederholung sind meist überflüssig. Ein sichtbarer Wert zum Prüfen reicht.",
   "Ein Namensfeld statt Vor- und Nachname spart ein Feld, solange das Backend nicht zwingend getrennte Werte braucht.",
   "Selten nötige Felder wie Firma oder Adresszusatz werden hinter einem Link oder `<details>` versteckt.",
   "Die Land-Auswahl lässt sich oft aus der Sprache oder IP vorbelegen, die Stadt aus der Postleitzahl."],
  "Felder nur im Frontend entfernen, aber im Backend weiterhin als Pflicht validieren. Dann scheitert die Bestellung an einem Feld, das niemand ausfüllen konnte. Frontend- und Backend-Validierung müssen zusammenpassen.",
  "Abschlussrate des Formulars und Abbruch pro Feld. Viele Analytics-Tools können Formular-Analysen, oder du trackst `field_focus` und `field_error` selbst.",
  "Warum ist ein Feld „E-Mail wiederholen“ meist überflüssig?",
  "Weil die meisten die Adresse einfach kopieren oder vom Browser ausfüllen lassen. Fehler fängt eine klare Anzeige der Adresse vor dem Absenden besser ab."),
 [("Checkout-Felder (Baymard, EN)", BAY), ("autocomplete (MDN)", MDN+"Web/HTML/Attributes/autocomplete")],
 labels=("Vorher", "Nachher")),

C("Fehlermeldungen am Feld",
  "Fehler sofort und am richtigen Ort zeigen, mit einer Anleitung zur Lösung.",
  """
<form onsubmit="if (!valid()) { alert('Fehler im Formular!'); return false; }">
  <input name="email">
  <input name="zip">
  <button>Weiter</button>
</form>
""", """
<label for="zip">Postleitzahl</label>
<input id="zip" name="zip" inputmode="numeric" pattern="[0-9]{5}" required
       aria-describedby="zip-error">
<p id="zip-error" class="error" hidden>
  Bitte eine 5-stellige Postleitzahl eingeben, z.B. 10115.
</p>

<script>
  zip.addEventListener("blur", () => {
    const ok = zip.checkValidity();
    document.getElementById("zip-error").hidden = ok;
    zip.setAttribute("aria-invalid", String(!ok));
  });
</script>
""",
 ("Eine gute Fehlermeldung ist wie ein Navi, das sagt: „Hier links abbiegen.“ Eine schlechte ist ein Warnton ohne Erklärung, und man weiß nicht einmal, welche Abzweigung falsch war.",
  ["Fehler direkt am betroffenen Feld zeigen, nicht oben im Formular oder als `alert`.",
   "Der Text sagt, was erwartet wird und gibt ein Beispiel, statt nur „ungültig“ zu melden.",
   "Geprüft wird beim Verlassen des Feldes (`blur`), nicht bei jedem Tastendruck. Sonst erscheint der Fehler schon, während man noch tippt.",
   "`aria-describedby` verknüpft die Meldung mit dem Feld, sodass Screenreader sie vorlesen. `aria-invalid` markiert das Feld als fehlerhaft.",
   "Bereits eingegebene Daten bleiben nach einem Fehler erhalten. Ein leeres Formular nach dem Absenden ist einer der häufigsten Abbruchgründe."],
  "Fehler nur über Farbe anzeigen, z.B. einen roten Rahmen. Wer Farben schlecht unterscheiden kann oder einen Screenreader nutzt, sieht den Fehler nicht. Es braucht immer auch Text.",
  "Anzahl der Fehler pro Feld als Event (`form_error` mit Feldname). Felder mit vielen Fehlern sind Kandidaten für bessere Hinweise, ein anderes Eingabeformat oder ganz zum Streichen.",
  "Wann sollte die Fehlermeldung wieder verschwinden?",
  "Sobald die Eingabe korrekt ist, also beim nächsten `input`- oder `blur`-Event mit gültigem Wert. Nicht erst beim erneuten Absenden."),
 [("Formularvalidierung (MDN)", MDN+"Learn_web_development/Extensions/Forms/Form_validation"), ("HTML-Spickzettel: Formulare", HTMLSHEET+"#formulare")],
 labels=("Vorher", "Nachher")),

C("Gastbestellung erlauben",
  "Eine Pflicht zur Kontoerstellung nennen in Baymards Befragung 18 % als Abbruchgrund. Das Konto kann nach der Bestellung angeboten werden.",
  """
<!-- Checkout-Schritt 1 -->
<h2>Bitte melde dich an oder registriere dich</h2>
<form action="/login">...</form>
<form action="/register">...</form>
""", """
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
""",
 ("Eine Kontopflicht vor dem Kauf ist wie ein Laden, in dem man erst eine Kundenkarte beantragen muss, bevor man an die Kasse darf. Ein Konto nach dem Kauf ist die freundliche Frage an der Kasse: „Möchten Sie Punkte sammeln?“",
  ["Gastbestellung als gleichwertige oder hervorgehobene Option anbieten.",
   "Für Bestandskunden bleibt die Anmeldung einen Klick entfernt.",
   "Nach der Bestellung liegen Name, E-Mail und Adresse bereits vor. Für ein Konto fehlt nur noch ein Passwort.",
   "Im Backend muss eine Bestellung ohne `userId` möglich sein. Die E-Mail-Adresse wird dann zum Schlüssel, um eine spätere Kontoerstellung mit der Bestellung zu verknüpfen."],
  "Die Gastoption verstecken, z.B. als kleinen grauen Link unter einem großen Registrierungsformular. Wer sie nicht findet, bricht genauso ab wie ohne Gastoption.",
  "Abbruchrate auf dem ersten Checkout-Schritt und Anteil der Gastbestellungen. Zusätzlich: Wie viele Gäste legen nach der Bestellung ein Konto an?",
  "Welche Daten brauchst du, um eine Gastbestellung später einem neuen Konto zuzuordnen?",
  "Die E-Mail-Adresse. Nach Bestätigung der Adresse kann das Backend frühere Gastbestellungen mit derselben E-Mail dem Konto zuordnen."),
 [("Kaufabbrüche und Gründe (Baymard, EN)", BAY)],
 labels=("Vorher", "Nachher")),
]))

SECTIONS.append(("performance", "Ladezeit", "speed", "Langsame Seiten verlieren Besucher, bevor sie überhaupt etwas sehen. Hier ist Entwicklerarbeit Conversion-Arbeit.", [
C("Core Web Vitals echt messen",
  "Lighthouse auf dem eigenen Laptop ist ein Labortest. Entscheidend ist, wie schnell die Seite bei echten Besuchern ist.",
  """
// Nur lokal: Lighthouse im schnellen Entwickler-Laptop
// "Performance 98 – passt!"
""", """
import { onLCP, onINP, onCLS } from "web-vitals";

function send(metric) {
  navigator.sendBeacon("/api/vitals", JSON.stringify({
    name: metric.name,          // "LCP" | "INP" | "CLS"
    value: metric.value,
    rating: metric.rating,      // "good" | "needs-improvement" | "poor"
    page: location.pathname,
  }));
}

onLCP(send);
onINP(send);
onCLS(send);
""",
 ("Lighthouse ist ein Probelauf im Trainingsraum. Echte Besucher laufen draußen, bei Regen, mit altem Handy und schlechtem Netz. Erst die Messung im Feld zeigt, wie es ihnen wirklich geht.",
  ["Die drei Core Web Vitals: LCP (Ladezeit des größten Inhalts, gut bis 2,5 s), INP (Reaktionszeit auf Eingaben, gut bis 200 ms) und CLS (Layoutverschiebungen, gut bis 0,1).",
   "Bewertet wird das 75. Perzentil aller Seitenaufrufe, getrennt nach Mobil und Desktop. Drei von vier Besuchern sollen also eine gute Erfahrung haben.",
   "Die Bibliothek `web-vitals` misst die Werte im Browser echter Besucher (Real User Monitoring).",
   "`sendBeacon` schickt die Daten auch dann zuverlässig, wenn die Seite gerade verlassen wird.",
   "Im Backend speicherst du die Werte und wertest das 75. Perzentil pro Seite aus."],
  "Nur am eigenen Rechner mit Glasfaser testen. Für einen realistischen Labortest in den Chrome-Entwicklertools die Netzwerk- und CPU-Drosselung einschalten.",
  "Pro Seitentyp (Startseite, Produktseite, Checkout) das 75. Perzentil von LCP, INP und CLS beobachten. Öffentliche Felddaten für größere Seiten liefert PageSpeed Insights aus dem Chrome UX Report.",
  "Warum zählt das 75. Perzentil und nicht der Durchschnitt?",
  "Weil ein Durchschnitt gute Werte vieler schneller Besuche mit sehr schlechten Werten weniger Besuche verrechnet. Das 75. Perzentil stellt sicher, dass die große Mehrheit eine gute Erfahrung hat."),
 [("Core Web Vitals (web.dev, EN)", "https://web.dev/articles/vitals"), ("web-vitals (GitHub, EN)", "https://github.com/GoogleChrome/web-vitals"), ("sendBeacon (MDN)", MDN+"Web/API/Navigator/sendBeacon")],
 labels=("Vorher", "Nachher")),

C("Das Hauptbild schnell laden (LCP)",
  "Das größte Element im sichtbaren Bereich, meist ein Hero-Bild, bestimmt den LCP. Es braucht Vorrang statt Verzögerung.",
  """
<img src="hero-2400.jpg" alt="..." loading="lazy">
""", """
<link rel="preload" as="image" href="hero-1200.avif"
      imagesrcset="hero-800.avif 800w, hero-1200.avif 1200w"
      imagesizes="100vw">

<img src="hero-1200.avif"
     srcset="hero-800.avif 800w, hero-1200.avif 1200w"
     sizes="100vw"
     width="1200" height="600"
     fetchpriority="high"
     alt="...">
""",
 ("Der Browser lädt Dinge in einer Warteschlange. Das Hauptbild ist der wichtigste Gast, und `fetchpriority=\"high\"` ist der VIP-Eingang. `loading=\"lazy\"` schickt ihn dagegen ans Ende der Schlange.",
  ["`loading=\"lazy\"` beim Hauptbild verzögert genau das Element, das den LCP bestimmt.",
   "`fetchpriority=\"high\"` sagt dem Browser, dass dieses Bild vor anderen Ressourcen geladen werden soll.",
   "`<link rel=\"preload\">` im `<head>` startet den Download, bevor der Browser das `<img>` im HTML erreicht. Das hilft vor allem bei Bildern, die per CSS oder JavaScript eingebunden werden.",
   "Moderne Formate wie AVIF oder WebP und eine passende Größe per `srcset` sparen oft mehr als die Hälfte der Datenmenge.",
   "`width` und `height` reservieren den Platz und verhindern einen Layout Shift."],
  "Das Hauptbild per JavaScript nachladen, z.B. in einem Slider, der erst nach dem Framework-Start initialisiert wird. Dann wartet der LCP auf das ganze JavaScript.",
  "LCP-Wert und LCP-Element im Performance-Panel der Chrome-Entwicklertools prüfen. Dort steht, welches Element als größtes gilt und wie lange es gedauert hat.",
  "Ein Hero hat ein Hintergrundbild per CSS `background-image`. Wie beschleunigst du es?",
  "Mit `<link rel=\"preload\" as=\"image\" href=\"…\" fetchpriority=\"high\">` im `<head>`. Sonst entdeckt der Browser das Bild erst, nachdem er das CSS geladen und ausgewertet hat."),
 [("LCP optimieren (web.dev, EN)", "https://web.dev/articles/optimize-lcp"), ("fetchpriority (MDN)", MDN+"Web/HTML/Element/img#fetchpriority")],
 labels=("Vorher", "Nachher")),

C("Springende Seiten vermeiden (CLS)",
  "Wenn Inhalte beim Laden verrutschen, klicken Besucher daneben. Platz für spät ladende Elemente wird vorher reserviert.",
  """
<div id="banner"></div>   <!-- wird per JS mit 120px Inhalt gefüllt -->
<img src="produkt.jpg" alt="...">
<button>In den Warenkorb</button>
""", """
<div id="banner" style="min-height: 120px"></div>
<img src="produkt.jpg" alt="..." width="800" height="800">
<button>In den Warenkorb</button>

<style>
  /* Webfont mit ähnlicher Ersatzschrift, damit Text nicht springt */
  @font-face {
    font-family: "Brand";
    src: url("brand.woff2") format("woff2");
    font-display: swap;
  }
</style>
""",
 ("Ein Layout Shift ist wie ein Tisch, an den sich plötzlich jemand dazwischen setzt: Alle rutschen, und dein Teller landet beim Nachbarn. Wer vorher einen Stuhl freihält, verhindert das Rutschen.",
  ["CLS misst, wie stark sichtbare Elemente sich unerwartet verschieben. Gut ist ein Wert bis 0,1.",
   "Typische Ursachen: Bilder ohne Maße, nachgeladene Banner und Werbung, Webfonts mit anderer Breite, eingeblendete Hinweise oben auf der Seite.",
   "`width` und `height` an Bildern und `min-height` für nachgeladene Bereiche reservieren den Platz vorab.",
   "Cookie-Banner und Hinweise als Overlay unten einblenden statt oben in den Inhalt einzuschieben.",
   "Verschiebungen direkt nach einer Nutzeraktion, z.B. beim Aufklappen, zählen nicht als CLS."],
  "Ein Banner „Kostenloser Versand ab 50 €“ nachträglich oben einfügen. Genau dann rutscht der „In den Warenkorb“-Button weg, während jemand darauf tippen will.",
  "CLS im Feld mit `web-vitals` messen. Im Chrome-Performance-Panel zeigt die Spur „Layout Shifts“, welches Element sich verschoben hat und warum.",
  "Ein Bild hat `width=\"800\" height=\"800\"`, wird aber per CSS mit `width: 100%` angezeigt. Springt es trotzdem?",
  "Nein, solange im CSS auch `height: auto` gilt. Der Browser berechnet aus den Attributen das Seitenverhältnis und reserviert den passenden Platz."),
 [("CLS optimieren (web.dev, EN)", "https://web.dev/articles/optimize-cls"), ("CSS-Spickzettel: aspect-ratio", "https://claude.ai/artifact/9i6icDS2mpDmQm3j3fzdpT#responsive")],
 labels=("Vorher", "Nachher")),
]))

SECTIONS.append(("recht", "Rechtliches in Deutschland", "recht", "Was Shops und Websites in Deutschland beachten müssen. Kein Rechtsrat, aber die Punkte, die du als Entwickler kennen solltest.", [
C("Der Bestell-Button",
  "Nach § 312j Abs. 3 BGB muss der Bestell-Button eindeutig auf die Zahlungspflicht hinweisen. Sonst kommt kein wirksamer Vertrag zustande.",
  """
<button>Bestellen</button>
<button>Weiter zur Zahlung</button>
<button>Jetzt kostenlos testen</button>   <!-- Abo wird danach kostenpflichtig -->
""", """
<section class="summary">
  <h2>Deine Bestellung</h2>
  <!-- Artikel, Gesamtpreis inkl. MwSt., Versand, Laufzeit bei Abos -->
</section>

<button type="submit">Zahlungspflichtig bestellen</button>
""",
 ("Der Bestell-Button ist die Unterschrift unter einem Vertrag. Das Gesetz verlangt, dass auf dem Stift steht, dass die Unterschrift Geld kostet.",
  ["Der Gesetzeswortlaut nennt „zahlungspflichtig bestellen“ oder eine entsprechend eindeutige Formulierung.",
   "Gerichte haben u.a. „Bestellen“, „Bestellung abschicken“, „Abonnieren“, „Bezahlen“ und „Jetzt anmelden“ als nicht ausreichend bewertet.",
   "Bei kostenlosen Testphasen, die in ein bezahltes Abo übergehen, muss die Zahlungspflicht ebenfalls auf dem Button erkennbar sein.",
   "Direkt vor dem Button muss eine Zusammenfassung mit den wesentlichen Merkmalen, dem Gesamtpreis und bei Abos der Laufzeit stehen.",
   "Bei einem Verstoß kommt laut Gesetz kein Vertrag zustande. Zusätzlich drohen Abmahnungen."],
  "Den Button-Text im Rahmen eines A/B-Tests „optimieren“, z.B. zu „Jetzt loslegen“. Die gesetzliche Beschriftung ist nicht verhandelbar und gehört aus jedem Test heraus.",
  "Hier wird nicht gemessen, sondern geprüft: Steht auf jedem Button, der einen kostenpflichtigen Vertrag auslöst, eine eindeutige Formulierung? Das gilt auch für Upgrades und In-App-Käufe.",
  "Ist „Kostenpflichtig bestellen“ ebenfalls in Ordnung?",
  "Ja, das gilt als entsprechend eindeutige Formulierung. Im Zweifel ist „zahlungspflichtig bestellen“ als Gesetzeswortlaut die sicherste Wahl."),
 [("§ 312j BGB (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__312j.html"), ("Button-Lösung: aktuelle Rechtsprechung (CR-online)", "https://www.cr-online.de/blog/2025/02/14/die-button-loesung-im-online-handel-aktuelle-anforderungen-und-rechtliche-vorgaben/")],
 labels=("Vorher", "Nachher")),

C("Fairer Consent-Banner",
  "Nach § 25 TDDDG brauchen nicht notwendige Cookies und Tracking eine Einwilligung. Ablehnen muss so einfach sein wie Zustimmen.",
  """
<div class="cookie-banner">
  <button class="big-green">Alle akzeptieren</button>
  <a class="tiny-grey" href="/einstellungen">Einstellungen</a>
</div>

<!-- Tracking läuft schon vor der Entscheidung -->
<script src="https://www.googletagmanager.com/gtag/js?id=G-XXXX"></script>
""", """
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
""",
 ("Ein Consent-Banner ist eine Tür mit zwei Klinken: „Ja“ und „Nein“. Sie müssen gleich groß sein und gleich leicht zu drücken. Ein „Nein“, das man erst hinter einer zweiten Tür findet, ist keine echte Wahl.",
  ["Seit Mai 2024 heißt das TTDSG Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz (TDDDG). § 25 verlangt eine Einwilligung, bevor Informationen auf dem Gerät gespeichert oder ausgelesen werden, außer sie sind unbedingt erforderlich.",
   "Unbedingt erforderlich sind z.B. Warenkorb- oder Login-Cookies. Analyse- und Marketing-Tracking gehören nicht dazu.",
   "Datenschutzbehörden verlangen, dass Ablehnen und Zustimmen gleichwertig angeboten werden, ohne Extra-Klicks und ohne optische Benachteiligung.",
   "Technisch heißt das: Tracking-Skripte werden erst nach der Zustimmung geladen. Ein Skript, das schon im HTML steht, hat bereits Daten gesendet.",
   "Die Entscheidung muss sich später ändern lassen, z.B. über einen Link im Footer."],
  "Das Tracking-Skript direkt im `<head>` laden und den Banner nur zur Deko anzeigen. Im Netzwerk-Tab ist sofort zu sehen, dass Anfragen an das Tracking-Tool rausgehen, bevor jemand zugestimmt hat.",
  "Im Netzwerk-Tab prüfen, dass vor der Zustimmung keine Anfragen an Tracking-Dienste gehen. Die Zustimmungsrate selbst kannst du zählen, ohne Personen zu tracken, z.B. als serverseitigen Zähler.",
  "Brauchst du für ein Warenkorb-Cookie eine Einwilligung?",
  "Nein. Ohne das Cookie funktioniert der vom Nutzer gewünschte Dienst nicht, es ist unbedingt erforderlich."),
 [("§ 25 TDDDG (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/ttdsg/__25.html"), ("TDDDG-Überblick (eRecht24)", "https://www.e-recht24.de/datenschutz/12834-tdddg.html")],
 labels=("Vorher", "Nachher")),

C("Barrierefreiheit ist seit 2025 Pflicht",
  "Seit dem 28. Juni 2025 müssen viele Onlineshops und digitale Dienste für Verbraucher nach dem BFSG barrierefrei sein.",
  """
<div class="btn" onclick="addToCart()">
  <img src="cart.svg">
</div>
<input placeholder="E-Mail">
<span style="color:#bbb">Nur noch heute!</span>
""", """
<button type="button" onclick="addToCart()">
  <img src="cart.svg" alt=""> In den Warenkorb
</button>
<label for="email">E-Mail</label>
<input id="email" type="email" autocomplete="email">
<p class="notice">Angebot gilt bis 31.10.2026</p>   <!-- ausreichender Kontrast -->
""",
 ("Barrierefreiheit ist eine Rampe neben der Treppe. Gebaut wird sie für Rollstuhlfahrer, aber sie hilft auch allen mit Kinderwagen oder Koffer. Genauso helfen klare Labels und Tastaturbedienung allen Besuchern.",
  ["Das Barrierefreiheitsstärkungsgesetz (BFSG) gilt u.a. für Dienstleistungen im elektronischen Geschäftsverkehr mit Verbrauchern, also typische Onlineshops.",
   "Ausgenommen sind Kleinstunternehmen, die Dienstleistungen erbringen: weniger als 10 Beschäftigte und höchstens 2 Mio. € Jahresumsatz.",
   "Maßstab ist die Norm EN 301 549, die auf die WCAG 2.1 in Stufe AA verweist.",
   "Verstöße können mit Bußgeldern bis 100.000 € geahndet werden.",
   "Fast alles, was dafür nötig ist, steht im HTML-Spickzettel: echte Buttons, Labels, Alternativtexte, Tastaturbedienung, sichtbarer Fokus und ausreichender Kontrast."],
  "Barrierefreiheit als nachträgliches Projekt behandeln oder mit einem Overlay-Plugin „nachrüsten“. Solche Overlays beheben die Ursachen nicht. Barrierefreiheit entsteht im HTML und CSS, beim Bauen.",
  "Lighthouse und axe DevTools für automatische Prüfungen, dazu einmal die ganze Bestellung nur mit der Tastatur und einmal mit einem Screenreader durchspielen. Automatische Tests finden nur einen Teil der Probleme.",
  "Ein Shop eines Ein-Personen-Unternehmens mit 300.000 € Umsatz: Gilt das BFSG?",
  "Für die Dienstleistung Onlineshop greift die Ausnahme für Kleinstunternehmen. Barrierefreiheit lohnt sich trotzdem, weil sie für alle die Bedienung verbessert."),
 [("BFSG (IHK Stuttgart)", "https://www.ihk.de/stuttgart/fuer-unternehmen/recht-und-steuern/it-recht/barrierefreie-webseiten-6200594"), ("HTML-Spickzettel: Barrierefreiheit", HTMLSHEET+"#a11y"), ("WCAG 2.1 (W3C, EN)", "https://www.w3.org/TR/WCAG21/")],
 labels=("Vorher", "Nachher")),

C("Dark Patterns vermeiden",
  "Tricks, die Nutzer zu ungewollten Entscheidungen drängen, kosten Vertrauen und sind in vielen Fällen unzulässig.",
  """
<label>
  <input type="checkbox" name="insurance" checked>
  Versicherung für 4,99 €/Monat
</label>

<button>Ja, ich will sparen!</button>
<a class="tiny">Nein danke, ich zahle lieber den vollen Preis</a>
""", """
<label>
  <input type="checkbox" name="insurance">
  Versicherung für 4,99 €/Monat hinzufügen
</label>

<button>Gutschein einlösen</button>
<button class="btn-ghost">Ohne Gutschein fortfahren</button>

<!-- Abos: Kündigen so leicht wie Abschließen -->
<a href="/vertraege/kuendigen">Verträge hier kündigen</a>
""",
 ("Dark Patterns sind wie ein Verkäufer, der dir unauffällig etwas zusätzlich in die Tüte legt. Kurzfristig steigt der Umsatz, langfristig kommt niemand wieder.",
  ["Vorausgewählte kostenpflichtige Zusatzleistungen sind in der EU unzulässig. Ein Häkchen für einen Aufpreis muss der Kunde selbst setzen.",
   "Confirmshaming macht die Ablehnung lächerlich („Nein, ich zahle lieber mehr“). Neutrale Texte für beide Optionen sind fair.",
   "Seit Juli 2022 schreibt § 312k BGB für online abschließbare Abos einen Kündigungsbutton vor, z.B. beschriftet mit „Verträge hier kündigen“.",
   "Weitere Muster: versteckte Kosten, erzwungene Konten, falsche Dringlichkeit und Abos, die sich nur per Brief kündigen lassen.",
   "Der Digital Services Act der EU verbietet Online-Plattformen ausdrücklich, ihre Oberflächen so zu gestalten, dass Nutzer getäuscht oder manipuliert werden."],
  "Den Erfolg eines Dark Patterns an der kurzfristigen Conversion messen. Mehr Zusatzverkäufe sehen gut aus, bis Rücksendungen, Rückbuchungen und Beschwerden dazukommen.",
  "Nicht nur Conversions messen, sondern auch Rückgaben, Kündigungen, Support-Anfragen und wiederkehrende Kunden. Faire Muster zeigen sich in diesen Zahlen langfristig besser.",
  "Ist eine bereits angehakte Checkbox für den Newsletter erlaubt?",
  "Nein. Eine Einwilligung muss aktiv erteilt werden, ein vorausgefülltes Häkchen reicht nach der DSGVO nicht."),
 [("§ 312k BGB (gesetze-im-internet.de)", "https://www.gesetze-im-internet.de/bgb/__312k.html"), ("Deceptive Patterns (EN)", "https://www.deceptive.design/")],
 labels=("Vorher", "Nachher")),
]))

INFOBOX = """
<h2>Mehr aus Marketing-Sicht</h2>
<p>Dieser Zettel schaut mit Entwickleraugen auf Conversion-Optimierung. Wer tiefer in Texte, Psychologie und Angebotsgestaltung einsteigen will, findet hier gute Startpunkte.</p>
<ul>
  <li><b>Wertversprechen zuerst.</b> Besucher entscheiden in wenigen Sekunden, ob eine Seite für sie relevant ist. Die Überschrift sollte sagen, was man bekommt und für wen, nicht wie toll das Unternehmen ist.</li>
  <li><b>Message Match.</b> Die Landingpage sollte das Versprechen der Anzeige oder des Links aufgreifen, mit denselben Worten und demselben Angebot. Jeder Bruch kostet Vertrauen.</li>
  <li><b>Einwände beantworten.</b> Sammle die häufigsten Fragen aus Support, Vertrieb und Bewertungen und beantworte sie dort, wo sie entstehen, statt in einer versteckten FAQ.</li>
</ul>
<p><b>Lesenswert:</b></p>
<ul>
  <li><a href="https://baymard.com/research" target="_blank" rel="noopener">Baymard Institute</a>: große Studien zu E-Commerce- und Checkout-Usability (EN)</li>
  <li><a href="https://www.nngroup.com/articles/" target="_blank" rel="noopener">Nielsen Norman Group</a>: fundierte UX-Artikel zu Formularen, Navigation und Inhalten (EN)</li>
  <li><a href="https://cxl.com/blog/" target="_blank" rel="noopener">CXL Blog</a>: Conversion-Optimierung und Experimente aus Marketing-Sicht (EN)</li>
  <li><a href="https://goodui.org/" target="_blank" rel="noopener">GoodUI</a>: Muster aus veröffentlichten A/B-Tests mit Ergebnissen (EN)</li>
  <li><a href="https://growth.design/case-studies" target="_blank" rel="noopener">Growth.Design</a>: Fallstudien als Comics, kurzweilig zu Psychologie im Produktdesign (EN)</li>
  <li>Bücher: Steve Krug, „Don't Make Me Think“ (Usability-Klassiker, auch auf Deutsch). Robert Cialdini, „Die Psychologie des Überzeugens“ (Grundlagen, mit kritischem Blick lesen). Ron Kohavi u.a., „Trustworthy Online Controlled Experiments“ (A/B-Tests richtig gemacht, EN).</li>
</ul>
"""
