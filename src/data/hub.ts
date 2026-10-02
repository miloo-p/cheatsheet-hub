/** Themenbereiche auf der Startseite, in dieser Reihenfolge */
export const CATEGORIES = [
  {
    id: 'grundlagen',
    title: 'Web-Grundlagen',
    text: 'Die vier Sprachen des Webs, in Lernreihenfolge. Jede Karte zeigt eine kurze und eine ausführliche Schreibweise.',
  },
  {
    id: 'animation',
    title: 'Animation & 3D',
    text: 'Bewegung und Raum im Browser. Mit Live-Demos auf fast jeder Karte, direkt zum Ausprobieren.',
  },
  {
    id: 'produkt',
    title: 'Produkt & Wirkung',
    text: 'Was Besucher zu Kunden macht, aus Entwicklersicht: messen, testen, schneller werden und rechtlich sauber bleiben.',
  },
] as const;

/** Ideen für die nächsten Zettel */
export const PLANNED = [
  { title: 'Node & Express', text: 'Routing, Middleware, Fehlerbehandlung, Umgebungsvariablen' },
  { title: 'SQL & Datenbanken', text: 'SELECT, JOIN, Relationen, Migrations, ORM-Grundlagen' },
  { title: 'React Hooks', text: 'useEffect im Detail, useRef, useContext, eigene Hooks' },
  { title: 'Git', text: 'Branches, Merge vs. Rebase, Konflikte lösen, Pull Requests' },
];
