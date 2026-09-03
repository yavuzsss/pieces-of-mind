# muzik_karanlik_uret.py — Pieces of Mind: ana ortam sesi
#
# game/audio/muzik_karanlik.ogg — oyunun %90'ında duyulan parça.
#
# Tasarım: bu bir "müzik" değil, bir MEKÂN. Zindanın kendi sesi.
#   1. Alçak temel (55 Hz) + hafif detune ikizi -> yavaş vuruşma (beating).
#      İki ses saniyede ~0.15 kez örtüşüp ayrılır: nefes gibi, ritim değil.
#   2. Üstüne beşli ve oktav — ama çok kısık: akor duyulmasın, "büyüklük"
#      duyulsun.
#   3. Kahverengi gürültü yatağı, alçak geçiren: taşın hava sesi.
#   4. Seyrek metalik tınlamalar (~18-30 sn arayla): uzakta bir şey.
#      Zindan boş değil — ama ne olduğu söylenmiyor.
#   5. Konvolüsyonlu yankı: sönen gürültüyle bulanıklaştırma. Oda büyük.
#   6. Çok yavaş genlik salınımı — parça hiç aynı yerde durmaz.
#
# Döngü: son 3 sn başa çapraz geçişle bindirilir; dikişsiz döner.

import numpy as np
import os
import wave

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SR = 22050
SURE = 48.0
N = int(SR * SURE)
t = np.arange(N) / SR
rng = np.random.default_rng(7)

def alcak_gecir(x, kesim, mertebe=3):
    """Basit tek kutuplu alçak geçiren, birkaç kez uygulanır."""
    a = np.exp(-2.0 * np.pi * kesim / SR)
    y = x
    for _ in range(mertebe):
        z = np.empty_like(y)
        onceki = 0.0
        for i in range(len(y)):
            onceki = (1 - a) * y[i] + a * onceki
            z[i] = onceki
        y = z
    return y

# ── 1) Temel + detune ikizi ─────────────────────────────────────────────
# NOT: ilk sürüm enerjinin %61'ini 80 Hz altına koyuyordu — dizüstü
# hoparlörde neredeyse hiç duyulmuyordu. Temel yukarı alındı ve gövde
# üst harmoniklere kaydırıldı: kulaklıkta hâlâ derin, hoparlörde duyulur.
F0 = 65.0
ses = np.zeros(N)
ses += 0.26 * np.sin(2 * np.pi * F0 * t)
ses += 0.24 * np.sin(2 * np.pi * (F0 + 0.17) * t + 1.1)     # vuruşma
ses += 0.30 * np.sin(2 * np.pi * F0 * 2 * t + 0.4)          # oktav — gövde burada
ses += 0.26 * np.sin(2 * np.pi * (F0 * 2 + 0.23) * t + 2.6)
ses += 0.17 * np.sin(2 * np.pi * F0 * 3 * t + 2.2)          # beşli üstü
ses += 0.10 * np.sin(2 * np.pi * F0 * 4 * t + 0.9)          # iki oktav
ses += 0.05 * np.sin(2 * np.pi * F0 * 6 * t + 4.1)          # ince parlaklık

# ── 2) Gürültü yatağı (kahverengi -> alçak geçiren) ────────────────────
beyaz = rng.normal(0, 1, N)
kahve = np.cumsum(beyaz)
kahve = kahve / (np.max(np.abs(kahve)) + 1e-9)
ses += 0.26 * alcak_gecir(kahve, 620.0, 2)   # yatağı biraz açtık

# ── 3) Seyrek metalik tınlamalar ────────────────────────────────────────
tinla = np.zeros(N)
konum = 6.0
while konum < SURE - 6:
    i0 = int(konum * SR)
    uz = int(SR * rng.uniform(2.5, 4.5))
    yerel = np.arange(uz) / SR
    zarf = np.exp(-yerel * rng.uniform(1.1, 2.0))
    temel = rng.uniform(150, 320)
    v = np.zeros(uz)
    for kat, agir in ((1.0, 1.0), (2.76, 0.5), (5.4, 0.22), (8.9, 0.1)):
        v += agir * np.sin(2 * np.pi * temel * kat * yerel + rng.uniform(0, 6))
    v *= zarf * rng.uniform(0.05, 0.10)
    if i0 + uz <= N:
        tinla[i0:i0 + uz] += v
    konum += rng.uniform(18.0, 30.0)
ses += tinla

# ── 4) Yankı: sönen gürültüyle konvolüsyon (oda büyük) ─────────────────
kuyruk_uz = int(SR * 1.6)
kuyruk = rng.normal(0, 1, kuyruk_uz) * np.exp(-np.arange(kuyruk_uz) / (SR * 0.42))
kuyruk = alcak_gecir(kuyruk, 1800.0, 1)
kuyruk /= (np.sum(np.abs(kuyruk)) + 1e-9)
yanki = np.convolve(ses, kuyruk, mode="full")[:N]
ses = 0.78 * ses + 0.32 * yanki

# ── 5) Çok yavaş genlik salınımı ────────────────────────────────────────
ses *= (0.80
        + 0.13 * np.sin(2 * np.pi * t / 19.0)
        + 0.07 * np.sin(2 * np.pi * t / 7.3 + 1.7))

# ── 6) Dikişsiz döngü: son 3 sn'yi başa çapraz geçir ───────────────────
CG = int(SR * 3.0)
ramp = np.linspace(0, 1, CG)
ses[:CG] = ses[:CG] * ramp + ses[-CG:] * (1 - ramp)
ses = ses[:-CG]

# ── Normalize + yaz ─────────────────────────────────────────────────────
ses = ses / (np.max(np.abs(ses)) + 1e-9) * 0.52
pcm = (ses * 32767).astype(np.int16)

gecici = "/tmp/muzik_karanlik.wav"
with wave.open(gecici, "w") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wav yazildi:", gecici, "%.1f sn" % (len(pcm) / float(SR)))
