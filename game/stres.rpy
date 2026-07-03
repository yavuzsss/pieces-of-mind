# stres.rpy — Pieces of Mind
# Gizli stres sistemi (0-15). GÖSTERGE YOK — yalnızca etkileriyle hissedilir:
#   stres >= 5  : seviye 1 — CRT titreme/parazit yoğunlaşır (effects.rpy) +
#                 diyalog kutusunda çok hafif glitch (ui.rpy)
#   stres >= 10 : seviye 2 — textbox glitch'i belirginleşir, metinde
#                 karakterler bozulmaya başlar (çözülebilir taban — satır
#                 daima sökülebilir; tamamen okunmaz metin yalnızca senaryonun
#                 bilinçli anlarında kullanılır)
#   stres = 15  : son seviye — seçim kutuları titrer ve sıraları karışır,
#                 metin bozulması yoğunlaşır
#
# Otomatik kaynaklar: doğal 1 (dice.rpy +1) + şiddetli glitch (effects.rpy +1).
# Diğer her şey senaryo eliyle: $ stres_degistir(+n/-n)
# Yeni koşuda (ölüm sonrası) otomatik sıfırlanır (store değişkeni).

default stres = 0


init -1 python:

    import zlib
    import random as _pyrandom

    def stres_degistir(delta):
        """Stresi değiştirir (0-15 aralığına sıkıştırılır)."""
        store.stres = max(0, min(15, store.stres + delta))

    # VT323'te blok karakterleri yok — bozulma havuzu ASCII.
    _BOZUK_HAVUZ = "#/\\_X"

    def _stres_boz(metin):
        """Deterministik metin bozulması (say + menü metinleri).

        Satırın CRC'siyle tohumlanır: aynı satır aynı streste hep aynı
        şekilde bozulur (rollback/kayıt tutarlılığı). {etiketler} ve
        [değişkenler] atlanır. Bozulan karakter sayısı sınırlıdır —
        satır daima çözülebilir kalır.
        """
        seviye = getattr(store, "stres", 0)
        if seviye < 10 or not metin:
            return metin

        r = _pyrandom.Random(zlib.crc32(metin.encode("utf-8")) + seviye)
        olasilik = 0.05 if seviye < 15 else 0.09
        limit = max(1, len(metin) // 12)
        sayac = 0
        derin_tag = 0
        derin_kose = 0
        cikti = []

        for ch in metin:
            if ch == "{":
                derin_tag += 1
            elif ch == "}":
                derin_tag = max(0, derin_tag - 1)
                cikti.append(ch)
                continue
            elif ch == "[":
                derin_kose += 1
            elif ch == "]":
                derin_kose = max(0, derin_kose - 1)
                cikti.append(ch)
                continue

            if derin_tag or derin_kose or not ch.isalpha() or sayac >= limit:
                cikti.append(ch)
            elif r.random() < olasilik:
                cikti.append(r.choice(_BOZUK_HAVUZ))
                sayac += 1
            else:
                cikti.append(ch)

        return "".join(cikti)

    config.say_menu_text_filter = _stres_boz

    def stres_karistir(liste):
        """stres = 15 (son seviye): seçim kutularının sırasını karıştırır.

        Etkileşim başına deterministik (kutu metinleri + stresle tohumlanır) —
        ekran yeniden çizildiğinde kutular imlecin altında dans etmez.
        """
        if getattr(store, "stres", 0) < 15 or len(liste) < 2:
            return liste
        anahtar = "".join((getattr(i, "caption", "") or "") for i in liste)
        tohum = zlib.crc32(anahtar.encode("utf-8")) + store.stres
        yeni = list(liste)
        _pyrandom.Random(tohum).shuffle(yeni)
        return yeni
