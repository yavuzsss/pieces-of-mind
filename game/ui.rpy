# ui.rpy — Pieces of Mind
# Diyalog ve arayüz özelleştirmesi. gui.rpy'ye dokunmaz; tüm geçersiz kılmalar
# burada yaşar (gui.rpy init offset -2'de çalışır, bu dosya 0'da — sonra gelir).
#
# Palet: kırmızı #cc2222 / krem #f5e9d0 / siyah #0a0a0a / soluk krem #b8ac93
# Font:  VT323 (CRT terminal piksel fontu, OFL lisansı, Türkçe destekli)


################################################################################
## GUI Değişkenleri
################################################################################

init python:

    ## Fontlar — her şey VT323.
    gui.text_font = "fonts/VT323-Regular.ttf"
    gui.name_text_font = "fonts/VT323-Regular.ttf"
    gui.interface_text_font = "fonts/VT323-Regular.ttf"

    ## Boyutlar — VT323 ince kesimli, DejaVu'dan büyük kullanılmalı.
    gui.text_size = 44
    gui.name_text_size = 40
    gui.interface_text_size = 38
    gui.label_text_size = 44
    gui.notify_text_size = 30
    gui.title_text_size = 110

    ## Renkler.
    gui.accent_color = '#cc2222'
    gui.text_color = '#f5e9d0'
    gui.interface_text_color = '#f5e9d0'
    gui.idle_color = '#8a8378'
    gui.idle_small_color = '#b8ac93'
    gui.hover_color = '#f5e9d0'
    gui.selected_color = '#cc2222'
    gui.insensitive_color = '#8a83787f'

    ## Menü arka planları — şablon PNG'leri yerine düz siyah.
    gui.main_menu_background = "#0a0a0a"
    gui.game_menu_background = "#0a0a0a"

    ## Diyalog kutusu.
    gui.textbox_height = 300

    ## Seçim düğmeleri: bekleme soluk krem; üzerine gelince kırmızı blok
    ## üstünde siyah metin (Milk tarzı).
    gui.choice_button_text_idle_color = '#b8ac93'
    gui.choice_button_text_hover_color = '#0a0a0a'


################################################################################
## Stil Geçersiz Kılmaları
################################################################################

## Diyalog kutusu: yarı saydam siyah, üstünde 3px kırmızı çizgi.
style window:
    background Fixed(
        Solid("#0a0a0ad9"),
        Transform(Solid("#cc2222"), ysize=3),
    )

## İsim kutusu: arka plansız — isim rengi karakter tanımından gelir.
style namebox:
    background None

## Seçim kutuları EKRANIN ÜSTÜNDE (Milk tarzı): Fısıltı'nın replikleri
## buradan seçilir (fisilti.rpy). Koyu blok, hover'da kırmızı blok, sesli.
style choice_vbox:
    ypos 60
    yanchor 0.0

style choice_button:
    background "#141414e6"
    hover_background "#cc2222"
    xpadding 40
    ypadding 10
    hover_sound "audio/ui_hover.wav"
    activate_sound "audio/ui_sec.wav"

## Ana menü başlığı: kırmızı, iri.
style main_menu_title:
    color "#cc2222"


################################################################################
## Ekran Geçersiz Kılmaları (stres etkileri)
################################################################################
## screens.rpy'ye dokunulmaz: say ve choice ekranları burada yeniden tanımlanır
## (ui.rpy dosya sırasında screens.rpy'den sonra yüklendiği için bunlar geçerli
## olur). Şablonla tek fark: strese bağlı bozulma etkileri.

## Diyalog kutusu glitch'i: stres >= 5'te çok hafif başlar, 15'te tepe yapar
## (0 şiddette etkisiz).
transform textbox_stres_fx(guc=0.0):
    mesh True
    shader "pom.glitch"
    u_pom_strength guc
    block:
        pause 0.05
        repeat

screen say(who, what):

    window:
        id "window"
        at textbox_stres_at()

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Yan görsel (side image) — şablon davranışı korunur.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Seçim kutuları: stres = 15'te (son seviye) titrer ve sıraları karışır.
transform kutu_titre:
    subpixel True
    block:
        linear 0.28 xoffset 3 yoffset -1
        linear 0.34 xoffset -2 yoffset 1
        linear 0.31 xoffset 1 yoffset 0
        linear 0.27 xoffset -3 yoffset -1
        repeat

screen choice(items):
    style_prefix "choice"

    $ kutular = stres_karistir(list(items))

    vbox:
        for i in kutular:
            if stres_seviye() >= 3:
                textbutton i.caption action i.action at kutu_titre
            else:
                textbutton i.caption action i.action


################################################################################
## Devam İmleci (CTC) ve Metin Hızı
################################################################################

