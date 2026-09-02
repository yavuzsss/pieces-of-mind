# muzik_finaller_uret.py — Pieces of Mind: dört finale özel PLACEHOLDER müzik
# Format mevcut hatla aynı: mono, 22050 Hz, 16-bit WAV, loop'lanabilir
# (son 1.5 sn başa crossfade edilir). Seviye muzik_karanlik RMS'ine eşitlenir.
#
#   muzik_teslim  — soğuk, inen dörtlü motif; her tekrarda sönükleşir
#   muzik_armagan — tek sıcak parça: majör pedal + yumuşak nefes, hafif detune
#   muzik_sonus   — boşluk: çok alçak pedal + 8-13 sn arayla yalnız bir nota
#   muzik_gasp    — yanlışlık: vuruşlu detune çift drone + küçük ikili + triton
#
# DİKKAT: bu betik WAV yazar, oyun ise .ogg çalar (audio.rpy). Yeni parça
# üretince ardından tools/ses_ogg_cevir.py çalıştır — WAV'ları Vorbis'e
# çevirip siler.

import wave
import numpy as np

SR = 22050
OUT = "/Users/yavuzseremetli/Documents/renpy/pom2/game/audio/"


def t_axis(saniye):
    return np.arange(int(SR * saniye)) / SR


def sine(f, t, ph=0.0):
    return np.sin(2 * np.pi * f * t + ph)


def swell(t, bas, sure):
    """sin^2 zarfı: bas anında başlar, sure boyunca kabarıp söner."""
    x = (t - bas) / sure
    e = np.zeros_like(t)
    m = (x >= 0) & (x <= 1)
    e[m] = np.sin(np.pi * x[m]) ** 2
    return e


def lownoise(t, seed, kuvvet=1.0):
    """Alçak geçirenden geçmiş rüzgâr benzeri gürültü."""
    rng = np.random.default_rng(seed)
    n = rng.standard_normal(len(t))
    # basit tek kutuplu alçak geçiren
    out = np.empty_like(n)
    acc = 0.0
    a = 0.015
    for i, v in enumerate(n):
        acc += a * (v - acc)
        out[i] = acc
    return out * kuvvet


def loopla(sig, xf_saniye=1.5):
    """Sonu başa crossfade ederek dikişsiz loop yap."""
    xf = int(SR * xf_saniye)
    fade = np.linspace(0, 1, xf)
    sig[:xf] = sig[:xf] * fade + sig[-xf:] * (1 - fade)
    return sig[:-xf]


def kaydet(ad, sig, hedef_rms):
    rms = np.sqrt(np.mean(sig ** 2)) or 1.0
    sig = sig * (hedef_rms / rms)
    tepe = np.max(np.abs(sig))
    if tepe > 0.9:
        sig = sig * (0.9 / tepe)
    data = (sig * 32767).astype(np.int16)
    with wave.open(OUT + ad, "w") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())
    print("yazildi:", ad, "sure:", round(len(sig) / SR, 1), "s")


# Hedef seviye: mevcut ana temanın RMS'i
with wave.open(OUT + "muzik_karanlik.wav") as w:
    ref = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16) / 32767.0
HEDEF = float(np.sqrt(np.mean(ref ** 2)))


# ── TESLİM — soğuk iniş ─────────────────────────────────────────────────
t = t_axis(36)
drone = (sine(55, t) * 0.35 + sine(110, t) * 0.18) * (0.75 + 0.25 * sine(0.05, t))
notalar = [220.0, 196.0, 174.6, 164.8]           # A3 G3 F3 E3
sig = drone
for tekrar, kuvvet in ((0, 1.0), (1, 0.55)):     # ikinci tur daha sönük
    for i, f in enumerate(notalar):
        bas = tekrar * 18 + i * 4.5
        e = swell(t, bas, 5.5) * kuvvet
        sig = sig + sine(f, t) * e * 0.30
        if tekrar == 0:
            sig = sig + sine(f * 1.5, t) * e * 0.07   # soğuk beşli
sig = sig + lownoise(t, 3, 0.05)
kaydet("muzik_teslim.wav", loopla(sig), HEDEF)

# ── ARMAĞAN — tek sıcak parça ───────────────────────────────────────────
t = t_axis(36)
nefes = 0.7 + 0.3 * sine(0.08, t)
pad = np.zeros_like(t)
for f in (130.8, 164.8, 196.0):                  # C3 E3 G3
    pad += (sine(f, t) + sine(f * 1.0015, t) + sine(f * 0.9985, t)) / 3 * 0.22
    pad += sine(f * 2, t) * 0.04                 # hafif parlaklık
pad *= nefes
melodi_notalar = [(261.6, 2), (329.6, 8), (392.0, 14), (440.0, 20), (392.0, 25), (329.6, 30)]
mel = np.zeros_like(t)
for f, bas in melodi_notalar:
    e = swell(t, bas, 6.0)
    mel += (sine(f, t) + sine(f * 1.002, t)) / 2 * e * 0.20
sig = pad + mel + lownoise(t, 7, 0.03)
kaydet("muzik_armagan.wav", loopla(sig), HEDEF)

# ── SÖNÜŞ — boşluk ──────────────────────────────────────────────────────
t = t_axis(40)
pedal = sine(46.25, t) * 0.28 * (0.6 + 0.4 * sine(0.03, t))     # F#1
ping = np.zeros_like(t)
for bas in (6.0, 19.0, 32.0):                    # düzensiz, yalnız
    x = t - bas
    e = np.where(x >= 0, np.exp(-x / 2.2), 0.0) * np.where(x >= 0, np.minimum(x * 30, 1), 0.0)
    ping += sine(329.6, t) * e * 0.16            # E4
    ping += sine(329.6 * 2, t) * e * 0.03
ruzgar = lownoise(t, 12, 0.09) * (0.5 + 0.5 * sine(0.045, t, 1.3))
sig = pedal + ping + ruzgar
kaydet("muzik_sonus.wav", loopla(sig), HEDEF * 0.7)   # bilinçli daha sessiz

# ── GASP — yanlışlık ────────────────────────────────────────────────────
t = t_axis(32)
d1 = sine(65.4, t) * 0.30                        # C2
d2 = sine(65.4 * 1.018, t) * 0.30                # vuruş ~1.2 Hz
kayma = 65.4 * (1 - 0.004 * t / 32)              # yavaşça pesleşen üçüncü katman
d3 = np.sin(2 * np.pi * np.cumsum(kayma) / SR) * 0.12
dis = sine(138.6, t) * 0.10 * (0.6 + 0.4 * sine(0.07, t))       # C#3 küçük dokuzlu
tri = sine(92.5, t) * swell(t, 10, 8) * 0.14 + sine(92.5, t) * swell(t, 24, 6) * 0.14  # F#2
ters = np.zeros_like(t)                           # ters zarf: kabarır ve KESİLİR
for bas in (8.0, 22.0):
    x = (t - bas) / 4.0
    m = (x >= 0) & (x <= 1)
    ters[m] += (x[m] ** 2) * 0.18
ters_sig = sine(220 * 0.985, t) * ters
sig = d1 + d2 + d3 + dis + tri + ters_sig + lownoise(t, 21, 0.05)
kaydet("muzik_gasp.wav", loopla(sig), HEDEF)
