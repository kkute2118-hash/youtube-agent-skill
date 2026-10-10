"""Render a landscape long video from a scene file (offline, free).

    python3 make_long.py scenes_survivorship.py out.mp4

Kokoro TTS for the voice (needs kokoro.onnx and voices.bin in the working
directory), Pillow for frames, ffmpeg for encoding. A scene file defines
SCENES: a list of dicts with `say` (narration) and `kind` plus that kind's
fields. Frames that do not change are drawn once and reused.
"""
import importlib.util, subprocess, sys
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro

W, H, FPS, GAP = 1920, 1080, 30, 0.45
BG, PANEL, FG, MUTED = (14, 17, 23), (28, 33, 43), (245, 245, 240), (150, 156, 168)
COL = dict(green=(52, 199, 120), red=(235, 87, 87), gold=(242, 184, 75), blue=(96, 165, 250), grey=(110, 116, 128))
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
REG = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
_fonts = {}


def F(p, s):
    if (p, s) not in _fonts:
        _fonts[p, s] = ImageFont.truetype(p, s)
    return _fonts[p, s]


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def fade(c, k):
    return tuple(int(BG[i] + (c[i] - BG[i]) * k) for i in range(3))


def centered(d, y, text, font, fill):
    d.text(((W - d.textlength(text, font=font)) / 2, y), text, font=font, fill=fill)


def wrap(d, text, font, width):
    lines, cur = [], ""
    for w in text.split():
        nxt = (cur + " " + w).strip()
        if d.textlength(nxt, font=font) > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = nxt
    return lines + [cur] if cur else lines


def anim_end(s):
    """Seconds after which a scene's drawing (captions aside) stops changing."""
    k = s["kind"]
    if k == "list":
        return s["_at"][-1] + 0.5
    if k == "bars":
        return 0.6 + 0.5 * len(s["bars"]) + 0.9
    return 2.6


