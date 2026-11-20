// Renderiza la portada (intro) de un vídeo tutorial como PNG 1280×720 con la paleta de Seven Assistant
// (tokens de single/template.html: ink #1e1e1e, primario rosa #e6336e) y el logotipo de la marca.
// Uso: node video/pipeline/card.mjs <salida.png> <texto alternativo de marca> <título> [subtítulo]
import { createRequire } from 'node:module';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [out, brandAlt = 'Seven Assistant', title, subtitle = ''] = process.argv.slice(2);
if (!out || !title) { console.error('Uso: card.mjs <salida.png> <marca> <título> [subtítulo]'); process.exit(1); }

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const logo = 'data:image/png;base64,' + (await readFile(path.join(ROOT, 'single', 'logo-seven-assistant.png'))).toString('base64');
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

const html = `<!doctype html><html lang="pt-BR"><meta charset="utf-8"><style>
  html,body{margin:0;width:1280px;height:720px;overflow:hidden}
  body{background:radial-gradient(ellipse 55% 60% at 12% 0%,rgba(230,51,110,.30) 0%,rgba(230,51,110,0) 70%),
                 linear-gradient(180deg,#242424 0%,#1e1e1e 60%,#171717 100%);
       color:#fff;font-family:"Plus Jakarta Sans",Inter,"Segoe UI",Helvetica,Arial,sans-serif;
       display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 80px;box-sizing:border-box}
  .logo{height:44px;margin-bottom:44px;filter:invert(1) hue-rotate(180deg)}
  .title{font-size:76px;font-weight:800;line-height:1.08;letter-spacing:-.015em;max-width:1080px;text-wrap:balance}
  .rule{width:88px;height:5px;border-radius:3px;background:#e6336e;margin:34px 0 26px}
  .sub{font-size:32px;color:#d6cfd9;max-width:1000px;text-wrap:balance;font-family:Inter,"Segoe UI",Helvetica,Arial,sans-serif}
</style><body>
  <img class="logo" src="${logo}" alt="${esc(brandAlt)}">
  <div class="title">${esc(title)}</div>
  <div class="rule"></div>
  ${subtitle ? `<div class="sub">${esc(subtitle)}</div>` : ''}
</body></html>`;

const browser = await chromium.launch({ executablePath: process.env.PW_CHROMIUM || '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
await page.setContent(html, { waitUntil: 'load' });
await page.evaluate(() => document.fonts && document.fonts.ready);
await page.screenshot({ path: out, type: 'png' });
await browser.close();
console.log(`✓ Portada: ${out}`);
