import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

/*
 * Zwei Sammlungen:
 *   sheets  src/content/sheets/<zettel>.md                  ein Spickzettel mit Texten, Farben und Abschnitten
 *   cards   src/content/cards/<zettel>/<abschnitt>/NN-*.md   eine Karte, NN bestimmt die Reihenfolge
 *
 * Texte dürfen Inline-Markdown enthalten: `Code`, **fett** und [Links](/css/).
 * Links, die mit / beginnen, zeigen auf Seiten dieser Website.
 */

const palette = z.object({
  accent: z.string(),
  accentSoft: z.string(),
  long: z.string(),
  longSoft: z.string(),
});

const tone = z.enum(['accent', 'long', 'warn']);
const pair = z.tuple([z.string(), z.string()]);

const sheets = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/sheets' }),
  schema: z.object({
    /** Überschrift der Seite, z.B. "CSS Spickzettel" */
    title: z.string(),
    /** Kurzer Name für Leiste, Hub und Suche, z.B. "CSS" */
    name: z.string(),
    order: z.number(),
    category: z.enum(['grundlagen', 'animation', 'produkt']),
    badge: z.string(),
    level: z.string(),
    blurb: z.string(),
    eyebrow: z.string(),
    /** Standardsprache der Code-Blöcke für das Highlighting */
    lang: z.string(),
    /** Beschriftung der beiden Code-Spalten */
    labels: pair.default(['Kurz', 'Ausführlich']),
    /** Beschriftung, wenn eine Karte nur einen Code-Block hat */
    singleLabel: z.string().default('Code'),
    /** Farben der beiden Spalten */
    tones: z.tuple([tone, tone]).default(['accent', 'long']),
    /** Umschalter "Beide / Nur … / Nur …" im Ansicht-Menü */
    variantToggle: z.boolean().default(true),
    whenHeading: z.string().default('Wann welche Schreibweise?'),
    /** Welche Bibliothek die Live-Demos brauchen */
    demos: z.enum(['gsap', 'three']).optional(),
    colors: z.object({ light: palette, dark: palette, keyword: z.string() }),
    /** {count} wird durch die Zahl der Karten ersetzt */
    lede: z.string(),
    disclaimer: z.string().optional(),
    legend: z.array(z.object({ label: z.string(), text: z.string() })),
    placeholder: z.string(),
    sections: z.array(
      z.object({
        id: z.string().regex(/^[a-z0-9]+$/, 'Abschnitts-IDs bitte nur mit Kleinbuchstaben und Ziffern'),
        title: z.string(),
        tag: z.string(),
        sub: z.string(),
      }),
    ),
    footer: z.string(),
    /** Überschrift des Zusatzkastens am Ende. Sein Inhalt ist der Markdown-Text dieser Datei. */
    infobox: z.string().optional(),
  }),
});

const cards = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/cards' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    /** Überschreibt die Spaltenbeschriftung des Zettels für diese Karte */
    labels: pair.optional(),
    code: z.object({
      short: z.string(),
      long: z.string().optional(),
    }),
    /** Überschreibt die Sprache pro Spalte, z.B. tsx oder css */
    lang: z
      .object({
        short: z.string().optional(),
        long: z.string().optional(),
      })
      .optional(),
    /** Live-Demo: html ist das Startmarkup, js der Funktionsrumpf mit der Variable stage */
    demo: z
      .object({
        height: z.number().default(160),
        flush: z.boolean().default(false),
        html: z.string().default(''),
        js: z.string(),
      })
      .optional(),
    /**
     * Vorschau: html und css werden isoliert in einem eigenen Rahmen gezeigt.
     * sizes schaltet die Breite um (in px, die erste ist der Start), replay zeigt "Neu starten".
     */
    preview: z
      .object({
        height: z.number().default(160),
        sizes: z.array(z.number().int().positive()).min(2).optional(),
        replay: z.boolean().default(false),
        html: z.string(),
        css: z.string(),
      })
      .optional(),
    explain: z.object({
      picture: z.string(),
      steps: z.array(z.string()).min(1),
      mistake: z.string(),
      when: z.string(),
      question: z.string(),
      answer: z.string(),
    }),
    /** Doku-Links. Ein Pfad wie /css/#grid verweist auf eine Seite dieser Website. */
    links: z.array(
      z.object({
        text: z.string(),
        url: z.union([z.url(), z.string().regex(/^\/[\w\-/#]*$/, 'Interne Links beginnen mit /, z.B. /css/#grid')]),
      }),
    ),
  }),
});

export const collections = { sheets, cards };
