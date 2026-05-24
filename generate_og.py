"""Generate Open Graph share image: 1200x630 with hero bg + tagline."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from bidi.algorithm import get_display

ROOT = Path(__file__).parent
HERO = ROOT / "assets" / "hero.jpg"
OUT = ROOT / "assets" / "og.jpg"

W, H = 1200, 630

# Load + cover-crop hero to OG aspect
src = Image.open(HERO).convert("RGB")
src_w, src_h = src.size
scale = max(W / src_w, H / src_h)
new_w, new_h = int(src_w * scale), int(src_h * scale)
src = src.resize((new_w, new_h), Image.LANCZOS)
left = (new_w - W) // 2
top = (new_h - H) // 2
img = src.crop((left, top, left + W, top + H))

# Dark gradient overlay for text legibility
overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(overlay)
for y in range(H):
    alpha = int(160 + (y / H) * 70)  # 160 top → 230 bottom
    draw.rectangle([0, y, W, y + 1], fill=(8, 10, 14, alpha))
img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

# Text — RTL Hebrew
draw = ImageDraw.Draw(img)

def find_font(*candidates, size=64):
    for name in candidates:
        for path in [
            f"C:/Windows/Fonts/{name}",
            f"/usr/share/fonts/truetype/{name}",
            f"/c/Users/saraa/.fonts/{name}",
            f"/c/Windows/Fonts/{name}",
        ]:
            if Path(path).exists():
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# Use arialbd / arial — guaranteed Hebrew support on Windows
title_font = find_font("arialbd.ttf", "Heebo-Bold.ttf", size=92)
sub_font   = find_font("arial.ttf", "Heebo-Regular.ttf", size=36)
brand_font = find_font("arialbd.ttf", "Heebo-Bold.ttf", size=24)

# Compose Hebrew text (RTL — but PIL renders left-to-right; modern PIL handles RTL automatically with Latin/numeric mix only.
# For pure Hebrew we just pass the string and rely on the font's bidi handling.)
# Use bidi to convert logical-order Hebrew to display-order for PIL.
title_line1 = get_display("העסק שלך")
title_line2 = get_display("מנהל את עצמו.")
subtitle = get_display("עוזר AI אישי בוואטסאפ · תוך 14 ימים · אפס סיכון")
brand = get_display("AI STUDIO · הילל אקנין")

# Title — right-aligned (RTL)
margin_r = 80
y = 200

# Line 1
bbox1 = draw.textbbox((0, 0), title_line1, font=title_font)
w1 = bbox1[2] - bbox1[0]
draw.text((W - margin_r - w1, y), title_line1, fill=(245, 246, 248), font=title_font)
y += 110

# Line 2 — gradient feel via slightly muted color
bbox2 = draw.textbbox((0, 0), title_line2, font=title_font)
w2 = bbox2[2] - bbox2[0]
draw.text((W - margin_r - w2, y), title_line2, fill=(200, 215, 235), font=title_font)
y += 130

# Subtitle
bbox3 = draw.textbbox((0, 0), subtitle, font=sub_font)
w3 = bbox3[2] - bbox3[0]
draw.text((W - margin_r - w3, y), subtitle, fill=(180, 195, 215), font=sub_font)

# Brand — bottom right
bbox4 = draw.textbbox((0, 0), brand, font=brand_font)
w4 = bbox4[2] - bbox4[0]
draw.text((W - margin_r - w4, H - 60), brand, fill=(120, 165, 230), font=brand_font)

# Accent dot — top left (the only Latin direction element)
draw.ellipse([margin_r, 60, margin_r + 14, 60 + 14], fill=(80, 160, 240))

img.save(OUT, "JPEG", quality=88, optimize=True)
print(f"Generated: {OUT} ({OUT.stat().st_size//1024}KB)")
