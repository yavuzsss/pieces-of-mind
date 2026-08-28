# ============================================================================
# KREDİLER — final sonrası jenerik
# ----------------------------------------------------------------------------
# Her finalin kapanış kartından sonra `call krediler` ile girilir.
# Milk minimali: siyah ekran, sırayla beliren birkaç satır, ardından tek kelime.
# `sicak=True` (yalnız Armağan): başlık krem, kapanış kelimesi «yürüyelim.»
# Soğuk finallerde başlık kırmızı, kapanış kelimesi «uyuma.» (soluk).
# Müziğe dokunulmaz — her finalin kendi sesi (ya da sessizliği) kredide sürer.
# ============================================================================

transform kredi_belir(gecikme=0.0):
    alpha 0.0
    pause gecikme
    linear 1.6 alpha 1.0

style kredi_text is text:
    font "fonts/VT323-Regular.ttf"

screen kredi_akisi(sicak=False):
    add Solid("#0a0a0a")

    vbox:
        align (0.5, 0.5)
        spacing 18
        xsize 1200

        text "PIECES OF MIND" style "kredi_text":
            xalign 0.5
            size 58
            color ("#f5e9d0" if sicak else "#cc2222")
            at kredi_belir(0.8)

        null height 30

        text _("Yavuz Selim Şeremetli tarafından yapılmıştır.") style "kredi_text":
            xalign 0.5
            size 34
            color "#f5e9d0"
            at kredi_belir(2.4)

        null height 14

        text _("Görseller: İsmail Alp Özüpek") style "kredi_text":
            xalign 0.5
            size 34
            color "#f5e9d0"
            at kredi_belir(4.0)

screen kredi_son(kelime, renk):
    add Solid("#0a0a0a")

    text kelime:
        align (0.5, 0.5)
        font "fonts/VT323-Regular.ttf"
        size 40
        color renk
        at kredi_belir(0.6)

label krediler(sicak=False):

    window hide
    $ quick_menu = False
    scene black with Dissolve(1.2)

    show screen kredi_akisi(sicak)
    with None
    $ renpy.pause(9.0)

    hide screen kredi_akisi
    with Dissolve(1.5)
    $ renpy.pause(0.8)

    # Son kelime — oyunun kapanan gözkapağı.
    if sicak:
        show screen kredi_son(_("yürüyelim."), "#f5e9d0")
    else:
        show screen kredi_son(_("uyuma."), "#7a1a1a")
    with None
    $ renpy.pause(3.5)

    hide screen kredi_son
    with Dissolve(2.0)
    $ renpy.pause(1.0)

    return
