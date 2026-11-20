// Borra de la cuenta demo las citas de prueba creadas por la grabación (cita.pt-BR), dejando `keep` copias.
// Uso: SEVEN_USER=... SEVEN_PASS=... node video/pipeline/clean-demo-citas.mjs "<título>" [keep=0]
// Usa la sesión guardada (AUTH_FILE) si existe; solo toca citas con el título exacto indicado.
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const [title, keepArg] = process.argv.slice(2);
const keep = Number(keepArg ?? 0);
if (!title) { console.error('Uso: clean-demo-citas.mjs "<título>" [keep]'); process.exit(1); }
const COURSE = process.env.CITAS_COURSE_URL || 'https://sevenai.es/educa/courses/9LFW6daqyOEv6a08FKD5mQ';
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
const ctx = await browser.newContext({ storageState: process.env.AUTH_FILE, locale: 'pt-BR', viewport: { width: 1280, height: 900 } });
const page = await ctx.newPage();
const label = `Ações para ${title}`;
const open = async () => { await page.goto(COURSE, { waitUntil: 'load' }); await page.waitForTimeout(2000); await page.locator('button:has-text("Compromissos")').first().click(); await page.waitForTimeout(1200); };
const count = () => page.locator(`button[aria-label="${label}"]`).count();
await open();
let n = await count();
console.log(`copias de "${title}": ${n} (dejar ${keep})`);
for (let i = 0; i < 20 && n > keep; i++) {
  await page.locator(`button[aria-label="${label}"]`).nth(n - 1).click(); await page.waitForTimeout(500);
  await page.locator('[role="menuitem"]:has-text("Eliminar")').first().click(); await page.waitForTimeout(700);
  const confirm = page.locator('[role="dialog"] button:has-text("Eliminar"), [role="alertdialog"] button:has-text("Eliminar")');
  if (await confirm.count()) { await confirm.first().click(); await page.waitForTimeout(900); }
  await open(); n = await count();
}
console.log(`quedan: ${n}`);
await browser.close();
