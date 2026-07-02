# scene5_kule.rpy — Pieces of Mind
# Sahne 5: Kule — Lamba Salonu.
# Merdiven (takipçi anı, kilic_var'a duyarlı), binlerce oyuklu salon
# (alev_kucuk'e duyarlı), şövalyenin kendi oyuğu ve kazınmış isim levhası.
# INT zarı DC 13. İsim verilmez; başarıda tek harf açılır (knight_name "E───").
# Görsel yok: sahne karanlıkta geçer (kule görselleri beklemede).

# Kritik fiyasko: kan levhaya değdi, kule şövalyeyi "tattı". İleride sonuç.
default kule_kani = False


################################################################################
## Merdiven
################################################################################

label sahne5_kule:

    si "Merdiven geniş. Basamakların ortaları çukur — aşınmış."

    s "Kaç ayak eskitir taşı bu kadar?"

    si "Çıkıyorum. Yüz basamak. İki yüz. Saymayı bırakıyorum."

    si "Lambanın ışığı hep önümde. Hep üç basamak yukarıda."

    s "Sanki yol gösteriyor. Sanki acele ediyor."

    si "Ve aşağıda, derinlerde: bir basamak gıcırdıyor."

    s "Ben gıcırdatmadım."

    if kilic_var:

        si "Elim kabzaya gidiyor. Pas, avucuma güven gibi oturuyor."

        s "Gel o zaman. Işığın içine gel."

        si "Ses kesiliyor. Gelmiyor."

    else:

        si "Elim kalçamı yokluyor. Orada olmayan bir kılıcı arıyor."

        si "Adımlarımı hızlandırıyorum."

    f "O içeri giremez. Kule onu tanımıyor."

    s "Ama beni tanıyor, öyle mi?"

    f "..."

    jump sahne5_salon


################################################################################
## Lamba Salonu
################################################################################

label sahne5_salon:

    si "Merdiven bir salona açılıyor."

    si "Işığım duvarlara değiyor ve duvarlar... bitmiyor."

    si "Oyuklar. Duvarlar boydan boya oyuk dolu. Yüzlerce. Binlerce."

    si "Her oyukta bir lamba."

    s "Hepsi sönmüş."

    si "Hayır — hepsi değil. Yukarıda, tek tük: kısık kırmızı alevler."

    s "Benimki gibi."

    if alev_kucuk:

        si "Lambam elimde titriyor. Sönmüşlere doğru eğilir gibi."

        s "Sanki katılmak istiyor onlara."

    f "Yürü. Bakma onlara."

    s "Bunlar... kim?"

    f "Kimse. Artık kimse."

    s "Sönmüş de böyle diyordu kendine."

    jump sahne5_oyuk


################################################################################
## Oyuk — Kazınmış İsim
################################################################################

label sahne5_oyuk:

    si "Sonra görüyorum. Görmemem imkânsız."

    si "Göz hizamda, boş bir oyuk. İçindeki halka... tanıdık."

    si "Lambamı kaldırıyorum. Halkaya tutuyorum. Tam oturuyor."

    s "Bu oyuk benim."

    si "Lambayı geri alıyorum. Hemen. Halka bırakmak istemiyor gibi."

    si "Oyuğun altında bir levha var. Üzerine bir isim kazınmıştı — bir zamanlar."

    si "Şimdi üstü derin, kararlı çiziklerle örtülü. Okunmuyor."

    s "Adım. Bu benim adımdı."

    f "Oku."

    s "Okunmuyor. Biri kazımış."

    f "Dene."

    menu:
        f "Ne fısıldayacaksın?"

        "«İncele. Çizikleri parmaklarınla oku.»":
            jump sahne5_incele

        "«Bakma. Uzaklaş buradan.»":
            jump sahne5_bakma


################################################################################
## Dal A — İnceleme (INT / ZİHİN zarı)
################################################################################

label sahne5_incele:

    if isim_uyarisi:

        # Sönmüş'ün uyarısını duyanlar korunmayı bilir.
        s "Sönmüşün sesi kulağımda: {i}Bulduğunda ona söyleme.{/i}"

        s "İçimden okuyacağım. Sadece içimden."

    si "Parmaklarımı levhaya koyuyorum. Çizikler soğuk."

    # --- INT zarı — DC 13 ---
    call roll_dice("INT", 13)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne5_incele_krit_basari
    elif sonuc.crit_fail:
        jump sahne5_incele_krit_fiyasko
    elif sonuc.success:
        jump sahne5_incele_basari
    else:
        jump sahne5_incele_basarisiz


