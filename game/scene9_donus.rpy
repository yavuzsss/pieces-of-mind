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
#   «...» (sessiz kalıp bekle) -> guven >= 4 ve gercek_sezgi ise şövalye
#        KENDİ uyanır ve adını hediye eder -> final_armagan;
#        değilse uyuyan elden isim alınır -> final_gasp.
# (Çalmayı deneyen oyuncu, bağ güçlüyse hediyeyle utandırılır —
#  "çalınamayan şey verilendir".)

# Şövalye gerçeğin kıyısına vardı (Armağan'ın ön koşulu).
default gercek_sezgi = False

# Merdivende "Neden hiç teslim etmedin beni?" sorusuna oyuncunun cevabı.
# "" / "bilmiyorum" / "sustu" / "istemedim"
default sahne9_cevap = ""


init -1 python:

    def gercege_kanit():
        """Şövalyenin, Fısıltı'nın kimliğine dair TANIK OLDUĞU kanıt sayısı.

        `gercek_sezgi` eskiden koşulsuz True'ydu: şövalye her koşuda
        gerçeğin kıyısına bedava varıyordu ve Armağan kapısı pratikte
        yalnızca guven'e bakıyordu. Artık varış kazanılıyor.

        alevdeki_ses ayrı tutulur — o kanıt değil, gerçeğin kendisidir
        (doğrudan yolu açar, bu sayıya girmez).

        Eşik ayarının TEK noktası: gercek_sezgi_esigi.
        """
        k = 0
        if sakli_neden:
            k += 1      # adını "Duymasın" diye sakladığını gördü
        if aclik_gorundu:
            k += 1      # fısıltının açlığı gözünün önünde çıplak kaldı
        if isyan >= 2:
            k += 1      # onu bir kez değil, defalarca sınadı
        if sahne9_cevap == "istemedim":
            k += 1      # "istemedim" — fısıltının onun hakkında bir iradesi var
        if persistent.olum_sayisi > 0:
            k += 1      # "Yeniden" kelimesi artık bir şey ifade ediyor
        if kurtarildi > 0:
            k += 1      # o ses onu ölümün kıyısından geri çekti — en somut kanıt
        if centikler_gorundu:
            k += 1      # kendi kemerinin kazıdığı çentikleri gördü (sezgi.rpy)
        return k

