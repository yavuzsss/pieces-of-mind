# stats.rpy — Pieces of Mind
# Stat sistemi (GÜÇ, ZEKÂ, ŞANS + CAN) ve D20 zar mekanizması.
# Kural: D20 + stat puanı vs. DC. Doğal 20 = kritik başarı, doğal 1 = kritik
# başarısızlık. Statlar 0'dan başlar ve yükselmelerle büyür (upgrade.rpy);
# bonus = stat puanının kendisi (D&D formülü YOK — kullanıcı kararı 2026-07-11).
#
# CAN: 20 ile başlar. Bedeller ve düşman vuruşları can götürür (can_hasar
# etiketi); can 0'a inerse permadeath (death.rpy). Yükselmede CAN +2
# (tavan da +2 büyür).
#
# HASAR (savaş): başarılı GÜÇ zarında DC'nin üstündeki her puan düşmana
# hasardır. Ör: DC 10'a karşı toplam 15 → 5 hasar. (RollResult.hasar)

init -10 python:

    class RollResult(object):
        """Tek bir zar atışının sonucunu taşır (UI'da göstermek için)."""

        def __init__(self, stat_name, die, bonus, dc, hasar_dc=None):
            self.stat_name = stat_name      # Hangi statla atıldı ("GUC" vb.)
            self.die = die                  # Zarın kendisi (1-20)
            self.bonus = bonus              # Stat puanı (doğrudan eklenir)
            self.total = die + bonus        # Toplam sonuç
            self.dc = dc                    # Zorluk derecesi
            self.crit_success = (die == 20) # Doğal 20
            self.crit_fail = (die == 1)     # Doğal 1
            self.savas = False              # roll_dice(savas=True) doldurur
            # Kritikler bonustan bağımsız olarak sonucu belirler.
            if self.crit_success:
                self.success = True
            elif self.crit_fail:
                self.success = False
            else:
                self.success = self.total >= dc
            # Savaş hasarı: hasar tabanının üstündeki her puan.
            # hasar_dc, isabet DC'sinden AYRILABİLİR: yüksek DC'li bir seçenek
            # (ör. kılıçsız dövüş) yoksa hem zor hem düşük hasarlı olurdu —
            # bu bir takas değil, ölüm sarmalı olur.
            _hdc = dc if hasar_dc is None else hasar_dc
            self.hasar = max(0, self.total - _hdc) if self.success else 0

        def __str__(self):
            return "{} check: d20({}) + {} = {} vs DC {} -> {}".format(
                self.stat_name, self.die, self.bonus, self.total, self.dc,
                "CRIT!" if self.crit_success else
                "FUMBLE!" if self.crit_fail else
                ("Success" if self.success else "Failure"))


    class PlayerStats(object):
        """Yorgun Şövalye'nin statları, canı ve zar mekanizması."""

        STAT_NAMES = ("GUC", "ZEKA", "SANS")

        def __init__(self, guc=0, zeka=0, sans=0, can=20):
            self.stats = {
                "GUC": guc,
                "ZEKA": zeka,
                "SANS": sans,
            }
            self.can = can
            self.can_max = can

        def get(self, stat_name):
            return self.stats[stat_name.upper()]

        def set(self, stat_name, value):
            self.stats[stat_name.upper()] = max(0, min(20, value))

        def modify(self, stat_name, delta):
            """Stat'ı artır/azalt (0-20 aralığına sıkıştırılır)."""
            self.set(stat_name, self.get(stat_name) + delta)

        def bonus(self, stat_name):
            """Bonus = stat puanının kendisi."""
            return self.get(stat_name)

        def can_degistir(self, delta):
            """Canı değiştirir (0..can_max). Ölüm kontrolü can_hasar etiketinde."""
            self.can = max(0, min(self.can_max, self.can + delta))

        def yukselt(self, secim):
            """Yükselme: GUC/ZEKA/SANS +1 ya da CAN +2 (tavanla birlikte)."""
            if secim == "CAN":
                self.can_max += 2
                self.can += 2
            else:
                self.modify(secim, +1)

        def roll(self, stat_name, dc, hasar_dc=None):
            """D20 at, stat puanını ekle, DC ile karşılaştır.

            Sonuç bir RollResult nesnesi olarak döner; ayrıca
            'last_roll' store değişkenine yazılır ki ekranlarda
            (zar animasyonu, sonuç paneli) kullanılabilsin.
            """
            # renpy.random: durumu kayıt/rollback ile birlikte saklanır —
            # geri sarıp yeniden atmak aynı sonucu verir (save-scum engeli).
            die = renpy.random.randint(1, 20)
            result = RollResult(stat_name.upper(), die, self.bonus(stat_name), dc,
                                hasar_dc=hasar_dc)
            store.last_roll = result
            return result

        def check(self, stat_name, dc):
            """Sadece basari/basarisizlik (True/False) dondüren kısayol."""
            return self.roll(stat_name, dc).success


# Oyuncu durumu — save/load ve rollback uyumu için 'default' ile tanımlanır.
default player_stats = PlayerStats()

# Son zar atışının sonucu (UI'da göstermek için).
default last_roll = None


################################################################################
## Can Hasarı — ölüme bağlı
################################################################################

# Kullanım: call can_hasar(3, "yarım olanın pençeleri")
# Can 0'a inerse sebep, ölüm ekranına taşınır (permadeath).
label can_hasar(miktar, sebep="canın tükendi"):

    $ player_stats.can_degistir(-miktar)

    centered "{color=#cc2222}CAN -[miktar]{/color}\n{color=#b8ac93}kalan: [player_stats.can]{/color}"

    if player_stats.can <= 0:
        call olum(sebep)

    return


# --- Kullanım örneği (script.rpy içinden) ---------------------------------
#
#   call roll_dice("GUC", 10)              # görsel panel (dice.rpy)
#   $ sonuc = _return
#   if sonuc.success:
#       $ dusman_can -= sonuc.hasar        # savaşta: marj = hasar
#
# Can ve yükselme:
#
#   call can_hasar(3, "uçurumun dişleri")  # can biterse ölüm
#   call yukselme                          # stat seçim paneli (upgrade.rpy)
# ---------------------------------------------------------------------------
