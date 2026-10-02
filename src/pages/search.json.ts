/* Suchindex für die Startseite: eine Zeile pro Karte, inklusive Erklärungstext */
import type { APIRoute } from 'astro';
import { getSheets } from '../lib/content';
import { plain } from '../lib/inline';

export const GET: APIRoute = async () => {
  const index = [];
  for (const sheet of await getSheets()) {
    for (const sec of sheet.sections) {
      for (const card of sec.cards) {
        const d = card.entry.data;
        const e = d.explain;
        const text = [e.picture, ...e.steps, e.mistake, e.when, e.question, e.answer].map(plain).join(' ');
        index.push({
          id: card.id,
          s: sheet.key,
          st: sheet.entry.data.name,
          sec: sec.title,
          t: plain(d.title),
          d: plain(d.description),
          x: text.slice(0, 900),
        });
      }
    }
  }
  return new Response(JSON.stringify(index), { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
};
