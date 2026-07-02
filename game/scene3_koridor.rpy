# scene3_koridor.rpy — Pieces of Mind
# Sahne 3: Kapı ve Koridor.
# Lambanın alınışı (lamba_bagi'ye duyarlı), geride kalan odanın yok oluşu,
# ışık çemberinin dışındaki takipçi, ve ilk ölümcül engel: uçurum geçişi.
# İlk STR zarı. İlk olası ölüm: yalnızca doğal 1 öldürür (call olum);
# normal başarısızlık kalıcı bedel ödetir (KUVVET -1).

# Uçurum geçişinde lamba tek elde miydi? (başarısızlık metnini değiştirir)
default tek_el = False


################################################################################
## Lambanın Alınışı
################################################################################

label sahne3_koridor:

    si "Parmaklarım sapın etrafında kapanıyor."

    if lamba_bagi >= 2:

        s "Sap avucuma oturuyor. Eksik bir uzvum yerine takılmış gibi."

        s "Bu his yanlış. Ama iyi."

    else:

        s "Sap sıcak. Metal, avucumda kalp gibi atıyor."

    si "Lambayı halkasından kaldırıyorum."

    si "Ve oda... nefesini bırakıyor."

    s "Duvarlar uzaklaşmış gibi. Ayna kapkara."

    si "Lambanın ışığı çevremde bir çember çiziyor. Kırmızı, sıcak bir çember."

    s "Çemberin dışında hiçbir şey yok."

    f "Artık kapı var. Sadece kapı."

    jump sahne3_esik


################################################################################
## Eşik
################################################################################

label sahne3_esik:

    # Demir kapı yakın plan.
    scene bg_zindan_kapisi with sahne_gecis

    si "Kapının kolu soğuk."

    si "Çeviriyorum. Kapı sessizce açılıyor. Gıcırdamıyor bile."

    s "Menteşeler yağlı. Biri bu kapıyı kullanıyor."

    # Kapının ötesi: koridor.
    scene bg_zindan_koridoru with sahne_gecis

    si "Ötesi: koridor. Taş. Uzun."

    si "Işığımın çemberi üç adım öteye ulaşıyor. Sonrası siyah."

    f "Yürü."

    si "Eşikten geçiyorum."

    si "Arkamda bir şey kapanıyor. Kapı değil. Daha büyük bir şey."

    si "Dönüp bakıyorum: oda yok. Kapı yok. Duvar bile yok."

    s "Sadece ışığımın ulaşmadığı yer var."

    f "Geriye bakma. Geri diye bir yer yok."

    jump sahne3_yuruyus


################################################################################
## Yürüyüş — Takipçi
################################################################################

label sahne3_yuruyus:

    si "Yürüyorum. Adımlarım taşta yankılanıyor."

    si "Damla sesleri. Uzakta. Düzenli."

    s "Ve... başka bir şey."

    si "Duruyorum."

    si "Yankım bir adım daha atıyor. Sonra susuyor."

    s "Yankılar gecikmez."

    menu:
        f "Ne fısıldayacaksın?"

        "«Dur. Dinle.»":

            si "Nefesimi tutuyorum."

            si "Çemberin hemen dışında: bir sürtünme sesi. Kumaş gibi. Ya da deri."

            s "Işığın kenarında duruyor. İçeri giremiyor."

            s "Giremiyor... değil mi?"

            f "Girmiyor. Şimdilik. Yürü."

        "«Yürü. Sakın arkana bakma.»":

            si "Yürüyorum. Daha hızlı."

            si "Arkamdaki adımlar da hızlanıyor."

            s "Bakmıyorum. Bakmayacağım."

            si "Ense köküm karıncalanıyor. Bakış gibi. Parmak gibi."

    jump sahne3_ucurum


################################################################################
## Uçurum
################################################################################

label sahne3_ucurum:

    # Çökmüş koridor / uçurum.
    scene bg_koridor_tuzak with sahne_gecis

    si "Koridor birden bitiyor."

    s "Zemin yok."

    si "Lambayı kenardan aşağı tutuyorum: hiçbir şey. Işık dibe ulaşmıyor."

    s "Işık her yere ulaşır. Buraya ulaşmıyor."

    si "Karşı kenar dört-beş adım ötede."

    si "Arada, duvar boyunca, bir karış genişliğinde bir çıkıntı."

    s "Geçilebilir. Tek yol bu."

    s "Ama iki elim de lazım olacak. Ve lamba..."

    menu:
        f "Ne fısıldayacaksın?"

        "«Lambayı kemerine as. İki elin de serbest olsun.»":
            jump sahne3_gecis_kemer

        "«Lambayı bırakma. Alev sönmemeli.»":
            jump sahne3_gecis_tekel


label sahne3_gecis_kemer:

    $ tek_el = False

    si "Lambanın sapını kemerime geçiriyorum."

    si "Kalçamda sallanıyor; ışık çemberi ayaklarımın dibinde titriyor."

    s "İki elim serbest. Tamam."

    si "Sırtımı duvara veriyorum. Çıkıntıya adım atıyorum."

    # --- STR zarı — DC 12 ---
    call roll_dice("STR", 12)
    $ sonuc = _return

    jump sahne3_gecis_sonuc


