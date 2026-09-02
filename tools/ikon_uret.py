# ikon_uret.py — Pieces of Mind uygulama ikonu
#
# Üretilenler (hepsi TEK kaynaktan, 32x32 piksel çizimden):
#   game/gui/window_icon.png : 256x256  — pencere/dock ikonu (config.window_icon)
#   icon.ico                 : Windows yürütülebilir ikonu (Ren'Py build alır)
#   icon.icns                : macOS .app ikonu (Ren'Py build alır)
#
# Tasarım: karanlıkta yerde duran kırmızı lamba — oyunun ilk görüntüsü ve
# tek güvenlik kuralı ("ışık küçülünce dünya da küçülüyor"). 16x16'ya
# indiğinde bile okunan tek şey kalır: karanlıkta kırmızı bir leke.
# Palet ve çizim dili bg_ana_menu_uret.py ile aynı.

import math
import os
import shutil
import subprocess
from PIL import Image, ImageDraw

KOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
KOK = os.path.normpath(KOK)

S = 32                       # kaynak piksel tuvali
SIYAH   = (10, 10, 10)
METAL   = (46, 40, 34)
METAL_H = (86, 76, 64)
CAM_K   = (122, 26, 22)
CAM_A   = (176, 34, 30)
ALEV_D  = (214, 92, 40)
ALEV    = (245, 233, 208)
ISIK    = (204, 34, 34)      # ışık çemberinin rengi

img = Image.new("RGB", (S, S), SIYAH)
px = img.load()

# ── Işık çemberi: lambadan uzaklığa göre karanlığı ısıtır ────────────────
LX, LY = 16, 20              # alevin merkezi
YARICAP = 17.0
for y in range(S):
    for x in range(S):
        d = math.hypot(x - LX, y - LY)
        k = max(0.0, 1.0 - d / YARICAP) ** 2.2
        if k > 0:
            px[x, y] = (int(SIYAH[0] + (ISIK[0] - SIYAH[0]) * k * 0.75),
                        int(SIYAH[1] + (ISIK[1] - SIYAH[1]) * k * 0.75),
                        int(SIYAH[2] + (ISIK[2] - SIYAH[2]) * k * 0.75))

d = ImageDraw.Draw(img)

# ── Lamba (32x32'ye ölçeklenmiş hali; bg_ana_menu'deki siluetin aynısı) ──
TABAN = 27
d.rectangle([LX - 6, TABAN - 2, LX + 6, TABAN], fill=METAL)          # taban
d.line([LX - 6, TABAN - 2, LX + 6, TABAN - 2], fill=METAL_H)
d.rectangle([LX - 5, TABAN - 14, LX + 5, TABAN - 3], fill=CAM_K)     # cam gövde
d.rectangle([LX - 5, TABAN - 14, LX - 2, TABAN - 3], fill=CAM_A)     # ışık yüzü
d.rectangle([LX - 1, TABAN - 11, LX + 1, TABAN - 5], fill=ALEV_D)    # alev
d.rectangle([LX - 1, TABAN - 10, LX, TABAN - 7], fill=ALEV)          # çekirdek
d.rectangle([LX - 6, TABAN - 17, LX + 6, TABAN - 15], fill=METAL)    # kapak
d.line([LX - 6, TABAN - 17, LX + 6, TABAN - 17], fill=METAL_H)
d.arc([LX - 4, TABAN - 22, LX + 4, TABAN - 16], 180, 360, fill=METAL_H)  # kulp

# ── Kaydet ───────────────────────────────────────────────────────────────
def buyut(n):
    """NEAREST ile tam katına büyüt — piksel sınırları keskin kalsın."""
    return img.resize((n, n), Image.NEAREST)

gui_yol = os.path.join(KOK, "game", "gui", "window_icon.png")
buyut(256).save(gui_yol)
print("yazildi:", os.path.relpath(gui_yol, KOK))

ico_yol = os.path.join(KOK, "icon.ico")
buyut(256).save(ico_yol, sizes=[(16, 16), (24, 24), (32, 32),
                                (48, 48), (64, 64), (128, 128), (256, 256)])
print("yazildi: icon.ico")

# macOS .icns: iconutil (sistemde her zaman var) ile .iconset'ten üretilir.
iconset = os.path.join(KOK, "icon.iconset")
if os.path.isdir(iconset):
    shutil.rmtree(iconset)
os.makedirs(iconset)
for boy in (16, 32, 128, 256, 512):
    buyut(boy).save(os.path.join(iconset, "icon_%dx%d.png" % (boy, boy)))
    buyut(boy * 2).save(os.path.join(iconset, "icon_%dx%d@2x.png" % (boy, boy)))
subprocess.run(["iconutil", "-c", "icns", iconset,
                "-o", os.path.join(KOK, "icon.icns")], check=True)
shutil.rmtree(iconset)
print("yazildi: icon.icns")
