# scene7_inis.rpy — Pieces of Mind
# Sahne 7: İniş ve Yarım.
# Kuleden iniş (ultimatomun ağırlığı), lamba salonundan ikinci geçiş
# (Sönmüş'ün lambası — ihanet ödemesi zarsız), ve kapıda Yarım:
# taşıyıcısının adını kendine almış, kovulmuş bir fısıltı (Gasp aynası).
# Kılıç ödemesi: GÜÇ savaşı (marj = hasar, Yarım'ın canı 10), kılıçla DC 11 /
# kılıçsız DC 15 (tasarım niyeti; DC şu an sabit 10). Doğal 1 ölüm; ıska CAN -3.
# Çalınan isim asla duyulmaz/gösterilmez (isim kuralı biçime uygulanır).
# Sonu: kapı başladıkları odaya çıkar + "Uyuma." kancası (Sahne 8 kurulumu).

# Yarım — çalıntı bedendeki fısıltı. Yanlış bir et rengi: ne kırmızı ne krem.
define yr = Character("Yarım", color="#a05a5a", what_color="#a05a5a",
                      ctc="ctc_blink", ctc_position="nestled")

# Yarım'a "nasıl aldın" sorusu soruldu mu? (menü tekrarı için)
default sahne7_soruldu = False

# Dövüş durumu: Yarım'ın canı ve tur sayacı (savaş döngüsü).
default yarim_can = 10
default dovus_tur = 0

# Yarım öldü mü? (yalnızca doğal 20 öldürür — diğer yollarda sağ ve bekliyor)
default yarim_oldu = False


################################################################################
## İniş
################################################################################

label sahne7_inis:

    scene bg_kule_merdiven with sahne_gecis

    si "İniyoruz."

    si "Çıkarken saymayı bırakmıştım. İnerken de bırakıyorum."

    s "Tutarlılık iyidir."

    si "Basamaklar aynı değil. Çıkarken düzdüler. Şimdi... eğik."

    s "Kule bizi aynı yoldan bırakmıyor."

    if kule_kani:

        si "Ve basamaklar ayaklarıma yapışıyor sanki. Bir saniyelik bir isteksizlikle."

        s "Kule tadımı biliyor. Bırakmak istemiyor."

    if zihin_izi:

        si "Kafamın içinde, altın parmağın gezdiği raflar... kaşınıyor."

        s "Gitti. Ama parmak izi kaldı. Hâlâ orada."

    s "Ya adı... ya kendini. Öyle dedi."

    s "Kendini verirsen bana ne olur?"

    $ fis("...")

    s "Sönmüş'e ne olduysa o. Değil mi?"

    $ fis("Yürü.")

    if alevdeki_ses:

        # Doğal 20 direniş yolunda: alevin içindeki kadın sesi.
        s "Bir şey daha var."

        s "Alevin içinde biri vardı. Bir kadın. Beni çağırıyordu."

        s "Sen de duydun mu?"

        # Yalan da sessizlik de kurtarıcı değil.
        menu:

            "«Duymadım.»":

                si "Cevap hızlı geldi. Yine."

                s "Duymadın demek."

                $ guven_degistir(-1)

            "«...»":

                s "Susuyorsun."

                s "Son zamanlarda hep yanlış yerlerde susuyorsun."

                $ stres_degistir(1)

    jump sahne7_salon_donus


################################################################################
## Salondan İkinci Geçiş — Sönmüş'ün Lambası
################################################################################

