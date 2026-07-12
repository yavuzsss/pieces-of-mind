# scene9_donus.rpy — Pieces of Mind
# Sahne 9: Dönüş ve Ayrım.
# Kuleye geri tırmanış (alev sayacı: "bir alev boyu" tükeniyor), merdivende
# gerçeğin SEZDİRİLMESİ (Fısıltı'nın kimliği — asla açık söylenmez, İlke 8;
# `gercek_sezgi` bayrağı) ve tepede dört finalin ayrım noktası.
#
# Final ayrımı (zarsız, telafisiz — İlke 7; suçluluk %100 oyuncunun):
# şövalye uykusuzluktan Koro'nun önünde çökerken elleri kendiliğinden açılır
# (UYUMA kuralının final ödemesi). Fısıltı'nın (oyuncunun) üç kutusu:
#   «UYAN. Adı ver...»   -> final_teslim
#   «UYAN. Beni alacak.» -> final_sonus
#   «...» (sessiz kalıp bekle) -> guven >= 5 ve gercek_sezgi ise şövalye
#        KENDİ uyanır ve adını hediye eder -> final_armagan;
#        değilse uyuyan elden isim alınır -> final_gasp.
# (Çalmayı deneyen oyuncu, bağ güçlüyse hediyeyle utandırılır —
#  "çalınamayan şey verilendir".)

# Şövalye gerçeğin kıyısına vardı (Armağan'ın ön koşulu).
default gercek_sezgi = False


################################################################################
## Koridor — Geri
################################################################################

label sahne9_donus:

    scene bg_zindan_koridoru with sahne_gecis

    si "Koridor beni tanıyor artık."

    si "Taşlar ayak sesimi geri veriyor. Bir adım benden, bir adım..."

    si "Hayır. Sadece benden. Sadece benden olsun."

    s "İki gündür uyumadım. Belki daha fazla."

    s "Adımlarımı sayıyordum az önce. Sayılar birbirine karıştı."

    s "Saymayı bırakıyorum. Saymak artık iyi bir fikir değil."

    $ fis("Az kaldı.")

    s "Bunu hangi anlamda dedin, sormayacağım."

    si "Lambayı kaldırıyorum."

    if ayna_bedeli == "alev":

        si "Alev... alev değil artık. Bir közün son nefesi. Camın dibinde büzülmüş."

        s "Bir alev boyu, demişti. Ben alevi kapıya harcadım."

        s "Süreyi kendi elimle kestim."

    else:

        si "Alev kısık. Her adımda bir kum tanesi düşüyor sanki."

        s "Bir alev boyu. Sürem bu kadar."

    $ stres_degistir(1)

    jump sahne9_ucurum


################################################################################
## Uçurum — İkinci Geçiş (zarsız: kule istiyor)
################################################################################

label sahne9_ucurum:

    scene bg_koridor_tuzak with sahne_gecis

    si "Uçurum. Daralan çıkıntı. İlk geçişimde burada zar zor tutunmuştum."

    si "Adım atıyorum ve—"

    si "Taş, ayağımın altında kendini düzeltiyor."

    s "..."

    s "Kule düşmeme izin vermiyor."

    if kule_kani:

        s "Tadımı biliyor. Tattığını kırmaz."

    s "Beni yukarıda istiyor. Bütün."

    $ fis("Yürü.")

    si "Karşıya geçiyorum. Kolayca. Hiç zorlanmadan."

    s "Dünyada güvenebileceğim tek zemin, beni yemek isteyen kulenin zemini."

    s "Güzel."

    $ stres_degistir(1)

    jump sahne9_kapi


################################################################################
## Kulenin Kapısı — Yarım'ın Yeri
################################################################################

