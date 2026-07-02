# stats.rpy — Pieces of Mind
# Stat sistemi (STR, DEX, INT, CHA) ve D20 zar mekanizması.
# Kural: D20 + stat bonusu vs. DC. Doğal 20 = kritik başarı, doğal 1 = kritik başarısızlık.

init -10 python:

    class RollResult(object):
        """Tek bir zar atışının sonucunu taşır (UI'da göstermek için)."""

        def __init__(self, stat_name, die, bonus, dc):
            self.stat_name = stat_name      # Hangi statla atıldı ("STR" vb.)
            self.die = die                  # Zarın kendisi (1-20)
            self.bonus = bonus              # Stat bonusu
            self.total = die + bonus        # Toplam sonuç
            self.dc = dc                    # Zorluk derecesi
            self.crit_success = (die == 20) # Doğal 20
            self.crit_fail = (die == 1)     # Doğal 1
            # Kritikler bonustan bağımsız olarak sonucu belirler.
            if self.crit_success:
                self.success = True
            elif self.crit_fail:
                self.success = False
            else:
                self.success = self.total >= dc

        def __str__(self):
            return "{} check: d20({}) + {} = {} vs DC {} -> {}".format(
                self.stat_name, self.die, self.bonus, self.total, self.dc,
                "CRIT!" if self.crit_success else
                "FUMBLE!" if self.crit_fail else
                ("Success" if self.success else "Failure"))


    class PlayerStats(object):
        """Yorgun Şövalye'nin zihinsel/fiziksel statları ve zar mekanizması."""

        STAT_NAMES = ("STR", "DEX", "INT", "CHA")

        def __init__(self, str_=10, dex=10, int_=10, cha=10):
            self.stats = {
                "STR": str_,
                "DEX": dex,
                "INT": int_,
                "CHA": cha,
            }

        def get(self, stat_name):
            return self.stats[stat_name.upper()]

        def set(self, stat_name, value):
            self.stats[stat_name.upper()] = max(1, min(20, value))

        def modify(self, stat_name, delta):
            """Stat'ı artır/azalt (1-20 aralığına sıkıştırılır)."""
            self.set(stat_name, self.get(stat_name) + delta)

        def bonus(self, stat_name):
            """D&D usulü bonus: (stat - 10) // 2"""
            return (self.get(stat_name) - 10) // 2

        def roll(self, stat_name, dc):
            """D20 at, stat bonusunu ekle, DC ile karşılaştır.

            Sonuç bir RollResult nesnesi olarak döner; ayrıca
            'last_roll' store değişkenine yazılır ki ekranlarda
            (zar animasyonu, sonuç paneli) kullanılabilsin.
            """
            # renpy.random: durumu kayıt/rollback ile birlikte saklanır —
            # geri sarıp yeniden atmak aynı sonucu verir (save-scum engeli).
            die = renpy.random.randint(1, 20)
            result = RollResult(stat_name.upper(), die, self.bonus(stat_name), dc)
            store.last_roll = result
            return result

        def check(self, stat_name, dc):
            """Sadece basari/basarisizlik (True/False) dondüren kısayol."""
            return self.roll(stat_name, dc).success


# Oyuncu durumu — save/load ve rollback uyumu için 'default' ile tanımlanır.
default player_stats = PlayerStats()

# Son zar atışının sonucu (UI'da göstermek için).
default last_roll = None


# --- Kullanım örneği (script.rpy içinden) ---------------------------------
#
#   if player_stats.check("STR", 15):
#       "Kapı gıcırdayarak açılıyor."
#   else:
#       "Kapı kımıldamıyor bile."
#
# Detaylı sonuç gerekiyorsa:
#
#   $ sonuc = player_stats.roll("CHA", 12)
#   "[sonuc]"          # ör: CHA check: d20(14) + 0 = 14 vs DC 12 -> Success
#   if sonuc.crit_fail:
#       jump kotu_son
#
# Stat değiştirme:
#
#   $ player_stats.modify("INT", +1)
# ---------------------------------------------------------------------------
