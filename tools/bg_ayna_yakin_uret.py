# bg_ayna_yakin.png üreteci — Pieces of Mind şövalye portresi (ayna yakın planı)
# Pipeline: 480x270 tuval -> 4x NEAREST -> 1920x1080 (mevcut bg'lerle aynı)
# Palet: zindan koyuları + krem ten rampası + kırmızı (lamba/kan)

from PIL import Image, ImageDraw
import random

random.seed(11)

W, H = 480, 270

# ── Renkler ──────────────────────────────────────────────────────────────
DUVAR1 = (19, 16, 16)
DUVAR2 = (24, 19, 19)
DUVAR3 = (28, 22, 22)
DERZ   = (13, 11, 11)
CERCEVE  = (42, 30, 26)
CERCEVE2 = (58, 42, 34)
CERCEVE_H = (96, 82, 62)
AYNA_ICI = (11, 10, 10)

PAL = {
    "K": (13, 11, 11),    # en koyu kontur
    "k": (32, 27, 22),    # saç
    "b": (54, 47, 38),    # sakal
    "d": (110, 100, 84),  # ten gölgesi
    "s": (150, 138, 114), # ten orta
    "l": (184, 172, 147), # ten açık
    "h": (216, 201, 168), # vurgu
    "H": (245, 233, 208), # parlak (göz parıltısı / burun sırtı)
    "E": (20, 17, 15),    # göz karanlığı
    "r": (122, 26, 22),   # kurumuş kan
    "R": (204, 34, 34),   # kırmızı kenar ışığı (lamba)
    "g": (92, 84, 70),    # sakaldaki kır teller (soluk)
}

# ── Yüz haritası (44 sütun; '.' = boş) ───────────────────────────────────
FACE = """
..............kkkkkkkkkkkkkk..............
...........kkkkkkkkkkkkkkkkkkk...........
.........kkkkkkkkkkkkkkkkkkkkkkk.........
........kkkkkkkkkkkkkkkkkkkkkkkkk........
.......kkkkkkkkkkkkkkkkkkkkkkkkkk........
.......kkkkkkkkkkkkkkkkkkkkkkkkkkk.......
......kkkkkkkkkkkkkkkkkkkkkkkkkkkk.......
......kkkKddsssssssssssssssdKkkkkk.......
......kkKdsslllllllllllllssssdKkkk.......
......kkKdslllllllllllllllllsdKkkk.......
......kkKdslllllllllllllllllsdKkkk.......
......rkKdslllllllllllllllllsdKkkk.......
......rrKdsllllllllllllllllssdKkkk.......
......krKdsslllllllllllllssssdKkkk.......
......kkKrsskkkksssssssskkkkssdKkk.......
......kkKrssKKKKssssssssKKKKssdKkk.......
......kkKdssKEEKKssllssKKEEKssdKkk.......
......kkKdssKEhEKssllssKEhEKssdKkk.......
......kkKdssdKKKdssllssdKKKdssdKkk.......
......kkKddssdddssslssssdddsssdKkk.......
......kkKdsssssssllllsssssssddKkkk.......
......kkKdsssssssllllsssssssddKkkk.......
......kkKddsssssslhllssssssddKkkkk.......
......kkKddsssssdhhlldssssdddKkkkk.......
......kkKKddssssdhhlldsssdddKKkkkk.......
.......kKKddsssddhhllddsssddKKkkk........
.......kkKKdssssdKKKKddsssdKKkkkk........
.......kkKKdssssssssssssssdKKkkk.........
.......kkKKbbssddssssssdssbbKKkk.........
........kKKbbbbdssKKKssdbbbbKKkk.........
........kKKbbbbbbKKKKKbbbbbbKKk..........
........kKKbbbbbbbbbbbbbbbbKKkk..........
.........kKbbbbbgbbbbbgbbbbKkk...........
.........kKKbbbbbbbbbbbbbbKKkk...........
.........kKKbbgbbbbbbbgbbbKKk............
..........kKKbbbbbgbbbbbbKKk.............
..........kKKKbbbbbbbbbKKKk..............
...........kKKKbbbbbbbKKKk...............
............kKKKbbbbbKKKk................
.............kKKKbbbKKK..................
..............KKbddKK....................
..............KbdddK.....................
..............KbdddK.....................
.............KKbdddbKK...................
......KKKKKKKKKbddddbKKKKKKKKK...........
....KKKKKKKKKKKbddddbKKKKKKKKKKKK........
...KKKKKKKKKKKKbbddbbKKKKKKKKKKKKKK......
..KKKKKKKKKKKKKKbbbbKKKKKKKKKKKKKKKK.....
""".strip("\n").split("\n")

FACE = [row.ljust(44, ".")[:44] for row in FACE]
FH = len(FACE)

img = Image.new("RGB", (W, H), DUVAR1)
d = ImageDraw.Draw(img)

