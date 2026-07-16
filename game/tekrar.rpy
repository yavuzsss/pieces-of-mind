# tekrar.rpy — Pieces of Mind
# Ölüm sonrası hızlı geçiş: "Fısıltı hatırlıyor."
#
# Tasarım:
#   - İlk koşuda acele edilmez: skip tamamen kapalı (Ctrl dahil).
#     Quick menu'de düğmesi de yok — oyuncu ilk yaşayışında her kelimeyi okur.
#   - En az bir ölümden sonra açılır. Tematik gerekçe: beden ölür, Fısıltı
#     (oyuncu) kalır ve yaşananları hatırlar. Bu yüzden yalnızca GÖRÜLMÜŞ
#     metin geçilebilir (skip_unseen bilinçli olarak kapalı bırakılır —
#     kule yalnızca yaşananı hatırlar).
#   - Fısıltı kutuları (fis) menüdür; skip menülerde durur. Bu da bilinçli:
#     oyuncunun sözü her koşuda yine oyuncunun sözüdür — fısıltılar
#     hızla geçilemez.
#   - Arayüz: quick menu'ye tek silik kelime eklenir — «geç» (ui.rpy).
#     İlk ölüm ekranında bir defalık küçük bir açıklama görünür (death.rpy).

default persistent.gec_acildi = False   # «geç» ilk açılışında bir defalık ayar.

init python:

    def gec_hakki():
        """Ölüm görmüş oyuncu görülmüş metni geçebilir."""
        return (persistent.olum_sayisi or 0) > 0

    def gec_uygula():
        """Skip iznini ölüm sayısına göre kurar.

        _skipping store değişkenidir (Ctrl ve Skip() bunu dinler);
        her koşu başında ve her yüklemede yeniden değerlendirilir.
        """
        store._skipping = gec_hakki()
        if store._skipping and not persistent.gec_acildi:
            persistent.gec_acildi = True
            # Fısıltı kutuları menüdür; seçimden sonra geçiş kaldığı
            # yerden sürsün (oyuncu ayarlardan kapatabilir).
            _preferences.skip_after_choices = True

    config.after_load_callbacks.append(gec_uygula)
