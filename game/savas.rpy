# savas.rpy — Pieces of Mind
# Dövüş sunumu: düşman görseli, isabet yanıp sönmesi, iki can barı,
# ve GİZLİ zarlar (kaçma + düşman hasarı).
#
# Tasarım notu — neden bazı zarlar gizli:
#   Oyuncunun KENDİ hamlesi panelde atılır (dice.rpy): failin sahibi o.
#   Düşmanın hamlesi ve bedenin refleksi panelsizdir — şövalye bunları
#   seçmiyor, yaşıyor. Panel açmak "sen attın" der; oysa oyuncu fısıltı,
#   bedeni o savurmuyor. Sonuç metinden okunur (İlke 8: sezdirme).
#
# Kullanım (scene7_inis.rpy):
#   call savas_basla("Yarım", 10, "yarim")
#   call dusman_vur(sonuc.hasar)          # bizim isabetimiz -> yanıp söner
#   call dusman_saldirisi("sebep")        # kaçma zarı + hasar zarı
#   call savas_bitir


################################################################################
## Ayarlar — dengeyi buradan çevir (zar_dc_sabit / stres_bolen ile aynı kalıp)
################################################################################

# Kaçma: gizli ŞANS zarı. d20 + ŞANS >= kacma_dc ise vuruş ıskalar.
# ŞANS 0'da %40, her ŞANS puanı +%5.
define kacma_dc = 13

# Düşmanın vuruşu: bizim hasar mantığımızın AYNISI — DC'nin üstündeki
# her puan hasardır (bkz. stats.rpy RollResult.hasar).
#
# hasar_dc 12 -> 10 (kullanıcı kararı 2026-09-03): ŞANS artık hasardan
# DOĞRUDAN düşüldüğü için ham hasarın büyümesi gerekiyordu. 12'de ham
# ortalama 3,2 idi; ŞANS'ı çıkarınca vuruşların çoğu taban 1'e yapışıyor
# ve ŞANS'ın bir puanı ile üç puanı arasında fark kalmıyordu. 10'da ham
# ortalama 4,3 (maks 12) — çıkarma anlamlı, ölüm eğrisi ŞANS'a duyarlı.
define dusman_bonus = 2
define dusman_hasar_dc = 10

# Görsel
define dusman_yeri_x = 0.70


################################################################################
## Durum (save/rollback uyumu için default)
################################################################################

default savas_acik = False
default savas_dusman_ad = ""
default savas_dusman_can = 0
default savas_dusman_can_max = 1
default savas_dusman_gorsel = ""


init -1 python:

    def kacabildi_mi():
        """Gizli ŞANS zarı: beden kendini çekebildi mi?

        Panelsiz — şövalyenin refleksi oyuncunun kararı değil.
        """
        return player_stats.roll("SANS", kacma_dc).success

    def dusman_hasari():
        """Düşmanın gizli zarı. Bizim hasar mantığımızın aynısı:
        d20 + bonus, dusman_hasar_dc'nin üstündeki her puan = hasar.

        ŞANS puanı hasardan DOĞRUDAN düşülür (kullanıcı kararı 2026-09-03):
        ŞANS 2 iken 8'lik bir vuruş 6 olur. Böylece ŞANS iki kez iş yapar —
        kaçma ihtimali (kacabildi_mi) ve isabet ettiğinde zırh gibi.
        Yükselme panelinde ŞANS artık gerçek bir yatırım.

        Taban 1: değen vuruş hiç acıtmasın olmaz.
        """
        zar = renpy.random.randint(1, 20)
        ham = max(1, zar + dusman_bonus - dusman_hasar_dc)
        return max(1, ham - player_stats.get("SANS"))


################################################################################
## Görsel: duruş ve isabet yanıp sönmesi
################################################################################

# Yerinde duruş — çok hafif bir salınım (nefes değil; Yarım nefes almıyor).
transform dusman_yeri:
    xalign dusman_yeri_x
    yalign 1.0
    subpixel True
    block:
        linear 2.2 yoffset -4
        linear 2.4 yoffset 2
        repeat

# İsabet: kırmızı yanıp söner + geri savrulur.
transform dusman_vuruldu:
    matrixcolor TintMatrix("#ff5a5a")
    xoffset 14
    linear 0.07 matrixcolor TintMatrix("#ffffff") xoffset 0
    matrixcolor TintMatrix("#ff5a5a")
    xoffset 8
    linear 0.09 matrixcolor TintMatrix("#ffffff") xoffset 0


################################################################################
## HUD — iki can barı
################################################################################

# Milk minimali: yuvarlak hatlı gösterge yok. İnce, blok, kırmızı üst çizgili —
# textbox'la aynı dil.
screen savas_hud():

    zorder 900

    # ── SOL ÜST: şövalye ──────────────────────────────────────────────
    vbox:
        xpos 46
        ypos 34
        spacing 4

        hbox:
            spacing 14
            text _("ŞÖVALYE") size 30 color "#b8ac93"
            text "[player_stats.can]/[player_stats.can_max]" size 30 color "#f5e9d0"

        frame:
            background Transform(Solid("#cc2222"), ysize=2)
            xsize 360
            ysize 2

        bar:
            value player_stats.can
            range player_stats.can_max
            xsize 360
            ysize 16
            left_bar Solid("#cc2222")
            right_bar Solid("#2a1414")
            thumb None
            thumb_shadow None

    # ── SAĞ ÜST: düşman ───────────────────────────────────────────────
    vbox:
        xpos 1514
        ypos 34
        spacing 4
        xsize 360

        hbox:
            xalign 1.0
            spacing 14
            text "[savas_dusman_can]/[savas_dusman_can_max]" size 30 color "#f5e9d0"
            text "[savas_dusman_ad!t]" size 30 color "#a05a5a"

        frame:
            background Transform(Solid("#a05a5a"), ysize=2)
            xsize 360
            ysize 2

        bar:
            value savas_dusman_can
            range savas_dusman_can_max
            xsize 360
            ysize 16
            left_bar Solid("#2a1414")
            right_bar Solid("#a05a5a")
            thumb None
            thumb_shadow None


################################################################################
## Etiketler
################################################################################

label savas_basla(ad, can, gorsel):

    $ savas_dusman_ad = ad
    $ savas_dusman_can = can
    $ savas_dusman_can_max = can
    $ savas_dusman_gorsel = gorsel
    $ savas_acik = True

    # renpy.show: görsel adı bir DEĞİŞKENDEN geliyor ("show expression" bir
    # dizeyi dosya adı sanabilir; bu yol görsel adını doğrudan çözer).
    $ renpy.show(savas_dusman_gorsel, at_list=[dusman_yeri], tag="dusman")
    with Dissolve(0.6)

    show screen savas_hud
    with Dissolve(0.4)

    return


label dusman_vur(miktar):

    # Barı önce düşür, sonra yanıp söndür: sayı ve darbe aynı anda okunsun.
    $ savas_dusman_can = max(0, savas_dusman_can - miktar)

    $ renpy.show(savas_dusman_gorsel, at_list=[dusman_yeri, dusman_vuruldu],
                 tag="dusman")
    play sound olum_vurusu volume 0.35
    $ renpy.pause(0.32, hard=True)
    $ renpy.show(savas_dusman_gorsel, at_list=[dusman_yeri], tag="dusman")

    return


label savas_bitir(sonduren=True):

    hide screen savas_hud
    if sonduren:
        hide dusman
    with Dissolve(0.8)

    $ savas_acik = False

    return
