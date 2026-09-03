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
default guven = 5


################################################################################
## DUYMADI — reddi sistem yapan katman (2026-09-03)
################################################################################
# Eskiden reddediş yalnız İKİ elle yazılmış anda yaşıyordu (sahne5_incele,
# sahne6_izin); geri kalan 141 kutuda oyuncunun sözü tartışmasız geçiyordu.
# Oysa oyunun tezi şu: şövalye seni duyuyor ama sana güvenmiyor.
#
# Artık güven düştükçe tıkladığın kutu bedene ULAŞMAYABİLİR. Kutu geri gelir;
# tekrar söylemen gerekir. Arada tek bir boşluk satırı ("...") düşer.
#
# Neden bu biçim: senaryoya HİÇ dokunmaz (sahnelerin metni fısıltının
# ulaştığını varsayar — sonunda ulaşıyor), ama kontrol kaybı METİNDE değil
# OYUNCUNUN ELİNDE hissedilir. Açıklama yok, uyarı yok (İlke 8).
#
# En fazla BİR fazladan tıklama: bu bir duygu, angarya değil.

# Bu güvenin altında başlar. 5 = başlangıç değeri, yani sağlam bağda hiç olmaz.
define fis_reddi_esigi = 5

# Eşiğin altındaki her puan bu kadar olasılık ekler.
# guven 4 -> %9, guven 2 -> %27, guven 0 -> %45.
define fis_reddi_egim = 0.09

# Finaller bunu kapatır: kapanışta oyuncunun son sözü daima ulaşmalı.
default fis_reddi_acik = True


################################################################################
## KURTARILDI — doğal 1'in yeni anlamı (2026-09-03)
################################################################################
# Doğal 1 artık öldürmüyor: Fısıltı'nın çığlığı bedeni geri çekiyor, bedel
# ağır ve telafisiz kalıyor (bkz. sahne3/4/6/7/8'deki krit_fiyasko dalları).
#
# Bu sayaç yalnız bir denge kalemi değil, KANIT: şövalye kaç kez o sesin
# onu bırakmadığına tanık oldu. Sahne 9'da gercege_kanit() bunu okur —
# "lanetler beklemez" zincirinin en somut halkası.
default kurtarildi = 0


################################################################################
## KAÇAN KUTU — ritmin bilinçli kırılması (2026-09-03)
################################################################################
# Oyun 141 fısıltı kutusu boyunca oyuncuya HER SEFERİNDE söz hakkı veriyor.
# Bu, etkileşimi dinamiksiz bırakıyor: konuşamadığın bir an hiç yok.
#
# fis_kacan(): kutu belirir, TIKLANIR — ama hiçbir şey olmaz. Sonra solar
# ve gider. Oyuncu ne söylemek istediğini görür ve söyleyemez.
#
# Sahne 3'ün sonunda bu aynı zamanda bir ÇELİŞKİYİ de kapatıyor: orada
# oyuncu fis("...") kutusuna tıklıyordu (yani konuşuyordu), ama şövalye
# hemen ardından "İlk defa... sesin sustu" diyordu. Artık gerçekten susuyor.

transform fis_kacis(sure=3.2):
    alpha 1.0
    pause sure * 0.40
    linear sure * 0.60 alpha 0.0

screen fis_kacan_ekran(kutular, sure):

    style_prefix "choice"
    zorder 100

    vbox:
        at fis_kacis(sure)
        for k in kutular:
            # NullAction: tıklanabilir görünür, tıklanır — ve hiçbir şey olmaz.
            textbutton k action NullAction()

    timer sure action Return(0)


init -1 python:

    def fis_duymadi_mi():
        """Bu fısıltı bedene ulaşmayacak mı? (bkz. yukarıdaki DUYMADI notu)"""
        if not store.fis_reddi_acik:
            return False
        if store.guven >= fis_reddi_esigi:
            return False
        pay = (fis_reddi_esigi - store.guven) * fis_reddi_egim
        return renpy.random.random() < pay

    def fis(*metinler):
        """Fısıltı repliği: üstteki kutu(lar)dan seçilir. İndeks döner.

        Metinler __() ile çevrilir (dil desteği): kaynak dizgiler Türkçe,
        karşılıkları tl/english/fisilti_strings.rpy içinde yaşar.

        Güven düşükse söz bedene ulaşmayabilir: kutu geri gelir (DUYMADI).
        """
        cevrili = [__(m) for m in metinler]
        secenekler = [("«%s»" % m, i) for i, m in enumerate(cevrili)]

        if fis_duymadi_mi():
            renpy.display_menu(secenekler)      # tıklandı — ve hiçbir şey olmadı
            renpy.say(si, "...")                # boşluk: cevap gelmiyor

        secim = renpy.display_menu(secenekler)
        # Seçilen fısıltıyı geçmişe (history) Fısıltı satırı olarak işle.
        try:
            f.add_history("adv", __("Fısıltı"), cevrili[secim])
        except Exception:
            pass
        return secim

    def fis_kacan(*metinler, **kw):
        """Söylenemeyen fısıltı: kutu belirir, tıklanır, hiçbir şey olmaz, solar.

        Geçmişe İŞLENMEZ — çünkü söylenmedi.
        """
        sure = kw.get("sure", 3.2)
        kutular = ["«%s»" % __(m) for m in metinler]
        renpy.call_screen("fis_kacan_ekran", kutular=kutular, sure=sure)

    def guven_degistir(delta):
        """Şövalyenin güvenini değiştirir (0-10 aralığına sıkıştırılır)."""
        store.guven = max(0, min(10, store.guven + delta))