label sahne7_salon_donus:

    scene bg_lamba_salonu with sahne_gecis

    si "Salon. Binlerce oyuk, binlerce sönmüş lamba."

    si "Ama bir şey değişmiş."

    si "Alt sırada, daha önce boş olan bir oyukta: yeni bir lamba."

    si "Camı çatlak. İçi karanlık. Dokunuyorum — taşı hâlâ sıcak."

    s "Bunu tanıyorum. Bu onun lambası."

    s "Sönmüş'ün."

    if sahne6_ihanet:

        # İhanetin ödemesi — zarsız, telafisiz (Tasarım İlkesi 7).
        s "Kule onu topladı. İzini verdiğin gece."

        s "Onu sen verdin."

        s "Ve ben seyrettim."

        $ fis("...")

        s "Sus. Artık susman daha iyi."

        $ guven_degistir(-1)
        $ stres_degistir(2)

    else:

        s "Buraya kendi mi geldi? Yoksa kule mi getirdi?"

        $ fis("Alevler kulede daha yavaş ölür.")

        s "Ama ölür."

        $ fis("Ama ölür.")

        $ stres_degistir(1)

    si "Kendi oyuğumun önünden geçiyorum. Levha. Çizikler."

    si "Ve halka... parlatılmış. Yeni cilalanmış gibi."

    s "Beni bekliyorlar."

    $ stres_degistir(1)

    jump sahne7_kapi_esik


################################################################################
## Kapı Eşiği — Yarım
################################################################################

label sahne7_kapi_esik:

    scene bg_zindan_kapisi with sahne_gecis

    si "Merdivenin dibi. Kulenin ağzı: ağır, demir kuşaklı bir kapı."

    si "Koro'nun dediği kapı bu olmalı."

    s "Ve önünde biri var."

    si "Işığımın çemberinin tam sınırında. Bir adım içeride, bir adım dışarıda."

    si "Bir adam. Neredeyse."

    si "Duruşu yanlış. Eklemler doğru yerde ama... sonradan öğrenilmiş gibi."

    s "Koridordaki. Takipçi. Sen misin?"

    yr "Işık."

    yr "Işığı indir. Konuşalım."

    $ fis("İndirme.")

    si "İndirmiyorum."

    yr "Peki. Peki. Işıklı konuşuruz."

    si "Gülümsüyor. Dişleri doğru sayıda. Yine de yanlış."

    $ stres_degistir(1)

    jump sahne7_tanisma


label sahne7_tanisma:

    si "Başını yana eğiyor. Bana değil — içime bakıyor."

    yr "Sen. İçindeki."

    yr "Seni tanıyorum. Türünü tanıyorum."

    yr "Ben de senin gibiydim. Fısıltıydım. Kiracıydım."

    yr "Artık değilim."

    s "Nesin peki?"

    yr "Ev sahibi."

    si "Kendi göğsünü gösteriyor. Gururla. Çalınmış bir ceket gösterir gibi."

    yr "Adım var. Adım. VAR."

    si "Ve söylüyor."

    si "Bir isim söylüyor. Duyuyorum — ve aynı anda unutuyorum."

    si "İsim ağzında durmuyor. Çünkü ona ait değil."

    s "Adını taşıyamıyorsun bile."

    yr "Taşıyorum. TAŞIYORUM."

    si "Sesi bir an çatallanıyor: altında başka bir ses, çok derinden. Ağlıyor olabilir."

    $ stres_degistir(1)

    jump sahne7_teklif


label sahne7_teklif:

    si "Bir adım yaklaşıyor. Işığın sınırı derisinde cızırdıyor. Aldırmıyor."

    yr "Dinle, içindeki. Kardeşim. Dinle."

    yr "Koro sana ne dedi? Ya adı... ya kendini. Değil mi? Hep aynı şarkı."

    yr "Üçüncü yol var."

    yr "Adı Koro'ya verme. {b}Kendine al.{/b}"

    yr "Beden zaten senin. Hep senindi. Ben aldım — özgürüm."

    si "Özgür diyor. Kulenin kapısında bekleyen, ışığın almadığı, adı ağzından dökülen şey."

    s "İçimdeki... onu dinliyor musun?"

    # Oyuncuya doğrudan yapılan teklif — cevap oyuncunun.
    menu:

        "«Hayır.»":

            si "Kafamın içi kararlı bir sessizlik."

            s "Güzel."

            yr "Yalan söylüyor. Hepimiz yalan söyleriz. İşimiz bu."

            s "Olabilir."

            s "Ama benimki senin önünde \"hayır\" dedi. Sen diyemedin."

            # Teklif yüzüne yapıldı; reddin tanığı şövalye.
            $ guven_degistir(1)

        "«...»":

            s "Cevap vermiyorsun."

            s "Cevap vermeni isterdim."

            yr "Susuyor, bak. Düşünüyor demek."

            $ stres_degistir(1)

        "«Nasıl?»":

            si "Kafamın içinde tek kelime. Merakla, sessizce:"

            s "..."

            s "\"Nasıl\" mı?"

            s "Bunu mu soruyorsun? {b}Nasıl mı?{/b}"

            yr "İşte. İşte bu."

            si "Yarım'ın gülümsemesi genişliyor. Fazla genişliyor."

            $ guven_degistir(-2)
            $ stres_degistir(1)

    jump sahne7_yuzlesme_secim


