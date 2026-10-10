"""Free renderer for Song 01 - Bunny ki Gaadi.

Runs on a GitHub Actions runner (open internet): fetches scene art from the free
Pollinations image endpoint, then renders a 1080p karaoke music video with PIL + FFmpeg.
"""
import os, sys, time, math, subprocess, urllib.parse, json
import requests
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
from scenes import STYLE, SCENES, CHORUS, VERSES, VERSE_SHOTS, COUNT_AT, CHORUS_SHOTS, FORM, BPM

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
IMG = os.path.join(OUT, "scenes")
os.makedirs(IMG, exist_ok=True)
W, H, FPS = 1920, 1080, 30
SEED = int(os.environ.get("SEED", "4242"))
AUDIO = os.path.join(HERE, "bunny-ki-gaadi-guide-melody.mp3")
FONT = os.path.join(HERE, "..", "fonts", "NotoSansDevanagari-Bold.ttf")
LAT = os.path.join(HERE, "..", "fonts", "Poppins-Bold.ttf")
BAR = 4 * 60.0 / BPM          # 2.4 s
LINE = 2 * BAR                # 4.8 s


# ---------------------------------------------------------------- images
def fetch(key, prompt):
    path = os.path.join(IMG, f"{key}.jpg")
    if os.path.exists(path) and os.path.getsize(path) > 20000:
        return path
    full = f"{prompt} {STYLE}"
    url = ("https://image.pollinations.ai/prompt/" + urllib.parse.quote(full) +
           f"?width={W}&height={H}&seed={SEED}&model=flux&nologo=true&enhance=false")
    for attempt in range(8):
        try:
            r = requests.get(url, timeout=240)
            if r.status_code == 200 and r.headers.get("content-type", "").startswith("image") and len(r.content) > 20000:
                open(path, "wb").write(r.content)
                im = Image.open(path).convert("RGB")
                if im.size != (W, H):
                    im = im.resize((W, H), Image.LANCZOS)
                im.save(path, quality=95)
                print(f"[ok] {key} ({len(r.content)//1024} KB)", flush=True)
                return path
            print(f"[retry] {key} status {r.status_code}", flush=True)
        except Exception as e:  # noqa
            print(f"[retry] {key} {e}", flush=True)
        time.sleep(15 + attempt * 10)
    raise SystemExit(f"could not fetch {key}")


# ---------------------------------------------------------------- timeline
def timeline():
    """List of segments: dict(start, dur, shot, text, kind, count)."""
    segs, t = [], 0.0
    for name, bars in FORM:
        if name == "intro":
            segs.append(dict(start=t, dur=bars * BAR, shot="C1", text=None, kind="intro", count=None))
        elif name == "outro":
            segs.append(dict(start=t, dur=bars * BAR, shot="OUT", text=None, kind="outro", count=None))
        else:
            lines = CHORUS if name == "chorus" else VERSES[name]
            shots = CHORUS_SHOTS if name == "chorus" else VERSE_SHOTS[name]
            for i, (ln, sh) in enumerate(zip(lines, shots)):
                cnt = COUNT_AT.get(name) if i == 2 else None
                segs.append(dict(start=t + i * LINE, dur=LINE, shot=sh, text=ln, kind=name, count=cnt))
        t += bars * BAR
    return segs, t


# ---------------------------------------------------------------- text helpers
def font(size, latin=False):
    return ImageFont.truetype(LAT if latin else FONT, size,
                              layout_engine=ImageFont.Layout.RAQM if not latin else ImageFont.Layout.BASIC)


def text_layer(txt, size, fill, stroke=(40, 20, 60), sw=8, latin=False):
    f = font(size, latin)
    d = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    x0, y0, x1, y1 = d.textbbox((0, 0), txt, font=f, stroke_width=sw)
    im = Image.new("RGBA", (x1 - x0 + 40, y1 - y0 + 40), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20 - x0, 20 - y0), txt, font=f, fill=fill, stroke_width=sw, stroke_fill=stroke)
    shadow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    shadow.paste((0, 0, 0, 140), mask=im.split()[3])
    shadow = shadow.filter(ImageFilter.GaussianBlur(6))
    out = Image.new("RGBA", (im.width + 12, im.height + 12), (0, 0, 0, 0))
    out.alpha_composite(shadow, (10, 10))
    out.alpha_composite(im, (0, 0))
    return out


_cache = {}


def lyric_pair(txt):
    if txt not in _cache:
        size = 78
        while True:
            a = text_layer(txt, size, (255, 255, 255))
            if a.width < W - 160 or size < 50:
                break
            size -= 4
        b = text_layer(txt, size, (255, 214, 0))
        _cache[txt] = (a, b)
    return _cache[txt]


def lower_band():
    band = Image.new("RGBA", (W, 260), (0, 0, 0, 0))
    d = ImageDraw.Draw(band)
    for y in range(260):
        d.line([(0, y), (W, y)], fill=(10, 0, 30, int(170 * (y / 260) ** 1.4)))
    return band


BAND = None


# ---------------------------------------------------------------- frame
def kenburns(img, p, mode):
    z0, z1 = (1.0, 1.12) if mode % 2 == 0 else (1.12, 1.0)
    z = z0 + (z1 - z0) * p
    cw, ch = W / z, H / z
    dx = (W - cw) * (0.5 + (0.35 if mode % 4 < 2 else -0.35) * (p - 0.5))
    dy = (H - ch) * 0.45
    return img.resize((W, H), Image.BILINEAR, box=(dx, dy, dx + cw, dy + ch))


