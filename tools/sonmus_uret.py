# sonmus_uret.py — Pieces of Mind: Sönmüş Şövalye
#
# game/images/sonmus.png : 120x200 -> 4x NEAREST -> 480x800
#
# SANAT YÖNÜ — neden siluet:
# Bu oyunun görsel dili karanlık ve "ışığın değdiği kadar dünya". Arka
# planlar da böyle çalışıyor: neredeyse siyah, tek bir kırmızı kaynak.
# Karakteri tam aydınlık bir sprite olarak çizmek bu dile aykırı düşerdi —
# ve zaten Sönmüş'ün kendi alevi ölmek üzere, onu aydınlatan tek şey
# OYUNCUNUN lambası. O yüzden: gövde neredeyse siyah, yalnız SOL kenar
# (oyuncunun ışığı) yakalanıyor. Yüzün sadece elmacık kemiği, çene hattı
# ve iki çukur okunuyor. Gerisi karanlığa ait.
#
# Teknik: siluet maskesi -> kenar ışığı (soldan, mesafeye göre sönen) ->
# iç doku (Bayer, çok zayıf) -> lambanın tek parlak noktası.

import math
import os
from PIL import Image, ImageDraw

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
W, H = 120, 200
BOS = (0, 0, 0, 0)

GOVDE   = (14, 13, 12)        # siluet: neredeyse siyah
IC1     = (22, 20, 18)        # iç dokunun bir tık üstü
IC2     = (30, 27, 24)
KENAR1  = (58, 52, 45)        # kenar ışığı — uzak
KENAR2  = (96, 86, 74)        # kenar ışığı — yakın
KENAR3  = (138, 126, 110)     # kenar ışığı — en parlak (omuz/elmacık)
TEN_K   = (46, 42, 38)        # yüzde ışık almayan et
TEN     = (112, 104, 94)
TEN_H   = (152, 143, 130)
CUKUR   = (7, 7, 7)           # göz çukurları: ışık yok
LAMBA_M = (52, 46, 40)
ALEV_D  = (120, 50, 30)
ALEV    = (214, 132, 66)
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

img = Image.new("RGBA", (W, H), BOS)
d = ImageDraw.Draw(img)
MX = 58

# ── 1) SİLUET ────────────────────────────────────────────────────────────
# Çökük duruş: baş öne ve yana eğik, sol omuz düşük, sırt kambur.
d.ellipse([MX - 15, 16, MX + 15, 54], fill=GOVDE)                 # baş
d.polygon([(MX - 8, 50), (MX + 8, 50), (MX + 10, 62), (MX - 10, 62)], fill=GOVDE)  # boyun
d.polygon([                                                        # gövde: omuz geniş,
    (MX - 10, 58), (MX - 27, 67), (MX - 33, 86), (MX - 30, 112),   # belde daralır,
    (MX - 26, 126), (MX - 30, 158), (MX - 30, 196),                # etekte açılır
    (MX + 28, 196), (MX + 27, 156), (MX + 23, 126),
    (MX + 27, 110), (MX + 30, 84), (MX + 22, 64), (MX + 10, 58),
], fill=GOVDE)
d.polygon([(MX - 30, 74), (MX - 40, 104), (MX - 37, 140),          # sol kol (sarkık)
           (MX - 28, 138), (MX - 24, 96)], fill=GOVDE)
# sağ kol: omuzdan dirseğe, sonra öne — lambayı tutan el görünür
d.polygon([(MX + 24, 70), (MX + 34, 88), (MX + 36, 106),
           (MX + 28, 108), (MX + 22, 86)], fill=GOVDE)
d.polygon([(MX + 28, 104), (MX + 38, 108), (MX + 39, 116),
           (MX + 29, 114)], fill=GOVDE)                            # önkol
d.rectangle([MX + 33, 110, MX + 39, 117], fill=GOVDE)              # el
# etek: aşağı genişler; ortada bacakların ayırdığı bir yarık
d.polygon([(MX - 30, 152), (MX + 28, 152), (MX + 33, 200), (MX - 35, 200)], fill=GOVDE)
d.polygon([(MX - 3, 176), (MX + 3, 176), (MX + 4, 200), (MX - 4, 200)], fill=(0,0,0,0))

px = img.load()
maske = [[px[x, y][3] > 0 for y in range(H)] for x in range(W)]

# ── 2) İÇ DOKU: çok zayıf, sadece üst gövdede ──────────────────────────
for y in range(16, 150):
    for x in range(W):
        if maske[x][y] and BAYER[y % 4][x % 4] < 4:
            px[x, y] = IC1 + (255,)
        elif maske[x][y] and BAYER[y % 4][x % 4] == 15:
            px[x, y] = IC2 + (255,)

# ── 3) KENAR IŞIĞI: soldan. Işık kaynağına yakın kenarlar daha parlak. ──
# Her satırda soldaki ilk dolu pikselden itibaren birkaç piksel aydınlanır.
for y in range(H):
    ilk = None
    for x in range(W):
        if maske[x][y]:
            ilk = x
            break
    if ilk is None:
        continue
    # dikey konum: göğüs hizası en parlak (lamba orada tutuluyor)
    yakinlik = max(0.0, 1.0 - abs(y - 96) / 110.0)
    kalinlik = 1 + int(round(2 * yakinlik))
    for k in range(kalinlik + 1):
        x = ilk + k
        if not (0 <= x < W and maske[x][y]):
            break
        if k == 0:
            renk = KENAR3 if yakinlik > 0.65 else KENAR2
        elif k == 1:
            renk = KENAR2 if yakinlik > 0.5 else KENAR1
        else:
            renk = KENAR1
        # Bayer ile kırılsın: düz çizgi değil, yakalanmış ışık olsun
        if BAYER[y % 4][x % 4] < 9 + int(7 * yakinlik):
            px[x, y] = renk + (255,)

