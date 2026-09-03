# scene8_ayna.rpy — Pieces of Mind
# Sahne 8: Uyku ve Ayna.
# Odaya dönüş sonrası: uykuyla savaş (UYUMA kuralı: Koro zihinleri uykuda
# arar), aynadaki anahtar deliğinin ödenmesi (3 bedel, zarsız: alev/kan/anı),
# aynanın ardına uzanış (ZEKÂ zarı; doğal 1 = uykuda ölüm) ve ismin geri
# alınışı. İSİM OYUNCUYA ASLA GÖSTERİLMEZ — şövalye öğrenir, Fısıltı öğrenmez.
# Reddetme noktası: guven <= 2 iken «Uyan.» fısıltısı duyulur ama sorgulanır.
# Sonu: alev sayacı + kuleye dönüş kararı (Sahne 9 kurulumu).

# Aynaya ne ödendi? ("" / "alev" / "kan" / "ani") — finallerde iz bırakacak.
default ayna_bedeli = ""

# Şövalye adını geri aldı (Armağan finalinin ön koşulu).
default isim_geri = False

# Doğal 20: ismi aynanın ardına kimin, neden sakladığı görüldü.
default sakli_neden = False


################################################################################
## Oda — UYUMA kuralı
################################################################################

label sahne8_oda:

    # Sahne 7'den kesintisiz devam: aynı oda, aynı gece.

    s "Uyuma diyorsun."

    s "Neden?"

    $ fis("Uykuda ararlar.")

    s "Kim arar?"

    $ fis("...")

    s "Tabii. Sustuğun yer, cevabın olduğu yer."

    if sahne7_soruldu:

        si "Yarım'ın sesi kulağımda: {i}Uykuda ellerini açarlar.{/i}"

        s "Benimki de öyle mi gitti? Adım. Uyurken mi?"

        $ fis("Evet.")

        si "Tek kelime. Taş gibi düşüyor."

        $ stres_degistir(1)

    si "Lambanın tabanındaki kazıma. UYUMA. Kendi elimle."

    s "Demek bunu bir kere öğrenmişim."

    s "Ve unutacağımı da biliyormuşum."

    jump sahne8_yatak


label sahne8_yatak:

    si "Yatak köşeden bakıyor. Çökük, gri, sıradan."

    si "Bacaklarım ona doğru bir adım atmış bile. Ben atmadım."

    s "Dünyada tek yatak kaldı ve yasak."

    s "Şansım hep böyleydi galiba. Hatırlamıyorum ama böyleydi."

    si "Gözkapaklarım... her kapanışta biraz daha geç açılıyor."

    # Üç fısıltı — hepsi ayakta tutar, hiçbiri bedava değil.
    menu:

        "«Yürü. Dur ve düşersin.»":

            si "Yürüyorum. Duvardan duvara. Dört adım, dön. Dört adım, dön."

            si "Dizlerim her dönüşte biraz daha ağır."

            s "Kendi odamda devriye geziyorum. Neden kaçtığımı bilmeden."

            $ stres_degistir(1)

        "«Yaraya bas. Acı uyanıktır.»":

            si "Elim şakağıma gidiyor. Kurumuş kanın altı hâlâ hassas."

            si "Bastırıyorum."

            s "..."

            si "Oda keskinleşiyor. Acı, dünyayı yerine oturtuyor."

            s "Uyanığım. Bunu senden öğrendim: acıyla ödenen her şey işliyor."

            $ stres_degistir(1)

        "«Aleve bak. Alev uyumaz.»":

            si "Lambayı masadan alıyorum. Kısık, kırmızı alev."

            si "Bakıyorum. Bakmak kolay. Bakmayı bırakmak zor."

            s "Ne kadar baktım?"

            si "Bilmiyorum. Alevin içinde zaman düz akmıyor."

            $ lamba_bagi += 1

    si "Uyku geri çekiliyor. Köşesine. Beklemeye."

    s "Peki. Uyumayacağım."

    jump sahne8_sonsuzluk


################################################################################
## Sonsuzluk — uyanık kalmak için sohbet (Milk: rahatsız edici düşünce)
################################################################################