label sahne7_yuzlesme_secim:

    si "Yarım bir adım daha atıyor. Işık derisini yakıyor; umursamıyor."

    yr "Kapı açılmayacak, ben burada durdukça."

    yr "Konuşalım. Uzun uzun konuşalım."

    menu:

        "«Kılıcı çek.»" if kilic_var:
            jump sahne7_dovus

        "«Üstüne yürü. Çıplak elle.»" if not kilic_var:
            jump sahne7_dovus

        "«Lambayı kaldır. Işığı gözlerine tut.»":
            jump sahne7_isik

        "«Sor: adı nasıl aldın?»" if not sahne7_soruldu:
            jump sahne7_sor


################################################################################
## Soru — UYUMA'nın gölgesi
################################################################################

label sahne7_sor:

    $ sahne7_soruldu = True

    s "Adı nasıl aldın?"

    si "Yarım'ın yüzü yumuşuyor. Anı güzelmiş gibi."

    yr "Kolayca."

    yr "O uyuyordu."

    yr "Hepsi uyurken verir. Uyanıkken sıkı tutarlar. Ama uykuda..."

    yr "Uykuda ellerini açarlar."

    si "Lambamın tabanındaki kazıma. UYUMA."

    s "Bunu bilen biri yazmış demek."

    yr "Bilen biri. Evet. Bilenler yazar."

    si "Konuşurken iki adım daha yaklaşmış. Fark etmemişim."

    $ stres_degistir(1)

    jump sahne7_yuzlesme_secim


################################################################################
## Işık Yolu — zarsız, bedelli
################################################################################

label sahne7_isik:

    si "Lambayı kaldırıyorum. Göz hizasına. Onun gözlerinin hizasına."

    si "Ve camın küçük kapağını açıyorum."

    s "Işık istedin. Al."

    si "Alev, çıplak, kırmızı, dosdoğru yüzüne vuruyor."

    yr "HAYIR—"

    si "Derisi ışığın altında kâğıt gibi. Bedenin gerçek sahibi neredeyse görünüyor — bir an, altında, hâlâ orada."

    si "Yarım çığlık atıyor. İki ses birden: çalan ve çalınan."

    call glitch_burst(0.5, 1.3)

    si "Ve karanlığa savruluyor. Kapının önü boş."

    si "Kapağı kapatıyorum. Alev..."

    if alev_kucuk:

        si "Alev zaten küçüktü. Şimdi bir nefes daha küçük."

        s "Dünya bir nefes daha dar."

        $ stres_degistir(2)

    else:

        si "Alev eski boyunda değil artık."

        $ alev_kucuk = True

        centered "{color=#cc2222}ALEV KÜÇÜLDÜ{/color}"

    $ fis("Harcadın.")

    s "Kurtardım. Farklı şeyler."

    s "Hem sen fısıldadın. Işığı tut, dedin. Kendi hazineni bana harcadın."

    si "Cevap yok. Kafamın içinde, kendi sözüne kızan bir sessizlik."

    s "Beni alevden pahalı tuttun demek. Bunu bir yere yazıyorum, içimdeki."

    # Fısıltı en değer verdiğini (ışığı) bedene harcadı — şövalye gördü.
    # Bedel zaten ödendi: alev küçüldü (İlke 3 — kazanım bedava değil).
    $ guven_degistir(1)

    jump sahne7_kapi_acilis


################################################################################
## Dövüş — GÜÇ savaşı (marj = hasar; Yarım'ın canı 10)
################################################################################

