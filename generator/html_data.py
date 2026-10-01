MDN = "https://developer.mozilla.org/de/docs/"
E = MDN + "Web/HTML/Element/"
A = MDN + "Web/HTML/Attributes/"
G = MDN + "Web/HTML/Global_attributes/"
ARIA = MDN + "Web/Accessibility/ARIA/Attributes/"
A11Y = MDN + "Learn_web_development/Core/Accessibility/HTML"

def C(t, d, k, a, e, l):
    return dict(t=t, d=d, k=k.strip("\n"), a=a.strip("\n"), e=e, l=l)

SECTIONS = []

SECTIONS.append(("grundgeruest", "Grundgerüst", "basics", "Was in jeder HTML-Datei steht und wie Skripte richtig eingebunden werden.", [
C("Das Grundgerüst",
  "Jede Seite braucht dieselben paar Zeilen. Heute sind sie viel kürzer als früher.",
  """
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
""", """
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
""",
 ("Das Grundgerüst ist der Briefkopf: Sprache, Zeichensatz und Titel stehen immer an derselben Stelle, damit Browser und Suchmaschinen sofort wissen, womit sie es zu tun haben.",
  ["`<!doctype html>` schaltet den Browser in den Standardmodus. Ohne ihn rendert er im Quirks-Modus mit alten Sonderregeln.",
   "`lang=\"de\"` sagt Screenreadern, Übersetzungstools und der Silbentrennung, welche Sprache die Seite hat.",
   "`<meta charset=\"utf-8\">` sorgt dafür, dass Umlaute und Emojis richtig erscheinen. Es gehört möglichst weit nach oben in den `<head>`.",
   "Das Viewport-Meta-Tag lässt Handys mit der echten Bildschirmbreite rechnen, sonst greifen keine Media Queries.",
   "Die ausführliche Variante ist der alte XHTML-Stil. Den brauchst du nicht mehr, aber du begegnest ihm in alten Projekten."],
  "Das Viewport-Meta-Tag vergessen. Auf dem Handy erscheint die Seite dann winzig verkleinert, als wäre sie für den Desktop gebaut.",
  "Immer die kurze HTML5-Variante. In VS Code erzeugen `!` und Tab dieses Gerüst automatisch.",
  "Wo ist der Inhalt von `<title>` zu sehen?",
  "Im Browser-Tab, in Lesezeichen und als Überschrift im Suchergebnis. Darum sollte jede Seite einen eigenen, aussagekräftigen Titel haben."),
 [("<html>", E+"html"), ("<meta>", E+"meta"), ("lang", G+"lang")]),

C("Skripte laden: `defer` und `type=\"module\"`",
  "Skripte so einbinden, dass sie die Seite nicht blockieren und das HTML schon da ist, wenn sie laufen.",
  """
<head>
  <script src="app.js" defer></script>
  <!-- oder als ES-Modul, automatisch verzögert -->
  <script type="module" src="main.js"></script>
</head>
""", """
<body>
  ...
  <!-- ganz unten, damit das HTML vorher eingelesen ist -->
  <script src="app.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      init();
    });
  </script>
</body>
""",
 ("Ohne `defer` hält der Browser beim Lesen des HTML an jedem Skript an, wie jemand, der mitten im Satz aufsteht, um ein Buch zu holen. Mit `defer` wird das Buch nebenbei geholt und erst gelesen, wenn die Seite fertig ist.",
  ["Ein normales `<script>` stoppt das Einlesen des HTML, bis das Skript geladen und ausgeführt ist.",
   "Steht es im `<head>`, existieren die Elemente im `<body>` noch nicht. `document.querySelector` findet dann nichts.",
   "`defer` lädt das Skript parallel und führt es erst aus, wenn das HTML komplett eingelesen ist, in der Reihenfolge der Skripte.",
   "`type=\"module\"` verhält sich automatisch wie `defer` und erlaubt `import` und `export`. Vite erzeugt genau das.",
   "Die ausführliche Variante erreicht dasselbe mit Skripten am Ende des `<body>` und dem Event `DOMContentLoaded`."],
  "Ein Skript ohne `defer` in den `<head>` setzen und sich wundern, warum `document.querySelector(\"#app\")` `null` liefert. Das Element gibt es zu diesem Zeitpunkt noch nicht.",
  "`defer` oder `type=\"module\"` im `<head>`. Skripte am Ende des Body sind der klassische Weg, der genauso funktioniert, aber später mit dem Laden beginnt.",
  "Was ist der Unterschied zwischen `defer` und `async`?",
  "Beide laden parallel. `defer` wartet mit dem Ausführen, bis das HTML fertig ist, und hält die Reihenfolge ein. `async` führt sofort nach dem Laden aus, in beliebiger Reihenfolge. Das passt für unabhängige Skripte wie Statistik-Tools."),
 [("<script>", E+"script"), ("JavaScript-Module", MDN+"Web/JavaScript/Guide/Modules"), ("DOMContentLoaded", MDN+"Web/API/Document/DOMContentLoaded_event")]),

C("Boolesche Attribute",
  "Manche Attribute sind Schalter: Allein ihre Anwesenheit bedeutet „an“.",
  """
<input type="checkbox" checked>
<input type="email" required>
<button disabled>Speichern</button>
""", """
<input type="checkbox" checked="checked">
<input type="email" required="required">
<button disabled="disabled">Speichern</button>
""",
 ("Ein boolesches Attribut ist ein Lichtschalter, kein Dimmer. Es gibt nur an und aus, und an ist es, sobald es dasteht.",
  ["Attribute wie `checked`, `required`, `disabled`, `hidden` oder `open` brauchen keinen Wert.",
   "Steht das Attribut im Tag, gilt es als eingeschaltet.",
   "Die Schreibweise mit wiederholtem Namen stammt aus XHTML und ist weiterhin gültig.",
   "Zum Ausschalten muss das Attribut ganz verschwinden."],
  "`disabled=\"false\"` schreiben und erwarten, dass der Button aktiv ist. Er ist trotzdem deaktiviert, weil das Attribut vorhanden ist. Per JavaScript schaltest du es mit `button.disabled = false` oder `removeAttribute(\"disabled\")` aus.",
  "Immer die kurze Form. In JSX schreibst du dagegen `disabled={false}`, und React entfernt das Attribut dann selbst.",
  "Ist `<input required=\"no\">` ein Pflichtfeld?",
  "Ja. Der Wert ist egal, nur die Anwesenheit des Attributs zählt."),
 [("disabled", A+"disabled"), ("required", A+"required")]),
]))

