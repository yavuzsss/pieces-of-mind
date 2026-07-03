# audio.rpy — Pieces of Mind
# Ses tanımları ve genel ses davranışları.
#
# NOT: game/audio/ içindeki tüm dosyalar Python ile sentezlenmiş
# PLACEHOLDER'lardır. Gerçek sesleri AYNI DOSYA ADIYLA üzerine yaz,
# kod değişmeden yenileri çalar. (Gerçek dosyalar .ogg olacaksa buradaki
# uzantıları güncellemek yeterli.)


################################################################################
## Tanımlar
################################################################################

define audio.metin_tik = "audio/metin_tik.wav"        # replik başı kuru tık
define audio.ui_hover = "audio/ui_hover.wav"          # seçim üzerine gelme
define audio.ui_sec = "audio/ui_sec.wav"              # seçim onayı
define audio.zar = "audio/zar.wav"                    # zar takırtısı
define audio.glitch_sfx = "audio/glitch.wav"          # glitch cızırtısı
define audio.olum_vurusu = "audio/olum_vurusu.wav"    # ölüm vuruşu
define audio.muzik_karanlik = "audio/muzik_karanlik.wav"  # ana drone loop

# Ana menüde de aynı karanlık tema çalar.
define config.main_menu_music = "audio/muzik_karanlik.wav"


################################################################################
## Replik Tıkı (Milk tarzı)
################################################################################

init python:

    def metin_tik_cal(event, interact=True, **kwargs):
        """Her replik göründüğünde kuru bir tık çalar (atlama sırasında hariç)."""
        if event == "show" and interact and not renpy.is_skipping():
            renpy.sound.play(audio.metin_tik)

    config.all_character_callbacks.append(metin_tik_cal)
