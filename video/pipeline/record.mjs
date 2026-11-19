// Graba una lección siguiendo un guion de escenas en Chromium headless.
// Uso:  SEVEN_BASE_URL=https://sevenai.es SEVEN_USER=... SEVEN_PASS=... node video/pipeline/record.mjs video/scenes/1-1.es.json
// Las credenciales se leen de variables de entorno y nunca se escriben en el repositorio.
// La sesión (storageState) se guarda en video/work/ (ignorado por git) y se borra al terminar con --logout.
import { createRequire } from 'node:module';
import { readFile, mkdir, copyFile, writeFile, rm } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const sceneFile = process.argv[2];
if (!sceneFile) { console.error('Uso: node record.mjs <escenas.json>'); process.exit(1); }
const spec = JSON.parse(await readFile(sceneFile, 'utf8'));
const base = process.env.SEVEN_BASE_URL || spec.baseUrl;
const key = `${spec.lesson.replace('.', '-')}-${spec.locale}`;
const workDir = process.env.WORK_DIR || path.join(ROOT, 'video', 'work', key);
const authFile = path.join(workDir, 'auth.json');
const logoutAfter = process.argv.includes('--logout');
const LOCALE_TAG = { es: 'es-419', 'pt-BR': 'pt-BR' };

await mkdir(workDir, { recursive: true });
const browser = await chromium.launch({
  executablePath: process.env.PW_CHROMIUM || '/opt/pw-browsers/chromium',
  args: ['--no-sandbox'],
});

// 1) Inicio de sesión fuera de la grabación (el video no muestra el login).
async function ensureAuth() {
  // Sesión ya iniciada fuera de la grabación (save-session.mjs o AUTH_FILE).
  if (process.env.NO_AUTH) return undefined; // escena de alumnado: sin sesión del docente
  if (process.env.AUTH_FILE) return process.env.AUTH_FILE;
  if (!spec.login) return undefined;
  if (!process.env.SEVEN_USER || !process.env.SEVEN_PASS) {
    throw new Error('Esta escena requiere inicio de sesión: define SEVEN_USER y SEVEN_PASS como variables de entorno.');
  }
  const ctx = await browser.newContext({ baseURL: base, locale: LOCALE_TAG[spec.locale] });
  const page = await ctx.newPage();
  await page.goto(new URL(spec.login.path, base).href, { waitUntil: 'load' });
  await page.locator(spec.login.userSelector).first().fill(process.env.SEVEN_USER);
  await page.locator(spec.login.passSelector).first().fill(process.env.SEVEN_PASS);
  await page.locator(spec.login.submitSelector).first().click();
  await page.locator(spec.login.successSelector).first().waitFor({ state: 'visible', timeout: 60000 });
  await ctx.storageState({ path: authFile });
  await ctx.close();
  return authFile;
}

