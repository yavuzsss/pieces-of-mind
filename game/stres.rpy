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

# stres: TÜRETİLMİŞ seviye (0-15) — ui.rpy / effects.rpy bunu okur.
# stres_ham: senaryonun yazdığı ham puanın havuzu.
# Senaryo 76 çağrı noktasından temsilî bir koşuda ~30 net ham puan üretiyor;
# ham/bölen sayesinde 0-15 ölçeği bu bütçeye oturur (çağrı noktalarına
# dokunulmadan: $ stres_degistir(+1/-1) yazım dili aynen korunur).
default stres = 0
default stres_ham = 0

# ANA ANAHTAR (kullanıcı kararı 2026-08-11: yeniden ölçeklenip AÇILDI).
define stres_etkin = True

# Ölçek: kaç ham puan = 1 stres. Eğriyi ayarlamanın TEK noktası burası.
# bolen 2 ile: seviye 1 (5) Sahne 5-6, seviye 2 (10) Sahne 8,
# seviye 3 (15) yalnızca pahalı koşularda ve ancak Sahne 9'un sonunda.
define stres_bolen = 2
define stres_ham_tavan = 30

# ETKİ TAVANI — hangi seviyeye kadar etki uygulanır:
#   0 = tümü kapalı
#   1 = yalnız CRT şişmesi + hafif textbox glitch'i   <-- ŞU ANKİ AYAR
#   2 = + metin bozulması
#   3 = + seçim kutularının karışması
# zar_dc_sabit ile aynı kalıp: tasarım kodda duruyor, açmak tek sayı.
define stres_etki_tavani = 1


init -1 python:

    import zlib
    import random as _pyrandom

    def stres_degistir(delta):
        """Ham stresi değiştirir; görünen seviyeyi (0-15) yeniden türetir."""
        store.stres_ham = max(0, min(stres_ham_tavan, store.stres_ham + delta))
        store.stres = min(15, store.stres_ham // stres_bolen)

    def stres_seviye():
        """Etkin seviye (0-3), stres_etki_tavani ile kırpılmış.

        Ağır efektler bu yüzden bayrakla değil VERİYLE kapalı — tek
        kontrol noktası. Efekt uygulayan her yer bunu okur.
        """
        if not stres_etkin:
            return 0
        s = getattr(store, "stres", 0)
        lv = 3 if s >= 15 else (2 if s >= 10 else (1 if s >= 5 else 0))
        return min(lv, stres_etki_tavani)

    def stres_textbox_gucu():
        """Diyalog kutusu glitch şiddeti. 0.0 = efekt HİÇ uygulanmaz."""
        if stres_seviye() < 1:
            return 0.0
        s = getattr(store, "stres", 0)
        return 0.03 + 0.06 * min(1.0, (s - 5) / 10.0)   # 0.03 -> 0.09

    def stres_crt_gucu():
        """CRT şişmesi (seviye 1'in etkisi) — tavan 1 olsa da stresle büyür."""
        if not stres_etkin:
            return 0.0
        return min(1.0, max(0.0, (getattr(store, "stres", 0) - 4) / 11.0))

    def textbox_stres_at():
        """say penceresine uygulanacak transform listesi.

        Şiddet 0 iken BOŞ liste döner: mesh/shader/redraw döngüsü hiç
        kurulmaz. (Eskiden 0.0 şiddetle de her replikte render-to-texture
        pass'i çalışıyordu — kapalı bir özellik için sürekli GPU maliyeti.)
        """
        guc = stres_textbox_gucu()
        return [textbox_stres_fx(guc)] if guc > 0.0 else []

    # VT323'te blok karakterleri yok — bozulma havuzu ASCII.
    _BOZUK_HAVUZ = "#/\\_X"

    def _stres_boz(metin):
        """Deterministik metin bozulması (say + menü metinleri).

        Satırın CRC'siyle tohumlanır: aynı satır aynı streste hep aynı
        şekilde bozulur (rollback/kayıt tutarlılığı). {etiketler} ve
        [değişkenler] atlanır. Bozulan karakter sayısı sınırlıdır —
        satır daima çözülebilir kalır.
        """
        if stres_seviye() < 2 or not metin:
            return metin
        seviye = getattr(store, "stres", 0)

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
        if stres_seviye() < 3 or len(liste) < 2:
            return liste
        anahtar = "".join((getattr(i, "caption", "") or "") for i in liste)
        tohum = zlib.crc32(anahtar.encode("utf-8")) + store.stres
        yeni = list(liste)
        _pyrandom.Random(tohum).shuffle(yeni)
        return yeni
