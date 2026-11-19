# Video tutoriales — pipeline

Genera, por lección y por idioma, un MP4 (H.264 + AAC, 1280×720) con:
- grabación real de la plataforma en Chromium headless (Playwright),
- narración con voz femenina neuronal (Kokoro, local): `ef_dora` para español y `pf_dora` para portugués de Brasil,
- subtítulos WebVTT activables desde el reproductor (y transcripción con salto a tiempo en la web).

## Requisitos
- Acceso a `sevenai.es` desde el entorno (ver "Bloqueo de red" en el README raíz).
- `ffmpeg` / `ffprobe`, Node 22, Python 3 con `kokoro-onnx` y `soundfile` (`pip install kokoro-onnx soundfile`).
- Modelos en `video/models/`: `kokoro-v1.0.onnx` y `voices-v1.0.bin` (descarga desde las releases de `thewh1teagle/kokoro-onnx`; no se versionan).

## Uso
```bash
export SEVEN_BASE_URL=https://sevenai.es
export SEVEN_USER='<usuario demo>'      # nunca en el repositorio
export SEVEN_PASS='<contraseña demo>'
video/pipeline/run.sh video/scenes/1-1.es.json      # -> video/out/es/1-1.mp4 y .vtt
video/pipeline/run.sh video/scenes/1-1.pt-BR.json   # -> video/out/pt-br/1-1.mp4 y .vtt
```
Después, `npm run build` publica los vídeos que existan en `video/out/` junto a su lección.

Prueba del pipeline (sin tocar la plataforma): `npm run video:test`, con una página de prueba local en `video/test/fixture` (servir con `python3 -m http.server 8081 --directory video/test/fixture`).

## Formato del guion (`video/scenes/<lección>.<idioma>.json`)
```json
{
  "lesson": "1.1",
  "locale": "es",
  "baseUrl": "https://sevenai.es",
  "login": { "path": "/login", "userSelector": "…", "passSelector": "…", "submitSelector": "…", "successSelector": "…" },
  "scenes": [
    { "id": "bienvenida",
      "say": "Texto exacto de la narración. Una o dos frases por escena.",
      "actions": [
        { "do": "goto", "url": "/cursos" },
        { "do": "highlight", "selector": "…", "ms": 1500 },
        { "do": "click", "selector": "…" },
        { "do": "type", "selector": "…", "text": "…", "delay": 70 },
        { "do": "waitFor", "selector": "…" },
        { "do": "wait", "ms": 800 }
      ] }
  ]
}
```
Acciones: `goto`, `click`, `type`, `press`, `select`, `scroll`, `waitFor`, `wait`, `highlight`.

Reglas de calidad:
- La narración se escribe **después** de verificar la pantalla. Un selector o una etiqueta mal validada produce un vídeo que enseña algo distinto a lo que dice.
- Si la narración dura más que las acciones de la escena, el último fotograma se mantiene. Para que el ritmo sea natural, añade `wait` o `highlight` hasta igualar la duración de la voz.
- El login se hace fuera de la grabación (la sesión se guarda en `video/work/` y no entra en el vídeo). Con `--logout`, `record.mjs` borra la sesión al terminar.
- Las escenas de cada idioma deben abrir la plataforma en ese idioma (Configuración → idioma), para que la interfaz del vídeo coincida con la narración.

## Archivos
- `pipeline/record.mjs`: graba y genera `timeline.json` (tiempos por escena).
- `pipeline/narrate.py`: narración por escena (`narration.json`).
- `pipeline/assemble.py`: recorte, mezcla, MP4 final y VTT (máx. 2 líneas de 42 caracteres; subtítulos de al menos 1,6 s).
- `pipeline/run.sh`: encadena los tres pasos.
- `scenes/_plantilla.json`: plantilla vacía para las 23 lecciones; los selectores son marcadores que hay que validar.
- `models/`, `work/`, `test/out/`: no se versionan (ver `.gitignore`).