# Kaç kanıt gerçeğe vardırır. zar_dc_sabit / stres_bolen ile aynı kalıp.
define gercek_sezgi_esigi = 2


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

    # ALGI: ZEKÂ — çentikler (sezgi.rpy). Sahne 3'te olamazdı: orada her
    # stat 0. Burada oyuncu dört yükselme yapmış olur.
    # İSTİSNA: bu algı gercege_kanit()'e girer — gördüğü şey doğrudan
    # "biri burayı defalarca geçti" kanıtıdır.
    if zeka_gorur(2):

        si "Eğiliyorum. Kenardaki taşa bakıyorum."

        si "Çentikler. Tırnak değil — kemer tokası. Aynı yerde, üst üste."

        s "İlk geçişimde de buradaydılar. Görmemiştim."

        s "Biri burayı çok kez geçmiş."

        si "Ve o birinin kemeri benimkiyle aynı yeri kazımış."

        $ centikler_gorundu = True

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

            $ sahne9_cevap = "bilmiyorum"

            s "Bilmiyorsun."

            s "İlk dürüst cevabın bu olabilir. Korkutucu olan da bu."

        "«...»":

            $ sahne9_cevap = "sustu"

            s "Sustun. Yine."

            s "Ama bu sefer suskunluğun titriyor."

            $ stres_degistir(1)

        "«İstemedim.»":

            $ sahne9_cevap = "istemedim"

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

        $ gercek_sezgi = True

    elif gercege_kanit() >= gercek_sezgi_esigi:

        # Kırıntı yolu: gaflar ve oyalanma zinciri.
        # Artık bedava değil — şövalye bu zinciri ancak yeterince şey
        # gördüyse kurabilir (bkz. gercege_kanit).
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

        $ gercek_sezgi = True

    else:

        # YETERSİZ KANIT: zincir kurulmuyor. Şövalye eşiğe varıp geri döner.
        # Kayıp burada oynanır — oyuncu az önce söylenmeyeni bilir, şövalye
        # bilmez. Bayrak açılmaz; «...» yukarıda Gasp'a düşer (İlke 8).
        s "'Kalk. Yeniden.' İlk kelimelerin buydu."

        s "'Yeniden'i hep duydum. Hiç sormadım."

        si "Şimdi soracak gibi oluyorum. Soru ağzımda duruyor."

        si "Şekli var. İçi yok."

        s "..."

        s "Gitti."

        $ fis("...")

        si "Sen de tutmadın onu. Ya da tuttun ve bırakmadın."

        s "İkimiz de yorgunuz, içimdeki."

        s "Yukarı çıkalım. Orada belki hatırlarım."

        si "Hatırlamayacağımı ikimiz de biliyoruz."

    if gercek_sezgi and sakli_neden:

        s "Adımı 'Duymasın' diye saklamışım. Kendimden bile."

        s "Kimden sakladığımı artık biliyorum."

        s "Neden sakladığımı... çünkü duyduğunda bir şey olacaktı. Sende. Belki ikimizde."

    elif gercek_sezgi:

        s "Adımı aynanın ardına ben koymuşum. Bir sebepten."

        s "Sebep sendin galiba, içimdeki. Ya da sana benzeyen bir şeydi."

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

    # Son ton kancası: oyuncu «...» kumarını oynamadan önce bağın durumunu
    # şövalyenin sesinden okuyabilmeli (gösterge yok — İlke 8).
    if guven >= 4:

        s "Ve korkmuyorum. Garip, değil mi?"

        si "Kendi sesimi duyuyorum. Teslimiyet yok içinde. Rahatlık var. Birine yaslanan bir adamın sesi."

    elif guven <= 2:

        s "Kim olduğunu hiç bilmedim. Ne istediğini de."

        s "Ama başka kimsem yok. Gerisini de sen bitir."

        si "Kendi sesimi duyuyorum. Güven yok içinde. Sadece yorgunluk. Kumar oynayan bir adamın sesi."

    else:

        s "Sana güveniyor muyum? Bilmiyorum."

        s "Ama seni tanıyorum artık. Belki o daha önemlidir."

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

    # RİTİM KIRIĞI 3/3 — son sözden hemen ÖNCE söz elden alınır.
    # Amaç: final menüsü bir hak gibi değil, geri VERİLMİŞ bir şey gibi gelsin.
    $ fis_kacan("Bekle.", "Daha erken.", "Hazır değilim.", sure=3.6)

    si "Ağzım yok. Senin ağzın yok. İkimizin de yok."

    si "Sonra — bir yerden — geri geliyor."

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
            #
            # İKİ KAPI, İKİ FARKLI ŞEY ÖLÇER (2026-09-02):
            #   gercek_sezgi -> şövalye NE BİLİYOR (gercege_kanit, eşik 2)
            #   guven >= 4   -> aramızdaki BAĞ ne durumda (2026-07-16 ekonomisi:
            #                   sahne4 temiz geçiş, sahne6 dürüst sessizlik
            #                   [zorunlu +1], sahne7 «Hayır.»/ışık, sahne8
            #                   «Sakla», sahne6 «Bakma.»)
            #
            # gercek_sezgi eskiden koşulsuz True'ydu — kapı fiilen tek
            # kanattı. Artık iki ayrı şey isteniyor ve bunlar BİRBİRİYLE
            # ÇEKİŞİYOR: Sahne 8'de «Sakla.» guven +1 verir ama açlığı
            # göstermez (kanıt yok); «Söyle.»/«...» kanıt verir ama biri
            # guven götürür. Koruyucu oyuncu bağı kazanırken gerçeği
            # kaçırabilir. Armağan ikisini birden isteyen tek finaldir.
            #
            # Ulaşılabilirlik (kaba): gercek_sezgi ilk koşuda ~%53, ölüm
            # görmüş koşuda ~%89. Ayar noktası: gercek_sezgi_esigi.
            if gercek_sezgi and guven >= 4:

                jump final_armagan

            else:

                jump final_gasp
