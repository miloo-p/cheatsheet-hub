import { getCollection, type CollectionEntry } from 'astro:content';

export type SheetEntry = CollectionEntry<'sheets'>;
export type CardEntry = CollectionEntry<'cards'>;

export interface CardInfo {
  entry: CardEntry;
  /** Anker der Karte, z.B. "css-grid-2". Bleibt stabil, solange die Nummer im Dateinamen gleich bleibt. */
  id: string;
  n: number;
}

export interface SectionInfo {
  id: string;
  title: string;
  tag: string;
  sub: string;
  cards: CardInfo[];
}

export interface SheetInfo {
  key: string;
  entry: SheetEntry;
  sections: SectionInfo[];
  count: number;
}

const PATH = /cards\/([^/]+)\/([^/]+)\/(\d+)-[^/]*\.md$/;

async function load(): Promise<SheetInfo[]> {
  const sheets = (await getCollection('sheets')).sort((a, b) => a.data.order - b.data.order);
  const byKey = new Map<string, SheetInfo>();
  for (const entry of sheets) {
    byKey.set(entry.id, {
      key: entry.id,
      entry,
      sections: entry.data.sections.map((s) => ({ ...s, cards: [] })),
      count: 0,
    });
  }

  for (const card of await getCollection('cards')) {
    const m = (card.filePath ?? '').replace(/\\/g, '/').match(PATH);
    if (!m) throw new Error(`Karte ${card.filePath}: erwartet wird cards/<zettel>/<abschnitt>/NN-name.md`);
    const [, key, sectionId, num] = m;
    const sheet = byKey.get(key);
    if (!sheet) throw new Error(`Karte ${card.filePath}: Den Zettel "${key}" gibt es nicht in src/content/sheets/`);
    const section = sheet.sections.find((s) => s.id === sectionId);
    if (!section) throw new Error(`Karte ${card.filePath}: Abschnitt "${sectionId}" fehlt in sheets/${key}.md`);
    const n = Number(num);
    if (section.cards.some((c) => c.n === n)) throw new Error(`Karte ${card.filePath}: Nummer ${num} ist doppelt vergeben`);
    section.cards.push({ entry: card, id: `${key}-${sectionId}-${n}`, n });
  }

  for (const sheet of byKey.values()) {
    for (const s of sheet.sections) s.cards.sort((a, b) => a.n - b.n);
    sheet.count = sheet.sections.reduce((sum, s) => sum + s.cards.length, 0);
  }
  return [...byKey.values()];
}

let cache: Promise<SheetInfo[]> | undefined;

/** Alle Zettel in Reihenfolge, mit Abschnitten und sortierten Karten */
export function getSheets(): Promise<SheetInfo[]> {
  return (cache ??= load());
}
