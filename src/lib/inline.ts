/*
 * Kleines Inline-Markdown für Kartentexte: `Code`, **fett** und [Text](url).
 * Bewusst ohne Absätze, Listen oder HTML, damit die Texte überall gleich aussehen.
 */

const BASE = import.meta.env.BASE_URL.replace(/\/$/, '');

/** Pfad innerhalb der Website, z.B. url('/css/') -> '/cheatsheet-hub/css/' */
export function url(path = '/'): string {
  return BASE + (path.startsWith('/') ? path : '/' + path);
}

export function escapeHtml(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

type Part = { text: string } | { code: string };

/** Zerlegt einen Text in normale Abschnitte und Code-Spans (auch ``mit `Backticks` darin``). */
function split(s: string): Part[] {
  const parts: Part[] = [];
  let i = 0;
  let last = 0;
  while (i < s.length) {
    if (s[i] !== '`') {
      i++;
      continue;
    }
    let n = 0;
    while (s[i + n] === '`') n++;
    const fence = '`'.repeat(n);
    let j = i + n;
    let end = -1;
    while ((j = s.indexOf(fence, j)) !== -1) {
      if (s[j + n] !== '`') {
        end = j;
        break;
      }
      while (s[j] === '`') j++;
    }
    if (end === -1) {
      i += n;
      continue;
    }
    parts.push({ text: s.slice(last, i) });
    let code = s.slice(i + n, end);
    if (code.length > 2 && code.startsWith(' ') && code.endsWith(' ') && code.trim()) code = code.slice(1, -1);
    parts.push({ code });
    i = last = end + n;
  }
  parts.push({ text: s.slice(last) });
  return parts;
}

function text(s: string): string {
  return escapeHtml(s)
    .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>')
    .replace(/\[([^\]]+)\]\(([^)\s]+)\)/g, (_, label: string, href: string) =>
      href.startsWith('/')
        ? `<a href="${url(href)}">${label}</a>`
        : `<a href="${href}" target="_blank" rel="noopener">${label}</a>`,
    );
}

/** Inline-Markdown zu HTML */
export function inline(md: string): string {
  return split(md)
    .map((p) => ('code' in p ? `<code>${escapeHtml(p.code)}</code>` : text(p.text)))
    .join('');
}

/** Inline-Markdown zu reinem Text, z.B. für Inhaltsverzeichnis und Suche */
export function plain(md: string): string {
  return split(md)
    .map((p) => ('code' in p ? p.code : p.text.replace(/\*\*(.+?)\*\*/g, '$1').replace(/\[([^\]]+)\]\([^)\s]+\)/g, '$1')))
    .join('');
}

/** "Ausführlich" -> "Nur ausführlich", "Mit GSAP" -> "Nur mit GSAP" */
export function onlyLabel(label: string): string {
  return 'Nur ' + label.charAt(0).toLowerCase() + label.slice(1);
}