label sahne9_kapi:

    scene bg_zindan_kapisi with sahne_gecis

    si "Kulenin ağzı. Demir kuşaklı kapı."

    if yarim_oldu:

        si "Kapının önünde bir adam yatıyordu. Rahat bir yüzle."

        si "Artık yok. Taş, verilenleri tutmuyor."

        s "İyi uykular, her kimsen."

    else:

        si "Ve karanlıkta, ışığımın tam sınırının dışında... bir hışırtı."

        yr "Hâlâ o yüz."

        yr "Şimdilik."

        si "Ses uzaklaşıyor. Peşimden gelmiyor."

        s "Beklemekte iyiyim, demişti."

        s "Bekliyor."

        $ stres_degistir(1)

    si "Kapıyı itiyorum. Direnmiyor. Hiç direnmedi zaten."

    jump sahne9_salon


################################################################################
## Salon — Üçüncü Geçiş: Boş Levha
################################################################################

label sahne9_salon:

    scene bg_lamba_salonu with sahne_gecis

    si "Salon. Binlerce oyuk. Binlerce sönmüş lamba."

    if sahne6_ihanet:

        si "Sönmüş'ün lambası hâlâ alt sırada. Camı çatlak. Taşı artık soğuk."

        s "Soğumuş. Ben yukarıda pazarlık ederken."

    si "Kendi oyuğumun önünden geçerken duruyorum."

    si "Halka parlatılmış. Ve halkanın yanına..."

    si "...küçük bir levha eklenmiş. Boş bir levha."

    s "Kazınacak bir isim için."

    s "Benimki için."

    call glitch_burst(0.3, 0.8, shake=False)

    $ fis("Bakma. Yürü.")

    s "İkisini de yapabiliyorum artık. Bakıyorum ve yürüyorum."

    $ stres_degistir(1)

    jump sahne9_merdiven


################################################################################
## Merdiven — Gerçeğin Kıyısı
################################################################################

label sahne9_merdiven:

    scene bg_kule_merdiven with sahne_gecis

    si "Merdiven. Yukarı."

    if zihin_izi:

        si "Ve yaklaştıkça, kafamın içindeki o raflar... yine kaşınıyor. Altın parmağın izi, sahibini duyuyor."

    si "Bacaklarım tırmanıyor. Ben konuşuyorum. Uyanık kalmanın tek yolu bu."

    s "Bir soru soracağım, içimdeki. Doğru cevap istemiyorum. Cevap istiyorum."

    s "Koro, fısıltılar isim getirir dedi. Getirmeyen yoktur dedi. Sen getirmemişsin."

    if persistent.olum_sayisi > 0:

        s "Ve ben kaç kez öldüm — sen kaç kez 'Kalk. Yeniden.' dedin?"

    else:

        s "Uçurumun kenarındaki çentikleri gördüm. Biri burayı defalarca geçmiş."

    s "Neden hiç teslim etmedin beni?"

    # Üç fısıltı — hiçbiri kaçış değil.
    menu:

        "«Bilmiyorum.»":

            s "Bilmiyorsun."

            s "İlk dürüst cevabın bu olabilir. Korkutucu olan da bu."

        "«...»":

            s "Sustun. Yine."

            s "Ama bu sefer suskunluğun titriyor."

            $ stres_degistir(1)

        "«İstemedim.»":

            s "İstemedin."

            s "Neden?"

            $ fis("...")

            s "İstememeyi biliyorsun. Nedenini bilmiyorsun."

            s "Bende de öyle şeyler var. Aynanın ardına kendi elimle koyduklarım."

    jump sahne9_sezgi


