# ceviri.rpy — Pieces of Mind
# Şablon arayüz metinlerinin Türkçe karşılıkları (strings-only çeviri).
# gui.rpy/screens.rpy'ye dokunmadan _() ile işaretli her şey buradan çevrilir.
# Oyun metni zaten Türkçe — bu dosya yalnızca arayüzü kapsar.

define config.language = "turkish"


translate turkish strings:

    # ── Onay kutuları ────────────────────────────────────────────────────
    old "Are you sure?"
    new "Emin misin?"

    old "Are you sure you want to quit?"
    new "Gidiyor musun?"

    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "Ana menüye dönmek istiyor musun?\nKaydedilmemiş her şey silinir."

    old "Are you sure you want to overwrite your save?"
    new "Bu kaydın üzerine yazılsın mı?"

    old "Are you sure you want to delete this save?"
    new "Bu kayıt silinsin mi?"

    old "Are you sure you want to end the replay?"
    new "Tekrar oynatma bitsin mi?"

    old "Yes"
    new "evet"

    old "No"
    new "hayır"

    # ── Kayıt / yükleme ──────────────────────────────────────────────────
    old "Save"
    new "kaydet"

    old "Load"
    new "yükle"

    old "Page {}"
    new "sayfa {}"

    old "Automatic saves"
    new "otomatik"

    old "Quick saves"
    new "hızlı"

    old "Q."
    new "H."

    old "A."
    new "O."

    old "empty slot"
    new "boş yuva"

    old "{#file_time}%A, %B %d %Y, %H:%M"
    new "{#file_time}%d.%m.%Y %H:%M"

    old "<"
    new "<"

    old ">"
    new ">"

    # ── Geçmiş ───────────────────────────────────────────────────────────
    old "History"
    new "geçmiş"

    old "The dialogue history is empty."
    new "Geçmiş boş. Henüz kimse konuşmadı."

    # ── Ayarlar ──────────────────────────────────────────────────────────
    old "Preferences"
    new "ayarlar"

    old "Display"
    new "görüntü"

    old "Window"
    new "pencere"

    old "Fullscreen"
    new "tam ekran"

    old "Rollback Side"
    new "geri sarma kenarı"

    old "Disable"
    new "kapalı"

    old "Left"
    new "sol"

    old "Right"
    new "sağ"

    old "Skip"
    new "geç"

    old "Unseen Text"
    new "görülmemiş metin"

    old "After Choices"
    new "seçimlerden sonra"

    old "Transitions"
    new "geçişler"

    old "Text Speed"
    new "metin hızı"

    old "Auto-Forward Time"
    new "otomatik ilerleme"

    old "Music Volume"
    new "müzik"

    old "Sound Volume"
    new "ses"

    old "Voice Volume"
    new "konuşma"

    old "Mute All"
    new "tümünü sustur"

    old "Test"
    new "dene"

    # ── Erişilebilirlik (ui.rpy'deki preferences ekranı) ─────────────────
    old "Accessibility"
    new "erişilebilirlik"

    old "Scanlines"
    new "tarama çizgileri"

    old "Flashes and Shake"
    new "parazit ve sarsıntı"

    old "Flashes and shake off: the sound and the pause stay, only the screen keeps still."
    new "Parazit ve sarsıntı kapalıyken ses de bekleme de yerinde kalır; yalnız ekran sakinleşir."

    # ── Gezinti / diğer ──────────────────────────────────────────────────
    old "Start"
    new "başla"

    old "Main Menu"
    new "ana menü"

    old "Return"
    new "geri dön"

    old "About"
    new "hakkında"

    old "Help"
    new "yardım"

    old "Quit"
    new "çık"

    old "End Replay"
    new "tekrarı bitir"

    old "Back"
    new "geri"

    old "Auto"
    new "oto"

    old "Menu"
    new "menü"

    old "Skipping"
    new "geçiliyor"

    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "Yükleme, kaydedilmemiş ilerlemeyi siler.\nEmin misin?"