## Satır sonunda yanıp sönen terminal imleci.
image ctc_blink:
    Text(">", color="#cc2222", size=40, font="fonts/VT323-Regular.ttf")
    block:
        linear 0.5 alpha 0.2
        linear 0.5 alpha 1.0
        repeat

## Daktilo efekti (text_cps) options.rpy'deki "Preference defaults"
## bölümünde 45 olarak ayarlıdır.


################################################################################
## Ana Menü — Lamba, Ayna, Fısıltı
################################################################################

## screens.rpy'deki main_menu burada YENİDEN TANIMLANIR (teknik kural:
## şablon dosyalarına dokunulmaz, değişiklikler ui.rpy üzerinden).
## Sahne: karanlık oda, yerde nabız gibi atan kırmızı lamba, sağda içinde
## bir şeyin beklediği ayna (bg_ana_menu). Başlık ara ara glitch'ler;
## altında "uyuma." motifi soluk soluk belirir. Başlat düğmesi bir fısıltı
## kutusudur: «kalk.» — ölüm görmüş oyuncuya «kalk. yeniden.» der.

## Lambanın ışıması: yavaş nefes + ara sıra düzensiz titreme.
transform lamba_nabiz:
    subpixel True
    alpha 0.6
    block:
        ease 2.6 alpha 0.45
        ease 2.1 alpha 0.75
        choice:
            pass
        choice:
            linear 0.06 alpha 0.25
            linear 0.05 alpha 0.7
        choice:
            linear 0.05 alpha 0.9
            linear 0.07 alpha 0.5
        repeat

## Başlığın kırmızı hayaleti: çoğu zaman görünmez, ara ara yana kayar.
transform baslik_hayalet:
    alpha 0.0
    block:
        pause 4.3
        choice:
            block:
                alpha 0.55
                xoffset -7
                pause 0.06
                xoffset 8
                pause 0.05
                alpha 0.0
                xoffset 0
        choice:
            block:
                alpha 0.4
                xoffset 5
                yoffset 2
                pause 0.08
                alpha 0.0
                xoffset 0
                yoffset 0
        choice:
            pass
        pause 2.9
        repeat

## "uyuma." — motif, uzun aralıklarla nefes alır.
transform uyuma_soluk:
    alpha 0.0
    block:
        pause 7.0
        linear 2.6 alpha 0.3
        pause 1.2
        linear 3.4 alpha 0.0
        pause 9.0
        repeat

## Menü düğmesi: üzerine gelince kısa bir sarsıntı.
transform nav_sarsinti:
    on hover:
        xoffset -3
        pause 0.05
        xoffset 3
        pause 0.05
        xoffset 0
    on idle:
        xoffset 0

style ana_nav_button:
    xpadding 6
    ypadding 2
    hover_sound "audio/ui_hover.wav"
    activate_sound "audio/ui_sec.wav"

style ana_nav_button_text:
    font "fonts/VT323-Regular.ttf"
    size 42
    idle_color "#8a8378"
    hover_color "#cc2222"

screen main_menu():

    tag menu

    add "bg_ana_menu"

    ## Lambanın üstünde atan ışıma (lamba görselde 1200, 765 civarında).
    add "fx_glow_kirmizi" pos (944, 500) at lamba_nabiz

    ## Başlık + kırmızı hayaleti.
    fixed:
        pos (100, 96)
        xmaximum 1000
        ymaximum 260

        text "PIECES OF MIND" at baslik_hayalet:
            font "fonts/VT323-Regular.ttf"
            size 124
            color "#cc2222"

        text "PIECES OF MIND":
            font "fonts/VT323-Regular.ttf"
            size 124
            color "#f5e9d0"

    text _("uyuma.") at uyuma_soluk:
        pos (108, 238)
        size 30
        color "#cc2222"

    ## Fısıltı-menüsü: başlat bir fısıltı kutusudur, gerisi çıplak kelimeler.
    vbox:
        pos (105, 420)
        spacing 20

        if persistent.olum_sayisi > 0:
            textbutton _("«kalk. yeniden.»") action Start() style "ana_nav_button" at nav_sarsinti
        else:
            textbutton _("«kalk.»") action Start() style "ana_nav_button" at nav_sarsinti

        textbutton _("yükle") action ShowMenu("load") style "ana_nav_button" at nav_sarsinti
        textbutton _("ayarlar") action ShowMenu("preferences") style "ana_nav_button" at nav_sarsinti
        textbutton _("çık") action Quit(confirm=False) style "ana_nav_button" at nav_sarsinti

    ## Dil seçimi — hedef dilin adıyla, silik.
    if _preferences.language == "english":
        textbutton "türkçe" action Language("turkish") style "hizli_button":
            pos (108, 720)
    else:
        textbutton "english" action Language("english") style "hizli_button":
            pos (108, 720)

    ## Ölüm sayacı — lanet hatırlar.
    if persistent.olum_sayisi > 0:
        text _("ölüm: [persistent.olum_sayisi]"):
            pos (32, 1032)
            size 24
            color "#4a463e"

    ## Sürüm — köşede, silik.
    text "[config.version]":
        align (0.995, 0.995)
        size 16
        color "#2e2a26"

    # --- Final galerisi (görülmeden görünmez) ---
    python:
        finaller_gorulen = [
            (__("TESLİM"),  persistent.final_teslim,  "#cc2222"),
            (__("ARMAĞAN"), persistent.final_armagan, "#f5e9d0"),
            (__("SÖNÜŞ"),   persistent.final_sonus,   "#cc2222"),
            (__("GASP"),    persistent.final_gasp,    "#cc2222"),
        ]
        herhangi_final = any(g for _ad, g, _renk in finaller_gorulen)

    if herhangi_final:

        vbox:
            align (0.98, 0.94)
            spacing 6

            text _("sonlar"):
                xalign 1.0
                size 20
                color "#8a8378"

            for ad, gorulen, renk in finaller_gorulen:
                if gorulen:
                    text ad:
                        xalign 1.0
                        size 24
                        color renk
                else:
                    text "———":
                        xalign 1.0
                        size 24
                        color "#4a463e"