label sahne8_sonsuzluk:

    s "Konuş benimle, içimdeki."

    s "Susarsan dinlerim. Dinlersem uyurum."

    $ fis("Ne hakkında?")

    s "Fark etmez. Uyutmayacak bir şey olsun."

    # Oyuncu rahatsız edici düşünceyi kendi eliyle fısıldar.
    $ fis("Sonsuzluk.")

    s "..."

    s "Peki. Sonsuzluk."

    $ fis("Ölümden sonrasını düşündün mü hiç?")

    s "Bu aralar başka bir şey düşündüğüm yok."

    $ fis("Cezayı sormuyorum. Ödülü soruyorum.")

    s "Ödül mü?"

    s "Ödül iyidir. Dinlenmek. Işık. Ne bileyim — bahçeler."

    $ fis("Sonsuza kadar.")

    s "Evet. Sonsuza kadar. Güzel kelime."

    $ fis("Öyle mi?")

    si "Kelimeyi ağzımda çeviriyorum. Sonsuz. Son-suz."

    s "...dur."

    $ fis("Diyelim her dileğin oluyor.")

    $ fis("Bin yıl. Milyon yıl. Milyar asır.")

    $ fis("Sonra bir milyar daha. Sonra bin milyar daha. Say. Saymaya devam et.")

    s "Tamam. Saydım. Uzun süre eğlendik."

    $ fis("Geriye ne kadar kaldı?")

    s "..."

    s "Hâlâ sonsuz."

    s "Bütün o sayılar... ve geriye kalan {b}hâlâ sonsuz{/b}."

    si "Cümle midemin dibine oturuyor. Uçurumun kenarındaki his — ama dibi olmayan bir uçurum."

    s "Dileklerin biter. İsteklerin biter. Sen bitmezsin."

    s "Bahçeler kalır. Ve sen. Ve zaman."

    $ stres_degistir(1)

    $ fis("Belki zamanı alırlar.")

    s "...ne?"

    $ fis("Delirmeyelim diye. Saymayı bilmeyen, bitmediğini de bilmez.")

    s "Mutlak mutluluk için... zaman algımızı mı alırlar elimizden?"

    s "Dur. Bu mutluluk mu peki?"

    s "Bu bilmeyenin mutluluğu. Cahilin mutluluğu."

    s "Bir bahçede gülümseyen ve kaç gündür gülümsediğini sayamayan bir adam."

    si "Ve cümle biterken soğuk bir şey ensemden aşağı iniyor."

    s "Kulenin tepesindeki alev geldi aklıma. İçinde yanan isimler."

    s "Onlar da mı saymıyor?"

    $ fis("...")

    si "Duvarların ardındaki uğultu bir an... yaklaşıyor gibi. Ilık. Davetkâr."

    s "Ben ne kadar zamandır buradayım, içimdeki?"

    si "Bilmiyorum."

    s "Sayamıyorum. Saymayı... bilmiyorum."

    if persistent.olum_sayisi > 0:

        s "Sen biliyor musun?"

        $ fis("...")

        s "Sustuğun yer, cevabın olduğu yer."

    $ stres_degistir(2)

    s "Uykum kaçtı."

    s "Sanırım istediğin de buydu."

    s "Ama bir şey yapmam lazım. Bekleyen adam uyur."

    $ fis("Ayna.")

    jump sahne8_ayna


################################################################################
## Ayna — Anahtar Deliği ve Bedel
################################################################################

label sahne8_ayna:

    si "Aynanın karşısındayım."

    si "Cam yok gibi. Oda yok. Ben yokum."

    si "Sadece delik: kapkara, göz hizasında, bekliyor."

    s "Anahtarım yok."

    $ fis("Anahtar istemiyor.")

    s "Ne istiyor?"

    $ fis("Ödeme.")

    s "Elbette."

    s "Bu dünyada hiçbir kapı sadece açılmıyor. Hepsi önce bir şey alıyor."

    si "Deliğe yaklaşıyorum. Etrafında hava... emiyor. Az az. Sabırla."

    s "Ne vereyim?"

    # Üç bedel — zarsız, telafisiz (Tasarım İlkesi 7: suçluluk oyuncunun).
    menu:

        "«Alevden ver. Bir nefes.»":
            jump sahne8_bedel_alev

        "«Kanından ver. Kilidin dili kan.»":
            jump sahne8_bedel_kan

        "«Bir anı ver. En eskisini.»":
            jump sahne8_bedel_ani


label sahne8_bedel_alev:

    $ ayna_bedeli = "alev"

    si "Lambanın kapağını açıyorum."

    si "Alevden bir dil uzanıyor — ince, kırmızı, isteksiz — ve deliğe akıyor."

    si "Delik içiyor."

    if alev_kucuk:

        si "Alev zaten küçüktü. Şimdi bir nefes daha küçük."

        si "Işığımın çemberi duvarlardan geri çekiliyor. Oda büyümüyor — dünyam küçülüyor."

        $ stres_degistir(2)

    else:

        si "Kapağı kapatıyorum. Alev eski boyunda değil artık."

        $ alev_kucuk = True

        centered "{color=#cc2222}ALEV KÜÇÜLDÜ{/color}"

    $ fis("Süren alev boyuydu.")

    s "Biliyorum."

    s "Artık daha kısa."

    jump sahne8_acilis


