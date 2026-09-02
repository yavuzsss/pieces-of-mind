# audio.rpy — Pieces of Mind
# Ses tanımları ve genel ses davranışları.
#
# NOT: game/audio/ içindeki tüm dosyalar Python ile sentezlenmiş
# PLACEHOLDER'lardır. Gerçek sesleri AYNI DOSYA ADIYLA üzerine yaz,
# kod değişmeden yenileri çalar.
#
# Biçim: müzik .ogg (Vorbis), kısa efektler .wav.
# Müzik ham WAV olarak 7,2 MB tutuyordu — Vorbis'te 1 MB. Efektler WAV
# kaldı: metin tıkı her replikte çalıyor, çözme gecikmesi istemiyoruz ve
# hepsi toplam ~330 KB. Çevirici: tools/ses_ogg_cevir.py


################################################################################
## Tanımlar
################################################################################

define audio.metin_tik = "audio/metin_tik.wav"        # replik başı kuru tık
define audio.ui_hover = "audio/ui_hover.wav"          # seçim üzerine gelme
define audio.ui_sec = "audio/ui_sec.wav"              # seçim onayı
define audio.zar = "audio/zar.wav"                    # zar takırtısı
define audio.glitch_sfx = "audio/glitch.wav"          # glitch cızırtısı
define audio.olum_vurusu = "audio/olum_vurusu.wav"    # ölüm vuruşu
define audio.muzik_karanlik = "audio/muzik_karanlik.ogg"  # ana drone loop

# Finallere özel parçalar (tools/muzik_finaller_uret.py — PLACEHOLDER):
define audio.muzik_teslim = "audio/muzik_teslim.ogg"    # Teslim: soğuk, inen motif
define audio.muzik_armagan = "audio/muzik_armagan.ogg"  # Armağan: tek sıcak parça
define audio.muzik_sonus = "audio/muzik_sonus.ogg"      # Sönüş: boşluk + yalnız nota
define audio.muzik_gasp = "audio/muzik_gasp.ogg"        # Gasp: vuruşlu detune yanlışlık

# Ana menüde de aynı karanlık tema çalar.
define config.main_menu_music = "audio/muzik_karanlik.ogg"


################################################################################
## Replik Tıkı (Milk tarzı)
################################################################################

init python:

    def metin_tik_cal(event, interact=True, **kwargs):
        """Her replik göründüğünde kuru bir tık çalar (atlama sırasında hariç)."""
        if event == "show" and interact and not renpy.is_skipping():
            renpy.sound.play(audio.metin_tik)

    config.all_character_callbacks.append(metin_tik_cal)
