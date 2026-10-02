// @ts-check
import { defineConfig } from 'astro/config';

// Veröffentlicht unter https://miloo-p.github.io/cheatsheet-hub/
export default defineConfig({
  site: 'https://miloo-p.github.io',
  base: '/cheatsheet-hub',
  // Leerraum im HTML bleibt erhalten, damit Fließtext mit Code-Schnipseln nicht zusammenklebt.
  compressHTML: false,
});