label sahne7_dovus:

    if kilic_var:

        si "Kılıç kınsız, pas içinde, kör."

        si "Ama elimde doğru duruyor. Yıllardır ilk kez bir şey doğru duruyor."

        s "Çekil. Son söz."

        yr "Sözler. Hep sözler. Bedenler daha dürüst."

        si "Üstüme geliyor."

    else:

        si "Elim boş. Yumruklarımı sıkıyorum."

        s "Çekil. Son söz."

        yr "Silahsız. Fısıltın sana kılıç bile bulamadı mı?"

        si "Üstüme geliyor."

    $ yarim_can = 10
    $ dovus_tur = 0

    jump sahne7_dovus_tur


label sahne7_dovus_tur:

    $ dovus_tur += 1

    if dovus_tur > 1:

        if dovus_tur % 2 == 0:

            si "Yarım toparlanıyor. Yeniden geliyor — daha alçak, daha hızlı."

        else:

            si "Dönüyor. Gülümseme gitti; geriye sadece açlık kaldı."

    # --- GÜÇ zarı (savaş: hasar tabanının üstündeki her puan = hasar) ---
    # İşaretli takas (dc_serbest): kılıçla DC 11 / çıplak elle DC 15.
    # Çıplak elin hasar tabanı 10'da bırakılır — yoksa hem zor hem düşük
    # hasarlı olur, bu takas değil ölüm sarmalı olurdu.
    #   Kılıç      : ~%60 isabet, ~4-5 hasar — istikrarlı.
    #   Çıplak el  : ~%40 isabet, ~7-8 hasar — nadir ve belirleyici.
    if kilic_var:
        call roll_dice("GUC", 11, savas=True, dc_serbest=True)
    else:
        call roll_dice("GUC", 15, savas=True, dc_serbest=True, hasar_dc=10)
    $ sonuc = _return

    if sonuc.crit_success:

        jump sahne7_dovus_krit_basari

    elif sonuc.crit_fail:

        jump sahne7_dovus_krit_fiyasko

    elif sonuc.success:

        $ yarim_can -= sonuc.hasar

        if yarim_can <= 0:
            jump sahne7_dovus_basari

        if sonuc.hasar == 0:

            si "Hamlem değiyor — ama sıyırıyor. Derisinden kâğıt gibi bir parça, o kadar."

        elif kilic_var:

            si "Kör kılıç etine gömülüyor. İçinden kan yerine toz dökülüyor."

        else:

            si "Yumruğum göğsüne oturuyor. İçinde bir şey çatırdıyor. Boş bir şey."

        si "Yarım sendeliyor. Ama düşmüyor."

        yr "Daha. DAHA."

        jump sahne7_dovus_tur

    else:

        # Iska — Yarım'ın pençeleri bedelini alır: CAN -3.
        si "Hamlem boşa gidiyor. Ve pençe gibi parmaklar açığımı buluyor."

        si "Et yırtılıyor. Sıcak bir çizgi, omzumdan dirseğime."

        call can_hasar(3, "yarım olanın pençeleri")

        $ stres_degistir(1)

        jump sahne7_dovus_tur


label sahne7_dovus_krit_basari:

    # Doğal 20 — temiz son; çalınan ad düşer, altından huzur çıkar.
    if kilic_var:

        si "Kör kılıç, doğru elde keskinleşiyor."

        si "Tek hamle. Omuzdan göğse."

    else:

        si "İlk hamlesini yakalıyorum. Bileğini büküyorum, dizimi göğsüne."

    si "Yarım taşa yığılıyor."

    si "İçinden hiçbir şey dökülmüyor. İçi yok."

    yr "Adım..."

    yr "Adımı... düşürdüm..."

    si "Ve isim onu bırakıyor. Nasıl olduğunu göremiyorum ama hissediyorum: oda bir an hafifliyor."

    si "Yerde artık bir adam yatıyor. Sadece bir adam. Yüzü... rahat."

    $ yarim_oldu = True

    s "Sonunda uyuyabildi."

    jump sahne7_kapi_acilis


