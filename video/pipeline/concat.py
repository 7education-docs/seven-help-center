"""Une varias grabaciones (mp4 + vtt) en una sola, con subtítulos desplazados.
Uso: python3 concat.py salida.mp4 salida.vtt entrada1.mp4 entrada1.vtt [entrada2.mp4 entrada2.vtt ...]"""
import re, subprocess, sys

def dur(p):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]).decode().strip())

def ts(x):
    return f"{int(x // 3600):02d}:{int((x % 3600) // 60):02d}:{x % 60:06.3f}"

def shift_vtt(path, offset):
    txt = open(path, encoding='utf-8').read()
    def repl(m):
        g = list(map(int, m.groups()[:8]))
        s = g[0]*3600 + g[1]*60 + g[2] + g[3]/1000 + offset
        e = g[4]*3600 + g[5]*60 + g[6] + g[7]/1000 + offset
        return f"{ts(s)} --> {ts(e)}"
    body = re.sub(r'(\d{2}):(\d{2}):(\d{2})\.(\d{3}) --> (\d{2}):(\d{2}):(\d{2})\.(\d{3})', repl, txt)
    body = body.split('\n', 1)[1] if body.startswith('WEBVTT') else body
    return body.strip() + '\n'

out_mp4, out_vtt = sys.argv[1], sys.argv[2]
pairs = list(zip(sys.argv[3::2], sys.argv[4::2]))
n = len(pairs)
inputs = []
for mp4, _ in pairs:
    inputs += ['-i', mp4]
parts, labels = [], []
for i in range(n):
    parts.append(f"[{i}:v]fps=25,scale=1280:720,setsar=1,setpts=PTS-STARTPTS[v{i}]")
    parts.append(f"[{i}:a]aformat=sample_rates=48000:channel_layouts=mono,asetpts=PTS-STARTPTS[a{i}]")
    labels.append(f"[v{i}][a{i}]")
graph = ';'.join(parts) + ';' + ''.join(labels) + f"concat=n={n}:v=1:a=1[vout][aout]"
subprocess.check_call(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', graph,
                       '-map', '[vout]', '-map', '[aout]', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '22',
                       '-c:a', 'aac', '-b:a', '128k', out_mp4])
cues, offset = [], 0.0
for mp4, vtt in pairs:
    cues.append(shift_vtt(vtt, offset))
    offset += dur(mp4)
open(out_vtt, 'w', encoding='utf-8').write('WEBVTT\n\n' + '\n'.join(c.strip('\n') + '\n' for c in cues))
print('joined', n, 'parts,', round(offset, 1), 's')
