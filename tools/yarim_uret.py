# yarim_uret.py — Pieces of Mind: Yarım'ın sprite'ı (PLACEHOLDER)
#
# game/images/yarim.png : 120x200 -> 4x NEAREST -> 480x800
#   Diğer görsellerle aynı piksel yoğunluğu (arka planlar 480x270 -> 4x).
#
# Tasarım: Yarım, şövalyenin adını çalmış kovulmuş bir fısıltı — "Hâlâ o yüz."
# Adı hem karakteri hem siluetini anlatıyor: SOL yarısı katı bir beden,
# SAĞ yarısı dikey çizgilere ayrışıyor (tamamlanmamış, çalıntı bir varlık).
# Et rengi bilinçli olarak yanlış (#a05a5a — yr karakterinin rengi).

import math
import os
import random
from PIL import Image, ImageDraw

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
W, H = 120, 200
SEED = 7
random.seed(SEED)

SEFFAF  = (0, 0, 0, 0)
PELERIN = (26, 22, 20, 255)      # yırtık pelerin, zifirin bir ton üstü
PELERIN_I = (44, 37, 33, 255)    # pelerinin ışık alan kenarı
ET      = (160, 90, 90, 255)     # #a05a5a — yanlış et
ET_K    = (108, 58, 58, 255)     # gölgeli et
ET_A    = (196, 122, 118, 255)   # lamba yönünden kenar ışığı
GOZ     = (204, 34, 34, 255)     # iki soluk kırmızı nokta
AGIZ    = (30, 16, 16, 255)

img = Image.new("RGBA", (W, H), SEFFAF)
d = ImageDraw.Draw(img)
MX = 58                           # gövde ekseni

# ── Gövde: pelerinli, omuzları çökük siluet ─────────────────────────────
d.polygon([(MX-26, 196), (MX-20, 96), (MX-14, 74), (MX+14, 74),
           (MX+20, 96), (MX+26, 196)], fill=PELERIN)
# pelerinin sol kenarına ışık
d.line([(MX-20, 96), (MX-26, 196)], fill=PELERIN_I)
d.line([(MX-14, 74), (MX-20, 96)], fill=PELERIN_I)

# yırtık etek: alt kenar düz değil, dişli
for x in range(MX-26, MX+27):
    kesik = random.randint(0, 7)
    d.line([(x, 196), (x, 196 - kesik)], fill=SEFFAF)

# ── Kollar: sol kol uzun ve pençeli, sağ kol kısa (yarım) ───────────────
d.polygon([(MX-20, 100), (MX-30, 132), (MX-27, 150), (MX-21, 148),
           (MX-16, 116)], fill=PELERIN)
for i in range(4):                                  # pençe parmakları
    d.line([(MX-27+i*2, 150), (MX-30+i*3, 162)], fill=ET_K)

d.polygon([(MX+20, 100), (MX+27, 124), (MX+24, 136), (MX+18, 118)],
          fill=PELERIN)

# ── Baş: şövalyenin yüzü, yanlış ette ──────────────────────────────────
d.ellipse([MX-15, 34, MX+15, 76], fill=ET)
d.ellipse([MX-15, 34, MX-4, 76], fill=ET_A)         # lamba yönü kenar ışığı
d.ellipse([MX+7, 40, MX+15, 74], fill=ET_K)         # gölgeli yanak

# göz çukurları + iki kırmızı nokta
d.rectangle([MX-10, 50, MX-4, 55], fill=AGIZ)
d.rectangle([MX+3, 50, MX+9, 55], fill=AGIZ)
d.point([(MX-7, 52), (MX+6, 52)], fill=GOZ)

# ağız: düz, gülümsemeyen bir çizgi
d.line([(MX-6, 66), (MX+5, 65)], fill=AGIZ)

# kaput: başı saran, tepesi sivri bir örtü — alın karanlıkta kalır
d.polygon([(MX-17, 52), (MX-17, 40), (MX-9, 28), (MX, 25), (MX+9, 28),
           (MX+17, 40), (MX+17, 52), (MX+13, 44), (MX+6, 40),
           (MX-6, 40), (MX-13, 44)], fill=PELERIN)
d.line([(MX-17, 44), (MX-9, 29)], fill=PELERIN_I)
# kaputun omuzlara inen kanatları
d.polygon([(MX-17, 48), (MX-23, 80), (MX-14, 76)], fill=PELERIN)
d.polygon([(MX+17, 48), (MX+23, 80), (MX+14, 76)], fill=PELERIN)

# ── "YARIM": sağ yarı dikey çizgilere ayrışır ──────────────────────────
# Eksenin sağında, yukarıdan aşağı arttan bir olasılıkla sütunlar silinir.
px = img.load()
BAS_ALT = 78                                    # bu satırın üstü = baş
for x in range(MX + 8, W):
    uzaklik = (x - MX - 8) / float(W - MX - 8)  # 0 -> 1
    for y in range(H):
        if px[x, y][3] == 0:
            continue
        pay = uzaklik ** 0.85
        # YÜZ KORUNUR: "Hâlâ o yüz." Baş bölgesinde ayrışma çok daha zayıf —
        # tanınabilir kalmalı, yoksa Yarım'ın bütün anlamı gider.
        if y < BAS_ALT:
            pay *= 0.30
        if random.random() < pay * 0.85:
            px[x, y] = SEFFAF
        elif random.random() < pay * 0.30:
            r, g, b, a = px[x, y]
            px[x, y] = (r, g, b, int(a * 0.45))

# ayrışan tarafta havada asılı birkaç kırıntı
for _ in range(120):
    x = random.randint(MX + 10, MX + 40)        # gövdeye yakın: kopuk değil, dökülen
    y = random.randint(60, 194)
    if 0 <= x < W and random.random() < 0.75:
        px[x, y] = (ET_K[0], ET_K[1], ET_K[2], random.randint(70, 170))

img = img.resize((W * 4, H * 4), Image.NEAREST)
hedef = os.path.join(KOK, "game", "images", "yarim.png")
img.save(hedef)
print("yazildi:", os.path.relpath(hedef, KOK), img.size)