label sahne7_dovus_basari:

    # Yarım'ın canı bitti — geri sürülür; ama döngünün dışında: hatırlıyor.
    si "Son vuruş. İçindeki boşluk, dışındaki bedeni artık taşıyamıyor."

    si "Yarım geriliyor, iki büklüm, karanlığa doğru."

    yr "Peki. Peki."

    yr "Ben beklerim. Beklemekte iyiyim."

    yr "Seni önceki yüzünle de görmüştüm. Sonrakiyle de görürüm."

    si "Karanlık onu alıyor."

    s "\"Önceki yüzüm\"?"

    s "Ne demek istedi?"

    $ fis("Hiçbir şey. Yürü.")

    $ stres_degistir(1)

    jump sahne7_kapi_acilis


label sahne7_dovus_krit_fiyasko:

    # Doğal 1 — Yarım sarılır: yarımlığını tamamlamak ister.
    si "Hamlem boşa düşüyor. Taş kaygan — hayır. Taş kaygan değil."

    si "Ayaklarım. Ayaklarım yine benim değil."

    yr "İşte."

    si "Kollarını açıyor. Ve sarılıyor."

    si "Soğuk değil. Daha kötüsü: eksik. Yarım bir şeyin içine çekiliyorum."

    yr "Tamamla beni."

    # Fısıltı'nın çığlığı — oyuncu tıklamak zorunda.
    $ fis("Onu ALAMAZSIN—")

    call olum("yarım olan, senin yarınla tamamlandı")


################################################################################
## Kapının Ardı — Oda
################################################################################

label sahne7_kapi_acilis:

    si "Kapının önü boş. Ayaktayım. İkisi de mucize."

    # Yarım'la yüzleşme atlatıldı (dövüş ya da ışık) — yükselme (upgrade.rpy).
    call yukselme

    si "Kapıya dönüyorum. Demir kuşaklar, ağır ahşap."

    si "Omuzluyorum. Direnmiyor. Sanki bekliyormuş."

    s "Dışarısı. Sonunda dışarısı."

    si "Ve öteki taraf..."

    scene bg_sovalye_odasi with sahne_gecis

    si "Taş duvarlar."

    si "Bir yatak."

    si "Bir masa — üstünde boş, tozsuz bir halka."

    s "Hayır."

    s "Hayır, hayır, hayır."

    s "Burası başladığımız oda."

    $ stres_degistir(2)

    s "Baştan beri biliyordun. Kapının buraya çıktığını."

    $ fis("Evet.")

    s "Başka çıkış var mı?"

    $ fis("Hayır.")

    si "Aynı iki kelime. Kulenin dibinde de böyle konuşmuştuk."

    si "Dünya küçük. Oda, koridor, kule. Işığımın değdiği kadar."

    jump sahne7_son


label sahne7_son:

    si "Ve ayna."

    si "Aynaya bakıyorum ve ayna artık odayı göstermiyor."

    si "Sadece bir anahtar deliği. Kapkara, göz hizasında, havada asılı."

    s "Bacaklarım ağır. Gözkapaklarım daha ağır."

    s "Ne kadar zamandır uyumadım ben?"

    si "Yatak köşede. Sıradan, çökük, gri bir yatak."

    si "Hayatımda hiçbir şeyi bu kadar istememiştim."

    $ fis("Uyuma.")

    s "...ne?"

    $ fis("Sakın uyuma.")

    # Ton guven'e göre — gösterge yok, ilişki sesle sezdirilir (tek gösterge bu).
    if guven >= 5:

        s "Sebep söylemeyeceksin. Biliyorum."

        s "Ama sesin... benim için korkan bir ses bu. İlk defa duyuyorum."

        s "Peki, içimdeki. Uyumam."

    elif guven <= 2:

        s "Yine emir. Yine sebepsiz."

        s "Ne sakladığını bilmiyorum. Ama bir şey sakladığını biliyorum."

        s "Uyumayacağım. Senin için değil. Sırf ne saklıyorsun diye."

        $ stres_degistir(1)

    else:

        s "Sebep yok, değil mi? Senden hiç sebep gelmez."

        s "Peki. Şimdilik peki."

    # Sahne 8: Uyku ve Ayna (scene8_ayna.rpy)
    jump sahne8_oda
