# fisilti.rpy — Pieces of Mind
# Milk tarzı etkileşim: Fısıltı'nın HER repliği oyuncu tarafından ekranın
# üstündeki kutulardan seçilir (tek seçenek olsa bile). Kutuya tıklamak =
# fısıldamaktır; replik alta tekrar yazılmaz, cevap şövalyeden gelir.
#
# İstisna: ölüm sonrası monolog (death.rpy) — dinleyen beden yok, düz f kalır.
#
# Kullanım:
#   $ fis("Kalk.")                          -> tek kutu
#   $ sec = fis("Diren.", "Direnme.")       -> çoklu; seçilen indeks döner
#   (Uzun dallanmalarda 'menu:' ifadesi kullanılmaya devam eder; kutular
#    aynı seçim ekranından geçer, görünüm aynıdır.)

# Şövalyenin Fısıltı'ya güveni (0-10, başlangıç 5). Senaryo eliyle değişir.
# guven <= 2 iken, ÖNCEDEN YAZILMIŞ kilit anlarda (sahne başına en fazla 1)
# şövalye fısıltıyı duyar ama reddeder — kontrol oyuncunun elinden kayar.
default guven = 5


init -1 python:

    def fis(*metinler):
        """Fısıltı repliği: üstteki kutu(lar)dan seçilir. İndeks döner.

        Metinler __() ile çevrilir (dil desteği): kaynak dizgiler Türkçe,
        karşılıkları tl/english/fisilti_strings.rpy içinde yaşar.
        """
        cevrili = [__(m) for m in metinler]
        secenekler = [("«%s»" % m, i) for i, m in enumerate(cevrili)]
        secim = renpy.display_menu(secenekler)
        # Seçilen fısıltıyı geçmişe (history) Fısıltı satırı olarak işle.
        try:
            f.add_history("adv", __("Fısıltı"), cevrili[secim])
        except Exception:
            pass
        return secim

    def guven_degistir(delta):
        """Şövalyenin güvenini değiştirir (0-10 aralığına sıkıştırılır)."""
        store.guven = max(0, min(10, store.guven + delta))