# ── 4) YÜZ: yalnız ışığın yakaladığı hatlar ────────────────────────────
# Elmacık kemiği ve çene, soldan; iki çukur; burun sırtının ucu.
def blok(x0, y0, x1, y1, renk):
    for yy in range(y0, y1):
        for xx in range(x0, x1):
            if 0 <= xx < W and 0 <= yy < H and maske[xx][yy]:
                px[xx, yy] = renk + (255,)

def piks(noktalar, renk):
    for (xx, yy) in noktalar:
        if 0 <= xx < W and 0 <= yy < H and maske[xx][yy]:
            px[xx, yy] = renk + (255,)

# Işığın yakaladığı hatlar — düz blok değil, kemiği izleyen eğriler.
# Kaş üstü ve elmacık: soldan gelen ışığın tuttuğu tek şerit.
piks([(MX-12,31),(MX-11,30),(MX-10,30),(MX-9,31),(MX-8,32)], TEN_H)
piks([(MX-13,33),(MX-12,34),(MX-11,35),(MX-11,36),(MX-10,37)], TEN)
piks([(MX-12,38),(MX-11,39),(MX-10,40),(MX-9,41),(MX-8,42)], TEN)
piks([(MX-10,42),(MX-9,43),(MX-8,44),(MX-7,45)], TEN_K)

# Göz çukurları: dairesel, kemiğin içine oturmuş
piks([(MX-10,33),(MX-9,33),(MX-8,33),(MX-9,34),(MX-8,34),(MX-7,34),
      (MX-8,35),(MX-7,35)], CUKUR)
piks([(MX+2,33),(MX+3,33),(MX+4,33),(MX+2,34),(MX+3,34),(MX+4,34),
      (MX+3,35),(MX+4,35)], CUKUR)
# çukur altı kemik kenarı
piks([(MX-10,36),(MX-9,36),(MX-8,36)], TEN_K)
piks([(MX+2,36),(MX+3,36)], TEN_K)

# Burun sırtı: iki piksellik bir ışık, ucunda gölge
piks([(MX-4,36),(MX-4,37),(MX-3,38),(MX-3,39)], TEN)
piks([(MX-2,40),(MX-1,40)], TEN_K)

# Çene hattı: aşağı-sağa inen, ucunda sönen
piks([(MX-7,46),(MX-6,47),(MX-4,48),(MX-2,48),(MX,47)], TEN_K)
piks([(MX-6,46),(MX-5,46)], TEN)

# çatlaklar: kurumuş toprak — yalnız ışık alan yüzeyde okunur
for (x0, y0, x1, y1) in [(MX - 12, 39, MX - 9, 45), (MX - 8, 30, MX - 7, 33),
                         (MX - 5, 41, MX - 3, 46), (MX - 10, 27, MX - 8, 30)]:
    for i in range(max(abs(x1 - x0), abs(y1 - y0)) + 1):
        xx = x0 + (i if x1 > x0 else 0)
        yy = y0 + i
        if 0 <= xx < W and 0 <= yy < H and maske[xx][yy]:
            px[xx, yy] = (26, 24, 22, 255)

# ── 4b) EL: lamba havada durmasın — önkolun üst kenarı ışık yakalasın ──
piks([(MX+29,105),(MX+31,105),(MX+33,106),(MX+35,107),(MX+37,108)], KENAR2)
piks([(MX+34,110),(MX+35,110),(MX+36,111),(MX+37,111),(MX+36,112)], KENAR3)
piks([(MX+34,113),(MX+35,114),(MX+36,115)], KENAR1)

# ── 5) LAMBA: tek parlak nokta — ölmek üzere ───────────────────────────
LX, LY = MX + 36, 118
d.rectangle([LX - 5, LY - 2, LX + 5, LY + 1], fill=LAMBA_M)
d.rectangle([LX - 4, LY + 1, LX + 4, LY + 17], fill=(20, 16, 15))
d.rectangle([LX - 6, LY + 17, LX + 6, LY + 20], fill=LAMBA_M)
d.arc([LX - 4, LY - 8, LX + 4, LY - 1], 180, 360, fill=LAMBA_M)
px[LX, LY + 12] = ALEV + (255,)
px[LX - 1, LY + 13] = ALEV_D + (255,)
px[LX, LY + 13] = ALEV_D + (255,)
# camda çok zayıf bir sıcaklık
for yy in range(LY + 9, LY + 17):
    for xx in range(LX - 3, LX + 4):
        if px[xx, yy][:3] == (20, 16, 15) and BAYER[yy % 4][xx % 4] < 4:
            px[xx, yy] = (44, 26, 20, 255)

# ── 6) Alt kenar: karanlığa karışsın, düz kesilmesin ───────────────────
for x in range(W):
    for y in range(184, H):
        if maske[x][y]:
            pay = (y - 184) / float(H - 184)
            if BAYER[y % 4][x % 4] < pay * 16:
                px[x, y] = BOS

img = img.resize((W * 4, H * 4), Image.NEAREST)
hedef = os.path.join(KOK, "game", "images", "sonmus.png")
img.save(hedef)
print("yazildi:", os.path.relpath(hedef, KOK), img.size)
