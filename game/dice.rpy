# dice.rpy — Pieces of Mind
# BG3 tarzı görsel zar paneli. Görsel varlık gerektirmez; elmas (d20) şekli
# döndürülmüş Solid'lerle çizilir. Palet: kırmızı / krem / siyah.
#
# Kullanım (script içinden):
#     call roll_dice("ZEKA", 10)
#     call roll_dice("GUC", 10, savas=True)   # savaş: panelde HASAR gösterilir
#     $ sonuc = _return          # RollResult nesnesi


init -5 python:

    # UI'da gösterilecek Türkçe stat adları.
    STAT_TR = {
        "GUC": "GÜÇ",
        "ZEKA": "ZEKÂ",
        "SANS": "ŞANS",
    }


# Son atılan zarın sonucu (roll_dice etiketi doldurur).
default dice_result = None

# ZORLUK SABİTLEME: tüm zar DC'leri 10'a sabit (kullanıcı kararı, 2026-07-11).
# Senaryodaki call roll_dice(..., DC) değerleri tasarım niyeti olarak yerinde
# durur ama fiilen kullanılmaz. Değişken zorluklara dönmek için: None yap.
define zar_dc_sabit = 10


################################################################################
## Transformlar
################################################################################

# Zar dönerken: elmas sağa sola yalpalar.
transform die_spin:
    subpixel True
    rotate 45
    block:
        easein 0.10 rotate 53
        easein 0.10 rotate 37
        repeat

# Zar durduğunda: düz elmas.
transform die_rest:
    subpixel True
    rotate 45

# Kritiklerde elmasın arkasında nabız gibi atan parlama.
transform crit_pulse:
    subpixel True
    rotate 45
    alpha 0.0
    block:
        easein 0.35 alpha 0.45
        easeout 0.35 alpha 0.10
        repeat

# Sonuç dökümü belirirken küçük bir "pop".
transform verdict_pop:
    alpha 0.0
    zoom 1.25
    easein 0.25 alpha 1.0 zoom 1.0

# "devam" ipucu yanıp söner.
transform soft_blink:
    block:
        easein 0.7 alpha 0.25
        easeout 0.7 alpha 1.0
        repeat


################################################################################
## Zar Paneli Ekranı
################################################################################

screen dice_panel(result):

    modal True
    zorder 200

    # Fazlar: spin (zar dönüyor) -> reveal (sayı durdu) -> done (döküm + hüküm)
    default phase = "spin"
    default spins = 0
    default spin_num = 1

    python:
        stat_label = __(STAT_TR.get(result.stat_name, result.stat_name))
        bonus_str = "%+d" % result.bonus
        if result.crit_success:
            verdict, verdict_color = __("KRİTİK BAŞARI"), "#f5e9d0"
        elif result.crit_fail:
            verdict, verdict_color = __("KRİTİK BAŞARISIZLIK"), "#cc2222"
        elif result.success:
            verdict, verdict_color = __("BAŞARI"), "#f5e9d0"
        else:
            verdict, verdict_color = __("BAŞARISIZLIK"), "#cc2222"

    # Arka planı karart.
    add Solid("#0a0a0af2")

    # Faz geçişleri ve tıklama davranışı.
    if phase == "spin":
        # spins her tikte değişir; böylece ekran her seferinde yeniden çizilir
        # ve spin_num için yeni bir rastgele sayı üretilir.
        timer 0.06 repeat True action [
            SetScreenVariable("spins", spins + 1),
            SetScreenVariable("spin_num", renpy.random.randint(1, 20))]
        timer 1.2 action SetScreenVariable("phase", "reveal")
        dismiss action SetScreenVariable("phase", "done")
    elif phase == "reveal":
        timer 0.8 action SetScreenVariable("phase", "done")
        dismiss action SetScreenVariable("phase", "done")
    else:
        dismiss action Return()

    vbox:
        align (0.5, 0.5)
        spacing 36
        xsize 700

        # Başlık + zorluk derecesi.
        vbox:
            xalign 0.5
            spacing 8
            text _("— [stat_label] ZARI —"):
                xalign 0.5
                size 34
                bold True
                color "#cc2222"
            text _("ZORLUK  [result.dc]"):
                xalign 0.5
                size 22
                color "#b8ac93"

        # Zar: kırmızı elmas çerçeve, içi siyah, ortada sayı.
        fixed:
            xysize (260, 260)
            xalign 0.5

            # Kritiklerde arkada nabız gibi atan parlama.
            if phase != "spin" and (result.crit_success or result.crit_fail):
                add Transform(Solid("#f5e9d0" if result.crit_success else "#cc2222"),
                              xysize=(225, 225)) align (0.5, 0.5) at crit_pulse

            if phase == "spin":
                add Transform(Solid("#cc2222"), xysize=(180, 180)) align (0.5, 0.5) at die_spin
                add Transform(Solid("#0a0a0a"), xysize=(150, 150)) align (0.5, 0.5) at die_spin
                text "[spin_num]":
                    align (0.5, 0.5)
                    size 54
                    color "#b8ac93"
            else:
                add Transform(Solid("#cc2222"), xysize=(180, 180)) align (0.5, 0.5) at die_rest
                add Transform(Solid("#0a0a0a"), xysize=(150, 150)) align (0.5, 0.5) at die_rest
                text "[result.die]":
                    align (0.5, 0.5)
                    size 64
                    bold True
                    color ("#cc2222" if result.crit_fail else "#f5e9d0")

        # Döküm + hüküm (sadece son fazda).
        if phase == "done":
            vbox:
                xalign 0.5
                spacing 14
                at verdict_pop
                text "d20([result.die])  [bonus_str]  =  {b}[result.total]{/b}":
                    xalign 0.5
                    size 26
                    color "#b8ac93"
                text "[verdict]":
                    xalign 0.5
                    size 40
                    bold True
                    color verdict_color
                # Savaş zarı: DC'nin üstündeki her puan = hasar.
                if result.savas and result.success:
                    text _("HASAR  [result.hasar]"):
                        xalign 0.5
                        size 26
                        bold True
                        color "#cc2222"
                text _("> devam"):
                    xalign 0.5
                    size 18
                    color "#b8ac93"
                    at soft_blink
        else:
            # Yer tutucu: panel yüksekliği faz geçişinde zıplamasın.
            null height 130


################################################################################
## Zar Atma Etiketi
################################################################################

label roll_dice(stat_name, dc, savas=False):

    # Zar burada atılır (ekran argümanı içinde DEĞİL — ekran ön-izlemeleri
    # yan etkili ifadeleri birden çok kez çalıştırabilir).
    # zar_dc_sabit doluysa senaryodan gelen dc yerine o kullanılır.
    # savas=True: panelde HASAR satırı gösterilir (marj = hasar).
    $ dice_result = player_stats.roll(stat_name, zar_dc_sabit if zar_dc_sabit is not None else dc)
    $ dice_result.savas = savas

    window hide
    play sound zar
    call screen dice_panel(dice_result)

    # Doğal 1: lanet kıpırdanır — panel kapanınca ekran bozulur.
    # (stres: +1 burada, +1 glitch_burst içinden = toplam +2)
    # İyi zarlar nefes aldırır: başarı -1, doğal 20 -2.
    if dice_result.crit_fail:
        $ stres_degistir(1)
        call glitch_burst(0.5, 1.3)
    elif dice_result.crit_success:
        $ stres_degistir(-2)
    elif dice_result.success:
        $ stres_degistir(-1)

    window auto

    return dice_result