// Superposición visual: cursor que se desplaza hasta cada elemento, onda al pulsar y rótulo de paso.
const OVERLAY = `(() => {
  if (window.__ov) return; window.__ov = true;
  const mount = () => {
    if (document.getElementById('__cursor')) return;
    const st = document.createElement('style');
    st.textContent = '#__cursor{position:fixed;left:0;top:0;width:26px;height:26px;z-index:2147483647;pointer-events:none;transition:transform .45s cubic-bezier(.2,.7,.2,1);transform:translate(-100px,-100px);filter:drop-shadow(0 2px 3px rgba(0,0,0,.35))}' +
      '#__ripple{position:fixed;width:38px;height:38px;margin:-19px 0 0 -19px;border-radius:50%;border:3px solid #0e9f9a;z-index:2147483646;pointer-events:none;opacity:0}' +
      '#__ripple.go{animation:rip .5s ease-out}@keyframes rip{from{opacity:.95;transform:scale(.35)}to{opacity:0;transform:scale(1.7)}}' +
      '#__cap{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);max-width:90%;background:rgba(5,5,89,.93);color:#fff;font:600 16px/1.35 Inter,system-ui,sans-serif;padding:10px 20px;border-radius:999px;z-index:2147483646;pointer-events:none;opacity:0;transition:opacity .3s;box-shadow:0 6px 24px rgba(0,0,0,.25);text-align:center}' +
      '#__cap.on{opacity:1}#__cap b{color:#7ff0ea;font-weight:800;margin-right:8px}';
    document.head.appendChild(st);
    const c = document.createElement('div'); c.id = '__cursor';
    c.innerHTML = '<svg viewBox="0 0 24 24" width="26" height="26"><path d="M4 2l15 9-6.5 1.6L16 20l-3 1.4-3.5-7.2L4 17z" fill="#fff" stroke="#050559" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    document.body.appendChild(c);
    const r = document.createElement('div'); r.id = '__ripple'; document.body.appendChild(r);
    const cap = document.createElement('div'); cap.id = '__cap'; document.body.appendChild(cap);
  };
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
  window.__moveTo = (x, y) => { const c = document.getElementById('__cursor'); if (c) c.style.transform = 'translate(' + x + 'px,' + y + 'px)'; };
  window.__ripple = (x, y) => { const r = document.getElementById('__ripple'); if (!r) return; r.style.left = x + 'px'; r.style.top = y + 'px'; r.classList.remove('go'); void r.offsetWidth; r.classList.add('go'); };
  window.__cap = (step, text) => { const cap = document.getElementById('__cap'); if (!cap) return; cap.innerHTML = (step ? '<b>' + step + '</b>' : '') + String(text || '').replace(/[<>&]/g, ''); cap.classList.toggle('on', !!text); };
})();`;

async function pointTo(page, locator) {
  const box = await locator.first().boundingBox().catch(() => null);
  if (!box) return;
  const x = box.x + box.width / 2, y = box.y + box.height / 2;
  await page.evaluate(([x, y]) => window.__moveTo && window.__moveTo(x, y), [x, y]);
  await page.waitForTimeout(480);
  await page.evaluate(([x, y]) => window.__ripple && window.__ripple(x, y), [x, y]);
}

// 2) Acciones de escena. Cada acción tiene "do" y sus parámetros.
async function run(page, a) {
  switch (a.do) {
    case 'goto': await page.goto(new URL(a.url, base).href, { waitUntil: 'load' }); await page.waitForLoadState('networkidle').catch(() => {}); await page.waitForTimeout(500); break;
    case 'click': { const loc = page.locator(a.selector).first(); await pointTo(page, loc); await loc.click(); await page.waitForLoadState('networkidle').catch(() => {}); await page.waitForTimeout(450); break; }
    case 'hover': { const loc = page.locator(a.selector).first(); await pointTo(page, loc); await page.waitForTimeout(a.ms ?? 600); break; }
    case 'type': { const loc = page.locator(a.selector).first(); await pointTo(page, loc); await loc.click(); await loc.pressSequentially(a.text, { delay: a.delay ?? 70 }); await page.waitForTimeout(250); break; }
    case 'fill': { const loc = page.locator(a.selector).first(); await pointTo(page, loc); await loc.click(); await loc.fill(a.value); await page.waitForTimeout(300); break; }
    case 'press': await page.keyboard.press(a.key); await page.waitForTimeout(250); break;
    case 'clickAt': await page.evaluate(([x, y]) => window.__moveTo && window.__moveTo(x, y), [a.x, a.y]); await page.waitForTimeout(480); await page.evaluate(([x, y]) => window.__ripple && window.__ripple(x, y), [a.x, a.y]); await page.mouse.click(a.x, a.y); await page.waitForLoadState('networkidle').catch(() => {}); await page.waitForTimeout(450); break;
    case 'upload': { await page.locator(a.selector).first().setInputFiles(a.file); await page.waitForTimeout(a.ms ?? 2500); break; }
    case 'select': await page.locator(a.selector).first().selectOption(a.value); await page.waitForTimeout(400); break;
    case 'scroll': await page.locator(a.selector).first().scrollIntoViewIfNeeded(); await page.waitForTimeout(300); break;
    case 'waitFor': await page.locator(a.selector).first().waitFor({ state: 'visible', timeout: 30000 }); break;
    case 'waitGone': await page.locator(a.selector).first().waitFor({ state: 'hidden', timeout: a.timeout ?? 60000 }).catch(() => {}); break;
    case 'wait': await page.waitForTimeout(a.ms); break;
    case 'caption': await page.evaluate(([step, text]) => window.__cap && window.__cap(step, text), [a.step || '', a.text || '']); break;
    case 'shot': {
      const dir = path.join(workDir, 'shots'); await mkdir(dir, { recursive: true });
      await page.waitForTimeout(250);
      await page.screenshot({ path: path.join(dir, `${a.name}.jpg`), type: 'jpeg', quality: 90 });
      shots.push(a.name); break;
    }
    case 'highlight': {
      // Marca visual temporal sobre un elemento para guiar la mirada del espectador.
      await page.locator(a.selector).first().evaluate((el, ms) => {
        const prev = el.style.outline, off = el.style.outlineOffset;
        el.style.outline = '4px solid #0e9f9a'; el.style.outlineOffset = '4px';
        el.style.borderRadius = el.style.borderRadius || '8px';
        setTimeout(() => { el.style.outline = prev; el.style.outlineOffset = off; }, ms);
      }, a.ms ?? 1600);
      await page.waitForTimeout(a.ms ?? 1600);
      break;
    }
    default: throw new Error(`Acción desconocida: ${a.do}`);
  }
}
const shots = [];