# ── Taş duvar (kaba bloklar) ─────────────────────────────────────────────
by = 0
while by < H:
    bh = random.randint(22, 34)
    ofs = random.randint(0, 30)
    bx = -ofs
    while bx < W:
        bw = random.randint(40, 64)
        c = random.choice([DUVAR1, DUVAR2, DUVAR3, DUVAR2])
        d.rectangle([bx, by, bx + bw - 1, by + bh - 1], fill=c)
        d.line([bx, by, bx, by + bh - 1], fill=DERZ)
        bx += bw
    d.line([0, by, W, by], fill=DERZ)
    by += bh

# hafif vinyet (kenarlar kararır)
px = img.load()
cx, cy = W // 2, H // 2
for y in range(H):
    for x in range(W):
        dx, dy = (x - cx) / cx, (y - cy) / cy
        f = dx * dx + dy * dy
        if f > 0.55:
            r_, g_, b_ = px[x, y]
            k = max(0.35, 1.0 - (f - 0.55) * 0.9)
            px[x, y] = (int(r_ * k), int(g_ * k), int(b_ * k))

# ── Ayna ─────────────────────────────────────────────────────────────────
MX0, MY0, MX1, MY1 = 158, 16, 322, 254   # dış çerçeve
d.rectangle([MX0, MY0, MX1, MY1], fill=CERCEVE)
d.rectangle([MX0 + 2, MY0 + 2, MX1 - 2, MY1 - 2], fill=CERCEVE2)
# yıpranmış çerçeve vurguları
for _ in range(46):
    x = random.randint(MX0, MX1)
    y = random.choice([random.randint(MY0, MY0 + 5), random.randint(MY1 - 5, MY1)])
    if random.random() < 0.5:
        x = random.choice([random.randint(MX0, MX0 + 5), random.randint(MX1 - 5, MX1)])
        y = random.randint(MY0, MY1)
    d.point([x, y], fill=CERCEVE_H if random.random() < 0.4 else CERCEVE)
IX0, IY0, IX1, IY1 = MX0 + 7, MY0 + 7, MX1 - 7, MY1 - 7  # cam içi
d.rectangle([IX0, IY0, IX1, IY1], fill=AYNA_ICI)

# cam içinde lamba yansıması: sol-alttan kırmızı loş ışıma
for y in range(IY0, IY1 + 1):
    for x in range(IX0, IX1 + 1):
        dx = (x - IX0) / (IX1 - IX0)
        dy = (y - IY1) / (IY0 - IY1)   # 0 altta, 1 üstte
        g = max(0.0, 1.0 - (dx * 1.6 + dy * 1.25))
        if g > 0:
            r_, g_, b_ = px[x, y]
            px[x, y] = (min(255, int(r_ + 46 * g * g)), g_ + int(3 * g), b_ + int(3 * g))

# ── Yüz (x3 ölçek, ayna içine) ───────────────────────────────────────────
S = 3
FW = 44 * S
face_x = (IX0 + IX1) // 2 - FW // 2
face_y = IY1 - FH * S + 2   # alt kenara oturur (omuzlar camın dibinde)

for j, row in enumerate(FACE):
    for i, ch in enumerate(row):
        if ch in (".", " "):
            continue
        c = PAL.get(ch)
        if c is None:
            continue
        x0 = face_x + i * S
        y0 = face_y + j * S
        d.rectangle([x0, y0, x0 + S - 1, y0 + S - 1], fill=c)

# kırmızı kenar ışığı: yüzün sol (lamba yönü) silüeti boyunca
for j, row in enumerate(FACE):
    if j < 12:                     # saçın tepesine ışık vurmaz
        continue
    for i, ch in enumerate(row):
        if ch not in (".", " "):
            if 24 <= j <= 40 or j % 2 == 0:   # çene hattında kesiksiz rim
                x0 = face_x + i * S
                y0 = face_y + j * S
                d.rectangle([x0, y0, x0, y0 + S - 1], fill=PAL["R"])
            break

# cam lekesi / eski sırlar: birkaç soluk dikey çizik
for _ in range(5):
    x = random.randint(IX0 + 6, IX1 - 6)
    y0 = random.randint(IY0 + 4, IY0 + 60)
    ln = random.randint(18, 60)
    for y in range(y0, min(IY1, y0 + ln)):
        if random.random() < 0.6:
            r_, g_, b_ = px[x, y]
            px[x, y] = (min(255, r_ + 10), min(255, g_ + 9), min(255, b_ + 8))

# ── Kaydet ───────────────────────────────────────────────────────────────
img = img.resize((1920, 1080), Image.NEAREST)
out = "/Users/yavuzseremetli/Documents/renpy/pom2/game/images/bg_ayna_yakin.png"
img.save(out)
print("yazildi:", out)