################################################################################
## Hızlı Menü — Milk minimali
################################################################################

## Şablonun 8 düğmeli çubuğu yerine sağ altta dört silik kelime.
## (Geri sarma tekerlekle zaten çalışır; auto kasıtlı olarak yok —
## bu oyunda acele edilmez. «geç» yalnızca ölüm görmüş oyuncuda belirir:
## Fısıltı hatırlar, görülmüş metin geçilebilir — tekrar.rpy.)

screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            align (0.992, 0.988)
            spacing 34

            if persistent.olum_sayisi > 0:
                textbutton _("geç") action Skip() style "hizli_button"

            textbutton _("geçmiş") action ShowMenu("history") style "hizli_button"
            textbutton _("kaydet") action ShowMenu("save") style "hizli_button"
            textbutton _("yükle") action ShowMenu("load") style "hizli_button"
            textbutton _("ayarlar") action ShowMenu("preferences") style "hizli_button"

style hizli_button:
    hover_sound "audio/ui_hover.wav"
    activate_sound "audio/ui_sec.wav"

style hizli_button_text:
    font "fonts/VT323-Regular.ttf"
    size 24
    idle_color "#4a463e"
    hover_color "#cc2222"


################################################################################
## Oyun Menüsü (Esc) — navigasyon, çerçeve, onay
################################################################################

## Kenar navigasyonu Türkçe ve silik; kırmızı yalnızca dokununca.
screen navigation():

    vbox:
        style_prefix "ana_nav"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing 18

        if main_menu:
            textbutton _("«kalk.»") action Start() at nav_sarsinti
        else:
            textbutton _("geçmiş") action ShowMenu("history") at nav_sarsinti
            textbutton _("kaydet") action ShowMenu("save") at nav_sarsinti

        textbutton _("yükle") action ShowMenu("load") at nav_sarsinti
        textbutton _("ayarlar") action ShowMenu("preferences") at nav_sarsinti

        if not main_menu:
            textbutton _("ana menü") action MainMenu() at nav_sarsinti

        textbutton _("çık") action Quit(confirm=not main_menu) at nav_sarsinti

        ## Dil geçişi (Esc menüsünden de erişilebilir).
        if _preferences.language == "english":
            textbutton "türkçe" action Language("turkish") at nav_sarsinti
        else:
            textbutton "english" action Language("english") at nav_sarsinti

## Oyun menüsü zemini: siyah + tepede kırmızı çizgi (textbox diliyle aynı).
style game_menu_outer_frame:
    background Fixed(
        Solid("#0a0a0af5"),
        Transform(Solid("#cc2222"), ysize=3),
    )

style game_menu_label_text:
    font "fonts/VT323-Regular.ttf"
    size 64
    color "#cc2222"

## Onay ekranı: gri şablon kutusu yerine kırmızı çizgili karanlık kutu.
screen confirm(message, yes_action, no_action):

    modal True
    zorder 200

    add "#0a0a0ae0"

    frame:
        align (0.5, 0.5)
        xpadding 70
        ypadding 50
        background Fixed(
            Solid("#141414f5"),
            Transform(Solid("#cc2222"), ysize=3),
        )

        vbox:
            spacing 44
            xmaximum 900

            text _(message):
                xalign 0.5
                text_align 0.5
                size 40
                color "#f5e9d0"

            hbox:
                xalign 0.5
                spacing 160

                textbutton _("Yes") action yes_action style "ana_nav_button" at nav_sarsinti
                textbutton _("No") action no_action style "ana_nav_button" at nav_sarsinti
