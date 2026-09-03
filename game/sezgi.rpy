# sezgi.rpy — Pieces of Mind
# STATLAR NE GÖRDÜĞÜNÜ DEĞİŞTİRİR (2026-09-03)
#
# Sorun: GÜÇ/ZEKÂ/ŞANS yalnız "zarı geçtin mi" sorusunu etkiliyordu. Yüksek
# ZEKÂ ile oynamak düşük ZEKÂ ile oynamakla AYNI oyunu veriyordu — sadece
# bazı kapılar açılıyor/kapanıyordu. Farklı yükselme seçimleri farklı
# oyunlar üretmiyordu.
#
# Çözüm: eşiği tutan statlar ZAR ATMADAN ekstra algı katmanı açar.
#   ZEKÂ — bağlantı kurar: çentikleri, tutarsızlıkları, ikinci kazımayı görür.
#   GÜÇ  — beden hatırlar: kasların bildiği ama aklın bilmediği şeyler.
#   ŞANS — tuhaf tesadüfler: olmaması gereken denk gelişleri fark eder.
#
# Kullanım (senaryoda):
#   if zeka_gorur(2):
#       si "..."
#
# Kural: bu katmanlar ÖDÜLDÜR, zorunluluk değil. Hiçbiri olmadan da sahne
# tamdır; hiçbiri bir kapıyı açmaz. Yalnız görüşü derinleştirir (İlke 8 —
# gördüğünü oyuncu birleştirir). İkisi bunun istisnası: aşağıda işaretli
# iki yerde algı, gerçeğe varışın kanıtına dönüşür.

init -1 python:

    def stat_gorur(stat, esik):
        """Stat eşiği tutuyor mu? Zar YOK — bu bir algı katmanı, kontrol değil."""
        return player_stats.get(stat) >= esik

    def zeka_gorur(esik=1):
        return stat_gorur("ZEKA", esik)

    def guc_gorur(esik=1):
        return stat_gorur("GUC", esik)

    def sans_gorur(esik=1):
        return stat_gorur("SANS", esik)


# Uçurumun kenarındaki çentikler görüldü mü? (ZEKÂ, Sahne 3)
# Sahne 9 bunu zaten SÖYLÜYOR ("Biri burayı defalarca geçmiş") — artık
# dikkatli oyuncu aynı şeyi Perde 1'de KENDİ görebilir.
default centikler_gorundu = False