SECTIONS.append(("semantik", "Semantik und Struktur", "semantics", "Das passende Element sagt Browsern, Suchmaschinen und Screenreadern, was ein Inhalt ist.", [
C("Seitenstruktur mit Landmarks",
  "Semantische Elemente beschreiben, welche Rolle ein Bereich hat. Ein `<div>` sagt dazu nichts.",
  """
<header>...</header>
<nav>...</nav>
<main>
  <article>...</article>
  <aside>...</aside>
</main>
<footer>...</footer>
""", """
<div id="header" role="banner">...</div>
<div id="nav" role="navigation">...</div>
<div id="main" role="main">
  <div class="article">...</div>
  <div class="sidebar" role="complementary">...</div>
</div>
<div id="footer" role="contentinfo">...</div>
""",
 ("Semantische Elemente sind wie beschriftete Umzugskartons: „Küche“, „Bad“, „Bücher“. Ein `<div>` ist ein Karton ohne Aufschrift. Man kommt auch ans Ziel, muss aber jeden einzelnen öffnen.",
  ["`<header>`, `<nav>`, `<main>`, `<aside>` und `<footer>` heißen Landmarks. Screenreader können direkt zwischen ihnen springen.",
   "`<main>` gibt es pro Seite nur einmal sichtbar. Dort steht der eigentliche Inhalt.",
   "`<article>` ist ein in sich geschlossener Inhalt, der auch allein Sinn ergibt, z.B. ein Blogpost oder eine Produktkarte.",
   "Die ausführliche Variante erreicht dieselbe Bedeutung mit `role`-Attributen. So machte man es vor HTML5."],
  "Jedes `<div>` durch `<section>` ersetzen. `<section>` ist ein thematischer Abschnitt, der eine Überschrift haben sollte. Für reine Layout-Container bleibt `<div>` richtig.",
  "Immer die semantischen Elemente. `role` brauchst du nur, wenn es für eine Rolle kein passendes Element gibt.",
  "Wie oft darf `<header>` auf einer Seite vorkommen?",
  "Mehrfach. Neben dem Seitenkopf kann jedes `<article>` oder `<section>` einen eigenen `<header>` haben. Nur `<main>` ist einmalig."),
 [("<main>", E+"main"), ("<header>", E+"header"), ("<article>", E+"article"), ("<aside>", E+"aside")]),

C("Überschriften-Hierarchie",
  "Überschriften bilden das Inhaltsverzeichnis der Seite. Die Ebene richtet sich nach der Struktur, nicht nach der Schriftgröße.",
  """
<h1>Meine Todos</h1>
<h2>Heute</h2>
<h3>Arbeit</h3>
<h3>Privat</h3>
<h2>Diese Woche</h2>
""", """
<div class="title-xl" role="heading" aria-level="1">Meine Todos</div>
<div class="title-l" role="heading" aria-level="2">Heute</div>
<div class="title-m" role="heading" aria-level="3">Arbeit</div>
<div class="title-m" role="heading" aria-level="3">Privat</div>
<div class="title-l" role="heading" aria-level="2">Diese Woche</div>
""",
 ("Die Überschriften sind die Gliederung eines Buches: Kapitel, Unterkapitel, Abschnitte. Screenreader-Nutzer springen durch diese Gliederung wie durch ein Inhaltsverzeichnis.",
  ["`<h1>` ist der Titel der Seite, meist genau einer.",
   "Darunter folgen `<h2>` für Hauptabschnitte, `<h3>` für Unterabschnitte und so weiter.",
   "Ebenen sollten nicht übersprungen werden: Auf `<h2>` folgt `<h3>`, nicht `<h5>`.",
   "Wie groß eine Überschrift aussieht, regelst du mit CSS, nicht mit der Ebene."],
  "Die Ebene nach der gewünschten Größe wählen, z.B. `<h4>`, weil es kleiner aussieht. Dann stimmt die Gliederung nicht mehr, und Screenreader-Nutzer verlieren die Orientierung.",
  "Immer echte `<h1>` bis `<h6>`. Die Variante mit `role=\"heading\"` zeigt nur, wie viel Aufwand der Nachbau eines nativen Elements kostet.",
  "Eine Karte unter einem `<h2>` soll eine kleine Überschrift bekommen. Welche Ebene nimmst du?",
  "`<h3>`, weil sie inhaltlich unter dem `<h2>` liegt. Die kleine Darstellung erledigt CSS."),
 [("<h1> bis <h6>", E+"Heading_Elements"), ("HTML und Barrierefreiheit", A11Y)]),

C("`<button>` statt klickbarem `<div>`",
  "Ein `<button>` kann von Haus aus alles, was ein Button braucht. Ein klickbares `<div>` muss das mühsam nachbauen.",
  """
<button type="button" onclick="toggleMenu()">Menü</button>
""", """
<div class="button" role="button" tabindex="0"
     onclick="toggleMenu()"
     onkeydown="if (event.key === 'Enter' || event.key === ' ') toggleMenu()">
  Menü
</div>
""",
 ("Ein `<button>` ist ein Werkzeug von der Stange: Griff, Klinge und Sicherung sind schon dran. Ein klickbares `<div>` ist ein Stück Holz, an das du jedes Teil selbst schrauben musst.",
  ["`<button>` ist per Tab erreichbar, reagiert auf Enter und Leertaste und wird von Screenreadern als Schaltfläche angesagt.",
   "Ein `<div>` kann nichts davon. `role=\"button\"` sorgt für die Ansage, `tabindex=\"0\"` für die Erreichbarkeit per Tab.",
   "Die Tastaturbedienung musst du per `onkeydown` selbst nachbauen.",
   "`type=\"button\"` ist wichtig: In einem Formular ist der Standard `submit`, und jeder Klick würde das Formular absenden."],
  "`type=\"button\"` in Formularen vergessen. Ein Button zum Anzeigen des Passworts schickt dann bei jedem Klick das Formular ab.",
  "Immer `<button>` für Aktionen. Die div-Variante ist ein Beispiel, wie man es nicht machen sollte. Du triffst sie aber in vielen alten Codebasen.",
  "Wann nimmst du `<button>` und wann `<a>`?",
  "`<a href>` für Navigation zu einer anderen Seite oder Stelle. `<button>` für Aktionen auf der aktuellen Seite: öffnen, speichern, löschen, absenden."),
 [("<button>", E+"button"), ("HTML und Barrierefreiheit", A11Y)]),

C("Links: neue Tabs und Sprungmarken",
  "Externe Links in neuen Tabs öffnen und zu Stellen auf derselben Seite springen.",
  """
<a href="https://developer.mozilla.org" target="_blank">MDN</a>

<a href="#kontakt">Zum Kontakt</a>
<section id="kontakt">...</section>
""", """
<a href="https://developer.mozilla.org" target="_blank"
   rel="noopener noreferrer">MDN</a>

<a href="#" onclick="document.getElementById('kontakt').scrollIntoView(); return false;">
  Zum Kontakt
</a>
<section id="kontakt">...</section>
""",
 ("Ein Anker wie `#kontakt` ist ein Lesezeichen im Buch: Der Link schlägt die Seite genau an dieser Stelle auf, und die Adresse merkt sich die Stelle.",
  ["`target=\"_blank\"` öffnet den Link in einem neuen Tab.",
   "Früher konnte die neue Seite über `window.opener` die alte Seite manipulieren. Darum schrieb man `rel=\"noopener\"` dazu.",
   "Moderne Browser setzen `noopener` bei `target=\"_blank\"` automatisch. `noreferrer` verhindert zusätzlich, dass die Zielseite erfährt, woher der Besuch kam.",
   "`href=\"#kontakt\"` springt zum Element mit `id=\"kontakt\"`. Das funktioniert ohne JavaScript, mit Zurück-Button und als teilbarer Link."],
  "Sprungmarken mit JavaScript nachbauen. Dann funktionieren Zurück-Button, Lesezeichen und Teilen nicht. Ebenfalls häufig: Linktexte wie „hier klicken“. Screenreader-Nutzer lassen sich oft alle Links auflisten, und dann steht dort zehnmal „hier“.",
  "Die Kurzform reicht in aktuellen Browsern. `rel=\"noopener noreferrer\"` schadet nicht und ist bei fremden Seiten ein gutes Sicherheitsnetz. Für sanftes Scrollen genügt im CSS `scroll-behavior: smooth`.",
  "Wie verhinderst du, dass das Sprungziel unter einem Sticky-Header verschwindet?",
  "Mit `scroll-margin-top` im CSS auf dem Ziel, z.B. `section { scroll-margin-top: 5rem; }`."),
 [("<a>", E+"a"), ("rel=\"noopener\"", A+"rel/noopener"), ("scroll-margin-top", MDN+"Web/CSS/scroll-margin-top")]),

C("Betonung: `<strong>` und `<em>`",
  "Bedeutung mit dem passenden Element ausdrücken, Aussehen mit CSS.",
  """
<p><strong>Achtung:</strong> Das Löschen kann <em>nicht</em> rückgängig gemacht werden.</p>
""", """
<p>
  <span class="bold">Achtung:</span> Das Löschen kann
  <span class="italic">nicht</span> rückgängig gemacht werden.
</p>

<style>
  .bold { font-weight: bold; }
  .italic { font-style: italic; }
</style>
""",
 ("`<strong>` und `<em>` sind wie die Stimme beim Vorlesen: Wichtiges klingt ernster, Betontes wird betont. Ein `<span class=\"bold\">` ist nur dicker gedruckt, und wer vorliest, merkt nichts davon.",
  ["`<strong>` heißt: Dieser Teil ist wichtig, ernst oder dringend.",
   "`<em>` heißt: Diese Stelle wird betont, und das verändert die Aussage des Satzes.",
   "Browser zeigen beide standardmäßig fett bzw. kursiv, das lässt sich per CSS ändern.",
   "`<b>` und `<i>` gibt es auch. Sie heben hervor, ohne Wichtigkeit zu behaupten, z.B. Fachbegriffe oder fremdsprachige Wörter."],
  "`<strong>` benutzen, nur weil Text fett aussehen soll, z.B. bei allen Labels. Dann ist jedes zweite Wort „besonders wichtig“, und die Auszeichnung verliert ihren Sinn. Für reine Optik ist CSS da.",
  "`<strong>` und `<em>`, wenn sich Bedeutung oder Betonung ändern. CSS-Klassen, wenn es nur um das Aussehen geht.",
  "Wie unterscheiden sich „Ich habe das <em>nicht</em> gelöscht“ und „Ich habe <em>das</em> nicht gelöscht“?",
  "Im ersten Satz wird bestritten, dass überhaupt gelöscht wurde. Im zweiten wurde etwas anderes gelöscht. `<em>` trägt also echte Bedeutung."),
 [("<strong>", E+"strong"), ("<em>", E+"em"), ("<b>", E+"b")]),

C("Listen",
  "Aufzählungen als echte Listen auszeichnen. Nummerierung und Ansage übernimmt der Browser.",
  """
<ol>
  <li>Repository klonen</li>
  <li><code>npm install</code> ausführen</li>
  <li>Server starten</li>
</ol>
""", """
<div class="steps">
  <p>1. Repository klonen</p>
  <p>2. <code>npm install</code> ausführen</p>
  <p>3. Server starten</p>
</div>
""",
 ("Eine echte Liste ist ein Einkaufszettel, den der Screenreader mit „Liste, 3 Einträge“ ankündigt. Absätze mit Nummern davor sind lose Zettel ohne Zusammenhang.",
  ["`<ol>` ist eine geordnete Liste, die Reihenfolge zählt. `<ul>` ist eine ungeordnete Liste.",
   "Jeder Eintrag steht in einem `<li>`.",
   "Die Nummerierung erzeugt der Browser. Fügst du einen Schritt ein, zählt er automatisch neu.",
   "Screenreader sagen die Anzahl der Einträge an, und man kann von Liste zu Liste springen."],
  "Text oder ein `<div>` direkt in eine `<ul>` schreiben. Erlaubte Kinder sind nur `<li>` (plus `<script>` und `<template>`). Auch Navigationsmenüs sind typischerweise eine `<ul>` in `<nav>`.",
  "Immer echte Listen. Das Aussehen, z.B. ohne Aufzählungspunkte, regelst du mit `list-style: none` im CSS.",
  "Wie lässt du eine `<ol>` bei 5 statt bei 1 beginnen?",
  "Mit dem Attribut `start`, also `<ol start=\"5\">`."),
 [("<ol>", E+"ol"), ("<ul>", E+"ul"), ("<li>", E+"li")]),
]))

