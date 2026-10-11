"""Thumbnail for long video 2 (1280x720)."""
from PIL import Image, ImageDraw, ImageFont
W, H = 1280, 720
B = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
img = Image.new("RGB", (W, H), (14, 17, 23)); d = ImageDraw.Draw(img)
f = lambda s: ImageFont.truetype(B, s)
d.text((70, 90), "₹1,00,000", font=f(150), fill=(110, 116, 128))
x = 70 + d.textlength("₹1,00,000", font=f(150))
d.line([70, 195, x, 180], fill=(235, 87, 87), width=18)
d.text((70, 270), "₹88", font=f(300), fill=(235, 87, 87))
bx = 80 + d.textlength("₹88", font=f(300)) + 60
d.rounded_rectangle([bx, 330, bx + 330, 520], 28, fill=(242, 184, 75))
d.text((bx + 40, 345), "4X", font=f(150), fill=(14, 17, 23))
d.rounded_rectangle([70, 600, 70 + d.textlength("SAME TRADES", font=f(64)) + 50, 690], 18, fill=(245, 245, 240))
d.text((95, 607), "SAME TRADES", font=f(64), fill=(14, 17, 23))
img.save("thumb-long-02.png")