label sahne8_bedel_kan:

    $ ayna_bedeli = "kan"

    si "Başparmağımı deliğin kenarına bastırıyorum."

    si "Kenar keskin değil. Yine de kesiyor."

    si "Kan, deliğin karanlığına yürüyor. Damlamıyor — {b}çekiliyor{/b}."

    if kule_kani:

        si "Ve delik... duruyor. Tadıyor."

        s "Beni tanıdı."

        s "Kule tatmıştı. Ayna kulenin aynası."

        si "İkinci yudum ilkinden derin. Üçüncüsü daha da."

        $ stres_degistir(2)

    si "Elimi çektiğimde parmağım beyaz. Kolum ağır."

    si "Aldığı sadece kan değildi."

    call can_hasar(3, "ayna, kanını içti")

    s "Verdim işte. Aç."

    jump sahne8_acilis


label sahne8_bedel_ani:

    $ ayna_bedeli = "ani"

    si "Delik sıcak bir şey istiyor. Kan gibi ama daha eski."

    si "Gözlerimi kapatıyorum ve en dipteki şeyi buluyorum:"

    si "Yağmur. Çamur. Omuzlarımı çökerten bir zırh. Ve bana bağıran bir ses—"

    si "Deliğe uzatıyorum. Avucumda, kuş gibi."

    si "Ve gidiyor."

    s "..."

    s "Az önce bir şey biliyordum."

    s "Yağmurla ilgili bir şey. Önemliydi. Yemin gibi bir şeydi."

    s "Neydi?"

    $ fis("...")

    s "Sen de mi bilmiyorsun? Yoksa söylemiyor musun?"

    s "İkisi de aynı kapıya çıkıyor zaten."

    $ guven_degistir(-1)
    $ stres_degistir(1)

    jump sahne8_acilis


################################################################################
## Açılış — Aynanın Ardı
################################################################################

label sahne8_acilis:

    call glitch_burst(0.4, 1.0)

    si "Delik... genişliyor."

    si "Bir gözbebeği gibi. Karanlık, camın tamamına yayılıyor."

    si "Ayna artık bir çerçeve içinde duran gece."

    s "Aynadaki adam nerede?"

    $ fis("İçeride.")

    s "İçeride ne var?"

    $ fis("Adın.")

    si "Kelime göğsümde bir yeri buluyor. Kilit dilinin yuvasını bulması gibi."

    s "Adım."

    s "Bunca yol. Bunca ölü lamba. Ve adım, başladığım odada, camın arkasındaymış."

    s "En uzak yer hep en yakını."

    jump sahne8_uzanis


label sahne8_uzanis:

    si "Kolumu camın olduğu yere sokuyorum."

    si "Direnç yok. Soğuk yok. Hiçlik var — kolumun olduğu yerde kolumun olmadığı hissi."

    si "Dirseğe kadar. Omza kadar."

    si "Parmaklarım karanlığı tarıyor. Bir şey var. Uzakta. Küçük ve sıcak."

    si "Ve tam o anda—"

    si "Taşların ardından bir uğultu. Altın. Ilık. Tanıdık."

    si "Bir ninni gibi. Kimse söylemiyor ama bir ninni."

    s "Gözkapaklarım..."

    si "Uğultu ağırlaşıyor. Uyku, sıcak bir el gibi enseme yerleşiyor."

    # Fısıltı'nın tokadı — oyuncu tıklamak zorunda.
    $ fis("Uyan.")

    if guven <= 2:

        # REDDETME: güven dibe vurduysa şövalye tokada direnir —
        # uyku ona fısıltıdan kurtuluş gibi görünür.
        s "Sesini duyuyorum."

        s "Ama ya uyku senden kurtulmanın tek yoluysa?"

        si "Bir an — sadece bir an — bırakıyorum. Altın uğultu gözkapaklarımın altına sızıyor."

        si "Sıcak. Nazik. {b}Aç.{/b}"

        si "Ve açlığı hissettiğim anda kendim geri çekiliyorum. Sana itaatten değil. Korkudan."

        s "Senden kurtulmak için onlara uyuyacak değilim."

        $ stres_degistir(2)

    else:

        si "Silkiniyorum. Ense kökümdeki sıcak el bir an gevşiyor."

        s "Uyanığım. Uyanığım."

    si "Ama uğultu durmuyor. Ve parmaklarım hâlâ boş."

    si "Zihnimi iki yerde birden tutmam gerekiyor: avucumda ve gözkapaklarımda."

    # --- ZEKÂ zarı — DC 13: uğultuya karşı uyanık kalmak ---
    call roll_dice("ZEKA", 13)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne8_uzanis_krit_basari
    elif sonuc.crit_fail:
        jump sahne8_uzanis_krit_fiyasko
    elif sonuc.success:
        jump sahne8_uzanis_basari
    else:
        jump sahne8_uzanis_bedel