label sahne9_sezgi:

    if alevdeki_ses:

        # Derin yol: alevdeki kadın sesinin rezonansı.
        s "Bir şey daha var."

        s "Alevdeki kadın. Beni adımla çağıran."

        s "Sesini tanıyordum, içimdeki. Nereden tanıyordum, biliyor musun?"

        $ fis("...")

        s "Senden."

        s "Alçalt, yumuşat, kır — aynı ses."

        call glitch_burst(0.5, 1.2)

        # Fısıltı'nın ilk paniği — oyuncu tıklamak zorunda.
        $ fis("Sus.")

        s "İlk kez benden bir şey istedin ve sesin titredi."

        s "Kimsin sen?"

        $ fis("...")

        s "Belki sen de bilmiyorsun."

        s "İkimiz de aynayız, içimdeki. Arkasına bir şey saklanmış iki ayna."

    else:

        # Kırıntı yolu: gaflar ve oyalanma zinciri.
        s "'Kalk. Yeniden.' İlk kelimelerin buydu."

        s "'Yeniden'i hep duydum. Hiç sormadım."

        s "Koro seni azarladı — oyalanan fısıltı. Lanetler oyalanmaz, içimdeki."

        s "Lanetler biriktirmez. Lanetler beklemez."

        s "Bir şey seni burada tutuyor. Benimle."

        s "Ve ben soruyorum: lanetler sever mi?"

        # Tek kutu — oyuncu itirafa tıklamak zorunda.
        $ fis("Bilmiyorum.")

        s "Bilmiyorsun."

        s "Sevdiğini hatırlamayan biri gibi bilmiyorsun ama."

        call glitch_burst(0.4, 1.0, shake=False)

    if sakli_neden:

        s "Adımı 'Duymasın' diye saklamışım. Kendimden bile."

        s "Kimden sakladığımı artık biliyorum."

        s "Neden sakladığımı... çünkü duyduğunda bir şey olacaktı. Sende. Belki ikimizde."

    else:

        s "Adımı aynanın ardına ben koymuşum. Bir sebepten."

        s "Sebep sendin galiba, içimdeki. Ya da sana benzeyen bir şeydi."

    $ gercek_sezgi = True
    $ stres_degistir(2)

    si "Merdiven bitiyor. Yukarıda altın ışık."

    s "Cevapların kalanı orada."

    s "Ya da sonu."

    jump sahne9_tepe


################################################################################
## Tepe — Koro ve Sayaç
################################################################################

label sahne9_tepe:

    scene bg_altin_alev with sahne_gecis

    ko "Geldin."

    ko "Alev boyu doldu, küçük fısıltı."

    si "Lambama bakıyorum. Alev bir tırnak boyu. Belki daha az."

    ko "Adı mı getirdin..."

    ko "...kendini mi?"

    si "Kazandaki altın alev yükseliyor. İsimlerden örülü duvar."

    if alevdeki_ses:

        si "Ve içinde bir yerde, bir iplik ötekilerden farklı parlıyor. Beni çağıran."

    s "..."

    s "İçimdeki. Karar senin. Hep senindi zaten."

    si "Ve tam o anda uğultu... yumuşuyor."

    si "Bir beşik sallanıyor sanki. Bilerek yapıyorlar."

    s "Hayır. Hayır, şimdi değil—"

    si "İki gün. İki gün uyumadım. Tırmandım, kandım, kan verdim."

    si "Vücut faturayı kesiyor. Tam burada. Tam onların önünde."

    $ stres_degistir(2)

    jump sahne9_esik


label sahne9_esik:

    si "Dizlerim çözülüyor. Taşa iniyorum."

    si "Gözkapaklarım..."

    si "Ve ellerim. Ellerim kendiliğinden açılıyor. Uykuda herkes verir."

    ko "İşte."

    ko "Herkes uyur, küçük fısıltı. Sen sadece bekleyecektin."

    si "Altın ışık avucuma eğiliyor. Adım göğsümde, gevşeyen parmaklarımın ardında."

    si "Kafamın içinde son bir yer uyanık: sen."

    # ─── FİNAL AYRIMI — zarsız, telafisiz (İlke 7) ───
    # Oyuncunun fısıltısı üç kutu; dördüncü yol (Armağan) seçilmez, HAK EDİLİR.
    menu:

        "«UYAN. Adı ver. Bitsin.»":

            jump final_teslim

        "«UYAN. Adı değil — beni alacak.»":

            jump final_sonus

        "«...»":

            # Sessizlik: oyuncu bekler. Bağ güçlüyse şövalye KENDİ uyanır
            # ve çalınamayanı verir; değilse uyuyan elden isim alınır.
            if gercek_sezgi and guven >= 5:

                jump final_armagan

            else:

                jump final_gasp
