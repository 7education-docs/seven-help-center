// Inicio de sesión MANUAL en la cuenta demo (con PIN, huella o llave de seguridad), en una ventana visible.
// No escribe credenciales. Guarda solo la sesión (cookies) en video/work/auth-demo.json (ignorado por git).
// Uso en tu equipo (requiere pantalla):  npm i playwright && npx playwright install chromium
//                                         node video/pipeline/save-session.mjs
import { createRequire } from 'node:module';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const out = path.join(ROOT, 'video', 'work', 'auth-demo.json');
const base = process.env.SEVEN_BASE_URL || 'https://sevenai.es';

await mkdir(path.dirname(out), { recursive: true });
const browser = await chromium.launch({ headless: false });
const ctx = await browser.newContext({ viewport: { width: 1280, height: 720 }, locale: 'es-419' });
const page = await ctx.newPage();
await page.goto(new URL('/es/login', base).href);
console.log('Inicia sesión en la ventana abierta (PIN, huella o llave). Tienes 5 minutos.');

// Esperamos a salir de las pantallas de login de sevenai.es y Microsoft.
await page.waitForURL(url => {
  const u = new URL(url);
  return u.hostname.endsWith('sevenai.es') && !/login|authentication/.test(u.pathname);
}, { timeout: 300000 });
await page.waitForLoadState('networkidle').catch(() => {});
await ctx.storageState({ path: out });
console.log(`✓ Sesión guardada en ${out}. No la compartas: da acceso a la cuenta.`);
await browser.close();
