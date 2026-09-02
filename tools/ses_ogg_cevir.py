# ses_ogg_cevir.py — Pieces of Mind
#
# Uzun müzik parçalarını WAV -> OGG Vorbis'e çevirir. Kısa efektler WAV
# kalır: metin tıkı her replikte çalıyor, çözme gecikmesi istemiyoruz ve
# hepsi toplam ~330 KB.
#
# Neden: beş müzik parçası ham WAV olarak 7,2 MB tutuyordu ve pakete
# olduğu gibi giriyordu. Vorbis'te ~1 MB'a iniyor, kulakla fark edilmiyor.
#
# Bağımlılık: soundfile (libsndfile). Sistemde yoksa yalıtılmış bir venv:
#     python3 -m venv /tmp/oggvenv && /tmp/oggvenv/bin/pip install soundfile
#     /tmp/oggvenv/bin/python tools/ses_ogg_cevir.py
#
# NOT: tools/muzik_finaller_uret.py hâlâ WAV üretir (sentez placeholder).
# Yeni parça üretince bu betiği de çalıştır. Gerçek müzik geldiğinde
# doğrudan .ogg olarak game/audio/ içine koyulabilir — audio.rpy zaten
# .ogg bekliyor.

import os
import sys

try:
    import soundfile as sf
except ImportError:
    sys.exit("soundfile kurulu değil — dosya başındaki venv adımına bak.")

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SES = os.path.join(KOK, "game", "audio")

# Yalnızca müzik çevrilir; kısa efektler (metin_tik, ui_*, zar, glitch,
# olum_vurusu) WAV olarak kalır.
CEVRILECEK = [
    "muzik_karanlik",
    "muzik_teslim",
    "muzik_armagan",
    "muzik_sonus",
    "muzik_gasp",
]

# 0.0 = en iyi kalite/en büyük, 1.0 = en küçük. 0.4 ≈ Vorbis q5.
KALITE = 0.4

toplam_once = toplam_sonra = 0

for ad in CEVRILECEK:
    kaynak = os.path.join(SES, ad + ".wav")
    hedef = os.path.join(SES, ad + ".ogg")
    if not os.path.exists(kaynak):
        print("atlandı (yok):", ad + ".wav")
        continue

    veri, sr = sf.read(kaynak)
    sf.write(hedef, veri, sr, format="OGG", subtype="VORBIS",
             compression_level=KALITE)

    once = os.path.getsize(kaynak)
    sonra = os.path.getsize(hedef)
    toplam_once += once
    toplam_sonra += sonra
    os.remove(kaynak)
    print("%-20s %6.0f KB -> %5.0f KB" % (ad, once / 1024, sonra / 1024))

if toplam_once:
    print("-" * 40)
    print("toplam %.1f MB -> %.1f MB" % (toplam_once / 1048576,
                                         toplam_sonra / 1048576))