label sahne5_incele_krit_basari:

    # Doğal 20 — çizikler kendi eli. Adını kendinden kendisi saklamış.
    si "Parmaklarım çizikleri izliyor. Derinler. Aceleyle atılmamışlar."

    s "Tek tek. Bastıra bastıra. Sabırla kazınmış."

    s "Ve bu izleri tanıyorum."

    s "Bu el... {b}benim elim.{/b}"

    s "Adımı kendimden ben sakladım."

    f "..."

    f "Akıllıymışsın."

    s "\"Mışsın\"? Geçmiş zaman?"

    f "Yürü."

    si "Levhanın bir köşesi çiziklerden kaçmış. Tek harf sağlam: E."

    $ knight_name = "E───"

    jump sahne5_son


label sahne5_incele_basari:

    # Başarı — kazıma bilinçli ve koruyucu; tek harf okunur.
    si "Çizikler bıçakla atılmış. Düzenli. Bilinçli."

    s "Kim kazıdıysa... yok etmek için değil. {i}Korumak{/i} için kazımış."

    si "Ve levhanın köşesinde, çiziklerin ıskaladığı tek harf: E."

    $ knight_name = "E───"

    f "E."

    s "Sakın."

    f "Ne?"

    s "Adımı ağzına alma."

    f "..."

    jump sahne5_son


label sahne5_incele_basarisiz:

    # Başarısızlık — sadece oluklar.
    si "Parmaklarım olukların içinde dolaşıyor. Bir şey aramıyorlar artık; kayboluyorlar."

    s "Hiçbir şey. Sadece taş ve öfke."

    si "Şakaklarım zonkluyor. Gözlerimin arkasında bir yerde."

    f "Yeter. Zaman kaybı."

    s "Neden bu kadar acelecisin?"

    f "Neden bu kadar yavaşsın?"

    jump sahne5_son


label sahne5_incele_krit_fiyasko:

    # Doğal 1 — kan levhaya değer; kule tadar.
    # (roll_dice doğal 1'de otomatik glitch atar; devamı buraya düşer.)

    si "Levhanın keskin bir kıyısı parmağımı ısırıyor."

    s "Küçük bir kesik. Önemsiz."

    si "Bir damla kan, çiziklerin içine yürüyor. Taş, kanı içiyor."

    call glitch_burst(0.5, 1.3)

    si "Salondaki bütün lambalar — binlercesi — bir an için yanıyor."

    si "Ve sönüyor. Hep birlikte. Bir iç çekiş gibi."

    s "Kule beni tattı."

    f "Gitmemiz gerek. Hemen."

    s "Sesin... titriyor mu senin?"

    f "{b}Hemen.{/b}"

    $ kule_kani = True

    jump sahne5_son


################################################################################
## Dal B — Bakmamak (isyan: Fısıltı okumak istiyor, oyuncu uzaklaşıyor)
################################################################################

label sahne5_bakma:

    $ isyan += 1

    s "Hayır."

    f "Ne?"

    s "Bilmek istemiyorum. Henüz değil."

    f "Dön. Oku. {b}OKU.{/b}"

    call glitch_burst(0.3, 1.0)

    si "Ayaklarım duruyor."

    si "Ben durdurmadım."

    s "Ayaklarım. {b}Benim{/b} ayaklarım."

    si "Bir nefes. İki. Ayaklarım yeniden benim."

    si "Yürüyorum."

    f "..."

    si "Sessizlik. Ama küskün bir sessizlik değil. Hesap yapan bir sessizlik."

    jump sahne5_son


################################################################################
## Sahne Sonu — Altın Işık
################################################################################

label sahne5_son:

    si "Salonun ortasından merdiven devam ediyor. Spiral. Yukarı."

    si "Ve çok yukarıda — bir ışık."

    s "Kırmızı değil."

    s "Altın. Güneş gibi. Oyukların hiçbirine benzemiyor."

    f "Yukarı."

    s "İlk defa hevesli görünüyorsun."

    f "Yukarı."

    centered "{color=#cc2222}— devam edecek —{/color}"

    return