SECTIONS.append(("medien", "Bilder und Medien", "media", "Bilder zugänglich, schnell und ohne springendes Layout einbinden.", [
C("Bilder richtig einbinden",
  "Alternativtext, feste Maße und Lazy Loading sorgen dafür, dass Bilder zugänglich sind und die Seite nicht springt.",
  """
<img src="team.jpg" alt="Das Team beim Hackathon"
     width="800" height="450" loading="lazy">
""", """
<img class="lazy" data-src="team.jpg" alt="Das Team beim Hackathon"
     style="width: 800px; height: 450px">

<script>
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.src = entry.target.dataset.src;
        observer.unobserve(entry.target);
      }
    });
  });
  document.querySelectorAll("img.lazy").forEach(img => observer.observe(img));
</script>
""",
 ("`width` und `height` sind eine Tischreservierung im Restaurant: Der Platz ist frei gehalten, bevor der Gast kommt. Ohne Reservierung rücken alle zusammen, sobald er erscheint, und die Seite springt.",
  ["`alt` beschreibt, was das Bild zeigt. Screenreader lesen es vor, und es erscheint, wenn das Bild nicht lädt.",
   "Rein dekorative Bilder bekommen `alt=\"\"`, dann werden sie übersprungen.",
   "`width` und `height` geben das Seitenverhältnis vor. Der Browser reserviert den Platz, bevor das Bild geladen ist. Per CSS kann es trotzdem responsiv skalieren.",
   "`loading=\"lazy\"` lädt das Bild erst, wenn es in die Nähe des sichtbaren Bereichs kommt. Die ausführliche Variante baut genau das mit JavaScript nach."],
  "`alt` ganz weglassen. Dann liest der Screenreader oft den Dateinamen vor, z.B. „IMG-4711.jpg“. Ebenfalls ungünstig: `loading=\"lazy\"` beim großen Bild ganz oben. Das verzögert genau das Bild, das man zuerst sieht.",
  "Immer die native Variante. Lazy Loading nur für Bilder weiter unten auf der Seite.",
  "Welcher `alt`-Text passt zu einem Lupen-Icon in einem Suchbutton?",
  "Einer, der die Funktion beschreibt, also „Suchen“ und nicht „Lupe“. Bei Bildern in Links und Buttons zählt, was passiert."),
 [("<img>", E+"img"), ("HTML und Barrierefreiheit", A11Y)]),

C("Bildunterschriften: `<figure>`",
  "Bild und Bildunterschrift als zusammengehörige Einheit auszeichnen.",
  """
<figure>
  <img src="chart.png" alt="Umsatz steigt von 2 auf 5 Mio. Euro">
  <figcaption>Umsatzentwicklung 2022 bis 2025</figcaption>
</figure>
""", """
<div class="figure">
  <img src="chart.png" alt="Umsatz steigt von 2 auf 5 Mio. Euro"
       aria-describedby="caption-1">
  <p class="caption" id="caption-1">Umsatzentwicklung 2022 bis 2025</p>
</div>
""",
 ("`<figure>` ist der Kasten im Schulbuch, in dem Abbildung und „Abb. 3: …“ zusammenstehen. Wird der Kasten verschoben, wandert die Unterschrift mit.",
  ["`<figure>` umschließt einen in sich geschlossenen Inhalt: Bild, Diagramm, Code-Beispiel oder Zitat.",
   "`<figcaption>` ist die Beschriftung und wird automatisch mit der Figur verknüpft.",
   "Die ausführliche Variante muss diese Verbindung per `aria-describedby` und `id` selbst herstellen.",
   "`alt` und `<figcaption>` haben verschiedene Aufgaben: `alt` ersetzt das Bild, die Bildunterschrift ergänzt es."],
  "Denselben Text in `alt` und `<figcaption>` schreiben. Dann hört ein Screenreader-Nutzer alles doppelt. `alt` beschreibt den Bildinhalt, die Bildunterschrift liefert den Kontext.",
  "`<figure>` immer, wenn ein Bild eine sichtbare Unterschrift hat. Für Bilder ohne Unterschrift reicht `<img>`.",
  "Darf `<figure>` auch Code statt eines Bildes enthalten?",
  "Ja. `<figure>` kann jeden eigenständigen Inhalt enthalten, z.B. `<pre><code>` mit der Unterschrift „Beispiel 2: Express-Route“."),
 [("<figure>", E+"figure"), ("<figcaption>", E+"figcaption")]),

C("Responsive Bilder: `srcset` und `<picture>`",
  "Der Browser lädt die passende Bildgröße, statt dem Handy das riesige Desktop-Bild zu schicken.",
  """
<img src="hero-800.jpg"
     srcset="hero-480.jpg 480w, hero-800.jpg 800w, hero-1600.jpg 1600w"
     sizes="(width < 48rem) 100vw, 50vw"
     alt="Bergpanorama bei Sonnenaufgang">
""", """
<picture>
  <source media="(width < 30rem)" srcset="hero-480.jpg">
  <source media="(width < 64rem)" srcset="hero-800.jpg">
  <img src="hero-1600.jpg" alt="Bergpanorama bei Sonnenaufgang">
</picture>
""",
 ("`srcset` ist eine Speisekarte mit Portionsgrößen: Du bietest klein, mittel und groß an, und der Browser bestellt, was zu Bildschirm und Auflösung passt.",
  ["`srcset` listet die verfügbaren Dateien mit ihrer echten Breite: `480w` heißt 480 Pixel breit.",
   "`sizes` sagt, wie breit das Bild im Layout angezeigt wird: auf kleinen Bildschirmen die volle Breite, sonst die Hälfte.",
   "Aus beidem und der Pixeldichte des Displays wählt der Browser selbst die beste Datei.",
   "`<picture>` mit `<source media>` legt dagegen fest, welches Bild bei welcher Breite kommt. Das brauchst du, wenn sich der Bildausschnitt ändern soll (Art Direction) oder für moderne Formate wie AVIF mit Fallback."],
  "`sizes` vergessen. Dann geht der Browser davon aus, dass das Bild `100vw` breit ist, und lädt auf großen Bildschirmen eine viel zu große Datei, auch wenn das Bild nur in einer schmalen Spalte steht.",
  "`srcset` und `sizes` für dasselbe Motiv in verschiedenen Größen, das ist der häufigste Fall. `<picture>` für andere Ausschnitte je Bildschirm oder für Format-Fallbacks.",
  "Wie lieferst du ein AVIF-Bild mit JPEG als Fallback aus?",
  "Mit `<picture><source type=\"image/avif\" srcset=\"bild.avif\"><img src=\"bild.jpg\" alt=\"...\"></picture>`. Browser ohne AVIF-Unterstützung nehmen das `<img>`."),
 [("Responsive Bilder", MDN+"Web/HTML/Responsive_images"), ("<picture>", E+"picture")]),
]))

