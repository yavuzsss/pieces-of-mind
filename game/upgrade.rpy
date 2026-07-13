# upgrade.rpy — Pieces of Mind
# Yükselme sistemi: savaşlar/önemli olaylardan sonra oyuncu bir stat seçer.
# GÜÇ +1 / ZEKÂ +1 / ŞANS +1 / CAN +2 (can tavanıyla birlikte).
#
# Kullanım (sahne içinden, önemli olayın ardından):
#     call yukselme

# Son yükselme seçimi (save/rollback uyumu için default).
default yukselme_secim = None


################################################################################
## Yükselme Paneli
################################################################################

screen yukselme_panel():

    modal True
    zorder 200

    # Arka planı karart (zar paneliyle aynı ton).
    add Solid("#0a0a0af2")

    # Metin interpolasyonu fonksiyon çağrısı desteklemez — değerler burada hazırlanır.
    python:
        guc_v = player_stats.get("GUC")
        zeka_v = player_stats.get("ZEKA")
        sans_v = player_stats.get("SANS")
        can_v = player_stats.can
        can_m = player_stats.can_max

    vbox:
        align (0.5, 0.5)
        spacing 40
        xsize 760

        vbox:
            xalign 0.5
            spacing 10
            text _("— YÜKSELİŞ —"):
                xalign 0.5
                size 34
                bold True
                color "#cc2222"
            text _("Bir şey büyüyor içinde. Ne olduğunu sen seç."):
                xalign 0.5
                size 22
                color "#b8ac93"

        vbox:
            xalign 0.5
            spacing 18

            textbutton _("GÜÇ  +1      (şu an [guc_v])"):
                xalign 0.5
                action Return("GUC")
                text_size 26
                text_color "#f5e9d0"
                text_hover_color "#cc2222"

            textbutton _("ZEKÂ  +1      (şu an [zeka_v])"):
                xalign 0.5
                action Return("ZEKA")
                text_size 26
                text_color "#f5e9d0"
                text_hover_color "#cc2222"

            textbutton _("ŞANS  +1      (şu an [sans_v])"):
                xalign 0.5
                action Return("SANS")
                text_size 26
                text_color "#f5e9d0"
                text_hover_color "#cc2222"

            textbutton _("CAN  +2      (şu an [can_v]/[can_m])"):
                xalign 0.5
                action Return("CAN")
                text_size 26
                text_color "#f5e9d0"
                text_hover_color "#cc2222"


################################################################################
## Yükselme Etiketi
################################################################################

label yukselme:

    window hide

    call screen yukselme_panel

    $ yukselme_secim = _return
    $ player_stats.yukselt(yukselme_secim)

    if yukselme_secim == "GUC":
        centered "{color=#f5e9d0}GÜÇ ARTTI{/color}"
    elif yukselme_secim == "ZEKA":
        centered "{color=#f5e9d0}ZEKÂ ARTTI{/color}"
    elif yukselme_secim == "SANS":
        centered "{color=#f5e9d0}ŞANS ARTTI{/color}"
    else:
        centered "{color=#f5e9d0}CAN ARTTI  ([player_stats.can]/[player_stats.can_max]){/color}"

    window auto

    return