label sahne8_uzanis_krit_basari:

    # Doğal 20 — isim + saklama anısının kendisi: kimden sakladığı görülür.
    $ sakli_neden = True

    si "Uğultu bir an... duruyor. Sanki nefes alıyor."

    si "Ve o boşlukta parmaklarım kapanıyor. Küçük, sıcak, kıpır kıpır bir şeyin üstüne."

    si "Ve görüyorum—"

    si "Camın öte yüzünde bir adam. Ben. Uyanık, kararlı, daha az yorgun bir ben."

    si "Avucundakini karanlığa bırakıyor. Ve dudakları kıpırdıyor:"

    s "{i}Duymasın.{/i}"

    s "..."

    s "Adımı buraya ben koydum. Duymasın diye."

    s "Kim duymasın?"

    si "Sorunun cevabı, sorudan önce gelmişti zaten."

    $ stres_degistir(1)

    jump sahne8_cekis


label sahne8_uzanis_basari:

    # Başarı — temiz kavrayış.
    si "Uğultuyu bir kapı gibi kapatıyorum. Hâlâ orada — ama artık dışarıda."

    si "Ve parmaklarım buluyor."

    si "Küçük. Sıcak. Kıpır kıpır. Avucumda bir kuş yavrusu gibi."

    s "Seni tanıyorum."

    si "Tanımıyorum. Ama avucum tanıyor."

    jump sahne8_cekis


label sahne8_uzanis_bedel:

    # Başarısızlık — isim derine kayar; zihin ikiye bölünmenin bedelini öder.
    si "Uğultu ağır basıyor. Bir saniyelik bir dalış—"

    si "Ve parmaklarımın ucundaki sıcaklık kayıyor. Derine."

    s "Hayır. HAYIR."

    si "Omzumu boşluğa gömüyorum. Yanağım camın olduğu yerde. Karanlık kulağıma dolu."

    si "Uzanıyorum. Zihnimin dikişleri atıyor."

    call can_hasar(3, "aynanın ardındaki karanlık")

    si "Ve buluyorum. Avucum kapanıyor."

    si "Ama çekilirken... bir şey elimin üstünden geçiyor."

    si "Parmak gibi. Sayar gibi."

    s "Orada bir şey daha var. İsimden başka."

    $ fis("Çek. Hemen.")

    $ stres_degistir(1)

    jump sahne8_cekis


label sahne8_uzanis_krit_fiyasko:

    # Doğal 1 — uğultu kazanır: uykuda ölüm. UYUMA kuralı kanıtlanır.
    si "Uğultu bir el oluyor. El, bir kucak."

    si "Ve sıcak. Her şey sıcak."

    si "Biri adımı söylüyor. Sevgiyle. Sabırla. Uzun zamandır ilk kez—"

    s "...buradayım."

    si "Cevap verdim."

    si "Cevap vermemeliydim."

    si "Altın ışık gözkapaklarımın altında. Avucum... avucum açılıyor. Kendi kendine."

    # Fısıltı'nın çığlığı — oyuncu tıklamak zorunda.
    $ fis("UYAN. UYAN. UYA—")

    # DOĞAL 1 ARTIK ÖLDÜRMEZ: çığlık gözkapağını kaldırır.
    si "Gözkapağım açılıyor. Tek başına değil — biri kaldırdı."

    si "Avucum yumruğa dönüyor. İçinde ne varsa, orada kalıyor."

    si "Ve altın ışık, aldığını sandığı şeyi bulamadan çekiliyor."

    $ kurtarildi += 1

    call can_hasar(9, "uyku ile uyanıklığın arasında")

    s "Bağırdın."

    s "Sen hep bağırıyorsun. Ben hep uyanıyorum."

    si "Bu cümlenin altında bir şey var. Bakmayacağım."

    $ stres_degistir(3)


################################################################################
## Çekiş — İsim (asla gösterilmez)
################################################################################