SECTIONS.append(("formulare", "Formulare", "forms", "Die Brücke zu deinem Backend: Was im Formular steht, landet in req.body.", [
C("Labels",
  "Jedes Eingabefeld braucht eine Beschriftung, die technisch mit ihm verbunden ist.",
  """
<label>
  E-Mail
  <input type="email" name="email">
</label>
""", """
<label for="email">E-Mail</label>
<input type="email" id="email" name="email">
""",
 ("Ein Label ist das Namensschild am Eingabefeld. Ohne Verbindung hängt das Schild irgendwo daneben, und niemand weiß sicher, zu welchem Feld es gehört.",
  ["In der kurzen Variante umschließt das `<label>` das Feld. Die Verbindung entsteht automatisch.",
   "In der ausführlichen Variante verbindet `for` das Label mit der `id` des Feldes. So können beide getrennt im Layout stehen.",
   "Ein Klick auf das Label setzt den Fokus ins Feld. Bei Checkboxen wird die Klickfläche dadurch viel größer.",
   "Screenreader lesen das Label vor, sobald das Feld fokussiert ist."],
  "`placeholder` statt Label benutzen. Der Platzhalter verschwindet beim Tippen, hat oft zu wenig Kontrast und wird nicht von allen Screenreadern als Beschriftung gelesen. Und in React heißt `for` übrigens `htmlFor`.",
  "Beide Varianten sind gleichwertig. Die Variante mit `for` und `id` ist flexibler im Layout und in Formular-Bibliotheken üblich, das Umschließen spart IDs.",
  "Was passiert, wenn zwei Felder auf derselben Seite `id=\"email\"` haben?",
  "IDs müssen eindeutig sein. Das zweite Label zeigt dann auf das erste Feld. In wiederverwendbaren React-Komponenten erzeugst du eindeutige IDs mit `useId()`."),
 [("<label>", E+"label"), ("<input>", E+"input")]),

C("Eingabetypen und `autocomplete`",
  "Der richtige `type` bringt passende Tastatur, Prüfung und Bedienelemente mit. `autocomplete` lässt den Browser ausfüllen.",
  """
<input type="email" name="email" autocomplete="email">
<input type="tel" name="phone" autocomplete="tel">
<input type="date" name="birthday" autocomplete="bday">
<input type="password" name="password" autocomplete="new-password">
""", """
<input type="text" name="email" class="js-email">
<input type="text" name="phone" class="js-phone">
<input type="text" name="birthday" class="js-datepicker">
<input type="password" name="password">
<!-- dazu: eigene Prüfung, eigener Datepicker, eigene Tastaturlogik -->
""",
 ("Der Eingabetyp ist wie ein vorgedrucktes Papierformular: Beim Datum steht TT.MM.JJJJ schon da, bei der Telefonnummer gibt es Kästchen für Ziffern. Wer alles als Freitext anbietet, muss hinterher alles selbst prüfen.",
  ["`type=\"email\"` prüft das Format und zeigt auf dem Handy eine Tastatur mit @.",
   "`type=\"tel\"` öffnet ein Ziffernfeld, `type=\"date\"` den Datumswähler des Systems.",
   "`autocomplete` sagt dem Browser, welche gespeicherten Daten passen. `new-password` löst den Passwortgenerator aus, `current-password` das Ausfüllen beim Login.",
   "Der `name` bestimmt, unter welchem Schlüssel der Wert beim Absenden ans Backend geht."],
  "`type=\"number\"` für Postleitzahlen, Telefon- oder Kartennummern benutzen. Führende Nullen gehen verloren, und das Mausrad verändert den Wert. Für Ziffernfolgen ohne Rechenbedeutung besser `type=\"text\"` mit `inputmode=\"numeric\"`.",
  "Immer den passenden `type` und wo möglich `autocomplete`. Eigene Datepicker nur, wenn das Design es zwingend verlangt.",
  "Welches `autocomplete` gehört an das Passwortfeld im Login-Formular?",
  "`current-password`. `new-password` ist für Registrierung und Passwortänderung."),
 [("<input>-Typen", E+"input"), ("autocomplete", A+"autocomplete"), ("type=\"email\"", E+"input/email")]),

C("Optionen gruppieren: `<fieldset>`",
  "Zusammengehörige Felder, vor allem Radio-Buttons, mit einer gemeinsamen Überschrift versehen.",
  """
<fieldset>
  <legend>Versandart</legend>
  <label><input type="radio" name="shipping" value="standard" checked> Standard</label>
  <label><input type="radio" name="shipping" value="express"> Express</label>
</fieldset>
""", """
<div role="radiogroup" aria-labelledby="shipping-label">
  <p id="shipping-label">Versandart</p>
  <label><input type="radio" name="shipping" value="standard" checked> Standard</label>
  <label><input type="radio" name="shipping" value="express"> Express</label>
</div>
""",
 ("`<fieldset>` ist der Rahmen um eine Frage auf einem Fragebogen, `<legend>` die Frage selbst. Ohne sie stehen nur lose Antworten da: „Standard“, „Express“, aber wofür?",
  ["`<fieldset>` gruppiert Felder, `<legend>` beschriftet die Gruppe.",
   "Screenreader lesen die Legende vor, sobald man in die Gruppe springt: „Versandart, Standard, Optionsfeld“.",
   "Radio-Buttons mit demselben `name` gehören zusammen. Nur einer kann ausgewählt sein, und mit den Pfeiltasten wechselt man zwischen ihnen.",
   "Beim Absenden geht der `value` des ausgewählten Buttons unter dem `name` ans Backend: `shipping=express`."],
  "Radio-Buttons unterschiedliche `name`-Attribute geben. Dann lassen sich mehrere gleichzeitig auswählen. Oder den `value` vergessen: Dann kommt beim Server nur `on` an.",
  "`<fieldset>` immer bei Radio-Gruppen und zusammengehörigen Checkboxen. Ein `disabled` auf dem Fieldset deaktiviert alle Felder darin auf einmal.",
  "Was steht in `req.body.shipping`, wenn „Express“ gewählt und das Formular abgeschickt wurde?",
  "`\"express\"`, also der `value` des gewählten Radio-Buttons."),
 [("<fieldset>", E+"fieldset"), ("<legend>", E+"legend"), ("type=\"radio\"", E+"input/radio")]),

C("Validierung im Browser",
  "HTML-Attribute prüfen Eingaben schon vor dem Absenden, ohne eine Zeile JavaScript.",
  """
<input type="text" name="username" required minlength="3" maxlength="20"
       pattern="[a-z0-9_]+" title="Nur Kleinbuchstaben, Ziffern und _">
""", """
<input type="text" name="username" id="username">
<span class="error" id="username-error"></span>

<script>
  const input = document.getElementById("username");
  const error = document.getElementById("username-error");
  input.form.addEventListener("submit", e => {
    const v = input.value;
    let msg = "";
    if (!v) msg = "Bitte ausfüllen";
    else if (v.length < 3 || v.length > 20) msg = "3 bis 20 Zeichen";
    else if (!/^[a-z0-9_]+$/.test(v)) msg = "Nur a-z, 0-9 und _";
    if (msg) { e.preventDefault(); error.textContent = msg; }
  });
</script>
""",
 ("Die Browser-Validierung ist der Türsteher vor dem Club: Er weist offensichtlich falsche Gäste ab. Die Ausweiskontrolle an der Kasse, also das Backend, ersetzt er aber nicht.",
  ["`required` verlangt einen Wert, `minlength` und `maxlength` begrenzen die Länge.",
   "`pattern` prüft gegen einen regulären Ausdruck. Er muss den ganzen Wert treffen, `^` und `$` sind automatisch dabei.",
   "Ist etwas ungültig, verhindert der Browser das Absenden und zeigt eine Meldung am Feld.",
   "Im CSS markierst du ungültige Felder mit `:invalid` oder `:user-invalid`. `:user-invalid` greift erst, nachdem jemand mit dem Feld interagiert hat."],
  "Sich auf die Browser-Validierung verlassen. Jeder kann sie in den Entwicklertools abschalten oder direkt einen Request an deine API schicken. Prüfen muss immer auch das Backend.",
  "HTML-Attribute für alle einfachen Regeln. JavaScript zusätzlich für Regeln, die HTML nicht kann, z.B. dass zwei Passwortfelder übereinstimmen (mit `setCustomValidity`).",
  "Wie schaltest du die Browser-Meldungen für ein Formular ab, um eigene Fehlermeldungen zu zeigen?",
  "Mit `novalidate` auf dem `<form>`. Die Attribute bleiben trotzdem nützlich, weil du sie per JavaScript mit `checkValidity()` und `validity` abfragen kannst."),
 [("Formularvalidierung", MDN+"Learn_web_development/Extensions/Forms/Form_validation"), ("required", A+"required"), ("pattern", A+"pattern")]),

C("Formulare ans Backend senden",
  "Ein Formular kann Daten ganz ohne JavaScript an den Server schicken. Mit `fetch` bleibt die Seite dabei stehen.",
  """
<form action="/api/todos" method="post">
  <input name="title" required>
  <button>Anlegen</button>
</form>
""", """
<form id="todo-form">
  <input name="title" required>
  <button>Anlegen</button>
</form>

<script>
  document.getElementById("todo-form").addEventListener("submit", async e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target));
    await fetch("/api/todos", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
  });
</script>
""",
 ("Ein natives Formular ist ein Brief per Post: Er wird abgeschickt, und als Antwort kommt eine ganz neue Seite. `fetch` ist eine Chatnachricht: Sie geht raus, und die Seite bleibt, wie sie ist.",
  ["`action` ist die Zieladresse, `method` die HTTP-Methode. Formulare können nur `get` und `post`.",
   "Beim Absenden sammelt der Browser alle Felder mit `name` und schickt sie URL-kodiert, z.B. `title=Einkaufen`. Felder ohne `name` werden ignoriert.",
   "Im Express-Backend brauchst du dafür `express.urlencoded()`, damit `req.body.title` gefüllt ist.",
   "Die `fetch`-Variante verhindert mit `preventDefault()` das Neuladen, liest die Felder mit `FormData` und schickt JSON. Dafür braucht das Backend `express.json()`."],
  "Das `name`-Attribut am Input vergessen. Das Feld wird dann nicht mitgeschickt, und `req.body.title` ist `undefined`, obwohl im Browser alles ausgefüllt war.",
  "Native Formulare für einfache Seiten und als robuste Grundlage. `fetch` in Single-Page-Apps wie React, wo die Seite nicht neu laden soll.",
  "Welcher Express-Parser wird für das native Formular gebraucht und welcher für die `fetch`-Variante?",
  "Für das native Formular `express.urlencoded()`, für JSON per `fetch` `express.json()`."),
 [("<form>", E+"form"), ("FormData", MDN+"Web/API/FormData"), ("express.urlencoded (EN)", "https://expressjs.com/en/api.html#express.urlencoded")]),
]))

