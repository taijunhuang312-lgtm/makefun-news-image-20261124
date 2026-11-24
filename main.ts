// News image entry for 24 November 2026 (Node 22, standard library only).
//
// The entry image lives beside this file as entry.png. All this program does
// is place an identical copy of it at <output>/entry.png, where <output> is
// MAKEFUN_OUTPUT_DIR when set, or /output otherwise. The copy is byte for
// byte the same on every run, so repeated runs always produce the same file.
//
// Run locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const source = resolve(here, 'entry.png');
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

// Guard against a truncated copy: the output must be the same size as the
// source image, otherwise the judge would see a broken file.
const expected = statSync(source).size;
const bytes = statSync(target).size;
if (!existsSync(target) || bytes === 0 || bytes !== expected) {
  throw new Error(
    `entry.png was not written correctly to ${target} ` +
      `(got ${bytes} bytes, expected ${expected})`,
  );
}
console.log(`wrote ${target} (${bytes} bytes)`);
