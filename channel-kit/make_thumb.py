"""Thumbnail for long video 1 (1280x720)."""
from PIL import Image, ImageDraw, ImageFont
W, H = 1280, 720
B = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
img = Image.new("RGB", (W, H), (14, 17, 23)); d = ImageDraw.Draw(img)
f = lambda s: ImageFont.truetype(B, s)
d.text((70, 120), "20%", font=f(190), fill=(110, 116, 128))
x = 70 + d.textlength("20%", font=f(190))
d.line([70, 245, x, 225], fill=(235, 87, 87), width=22)
d.text((x + 30, 150), "→", font=f(140), fill=(245, 245, 240))
d.text((x + 200, 120), "15%", font=f(190), fill=(242, 184, 75))
d.rounded_rectangle([70, 470, 640, 640], 24, fill=(235, 87, 87))
d.text((105, 478), "IT LIED", font=f(130), fill=(255, 255, 255))
img.save("thumb-long-01.png")