SECTIONS.append(("interaktiv", "Interaktiv ohne JavaScript", "native", "Aufklappen, Dialoge und Menüs kann HTML heute selbst, mit Tastatur- und Screenreader-Unterstützung.", [
C("Aufklappen: `<details>`",
  "Ein Akkordeon zum Auf- und Zuklappen, ganz ohne JavaScript. Die Erklärungen auf diesen Spickzetteln funktionieren genau so.",
  """
<details>
  <summary>Was kostet der Versand?</summary>
  <p>Ab 30 € ist der Versand kostenlos.</p>
</details>
""", """
<button class="faq-toggle" aria-expanded="false" aria-controls="faq-1">
  Was kostet der Versand?
</button>
<div id="faq-1" hidden>
  <p>Ab 30 € ist der Versand kostenlos.</p>
</div>

<script>
  document.querySelector(".faq-toggle").addEventListener("click", e => {
    const btn = e.currentTarget;
    const open = btn.getAttribute("aria-expanded") === "true";
    btn.setAttribute("aria-expanded", String(!open));
    document.getElementById("faq-1").hidden = open;
  });
</script>
""",
 ("`<details>` ist eine Schublade mit Griff: `<summary>` ist der Griff, der Rest ist der Inhalt. Aufziehen, zuschieben, fertig.",
  ["`<summary>` ist immer sichtbar und lässt sich per Klick, Enter oder Leertaste bedienen.",
   "Der restliche Inhalt erscheint nur, wenn das Attribut `open` gesetzt ist. Der Browser schaltet es beim Klicken selbst um.",
   "Screenreader melden den Zustand „erweitert“ oder „reduziert“ automatisch.",
   "Haben mehrere `<details>` denselben `name`, ist immer nur eins offen, wie bei einem klassischen Akkordeon. Die ausführliche Variante baut all das mit `aria-expanded` und JavaScript nach."],
  "Links oder Buttons in `<summary>` legen. Klicks darauf lösen dann auch das Auf- und Zuklappen aus, und Screenreader kommen durcheinander.",
  "`<details>` für FAQs, Erklärungen und optionale Zusatzinfos. Einen eigenen Nachbau nur, wenn sich Optik oder Verhalten damit wirklich nicht umsetzen lassen.",
  "Wie entfernst du das Dreieck vor der `<summary>`?",
  "Mit `summary { list-style: none; }` und für Safari zusätzlich `summary::-webkit-details-marker { display: none; }`."),
 [("<details>", E+"details"), ("<summary>", E+"summary")]),

C("Dialoge: `<dialog>`",
  "Modale Dialoge mit eingebauter Tastatur- und Fokussteuerung.",
  """
<button onclick="document.getElementById('confirm').showModal()">Löschen</button>

<dialog id="confirm">
  <p>Wirklich löschen?</p>
  <form method="dialog">
    <button value="cancel">Abbrechen</button>
    <button value="ok">Löschen</button>
  </form>
</dialog>
""", """
<button id="open">Löschen</button>

<div class="overlay" hidden>
  <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-text">
    <p id="modal-text">Wirklich löschen?</p>
    <button class="cancel">Abbrechen</button>
    <button class="ok">Löschen</button>
  </div>
</div>

<script>
  // Öffnen, Schließen, Escape-Taste, Fokus in den Dialog setzen,
  // Fokus im Dialog halten, Hintergrund sperren, Fokus zurückgeben ...
  // schnell 40 Zeilen JavaScript
</script>
""",
 ("Ein modaler Dialog ist ein Behördenschalter, an dem du stehen bleibst, bis dein Anliegen erledigt ist. `<dialog>` baut den Schalter samt Absperrband auf. Beim Nachbau musst du jedes Band selbst spannen.",
  ["`showModal()` öffnet den Dialog in der obersten Ebene über allem anderen. Der Rest der Seite ist gesperrt.",
   "Der Fokus springt in den Dialog, Escape schließt ihn, und danach kehrt der Fokus zum auslösenden Button zurück.",
   "`<form method=\"dialog\">` schließt den Dialog beim Klick auf einen Button. Dessen `value` steht danach in `dialog.returnValue`.",
   "Der abgedunkelte Hintergrund lässt sich per CSS mit `::backdrop` gestalten."],
  "Das Attribut `open` direkt setzen statt `showModal()` aufzurufen. Dann ist der Dialog zwar sichtbar, aber nicht modal: kein Hintergrund, keine Sperre, kein Escape.",
  "`<dialog>` für Bestätigungen, Formulare im Overlay und Hinweise. Neuere Browser öffnen ihn sogar ganz ohne JavaScript über die Attribute `command` und `commandfor` am Button.",
  "Wie findest du nach dem Schließen heraus, welcher Button geklickt wurde?",
  "Über `dialog.returnValue`. Es enthält den `value` des Buttons aus dem `<form method=\"dialog\">`, hier also `\"ok\"` oder `\"cancel\"`."),
 [("<dialog>", E+"dialog"), ("::backdrop", MDN+"Web/CSS/::backdrop")]),

C("Menüs und Hinweise: `popover`",
  "Menüs, Tooltips und Hinweise, die über allem schweben und sich von selbst wieder schließen.",
  """
<button popovertarget="user-menu">Konto</button>

<div id="user-menu" popover>
  <a href="/profil">Profil</a>
  <a href="/logout">Abmelden</a>
</div>
""", """
<button id="menu-btn" aria-expanded="false" aria-controls="user-menu">Konto</button>
<div id="user-menu" class="dropdown" hidden>...</div>

<script>
  const btn = document.getElementById("menu-btn");
  const menu = document.getElementById("user-menu");
  btn.addEventListener("click", () => {
    menu.hidden = !menu.hidden;
    btn.setAttribute("aria-expanded", String(!menu.hidden));
  });
  document.addEventListener("click", e => {
    if (!menu.contains(e.target) && e.target !== btn) menu.hidden = true;
  });
  document.addEventListener("keydown", e => {
    if (e.key === "Escape") menu.hidden = true;
  });
</script>
""",
 ("Ein Popover ist ein Klebezettel, der kurz über der Seite erscheint. Ein Klick daneben oder Escape, und er ist wieder weg, ohne dass du das selbst programmieren musst.",
  ["Das Attribut `popover` macht ein Element zum Popover. Es ist zunächst unsichtbar.",
   "`popovertarget` am Button verknüpft ihn mit der `id` des Popovers. Ein Klick schaltet es um.",
   "Das Popover erscheint in der obersten Ebene. `z-index` und `overflow` der Elternelemente spielen keine Rolle.",
   "Ein Klick daneben oder Escape schließt es automatisch (Light Dismiss). Die ausführliche Variante baut jeden dieser Punkte einzeln nach."],
  "Ein Popover für etwas benutzen, das den Rest der Seite sperren soll. Popover sind nicht modal. Für „erst entscheiden, dann weiter“ ist `<dialog>` mit `showModal()` richtig.",
  "Popover für Dropdown-Menüs, Tooltips und Hinweise. Seit 2024 unterstützen alle aktuellen Browser das Attribut.",
  "Wie verhinderst du, dass sich ein Popover per Klick daneben schließt?",
  "Mit `popover=\"manual\"`. Dann schließt es sich nur über einen Button oder per JavaScript mit `hidePopover()`."),
 [("popover", G+"popover"), ("Popover API", MDN+"Web/API/Popover_API")]),

C("Eigene Daten: `data-*`",
  "Eigene Daten direkt am Element speichern, z.B. die Datenbank-ID für einen Löschen-Button.",
  """
<li data-id="42" data-status="done">Einkaufen</li>

<script>
  const li = document.querySelector("li");
  li.dataset.id;      // "42"
  li.dataset.status;  // "done"
</script>
""", """
<li class="todo todo-42 status-done">
  Einkaufen
  <input type="hidden" class="todo-id" value="42">
</li>

<script>
  const li = document.querySelector("li");
  li.querySelector(".todo-id").value;     // "42"
  li.classList.contains("status-done");   // true
</script>
""",
 ("`data-`-Attribute sind Etiketten, die du an ein Element klebst. Wer die Seite benutzt, sieht sie nicht, aber JavaScript und CSS können sie lesen.",
  ["Jedes Attribut, das mit `data-` beginnt, ist erlaubt und frei benennbar.",
   "In JavaScript liest du es über `element.dataset`. Aus `data-user-id` wird dabei `dataset.userId` in camelCase.",
   "Werte sind immer Strings. `\"42\"` musst du für Berechnungen mit `Number()` umwandeln.",
   "Auch CSS kann darauf reagieren, z.B. `[data-status=\"done\"] { text-decoration: line-through; }`."],
  "Vertrauliche Daten in `data-`-Attribute schreiben. Jeder kann sie im Quelltext lesen und in den Entwicklertools ändern. Eine ID aus `data-id` muss das Backend deshalb immer gegen die Rechte des Nutzers prüfen.",
  "`data-`-Attribute für Werte, die JavaScript oder CSS zu einem Element brauchen. Versteckte Inputs nur in Formularen, deren Wert mitgeschickt werden soll.",
  "Wie heißt `data-created-at` in `dataset`?",
  "`dataset.createdAt`. Bindestriche werden zu camelCase."),
 [("data-*", G+"data-*"), ("dataset", MDN+"Web/API/HTMLElement/dataset")]),
]))

