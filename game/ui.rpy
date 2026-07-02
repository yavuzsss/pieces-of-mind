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

## Seçim düğmeleri: koyu blok, hover'da kırmızı blok.
style choice_button:
    background "#141414e6"
    hover_background "#cc2222"
    xpadding 40
    ypadding 10

## Ana menü başlığı: kırmızı, iri.
style main_menu_title:
    color "#cc2222"


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
