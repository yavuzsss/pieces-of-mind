# karakterler.rpy — Pieces of Mind
# Karakter görsellerinin sahnede duruşu (2026-09-03).
#
# Tasarım: bu oyunun görsel dili karanlık ve "ışığın değdiği kadar dünya".
# Karakterler o yüzden aydınlık sprite'lar değil, karanlıktan sıyrılan
# siluetlerdir (bkz. tools/sonmus_uret.py). Sahneye giriş/çıkışları da
# aynı dili konuşur: yavaş çözülme, sert kesme yok.
#
# Kullanım:
#   show sonmus at sonmus_yeri
#   with karakter_belir
#   ...
#   hide sonmus with karakter_soner


define karakter_belir = Dissolve(1.4)
define karakter_soner = Dissolve(1.8)


# Sönmüş: sağda, biraz uzakta. Işık çemberinin kıyısında duruyor —
# yaklaşmıyor, uzaklaşmıyor. Nefes yok; çok yavaş bir ağırlık kayması var.
transform sonmus_yeri:
    xalign 0.72
    yalign 1.0
    zoom 0.92
    subpixel True
    block:
        linear 3.4 yoffset -2
        linear 3.8 yoffset 1
        repeat


# Koro: ekranın üstünden inen alev. Sabit durmaz — iplikler yandığı için
# hafifçe soluk alıp verir ve çok yavaş salınır.
transform koro_yeri:
    xalign 0.5
    yalign 0.62
    zoom 1.0
    alpha 0.94
    subpixel True
    block:
        parallel:
            linear 1.7 alpha 1.0
            linear 2.1 alpha 0.90
            repeat
        parallel:
            linear 2.9 zoom 1.03 xoffset 3
            linear 3.3 zoom 0.98 xoffset -3
            repeat


# Koro büyürken (arama / ultimatom anları): alev kabarır.
transform koro_kabarir:
    zoom 1.0
    linear 1.2 zoom 1.18 alpha 1.0