SECTIONS.append(("a11y", "Barrierefreiheit", "a11y", "Kleine Details, die entscheiden, ob deine Seite für alle benutzbar ist.", [
C("Icon-Buttons beschriften",
  "Buttons, die nur ein Icon zeigen, brauchen trotzdem einen Namen für Screenreader.",
  """
<button type="button" aria-label="Schließen">
  <svg aria-hidden="true">...</svg>
</button>
""", """
<button type="button">
  <svg aria-hidden="true">...</svg>
  <span class="visually-hidden">Schließen</span>
</button>

<style>
  .visually-hidden {
    position: absolute;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip-path: inset(50%);
    white-space: nowrap;
  }
</style>
""",
 ("Ein Icon-Button ohne Beschriftung ist eine Tür mit Bild statt Schild. Wer das Bild nicht sieht, hört nur „Schaltfläche“ und weiß nicht, was dahinter liegt.",
  ["Ohne Text liest der Screenreader nur „Schaltfläche“ vor.",
   "`aria-label` gibt dem Button einen unsichtbaren Namen.",
   "`aria-hidden=\"true\"` am Icon verhindert, dass das SVG zusätzlich vorgelesen wird.",
   "Die ausführliche Variante versteckt echten Text nur optisch, nicht für Screenreader. Vorteil: Übersetzungstools erfassen ihn zuverlässig."],
  "`display: none` oder `hidden` zum Verstecken des Textes benutzen. Dann ist er auch für Screenreader weg. Genau dafür gibt es die Klasse `visually-hidden`.",
  "`aria-label` für einzelne Icon-Buttons. Die Klasse `visually-hidden`, wenn die Seite übersetzt wird oder du sie ohnehin hast. In Tailwind heißt sie `sr-only`.",
  "Was hört ein Screenreader-Nutzer bei `<button><svg>...</svg></button>` ohne Beschriftung?",
  "Nur „Schaltfläche“, im schlimmsten Fall noch einen Dateinamen. Die Funktion bleibt unklar."),
 [("aria-label", ARIA+"aria-label"), ("aria-hidden", ARIA+"aria-hidden")]),

C("Datentabellen",
  "Tabellarische Daten gehören in eine echte Tabelle, mit Kopfzellen und Beschriftung.",
  """
<table>
  <caption>Bestellungen im Oktober</caption>
  <thead>
    <tr><th scope="col">Datum</th><th scope="col">Betrag</th></tr>
  </thead>
  <tbody>
    <tr><td>01.10.</td><td>49,90 €</td></tr>
  </tbody>
</table>
""", """
<div class="table" role="table" aria-label="Bestellungen im Oktober">
  <div class="row" role="row">
    <div role="columnheader">Datum</div>
    <div role="columnheader">Betrag</div>
  </div>
  <div class="row" role="row">
    <div role="cell">01.10.</div>
    <div role="cell">49,90 €</div>
  </div>
</div>
""",
 ("Eine Tabelle ist ein Koordinatensystem. Mit `<th>` weiß ein Screenreader bei jeder Zelle, zu welcher Spalte sie gehört: „Betrag: 49,90 €“. Ohne Kopfzellen hört man nur Zahlen ohne Bedeutung.",
  ["`<caption>` ist der Titel der Tabelle.",
   "`<thead>` enthält die Kopfzeile, `<tbody>` die Daten.",
   "`<th scope=\"col\">` markiert eine Spaltenüberschrift. Für Zeilenüberschriften gibt es `scope=\"row\"`.",
   "Die div-Variante braucht für jede Zelle eine ARIA-Rolle, um dieselbe Struktur zu beschreiben."],
  "Tabellen für das Seitenlayout benutzen, wie in den 2000ern. Und umgekehrt: echte Daten als div-Raster bauen, nur weil es sich leichter stylen lässt. Tabellen lassen sich heute gut mit CSS gestalten, auf schmalen Bildschirmen z.B. in einem Wrapper mit `overflow-x: auto`.",
  "`<table>` immer für Daten mit Zeilen und Spalten. Für Layout CSS Grid.",
  "Links in einer Tabelle stehen die Produktnamen als Zeilenüberschriften. Wie zeichnest du sie aus?",
  "Als `<th scope=\"row\">` statt `<td>` in der ersten Zelle jeder Zeile."),
 [("<table>", E+"table"), ("<th>", E+"th"), ("<caption>", E+"caption")]),

C("Verstecken: `hidden`, `aria-hidden`, `inert`",
  "Drei Arten, etwas zu verstecken: vor allen, nur vor Screenreadern oder nur vor der Bedienung.",
  """
<div hidden>Nirgends sichtbar</div>

<svg aria-hidden="true">...</svg>

<main inert>...</main>
""", """
<div style="display: none">Nirgends sichtbar</div>

<svg role="presentation" focusable="false">...</svg>

<main aria-hidden="true">
  <!-- zusätzlich jedes fokussierbare Element darin sperren: -->
  <button tabindex="-1">...</button>
  <a href="/" tabindex="-1">...</a>
</main>
""",
 ("`hidden` ist ein abgeschlossener Raum, den niemand betritt. `aria-hidden` ist ein Raum, den Sehende sehen, der aber im Lageplan für Blinde fehlt. `inert` ist ein Raum hinter Glas: sichtbar, aber nichts darin lässt sich anfassen.",
  ["`hidden` versteckt ein Element vollständig, wie `display: none`. Es ist weder sichtbar noch für Screenreader vorhanden.",
   "`aria-hidden=\"true\"` entfernt ein Element nur aus der Ansage für Screenreader. Sichtbar bleibt es. Gut für dekorative Icons.",
   "`inert` macht einen ganzen Bereich unbedienbar: kein Klick, kein Tab, keine Ansage. Praktisch für den Hintergrund hinter einem eigenen Overlay.",
   "Ohne `inert` musst du wie in der ausführlichen Variante jedes fokussierbare Element einzeln mit `tabindex=\"-1\"` sperren."],
  "`aria-hidden=\"true\"` auf ein fokussierbares Element setzen, z.B. einen Button. Dann landet man per Tab darauf, aber der Screenreader schweigt. Für solche Bereiche ist `inert` richtig.",
  "`hidden` für Inhalte, die erst später erscheinen. `aria-hidden` für reine Deko. `inert` für vorübergehend gesperrte Bereiche. `<dialog>` mit `showModal()` erledigt das sogar automatisch.",
  "Ein Element mit `hidden` bekommt per CSS `display: block`. Was passiert?",
  "Es wird sichtbar. `hidden` ist nur ein Standard-Style mit `display: none`, und CSS kann ihn überschreiben. Deshalb setzen viele Resets `[hidden] { display: none !important; }`."),
 [("hidden", G+"hidden"), ("inert", G+"inert"), ("aria-hidden", ARIA+"aria-hidden")]),
]))
