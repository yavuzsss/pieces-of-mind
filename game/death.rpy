# death.rpy — Pieces of Mind
# Permadeath (kalıcı ölüm) akışı.
#
# Tasarım:
#   - Ölüm anlatıdan tetiklenir:  call olum("alev seni yuttu")
#   - Ölüm anında geri sarma (rollback) kapatılır.
#   - Her koşunun (run) benzersiz bir kimliği vardır; ölümde bu kimlik
#     persistent'a "ölü" olarak işlenir. O koşuya ait bir kayıt yüklenirse
#     after_load yakalar ve koşunun bittiğini söyler — save-scum yolu yok.
#   - Fısıltı (oyuncu) ölümden etkilenmez: beden gider, lanet kalır.
#     persistent.olum_sayisi oyunlar arası taşınır; anlatı bunu bilir.


################################################################################
## Kalıcı Veri
################################################################################

default persistent.olum_sayisi = 0      # Tüm koşulardaki toplam ölüm.
default persistent.son_olum = None      # Son ölümün sebebi.
default persistent.olu_kosular = set()  # Ölümle bitmiş koşuların kimlikleri.

# Bu koşunun kimliği (start'ta yeni_kosu_id() ile atanır).
default run_id = None


init python:

    def yeni_kosu_id():
        """Her yeni oyuna benzersiz bir koşu kimliği üretir."""
        import time
        return "kosu-%d" % int(time.time() * 1000)


################################################################################
## Ölüm Ekranı
################################################################################

# "ÖLDÜN" yavaşça belirir.
transform olum_belirme:
    alpha 0.0
    linear 2.2 alpha 1.0

# Alt satırlar daha geç belirir.
transform olum_belirme_gec:
    alpha 0.0
    pause 2.4
    linear 1.2 alpha 1.0


screen olum_ekrani(sebep, sayi):

    modal True
    zorder 300

    add Solid("#0a0a0a")

    vbox:
        align (0.5, 0.45)
        spacing 40

        text "ÖLDÜN":
            xalign 0.5
            size 170
            color "#cc2222"
            at olum_belirme

        vbox:
            xalign 0.5
            spacing 12
            at olum_belirme_gec

            text "[sebep]":
                xalign 0.5
                size 34
                color "#8a8378"

            text "ölüm: [sayi]":
                xalign 0.5
                size 28
                color "#b8ac93"

            text "> devam":
                xalign 0.5
                size 22
                color "#8a8378"
                at soft_blink

    # Yazı belirmeden ekran kapatılamasın.
    timer 2.6 action SetScreenVariable("kapatilabilir", True)
    default kapatilabilir = False
    if kapatilabilir:
        dismiss action Return()


################################################################################
## Ölüm Akışı
################################################################################

# Kullanım: call olum("sebep metni")
# Sebep, ölüm ekranında küçük puntoyla görünür ("alev seni yuttu" gibi).
label olum(sebep="bilinmeyen bir son"):

    # Geri dönüş yok: bu noktadan öncesine rollback kapatılır.
    $ renpy.block_rollback()

    window hide

    stop music fadeout 1.0

    call glitch_burst(0.8, 1.6)

    play sound olum_vurusu

    # Ölüm kalıcı veriye işlenir; koşunun kayıtları geçersiz kılınır.
    python:
        persistent.olum_sayisi += 1
        persistent.son_olum = sebep
        if run_id is not None:
            persistent.olu_kosular = persistent.olu_kosular | {run_id}
        renpy.save_persistent()

    call screen olum_ekrani(sebep, persistent.olum_sayisi)

    scene black
    with Pause(0.8)

    # Fısıltı ölümden etkilenmez. Bu replikler oyuncunun kendi iç sesi:
    # beden öldü, lanet (oyuncu) kaldı.
    if persistent.olum_sayisi == 1:

        f "..."

        f "Demek böyle bitiyor."

        f "Hayır. Böyle bitmiyor. Beden biter. Ben bitmem."

        f "Karanlıkta bekleyeceğim. Bir sonraki uyanışı."

    else:

        f "Yine."

        f "[persistent.olum_sayisi]. beden. Hepsi aynı şekilde soğuyor."

        f "Önemi yok. Ben kalırım. Ben hep kalırım."

    f "Baştan başlıyoruz."

    call glitch_burst(0.4, 1.0)

    # Ana menüye dönüş. Yeni oyun = yeni koşu = yeni beden.
    $ renpy.full_restart()


################################################################################
## Ölü Koşu Kilidi
################################################################################

# Her yüklemeden sonra çalışan özel etiket: yüklenen kayıt ölmüş bir koşuya
# aitse oyuncu içeri alınmaz.
label after_load:

    if run_id is not None and run_id in persistent.olu_kosular:
        jump olum_kosu_bitti

    return


label olum_kosu_bitti:

    $ renpy.block_rollback()

    scene black

    call glitch_burst(0.5, 1.2)

    f "Hayır."

    f "O beden öldü. O hikâye bitti."

    f "Geri dönüş yok. Hiç olmadı."

    f "Yeni bir beden bul."

    $ renpy.full_restart()