label sahne3_gecis_tekel:

    $ tek_el = True
    $ lamba_bagi += 1

    si "Lambayı sol elime alıyorum. Parmaklarım sapa kilitleniyor."

    s "Alev sönmemeli. Bu her şeyden önemli."

    s "...neden her şeyden önemli?"

    f "Çünkü öyle."

    si "Tek elimle duvardaki çatlakları yokluyorum. Çıkıntıya adım atıyorum."

    # --- STR zarı — DC 15 (tek el: daha zor) ---
    call roll_dice("STR", 15)
    $ sonuc = _return

    jump sahne3_gecis_sonuc


################################################################################
## Geçişin Sonucu
################################################################################

label sahne3_gecis_sonuc:

    if sonuc.crit_success:
        jump sahne3_gecis_krit_basari
    elif sonuc.crit_fail:
        jump sahne3_gecis_krit_fiyasko
    elif sonuc.success:
        jump sahne3_gecis_basari
    else:
        jump sahne3_gecis_basarisiz


label sahne3_gecis_krit_basari:

    # Doğal 20 — beden hatırlar. Ve kenarda: çentikler.
    si "Ayaklarım çıkıntıyı kendiliğinden buluyor."

    s "Beden hatırlıyor. Bunu daha önce yaptım."

    s "Bu duvarı biliyorum. Bu boşluğu biliyorum."

    si "Karşıya adım atıyorum. Kolay. Fazla kolay."

    si "Ve kenarın dibinde, taşa kazınmış: çentikler."

    s "Onlarca çentik. Biri burayı geçmiş. Tekrar. Tekrar. Tekrar."

    s "En yenisi... taze. Tozu bile oturmamış."

    if persistent.olum_sayisi > 0:

        f "Sayma onları."

        s "Neden saymamı istemiyorsun?"

    else:

        f "Eski dünyadan kalma. Önemsiz. Yürü."

    jump sahne3_son


label sahne3_gecis_basari:

    # Başarı — gergin ama sağ salim.
    si "Sırtım duvarda, santim santim ilerliyorum."

    si "Taş bir kez ufalanıyor; topuğum boşluğu yalıyor."

    s "Aşağı bakma. Aşağı diye bir yer yok."

    si "Son adım. Karşı kenar. Zemin."

    s "Geçtim."

    if tek_el:

        si "Lamba hâlâ elimde. Alev, teşekkür eder gibi bir parmak yükseliyor."

    jump sahne3_son


label sahne3_gecis_basarisiz:

    # Başarısızlık — kurtulur ama bedel kalıcı: KUVVET -1.
    si "Üçüncü adımda taş, topuğumun altında ufalanıyor."

    s "Düşüyorum—"

    si "Elim kendiliğinden bir çatlağa saplanıyor."

    si "Omzum, bütün ağırlığımı tek başına yutuyor."

    if tek_el:

        si "Öbür elim lambayı havaya kaldırıyor. Düşerken bile."

        s "Önce lambayı kurtardım. Kendimden önce."

        s "Bu normal mi?"

        $ lamba_bagi += 1

    si "Omzumda bir şey kopuyor. Sıcak bir kopuş."

    si "Kendimi kenardan yukarı çekiyorum. Taşın üstünde, nefes nefese."

    s "Bu omuz bir daha eskisi gibi olmayacak."

    $ player_stats.modify("STR", -1)

    centered "{color=#cc2222}KUVVET -1{/color}"

    si "Ve lamba... alev, düşüş sırasında küçülmüş."

    si "Koridorun duvarları da yaklaşmış sanki."

    s "Işık küçülünce dünya da küçülüyor."

    jump sahne3_son


label sahne3_gecis_krit_fiyasko:

    # Doğal 1 — İLK ÖLÜM NOKTASI.
    si "Üçüncü adımda taş, topuğumun altında kayboluyor."

    s "Taş değilmiş."

    s "Gölgeymiş."

    si "Düşüyorum."

    si "Işığın çemberi benimle birlikte düşüyor. Küçülüyor. Küçülüyor."

    s "Alev sönmeden hemen önce, aşağıda beni bekleyen şeyi görüyorum."

    f "Gözlerini kapat."

    call olum("karanlık seni yuttu")


################################################################################
## Sahne Sonu — İkinci Işık
################################################################################

label sahne3_son:

    scene bg_zindan_koridoru with sahne_gecis

    si "Koridor devam ediyor. Ben de."

    # İleride ışık belirir.
    scene bg_koridor_isik with sahne_gecis

    si "Ve sonra — ileride, karanlığın içinde — bir ışık."

    s "Kırmızı bir ışık."

    si "Benimki gibi. Kısık, sıcak, kırmızı."

    s "Bir lamba daha."

    si "Ve yaklaşıyor."

    f "..."

    s "İlk defa... sesin sustu."

    # Sahne 4: Karşılaşma (scene4_karsilasma.rpy)
    jump sahne4_karsilasma
