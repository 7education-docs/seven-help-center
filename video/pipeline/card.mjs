// Renderiza la portada (intro) de un vídeo tutorial como PNG 1280×720, con el mismo estilo
// que el reproductor de la ayuda: fondo azul noche, marca en mayúsculas, título grande y subtítulo.
// Uso: node video/pipeline/card.mjs <salida.png> <marca> <título> <subtítulo>
import { createRequire } from 'node:module';
import { writeFile } from 'node:fs/promises';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const [out, brand, title, subtitle = ''] = process.argv.slice(2);
if (!out || !title) { console.error('Uso: card.mjs <salida.png> <marca> <título> [subtítulo]'); process.exit(1); }

const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const html = `<!doctype html><html lang="pt-BR"><meta charset="utf-8"><style>
  html,body{margin:0;width:1280px;height:720px;overflow:hidden}
  body{background:radial-gradient(ellipse 60% 55% at 28% 8%,#1d3a63 0%,#0d1d34 55%,#0a1424 100%);
       color:#fff;font-family:"Segoe UI","Inter","Helvetica Neue",Arial,sans-serif;
       display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 80px;box-sizing:border-box}
  .brand{font-size:20px;letter-spacing:.32em;text-transform:uppercase;color:#a9bdd3;margin-bottom:34px}
  .title{font-size:76px;font-weight:800;line-height:1.08;letter-spacing:-.01em;max-width:1080px;text-wrap:balance}
  .rule{width:84px;height:4px;border-radius:2px;background:#2f74e6;margin:34px 0 26px}
  .sub{font-size:32px;color:#c3d0de;max-width:1000px;text-wrap:balance}
</style><body>
  <div class="brand">${esc(brand)}</div>
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
