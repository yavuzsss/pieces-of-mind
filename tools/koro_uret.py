# koro_uret.py — Pieces of Mind: Koro (Altın Alev)
#
# game/images/koro.png : 170x210 -> 4x NEAREST -> 680x840
#
# Koro bir figür değil: isimlerden örülü altın bir alev. Senaryodaki tarif
# ("İsimler. Binlerce isim, altın iplikler gibi yanıyor. Alev isimlerden
# yapılmış.") doğrudan çizim talimatı — o yüzden alev, TEK TEK GÖRÜLEBİLEN
# dikey ipliklerden kuruldu. Uzaktan alev, yaklaşınca iplik yumağı.
#
# Renk bilinçli olarak palet dışı (#d9a441): Koro buradan değil.
#
# İplikler arasında birkaç tanesi ötekilerden PARLAK ve bir tanesi aşağı
# SARKIYOR — Sahne 6'nın ikinci yolu ("ipliklerden biri ötekiler gibi
# durmuyor... bana doğru sarkıyor") görselde karşılığını bulsun diye.

import math
import os
import random
from PIL import Image, ImageDraw

random.seed(41)
KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
W, H = 170, 210
BOS = (0, 0, 0, 0)

# Altın rampası — koyudan çekirdeğe
A = [(58, 38, 12), (92, 62, 20), (134, 94, 34), (178, 128, 52),
     (217, 164, 65), (238, 197, 118), (252, 232, 190)]

img = Image.new("RGBA", (W, H), BOS)
px = img.load()
MX = W // 2
TABAN = H - 6

def kat(x, y, renk, guc):
    """Işığı üst üste bindir: iplikler kesiştikçe çekirdek parlar."""
    if not (0 <= x < W and 0 <= y < H):
        return
    r, g, b, a = px[x, y]
    nr, ng, nb = renk
    px[x, y] = (min(255, int(r + nr * guc)), min(255, int(g + ng * guc)),
                min(255, int(b + nb * guc)), min(255, int(a + 255 * guc)))

# ── İPLİKLER ─────────────────────────────────────────────────────────────
IPLIK = 190
for n in range(IPLIK):
    # Her iplik tabandan çıkar, yukarı doğru daralarak yükselir.
    taban_x = MX + random.gauss(0, 20)
    yukseklik = random.uniform(0.35, 1.0)
    tepe_y = int(TABAN - yukseklik * (H - 30))
    faz = random.uniform(0, 6.28)
    genlik = random.uniform(1.5, 7.0) * yukseklik
    parlak = random.random()
    # merkeze yakın iplikler daha parlak
    merkezlik = max(0.0, 1.0 - abs(taban_x - MX) / 34.0)
    for y in range(TABAN, tepe_y, -1):
        t = (TABAN - y) / float(max(1, TABAN - tepe_y))     # 0 taban -> 1 tepe
        # yukarı çıktıkça merkeze doğru toplan + salın
        x = taban_x * (1 - t * 0.55) + MX * (t * 0.55)
        x += math.sin(faz + t * 5.0) * genlik * (0.35 + t)
        # yoğunluk: ortada güçlü, tepede söner
        yog = (0.30 + 0.70 * merkezlik) * (1.0 - t ** 1.7)
        if parlak > 0.90:
            yog *= 1.9                                       # birkaç iplik öne çıkar
        ton = A[min(6, int(yog * 8))]
        kat(int(x), y, ton, min(0.85, yog * 0.55))
        if yog > 0.5:                                        # kalın iplikler
            kat(int(x) + 1, y, ton, min(0.5, yog * 0.28))

# ── ÇEKİRDEK: tabanda yoğunlaşan ışık ───────────────────────────────────
for y in range(TABAN, TABAN - 60, -1):
    t = (TABAN - y) / 60.0
    genislik = int(26 * (1 - t * 0.6))
    for x in range(MX - genislik, MX + genislik):
        d = abs(x - MX) / float(max(1, genislik))
        guc = (1 - d * d) * (1 - t) * 0.5
        if guc > 0:
            kat(x, y, A[5], guc)

# ── SARKAN İPLİK: ötekiler yukarı yanar, bu aşağı sarkar ────────────────
sx, sy = MX + 14, TABAN - 96
for i in range(46):
    x = sx + int(math.sin(i * 0.22) * 4) + i // 6
    y = sy + i
    kat(x, y, A[5], 0.55)
    kat(x + 1, y, A[4], 0.30)
# ucunda bir düğüm — "bana doğru sarkıyor"
for (dx, dy) in [(0,0),(1,0),(0,1),(1,1),(2,0),(0,2)]:
    kat(sx + int(math.sin(45*0.22)*4) + 45//6 + dx, sy + 45 + dy, A[6], 0.7)

# ── HALE: alevin çevresine çok zayıf bir ışıma ──────────────────────────
hale = Image.new("RGBA", (W, H), BOS)
hp = hale.load()
for y in range(H):
    for x in range(W):
        dx = (x - MX) / 52.0
        dy = (y - (TABAN - 40)) / 78.0
        m = 1.0 - math.sqrt(dx*dx + dy*dy)
        if m > 0:
            a = int(46 * (m ** 2.6))
            hp[x, y] = (217, 164, 65, a)
img = Image.alpha_composite(hale, img)

img = img.resize((W * 4, H * 4), Image.NEAREST)
hedef = os.path.join(KOK, "game", "images", "koro.png")
img.save(hedef)
print("yazildi:", os.path.relpath(hedef, KOK), img.size)