try {
  const auth = await ensureAuth();
  const ctx = await browser.newContext({
    baseURL: base,
    locale: LOCALE_TAG[spec.locale],
    viewport: { width: 1280, height: 720 },
    storageState: auth,
    recordVideo: { dir: path.join(workDir, 'raw'), size: { width: 1280, height: 720 } },
  });
  await ctx.addInitScript(OVERLAY);
  const page = await ctx.newPage();
  const video = page.video();
  const t0 = Date.now();
  const rel = () => Date.now() - t0;
  const timeline = { lesson: spec.lesson, locale: spec.locale, baseUrl: base, scenes: [] };

  // Preparación fuera de la línea de tiempo: carga inicial, sin pantalla en blanco en las escenas.
  for (const a of spec.setup ?? []) await run(page, a);
  await page.waitForLoadState("networkidle").catch(() => {});
  await page.waitForTimeout(600);
  const t0Scenes = Date.now();
  const relScenes = () => Date.now() - t0Scenes;

  for (const sc of spec.scenes) {
    const startMs = rel();
    if (sc.caption) await run(page, { do: 'caption', step: sc.step, text: sc.caption });
    try {
      for (const a of sc.actions ?? []) await run(page, a);
    } catch (err) {
      console.error(`  ✗ escena ${sc.id}: ${err.message.split('\n')[0]} | URL: ${page.url()}`);
      await page.screenshot({ path: path.join(workDir, `error-${sc.id}.png`) }).catch(() => {});
      throw err;
    }
    timeline.scenes.push({ id: sc.id, say: sc.say, startMs, endMs: rel() });
    console.log(`  escena ${sc.id}: ${((rel() - startMs) / 1000).toFixed(1)} s`);
  }
  await ctx.close();
  await copyFile(await video.path(), path.join(workDir, 'recording.webm'));
  timeline.shots = shots;
  await writeFile(path.join(workDir, 'timeline.json'), JSON.stringify(timeline, null, 2), 'utf8');
  console.log(`✓ Grabación: ${path.join(workDir, 'recording.webm')}`);
} finally {
  await browser.close();
  if (logoutAfter) await rm(authFile, { force: true });
}