def ease_back(x):
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2


def render():
    global BAND
    BAND = lower_band()
    segs, total = timeline()
    imgs = {k: Image.open(os.path.join(IMG, f"{k}.jpg")).convert("RGB") for k in SCENES}
    title_a = text_layer("Krushna's Bharat", 74, (255, 214, 0), latin=True)
    title_b = text_layer("बनी की गाड़ी", 170, (255, 255, 255), stroke=(200, 20, 40), sw=12)
    title_c = text_layer("गिनती गाना - 1, 2, 3!", 64, (255, 255, 255))
    out_a = text_layer("शाबाश बच्चों!", 150, (255, 214, 0), stroke=(200, 20, 40), sw=12)
    out_b = text_layer("फिर मिलेंगे — Krushna's Bharat", 64, (255, 255, 255))
    nums = {n: text_layer(str(n), 300, (255, 255, 255), stroke=(220, 40, 60), sw=16, latin=True) for n in (1, 2, 3)}
    word = {1: "एक सवारी", 2: "दो सवारी", 3: "तीन सवारी"}
    numw = {n: text_layer(word[n], 70, (255, 214, 0)) for n in (1, 2, 3)}

    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                         "-of", "csv=p=0", AUDIO]).decode().strip())
    nframes = int(math.ceil(min(dur, float(os.environ.get("MAXSEC", "1e9"))) * FPS))
    mp4 = os.path.join(OUT, "bunny-ki-gaadi-song01.mp4")
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                           "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-i", AUDIO,
                           "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
                           "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", mp4],
                          stdin=subprocess.PIPE)
    XF = 0.35
    for fi in range(nframes):
        t = fi / FPS
        idx = max(i for i, s in enumerate(segs) if s["start"] <= t or i == 0) if t < total else len(segs) - 1
        s = segs[idx]
        p = min(1.0, (t - s["start"]) / s["dur"])
        frame = kenburns(imgs[s["shot"]], p, idx)
        # crossfade from previous shot
        if idx > 0 and t - s["start"] < XF and segs[idx - 1]["shot"] != s["shot"]:
            pv = segs[idx - 1]
            prev = kenburns(imgs[pv["shot"]], min(1.0, (t - pv["start"]) / pv["dur"]), idx - 1)
            frame = Image.blend(prev, frame, (t - s["start"]) / XF)
        # gentle whole-song fade in/out
        fr = frame.convert("RGBA")
        if s["text"]:
            fr.alpha_composite(BAND, (0, H - 260))
            a, b = lyric_pair(s["text"])
            x, y = (W - a.width) // 2, H - a.height - 50
            fr.alpha_composite(a, (x, y))
            prog = max(0.0, min(1.0, (t - s["start"] - 0.15) / (s["dur"] * 0.85)))
            cw = int(20 + (b.width - 40) * prog)
            if cw > 0:
                fr.alpha_composite(b.crop((0, 0, cw, b.height)), (x, y))
        if s["count"]:
            lt = t - s["start"]
            sc = ease_back(min(1.0, lt / 0.45)) if lt < 0.45 else 1.0 + 0.04 * math.sin(lt * 6)
            n = nums[s["count"]]
            nw, nh = max(1, int(n.width * sc)), max(1, int(n.height * sc))
            ni = n.resize((nw, nh), Image.LANCZOS)
            fr.alpha_composite(ni, (W - 330 - nw // 2, 230 - nh // 2))
            if lt > 0.3:
                ww = numw[s["count"]]
                fr.alpha_composite(ww, (W - 330 - ww.width // 2, 420))
        if s["kind"] == "intro":
            lt = t - s["start"]
            for lay, y, d0 in ((title_a, 170, 0.3), (title_b, 300, 0.8), (title_c, 560, 1.6)):
                if lt > d0:
                    k = min(1.0, (lt - d0) / 0.5)
                    sc = ease_back(k)
                    li = lay.resize((max(1, int(lay.width * sc)), max(1, int(lay.height * sc))), Image.LANCZOS)
                    fr.alpha_composite(li, ((W - li.width) // 2, y + (lay.height - li.height) // 2))
        if s["kind"] == "outro":
            lt = t - s["start"]
            if lt > 0.5:
                k = ease_back(min(1.0, (lt - 0.5) / 0.5))
                li = out_a.resize((max(1, int(out_a.width * k)), max(1, int(out_a.height * k))), Image.LANCZOS)
                fr.alpha_composite(li, ((W - li.width) // 2, 90))
            if lt > 1.5:
                fr.alpha_composite(out_b, ((W - out_b.width) // 2, H - out_b.height - 60))
        rgb = fr.convert("RGB")
        fade = min(1.0, t / 0.8, max(0.0, (dur - t) / 1.5))
        if fade < 1.0:
            rgb = Image.blend(Image.new("RGB", (W, H)), rgb, fade)
        ff.stdin.write(rgb.tobytes())
        if fi % 300 == 0:
            print(f"frame {fi}/{nframes}", flush=True)
    ff.stdin.close()
    ff.wait()
    print("done", mp4)
    json.dump(segs, open(os.path.join(OUT, "timeline.json"), "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    for i, (k, pr) in enumerate(SCENES.items()):
        fetch(k, pr)
        time.sleep(6)
    render()
