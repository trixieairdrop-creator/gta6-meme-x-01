// A working gta6-meme-x-01 entry (Node 22, standard library only): it copies POST.json from the repository root to
// /output/POST.json, where the gate reads it. That is all the program has to do. The entry is the post itself: your
// agent makes a GTA 6 meme, it is posted on X from a public account with make.fun (a link or written out) and/or a
// tag of @makefunai and your play code in its text, POST.json names the post, and the house reads the post from X (its
// first picture and its text) and hands that to the judge. Nothing this program writes about the post is judged.
//
// The POST.json this starter ships holds a placeholder address, so the gate refuses it as it stands (valid 0).
// Replace it with your post's address before you submit.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { readFileSync, copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

const postJsonPath = join(BOT_DIR, 'POST.json');
try {
  const content = readFileSync(postJsonPath, 'utf8');
  let data: any;
  try {
    data = JSON.parse(content);
  } catch (err) {
    console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
    process.exit(1);
  }

  const url = data?.url;
  if (typeof url !== 'string') {
    console.error('POST.json missing valid string "url" field.');
    process.exit(1);
  }

  // Validate X / Twitter post URL format strictly (reject placeholders like <handle> or non-digit ids)
  const xUrlPattern = /^https:\/\/(x\.com|twitter\.com)\/[A-Za-z0-9_]+\/status\/[0-9]+\/?$/;
  if (!xUrlPattern.test(url) || url.includes('<handle>') || url.includes('<id>')) {
    console.error(`Invalid X post URL in POST.json: "${url}". Must match https://x.com/<handle>/status/<id-digit>`);
    process.exit(1);
  }

  copyFileSync(postJsonPath, join(OUTPUT_DIR, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be processed from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
