# bg_ana_menu_uret.py — Pieces of Mind ana menü görseli + kırmızı ışıma
# bg_ana_menu.png : 480x270 -> 4x NEAREST -> 1920x1080
#   Kapkara oda; sağ-ortada yerde duran kırmızı gaz lambası ve zayıf ışık
#   çemberi; sağ uçta karanlıkta zar zor seçilen ayna; aynanın İÇİNDE iki
#   soluk kırmızı nokta (bir şey izliyor).
# fx_glow_kirmizi.png : 512x512 RGBA yumuşak radyal kırmızı ışıma
#   (ana menüde lambanın üstünde ATL ile nabız gibi atar).

from PIL import Image, ImageDraw
import math
import random

random.seed(7)

W, H = 480, 270

SIYAH   = (10, 10, 10)
TAS1    = (19, 16, 16)
TAS2    = (24, 19, 19)
DERZ    = (13, 11, 11)
METAL   = (38, 32, 28)
METAL_H = (74, 63, 50)
CAM_K   = (122, 26, 22)     # kırmızı cam koyu
CAM_A   = (176, 34, 30)     # kırmızı cam aydınlık yüz
ALEV    = (245, 233, 208)   # alev çekirdeği (krem)
ALEV_D  = (204, 34, 34)
CERCEVE = (31, 26, 22)      # ayna çerçevesi (zifirin bir ton üstü)
AYNA_IC = (14, 13, 13)
GOZ     = (150, 28, 26)     # aynadaki iki nokta (bağırmayan kırmızı)

img = Image.new("RGB", (W, H), SIYAH)
d = ImageDraw.Draw(img)
px = img.load()

# ── Zemin: yalnızca ışık çemberinin ulaştığı yerde taşlar görünür ─────────
LX, LY = 300, 208            # lambanın durduğu nokta (zemin)
YER_Y = 190                  # zemin çizgisi (arkası duvar karanlığı)

# zemin taşları (loş)
for gy in range(YER_Y, H, 14):
    ofs = random.randint(0, 20)
    for gx in range(-ofs, W, random.randint(34, 46)):
        d.rectangle([gx, gy, gx + 40, gy + 13], outline=DERZ)

# ışık çemberi: lambadan uzaklığa göre zemini/duvarı kırmızıyla ısıt
for y in range(H):
    for x in range(W):
        dx = (x - LX) / 150.0
        dy = (y - LY) / 95.0
        m = 1.0 - math.sqrt(dx * dx + dy * dy)
        if m > 0:
            r_, g_, b_ = px[x, y]
            r2 = min(255, int(r_ + 66 * m * m + 10 * m))
            g2 = min(255, int(g_ + 9 * m * m))
            b2 = min(255, int(b_ + 7 * m * m))
            px[x, y] = (r2, g2, b2)

# çemberin dışı: derin karanlık (taş çizgileri yutulur)
for y in range(H):
    for x in range(W):
        dx = (x - LX) / 170.0
        dy = (y - LY) / 115.0
        m = math.sqrt(dx * dx + dy * dy)
        if m > 1.0:
            r_, g_, b_ = px[x, y]
            k = max(0.0, 1.6 - m) / 0.6
            px[x, y] = (int(SIYAH[0] + (r_ - SIYAH[0]) * k),
                        int(SIYAH[1] + (g_ - SIYAH[1]) * k),
                        int(SIYAH[2] + (b_ - SIYAH[2]) * k))

# ── Ayna: sağ uçta, karanlığın bir ton üstü ──────────────────────────────
AX0, AY0, AX1, AY1 = 396, 52, 452, 186
d.rectangle([AX0, AY0, AX1, AY1], fill=CERCEVE)
d.rectangle([AX0 + 4, AY0 + 4, AX1 - 4, AY1 - 4], fill=AYNA_IC)
# çerçevede tek tük yıpranma
for _ in range(10):
    x = random.choice([random.randint(AX0, AX0 + 3), random.randint(AX1 - 3, AX1)])
    y = random.randint(AY0, AY1)
    d.point([x, y], fill=(44, 37, 30))
# aynanın içinde: iki soluk kırmızı nokta, göz hizası, hafif asimetrik
d.point([(419, 96), (426, 97)], fill=GOZ)

# ── Lamba (yerde) ────────────────────────────────────────────────────────
def lamba(cx, taban_y):
    # taban
    d.rectangle([cx - 7, taban_y - 3, cx + 7, taban_y], fill=METAL)
    d.line([cx - 7, taban_y - 3, cx + 7, taban_y - 3], fill=METAL_H)
    # cam gövde
    d.rectangle([cx - 5, taban_y - 17, cx + 5, taban_y - 4], fill=CAM_K)
    d.rectangle([cx - 5, taban_y - 17, cx - 2, taban_y - 4], fill=CAM_A)   # ışık yüzü
    # alev
    d.rectangle([cx - 1, taban_y - 13, cx, taban_y - 8], fill=ALEV_D)
    d.rectangle([cx - 1, taban_y - 11, cx, taban_y - 9], fill=ALEV)
    # üst kapak + kulp
    d.rectangle([cx - 6, taban_y - 20, cx + 6, taban_y - 18], fill=METAL)
    d.line([cx - 6, taban_y - 20, cx + 6, taban_y - 20], fill=METAL_H)
    d.arc([cx - 5, taban_y - 27, cx + 5, taban_y - 19], 180, 360, fill=METAL_H)
    # zeminde yansıma lekesi
    d.ellipse([cx - 16, taban_y + 2, cx + 16, taban_y + 8], outline=(96, 20, 18))

lamba(LX, LY)

# ── Kaydet: 4x NEAREST ───────────────────────────────────────────────────
img = img.resize((1920, 1080), Image.NEAREST)
img.save("/Users/yavuzseremetli/Documents/renpy/pom2/game/images/bg_ana_menu.png")
print("yazildi: bg_ana_menu.png")

# ── Işıma dokusu (RGBA, yumuşak) ─────────────────────────────────────────
G = 512
glow = Image.new("RGBA", (G, G), (0, 0, 0, 0))
gp = glow.load()
for y in range(G):
    for x in range(G):
        dx = (x - G / 2) / (G / 2)
        dy = (y - G / 2) / (G / 2)
        m = 1.0 - math.sqrt(dx * dx + dy * dy)
        if m > 0:
            a = int(120 * (m ** 2.4))
            gp[x, y] = (204, 34, 34, a)
glow.save("/Users/yavuzseremetli/Documents/renpy/pom2/game/images/fx_glow_kirmizi.png")
print("yazildi: fx_glow_kirmizi.png")
