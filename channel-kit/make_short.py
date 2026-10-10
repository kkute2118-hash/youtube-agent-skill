"""Render the sample faceless Short: 'Why a 50% Loss Needs a 100% Gain'.

Offline: Kokoro TTS for the voice, Pillow for frames, ffmpeg for encoding.
"""
import subprocess, sys, os, numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro_onnx import Kokoro

OUT = sys.argv[1]
W, H, FPS = 1080, 1920, 30
BG, FG, MUTED = (14, 17, 23), (245, 245, 240), (150, 156, 168)
GREEN, RED, GOLD = (52, 199, 120), (235, 87, 87), (242, 184, 75)
BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
REG = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
F = lambda p, s: ImageFont.truetype(p, s)

# Each scene: narration, headline, bar values (start->end, in rupees), colour.
SCENES = [
    dict(say="Lose half your money, and you need to double it just to get back to where you started. Here's the maths.",
         head="−50% needs +100%", bar=None),
    dict(say="Say you invest ten thousand rupees.",
         head="You invest", bar=(0, 10000), col=GREEN),
    dict(say="The stock falls fifty percent. You now have five thousand.",
         head="It falls 50%", bar=(10000, 5000), col=RED),
    dict(say="Then it rises fifty percent. Most people think you're back to even. You're not. Fifty percent of five thousand is only two thousand five hundred.",
         head="It rises 50%", bar=(5000, 7500), col=GOLD, note="Still down ₹2,500"),
    dict(say="To get from five thousand back to ten thousand, you have to gain five thousand. That's one hundred percent of what you have left.",
         head="To break even", bar=(5000, 10000), col=GREEN, note="You need +100%"),
    dict(say="And it gets worse the deeper you fall. Lose ten percent, you need eleven. Lose twenty five, you need thirty three. Lose fifty, you need a hundred. Lose seventy five, and you need three hundred percent.",
         head="The recovery table", table=[("−10%", "+11%"), ("−25%", "+33%"), ("−50%", "+100%"), ("−75%", "+300%")]),
    dict(say="So the first rule isn't finding winners. It's keeping your losses small. Follow for more money maths.",
         head="Rule #1", note="Keep losses small"),
]

tts = Kokoro("kokoro.onnx", "voices.bin")
GAP = 0.35
audio, sr = [], 24000
for s in SCENES:
    a, sr = tts.create(s["say"], voice="am_michael", speed=1.08, lang="en-us")
    a = np.concatenate([a, np.zeros(int(GAP * sr), dtype=a.dtype)])
    s["dur"] = len(a) / sr
    audio.append(a)
sf.write("voice.wav", np.concatenate(audio), sr)


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def centered(d, y, text, font, fill):
    w = d.textlength(text, font=font)
    d.text(((W - w) / 2, y), text, font=font, fill=fill)


def caption_chunks(text, n=5):
    words = text.split()
    return [" ".join(words[i:i + n]) for i in range(0, len(words), n)]


def frame(s, t):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    a = ease(t / 0.5)
    head_col = tuple(int(BG[i] + (FG[i] - BG[i]) * a) for i in range(3))
    centered(d, 260, s["head"], F(BOLD, 92), head_col)

    if s.get("bar"):
        v0, v1 = s["bar"]
        v = v0 + (v1 - v0) * ease((t - 0.3) / 0.9)
        base, top_max, bw = 1300, 520, 360
        h = (top_max) * v / 10000
        d.rectangle([(W - bw) / 2, base - top_max, (W + bw) / 2, base], outline=(40, 46, 58), width=4)
        d.rectangle([(W - bw) / 2, base - h, (W + bw) / 2, base], fill=s["col"])
        centered(d, base - top_max - 150, f"₹{int(round(v / 10) * 10):,}", F(BOLD, 120), FG)
    elif s.get("table"):
        for i, (loss, need) in enumerate(s["table"]):
            k = ease((t - 0.4 - i * 0.9) / 0.4)
            if k <= 0:
                continue
            y = 560 + i * 190
            c = lambda col: tuple(int(BG[j] + (col[j] - BG[j]) * k) for j in range(3))
            d.text((150, y), loss, font=F(BOLD, 96), fill=c(RED))
            d.text((480, y + 6), "→", font=F(BOLD, 90), fill=c(MUTED))
            d.text((620, y), need, font=F(BOLD, 96), fill=c(GREEN))
    elif s is SCENES[0]:
        k = ease((t - 0.6) / 0.6)
        centered(d, 800, "₹10,000 → ₹5,000", F(BOLD, 96), tuple(int(BG[j] + (RED[j] - BG[j]) * k) for j in range(3)))
        k2 = ease((t - 2.0) / 0.6)
        centered(d, 960, "needs +100% to recover", F(REG, 64), tuple(int(BG[j] + (GOLD[j] - BG[j]) * k2) for j in range(3)))

    if s.get("note"):
        k = ease((t - 1.2) / 0.5)
        y = 1400 if s.get("bar") else 900
        centered(d, y, s["note"], F(BOLD, 84 if not s.get("bar") else 70),
                 tuple(int(BG[j] + (GOLD[j] - BG[j]) * k) for j in range(3)))

    # burned-in captions, timed by word share
    chunks = caption_chunks(s["say"])
    speak = s["dur"] - GAP
    words = [len(c.split()) for c in chunks]
    acc, idx = 0.0, len(chunks) - 1
    for i, n in enumerate(words):
        acc += n / sum(words) * speak
        if t < acc:
            idx = i
            break
    cf = F(BOLD, 64)
    cw = d.textlength(chunks[idx], font=cf)
    d.rounded_rectangle([(W - cw) / 2 - 30, 1560, (W + cw) / 2 + 30, 1660], 24, fill=(255, 255, 255))
    d.text(((W - cw) / 2, 1572), chunks[idx], font=cf, fill=(10, 10, 10))

    centered(d, 1810, "Education only. Not investment advice.", F(REG, 34), MUTED)
    return img


enc = subprocess.Popen(
    ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
     "-r", str(FPS), "-i", "-", "-i", "voice.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p",
     "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "160k", "-shortest", OUT],
    stdin=subprocess.PIPE)
for s in SCENES:
    for f in range(int(round(s["dur"] * FPS))):
        enc.stdin.write(frame(s, f / FPS).tobytes())
enc.stdin.close()
enc.wait()
print("total seconds", round(sum(s["dur"] for s in SCENES), 1))