label sahne8_cekis:

    si "Kolumu çekiyorum. Karanlık bırakmak istemiyor; bırakıyor."

    scene bg_ayna_yakin with sahne_gecis

    si "Ayna yeniden ayna. Delik yok. Gece yok."

    si "Ve aynada yine bir adam var. Yorgun. Sakallı. Şakağında kurumuş kan."

    si "Avucum göğsümde. Kapalı."

    s "Açmama gerek yok."

    si "İsim avuçtan girmez. Nefesle girer."

    si "Nefes alıyorum."

    call glitch_burst(0.3, 0.8, shake=False)

    s "..."

    si "Ve biliyorum."

    si "Adımı biliyorum."

    $ isim_geri = True

    si "Aynadaki yüz aynı yüz. Ama artık üstüne oturan bir şey var."

    si "İsimsiz bir yüz bir oda gibidir. Şimdi odada biri oturuyor."

    jump sahne8_isim


label sahne8_isim:

    s "Duydun mu?"

    si "Soruyu ben sordum. Cevabı duymaktan korkarak."

    # Üç fısıltı — Fısıltı'nın açlığı ilk kez çıplak (oyuncunun açlığı).
    menu:

        "«Söyle.»":

            s "Hayır."

            if isim_uyarisi:

                s "Sönmüş ne demişti? {i}Bulduğunda ona söyleme.{/i}"

                s "O uyarıyı, onu bulan herkes ödeyerek öğrenmiş."

            s "İsim fısıltıya verilmez."

            s "Bunu neden bildiğimi bilmiyorum. Ama kanım biliyor."

            $ guven_degistir(-1)

            $ aclik_gorundu = True

        "«...»":

            s "Sessizsin."

            s "Sessizliğin aç ama."

            si "Kafamın içindeki boşluk, bir ağız gibi. Kibarca kapalı. Ama ağız."

            $ stres_degistir(1)

            # Sessizlik de açlığı gösterir — şövalye onu adlandırdı.
            $ aclik_gorundu = True

        "«Sakla. Kimseye söyleme. Bana bile.»":

            s "\"Bana bile.\""

            s "\"Bile\"nin içinde ne çok şey var."

            si "Kelimeyi evirip çeviriyorum. İçinde bir yakınlık iddiası. İçinde bir feragat."

            s "Saklayacağım. Senden de."

            s "Ama bunu sen istedin. Bunu unutmayacağım."

            $ guven_degistir(1)
            $ stres_degistir(1)

    if sakli_neden:

        s "Bir şey daha var, içimdeki."

        s "Adımı oraya ben koymuşum. \"Duymasın\" diye."

        s "O cümleyi kurarken kimi düşünüyordum, biliyor musun?"

        $ fis("...")

        s "Ben de öyle düşünmüştüm."

        $ stres_degistir(1)

    jump sahne8_son


################################################################################
## Son — Alev Sayacı ve Kuleye Dönüş
################################################################################

label sahne8_son:

    scene bg_sovalye_odasi with sahne_gecis

    si "Lamba masada. Alev..."

    if ayna_bedeli == "alev":

        si "Alev artık bir alev değil. Bir közün anısı."

        s "Süre \"bir alev boyu\"ydu."

        s "Ve ben alevi harcadım. Kapı için."

        s "Pazarlıkta hep aynı taraf kazanıyor. Ve o taraf hiç ben olmuyorum."

    else:

        si "Alev kısık. Her nefeste bir kum tanesi düşüyor sanki."

        s "Süre \"bir alev boyu\"ydu."

        s "Ve alev kimseyi beklemiyor."

    si "Duvarların ardında uğultu sürüyor. Altın, ılık, sabırlı."

    si "Kızgın değiller. Aceleleri yok."

    s "Uyumamı bekliyorlar. Herkes uyur."

    s "Ben uyumayacağım."

    $ stres_degistir(1)

    s "Ya adı... ya kendini. Öyle demişti."

    s "Yarım üçüncü yolun yalanını söyledi. Belki Koro da ikinin."

    s "Öğrenmenin tek yolu var."

    $ fis("Yürü.")

    s "Hep aynı kelime."

    s "Ama ilk kez ben de aynı yöne yürümek istiyorum."

    si "Kapıyı açıyorum. Koridor. Işığımın değdiği kadar dünya."

    si "Kule bekliyor. Alev sayıyor."

    s "Kuleye dönüyoruz, içimdeki."

    s "Ve ikimizden biri orada kalacak."

    # Sahne 9: Dönüş ve Ayrım (scene9_donus.rpy)
    jump sahne9_donus