def draw(s, t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    k = s["kind"]
    if s.get("tag"):
        d.text((90, 60), s["tag"].upper(), font=F(BOLD, 30), fill=COL["gold"])
    head_k = ease(t / 0.5)
    if k == "title":
        for i, line in enumerate(wrap(d, s["head"], F(BOLD, 96), 1600)):
            centered(d, 300 + i * 115, line, F(BOLD, 96), fade(FG, head_k))
        if s.get("sub"):
            centered(d, 600, s["sub"], F(REG, 50), fade(MUTED, ease((t - 0.8) / 0.6)))
    elif k == "big":
        centered(d, 150, s["head"], F(BOLD, 64), fade(FG, head_k))
        centered(d, 330, s["value"], F(BOLD, 220), fade(COL[s.get("col", "gold")], ease((t - 0.5) / 0.6)))
        if s.get("sub"):
            for i, line in enumerate(wrap(d, s["sub"], F(REG, 48), 1500)):
                centered(d, 650 + i * 64, line, F(REG, 48), fade(MUTED, ease((t - 1.2) / 0.6)))
    elif k == "list":
        d.text((160, 150), s["head"], font=F(BOLD, 72), fill=fade(FG, head_k))
        for i, item in enumerate(s["items"]):
            ik = ease((t - s["_at"][i]) / 0.5)
            if ik <= 0:
                continue
            y = 310 + i * 130
            d.ellipse([170, y + 22, 196, y + 48], fill=fade(COL["gold"], ik))
            d.text((230, y), item, font=F(REG, 54), fill=fade(FG, ik))
    elif k == "bars":
        d.text((160, 120), s["head"], font=F(BOLD, 64), fill=fade(FG, head_k))
        bars, vmax = s["bars"], max(abs(b[1]) for b in s["bars"]) or 1
        n = len(bars)
        slot = 1500 / n
        base, top = 820, 330
        zero = base if min(b[1] for b in bars) >= 0 else base - 120
        d.line([200, zero, 1720, zero], fill=COL["grey"], width=3)
        for i, (label, v, col) in enumerate(bars):
            bk = ease((t - 0.6 - 0.5 * i) / 0.9)
            x0 = 210 + i * slot + slot * 0.2
            x1 = x0 + slot * 0.6
            h = (zero - top) * abs(v) / vmax * bk
            y0, y1 = (zero - h, zero) if v >= 0 else (zero, zero + h)
            if bk > 0:
                d.rectangle([x0, y0, x1, y1], fill=COL[col])
                txt = f"{v * bk:+.1f}{s.get('unit', '%')}" if s.get("signed") else f"{v * bk:.1f}{s.get('unit', '%')}"
                f = F(BOLD, 56)
                tw = d.textlength(txt, font=f)
                ty = y0 - 75 if v >= 0 else y1 + 12
                d.text(((x0 + x1 - tw) / 2, ty), txt, font=f, fill=FG)
            lf = F(REG, 38)
            for j, line in enumerate(wrap(d, label, lf, slot * 0.95)):
                lw = d.textlength(line, font=lf)
                d.text(((x0 + x1 - lw) / 2, 870 + j * 46), line, font=lf, fill=fade(MUTED, ease(t / 0.5)))
    elif k == "table":
        d.text((160, 120), s["head"], font=F(BOLD, 64), fill=fade(FG, head_k))
        cols = s["cols"]
        cw = 1600 / len(cols)
        for j, c in enumerate(cols):
            d.text((160 + j * cw, 270), c, font=F(BOLD, 40), fill=MUTED)
        for i, row in enumerate(s["rows"]):
            rk = ease((t - 0.6 - 0.6 * i) / 0.5)
            y = 350 + i * 110
            d.rounded_rectangle([140, y - 18, 1780, y + 78], 18, fill=fade(PANEL, rk))
            for j, cell in enumerate(row):
                col = FG
                if isinstance(cell, tuple):
                    cell, col = cell[0], COL[cell[1]]
                d.text((160 + j * cw, y), cell, font=F(BOLD if j == 0 else REG, 50), fill=fade(col, rk))
    return img


def caption(img, s, t):
    d = ImageDraw.Draw(img)
    chunk = s["_chunks"][s["_cidx"](t)]
    f = F(BOLD, 50)
    cw = d.textlength(chunk, font=f)
    d.rounded_rectangle([(W - cw) / 2 - 28, 948, (W + cw) / 2 + 28, 1028], 20, fill=(255, 255, 255))
    d.text(((W - cw) / 2, 958), chunk, font=f, fill=(10, 10, 10))
    d.text((W - 560, 40), "Education only. Not investment advice.", font=F(REG, 26), fill=MUTED)
    return img


def prepare(s):
    words = s["say"].split()
    s["_chunks"] = [" ".join(words[i:i + 7]) for i in range(0, len(words), 7)]
    lens = [len(c.split()) for c in s["_chunks"]]
    speak, total = s["dur"] - GAP, sum(lens)
    ends, acc = [], 0.0
    for n in lens:
        acc += n / total * speak
        ends.append(acc)
    s["_cidx"] = lambda t, ends=ends: next((i for i, e in enumerate(ends) if t < e), len(ends) - 1)
    if s["kind"] == "list":
        # reveal each item when the narration reaches its share of the scene
        s["_at"] = [0.6 + i * (speak - 0.6) / len(s["items"]) for i in range(len(s["items"]))]


def main(scene_file, out):
    spec = importlib.util.spec_from_file_location("scenes", scene_file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    scenes = mod.SCENES
    tts = Kokoro("kokoro.onnx", "voices.bin")
    audio, sr = [], 24000
    for s in scenes:
        a, sr = tts.create(s.get("speak", s["say"]), voice=getattr(mod, "VOICE", "am_michael"), speed=1.05, lang="en-us")
        a = np.concatenate([a, np.zeros(int(GAP * sr), dtype=a.dtype)])
        s["dur"] = len(a) / sr
        audio.append(a)
        prepare(s)
    sf.write("voice_long.wav", np.concatenate(audio), sr)
    enc = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
         "-r", str(FPS), "-i", "-", "-i", "voice_long.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p",
         "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-shortest", out],
        stdin=subprocess.PIPE)
    for s in scenes:
        still, cache = None, {}
        end = anim_end(s)
        for f in range(int(round(s["dur"] * FPS))):
            t = f / FPS
            if t < end:
                img = draw(s, t)
            else:
                still = still or draw(s, end)
                img = still.copy()
            ci = s["_cidx"](t)
            if t >= end and ci in cache:
                enc.stdin.write(cache[ci])
                continue
            b = caption(img, s, t).tobytes()
            if t >= end:
                cache[ci] = b
            enc.stdin.write(b)
    enc.stdin.close()
    enc.wait()
    print("seconds", round(sum(s["dur"] for s in scenes), 1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
