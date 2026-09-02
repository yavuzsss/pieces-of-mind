# finaller.rpy — Pieces of Mind
#
#   TESLİM  — isim Koro'ya verilir; şövalye söner; kalıntı alevdeki adına
#             "kavuşur" (koroya karışır). Epilog: yeni beden, "Kalk." —
#             oyuncu artık o sesin kimin olduğunu bilir.
#   ARMAĞAN — tek sıcak final: şövalye gerçeği tamamlar ve adını kalıntıya
#             HEDİYE eder (çalınamayan şey verilendir); kuleden birlikte
#             çıkarlar. İsim oyuncuya yine GÖSTERİLMEZ.
#   SÖNÜŞ   — kalıntı ultimatoma uyar, kendini verir; alevde adıyla birleşir
#             (yakıt olarak); şövalye fısıltısız kalır — Sönmüş'ün yolu.
#             Çözülürken şövalye bir saniyeliğine yüzünü hatırlar.
#   GASP    — ada aç kalıntı ŞÖVALYENİN adını uyuyan elinden alır; roller
#             değişir; epilogda UI ters döner (şövalyenin metni kırmızı
#             italiğe, kalıntınınki kreme).
#
# Ortak kurallar: zarsız ve telafisiz (İlke 7); isim hiçbir finalde
# gösterilmez (bozuk/yanan harfler, "———", tepkiyle anlatım).
#
# DURUM: DÖRT FİNAL DE YAZILDI (2026-07-12).
#
# Anlatı istisnası (İlke 2'nin genişletilmesi): şövalye SÖNDÜKTEN sonra
# dinleyen beden kalmaz — ölüm monoloğundaki gibi Fısıltı düz `f` ile konuşur.
# Oyuncunun kutu koltuğu boşalır; epilogdaki "Kalk." da bu yüzden kutusuz.

# Hangi finaller görüldü? (oyunlar arası taşınır — ileride galeri/NG+ için)
default persistent.final_teslim = False
default persistent.final_armagan = False
default persistent.final_sonus = False
default persistent.final_gasp = False

# GASP epiloğu — UI ters döner (kilitli karar): bedeni alan kalıntı krem
# konuşur (adı asla gösterilmez: "———"), hapsolan şövalye kırmızı italik
# konuşur ve isim kutusunda "Fısıltı" yazar. Roller mekanikte değişir.
define gasp_kalinti = Character("———", color="#f5e9d0", what_color="#f5e9d0",
                                ctc="ctc_blink", ctc_position="nestled")
define gasp_sovalye = Character("Fısıltı", color="#cc2222", what_color="#cc2222",
                                what_italic=True,
                                ctc="ctc_blink", ctc_position="nestled")


################################################################################
## FİNAL 1 — TESLİM
################################################################################

label final_teslim:

    # «UYAN. Adı ver. Bitsin.» — oyuncunun tokadı ve hükmü.

    play music muzik_teslim fadeout 3.0 fadein 5.0

    si "Kafamın içinde sesin: keskin, kesin."

    si "Ve avucum kapanıyor. Uyanıyorum — dizlerimin üstünde, onların önünde."

    s "...ver, diyorsun."

    s "Adımı. Bunca yolu geri almak için indiğim, uyumadan taşıdığım adımı."

    $ fis("Bitsin.")

    s "Bitsin."

    s "Evet. Bitsin istiyorum. Ne kadar zamandır ayaktayım ben?"

    s "Çentikler kadar."

    ko "Beden uyanık."

    ko "Ve fısıltı kararını vermiş. Duyduk."

    si "Ayağa kalkıyorum. Bacaklarım son bir kez taşıyor beni."

    si "Kazana yaklaşıyorum. Altın alev yükseliyor. Sıcak değil."

    si "Aç."

    if isim_uyarisi:

        s "Sönmüş ne demişti? {i}Bulduğunda ona söyleme.{/i}"

        s "Sana söylemeyeceğim, içimdeki. Merak etme."

        s "İsmin gittiği yerden fısıltılar bile alamaz."

    s "Bir şartım var."

    s "Söylediğimde kimse tekrarlamayacak."

    ko "Kimse tekrarlayamaz, beden."

    ko "İsimler bizde yankılanmaz. Yanar."

    jump final_teslim_verilis


label final_teslim_verilis:

    si "Dudaklarım aralanıyor."

    si "Bir isim söylüyorum."

    si "Duyuyorum — ve duyduğum yerden alev alıyor. Bana kalan: kül tadı."

    call glitch_burst(0.6, 1.4)

    si "İsim ağzımdan altın bir iplik gibi çekiliyor. Uzun. Sandığımdan uzun."

    si "Sanki yıllardır bir ucundan tutuyormuşum da şimdi bırakıyormuşum."

    ko "Ahh."

    ko "Eski bir isim. Derin kök. İyi yanacak."

    if alevdeki_ses:

        si "Ve iplik, alevin içinde kıvrılıp {b}o{/b} ipliğin yanına yerleşiyor."

        si "Beni çağıran sesin yanına."

    si "Ve lambam..."

    si "Alev, camın içinde son bir kez doğruluyor. Veda eder gibi."

    si "Ve sönüyor."

    s "Alev boyu doldu."

    $ knight_name = "???"

    stop music fadeout 4.0

    jump final_teslim_sonus


label final_teslim_sonus:

    # Şövalye söner — isimsiz beden boşalır.

    s "Tuhaf."

    s "Hafifim. İlk kez hafifim."

    s "İçimdeki. Bir şey soracaktım sana."

    s "İçimde..."

    s "...ne vardı içimde?"

    $ fis("...")

    s "Kimse var mı?"

    si "..."

    s "Bekleyeceğim."

    s "Neyi beklediğimi unutana kadar."

    s "..."

    s "Unuttum bile."

    call glitch_burst(0.4, 1.0, shake=False)

    # Beden artık duymuyor — Fısıltı ilk kez düz sesle konuşur (İlke 2 istisnası).

    f "Boş."

    f "Kaç kez taşıdım bu bedeni. İlk kez bu kadar boş."

    ko "Küçük fısıltı."

    ko "Borç ödendi. Yer açıldı."

    ko "Gel."

    f "Alevde bir iplik parlıyor. Ötekilerden farklı."

    f "Hep farklıydı. Bunu kimseye söylemedim. Kendime bile."

    f "Onu tanıyorum."

    f "Tanımıyorum. Ama tanıyorum."

    f "Geliyorum."

    call glitch_burst(0.8, 1.6)

    scene black
    with Pause(2.0)

    jump final_teslim_epilog


label final_teslim_epilog:

    # Epilog — yeni beden, aynı oda, aynı açılış. Oyuncunun koltuğu boş:
    # "Kalk." artık kutudan değil, dışarıdan duyuluyor. Ses kimin, biliyorsun.

    play music muzik_karanlik fadein 3.0

    with Pause(2.0)

    si "...soğuk."

    si "Taş. Sırtımın altında taş var."

    si "Ne kadar zamandır buradayım?"

    s "..."

    s "Kalkmalıyım."

    call glitch_burst(0.15, 0.6, shake=False)

    f "Kalk."

    with Pause(1.5)

    $ persistent.final_teslim = True

    centered "{color=#cc2222}— TESLİM —{/color}\n \n{color=#b8ac93}isim yandı. sıra bekleyen isimler var.{/color}"

    call krediler

    return


################################################################################
## FİNAL 2 — ARMAĞAN (tek sıcak final)
################################################################################

label final_armagan:

    # «...» — sessizlik. Ama bağ güçlü: şövalye kendi uyanır.
    # Çalmayı bekleyen oyuncu, hediyeyle utandırılır.

    play music muzik_armagan fadeout 3.0 fadein 5.0

    si "Ellerim açılıyor. Altın ışık avucuma eğiliyor."

    si "Ve sesin gelmiyor."

    si "Uykunun dibinde bile bunu duyuyorum: gelmeyen sesini."

    si "Ve avucum... kendi kendine kapanıyor."

    si "Uyanıyorum. Kimse uyandırmadı."

    si "Uyandım."

    s "Gördüm, içimdeki."

    s "Elim açıktı. Sen sustun."

    s "Ne kadar aç olduğunu duyabiliyordum. Sustuğunu da."

    $ fis("...")

    s "Aç olan herkes hırsız değildir."

    s "Ama kimse açlığıyla baş başa da bırakılmamalı."

    ko "Beden uyanık. Yine."

    ko "Süre doldu, küçük fısıltı. Adı. Ya da onu."

    s "İkisini de alamayacaksın."

    s "Üçüncü yol yok demişlerdi. Doğruydu."

    s "Ama dördüncü var."

    jump final_armagan_gercek


label final_armagan_gercek:

    if alevdeki_ses:

        # Derin yol — gerçeğin son parçası oyuncuya söyletilir ("...bendim").
        s "Alevdeki ses. Beni adımla çağıran."

        s "Merdivende demiştim: sesini senden tanıyordum."

        s "Yanlış söylemişim."

        s "Senin sesini {b}ondan{/b} tanıyordum."

        call glitch_burst(0.4, 1.0, shake=False)

        # Kalıntının yarım hatırlayışı — oyuncu parçayı kendisi söyler.
        $ fis("...bendim.")

        s "Evet."

        s "Bilmiyordun, değil mi? Şimdi bile tam bilmiyorsun."

        s "Önemli değil."

        s "Bundan sonra ikimiz için de ben hatırlarım."

    else:

        # Kırıntı yolu — kimlik bilinmez ama doğası bilinir.
        s "Kim olduğunu bilmiyorum, içimdeki. Sen de bilmiyorsun."

        s "Ama ne olmadığını biliyorum."

        s "Lanet değilsin. Lanetler beklemez. Lanetler oyalanmaz."

        s "Ve lanetler, sahibi uyurken susup dayanmaz."

        $ fis("...")

    jump final_armagan_hediye


label final_armagan_hediye:

    if isim_uyarisi:

        s "Sönmüş demişti: adını ona söyleme."

        s "Çalınandan korkuyordu. Haklıydı da."

        s "Ama bir şeyi bilmiyordu."

    s "Çalınamayan şey, verilendir."

    si "Ayağa kalkıyorum. Bacaklarım titriyor; duruyorum yine de."

    s "İçimdeki. Sana bir armağanım var."

    s "Reddetme. Zaten geri alınamaz."

    si "Ve adımı söylüyorum."

    si "Yüksek sesle. İsteyerek. İlk kez."

    call glitch_burst(0.5, 1.1, shake=False)

    si "İsim havada altınlaşmıyor. Yanmıyor. Kaymıyor."

    si "Sadece yer değiştiriyor."

    si "Ya da çoğalıyor. Bilmiyorum. İkimizde birden."

    $ fis("...")

    s "Söyle bir şey."

    $ fis("Bunu geri alamazsın.")

    s "Biliyorum."

    s "Armağan dediğim bu."

    ko "..."

    ko "Verilmiş ad."

    ko "Verilmiş ad {b}yanmaz{/b}, küçük fısıltı. Küle bile yaramaz."

    ko "Ne getirdiniz bize? Hiç. Ne bırakacaksınız? Hiç."

    ko "Adlı şeyler. Gidin."

    ko "İkiniz. Tek."

    s "\"İkiniz. Tek.\""

    s "Koro'dan duyduğum ilk doğru cümle."

    jump final_armagan_cikis


label final_armagan_cikis:

    scene bg_kule_merdiven with sahne_gecis

    si "İniyoruz. Basamaklar düz. İlk kez düz."

    if kule_kani:

        s "Tadımı biliyorsun, kule. Afiyet olsun."

        s "Gerisi benim."

    si "Kule bırakıyor. Tattığını unutmaz — ama verileni tutamaz."

    scene bg_zindan_kapisi with sahne_gecis

    si "Kapı. Kulenin ağzı."

    si "İtiyorum."

    si "Ve öteki taraf..."

    stop music fadeout 4.0

    scene black
    with Pause(2.0)

    si "...oda değil."

    jump final_armagan_epilog


label final_armagan_epilog:

    # Dışarısı çizilmez — oyunun görsel dili zindanda kalır; ötesi karanlık
    # ekranda yalnızca kelimelerle var olur (Milk: metin esastır).

    si "Hava. Gerçek hava. Yüzüme çarpıyor."

    si "Ve yağmur."

    if ayna_bedeli == "ani":

        s "Yağmur..."

        s "Gözlerim doluyor ve nedenini bilmiyorum."

        s "Yağmurla ilgili bir şey vardı. Aynaya verdim."

        $ fis("Ben hatırlıyorum.")

        s "..."

        s "Anlat o zaman."

        s "Yol uzun."

    else:

        s "Yağmur. Çamur kokusu."

        s "Biri bana bağırıyordu yağmurun altında. Bir isim. Benim ismim."

        s "Kimin bağırdığını artık biliyorum galiba."

    si "Lambayı hâlâ taşıyorum. Alev bir kıvılcım. Kapının dışında... gereksiz."

    if lamba_bagi >= 3:

        si "Parmaklarım sapı bırakmak istemiyor."

        si "Teker teker açıyorum onları. Teker teker."

    si "Lambayı eşiğe bırakıyorum. İçeriye. Ait olduğu yere."

    s "Işığın değdiği kadardı dünya."

    s "Artık değil."

    s "Ee, içimdeki. Adlı şey."

    s "Nereye?"

    # Son kutu — oyunun ilk dürüst "biz"i.
    $ fis("Yürüyelim.")

    s "Yürüyelim."

    # Dışarıdaki sessizliğin içinden sıcak tema geri döner.
    play music muzik_armagan fadein 4.0

    with Pause(1.5)

    $ persistent.final_armagan = True

    centered "{color=#f5e9d0}— ARMAĞAN —{/color}\n \n{color=#b8ac93}çalınamayan şey, verilendir.{/color}"

    call krediler(sicak=True)

    return


################################################################################
## FİNAL 3 — SÖNÜŞ
################################################################################

label final_sonus:

    # «UYAN. Adı değil — beni alacak.» — kalıntının fedası.

    play music muzik_sonus fadeout 3.0 fadein 5.0

    si "Kafamın içinde sesin — ve avucum kapanıyor. Uyanıyorum."

    s "...ne dedin?"

    $ fis("Adı değil. Beni alacak.")

    s "Hayır."

    s "Hayır, dur. Bunu konuşmadık."

    ko "Duyduk."

    ko "Kalıntı kendini teklif ediyor. Nadirdir."

    ko "Kabul."

    s "Bekle—"

    si "Altın alev kazanın kenarından taşıyor. Bir kol gibi uzuyor. Acele etmeden."

    s "İçimdeki. Neden?"

    $ fis("...")

    s "Bilmiyorsun."

    s "Ya da biliyorsun ve söylemiyorsun. İkisini hiç ayıramadım zaten."

    s "Merdivende sormuştum: lanetler sever mi?"

    s "Cevabın bu mu?"

    $ fis("...")

    s "Söyle bir şey. Son kez."

    s "Ne olursa."

    # Son kutu — oyuncunun vedası. İlk sözü "Kalk."tı; son sözü de koruma.
    $ fis("Uyuma.")

    s "..."

    s "Uyumam."

    jump final_sonus_cekilis


label final_sonus_cekilis:

    si "Ve altın kol alnıma değiyor."

    si "Soğuk değil. Acı değil. Daha kötüsü: nazik."

    call glitch_burst(0.7, 1.5)

    si "Bir şey çekiliyor. Kafamın içindeki o yerden — adını hiç bilmediğim, hep dolu olan o yerden."

    si "Çekiliyor. Çekiliyor."

    si "Ve çıkıyor."

    si "İnce, kırmızı bir iplik. Işığa doğru."

    if alevdeki_ses:

        si "Ve alevin içinde, beni çağıran o iplik... parlıyor. Uzanıyor."

        si "İkisi birbirine sarılıyor."

    else:

        si "Alevin içinde bir iplik ona doğru eğiliyor. Sanki bekliyormuş."

    si "Ve yanarken—"

    call glitch_burst(0.5, 1.3)

    s "Bir yüz."

    s "Bir saniye. Yağmur altında bir yüz. Bana dönüyor. Gülüyor."

    s "Adımı söylüyor—"

    si "Ve bitiyor."

    s "..."

    s "Kimdi o?"

    s "{b}Kimdi o?{/b}"

    ko "Ödendi."

    ko "Git, beden. Borcun yok artık."

    jump final_sonus_sessizlik


label final_sonus_sessizlik:

    s "İçimdeki?"

    s "..."

    s "İçimde kimse yok."

    si "Kafamın içi geniş. Uçsuz. Boş bir salon gibi."

    si "İlk kez yalnızca kendi düşüncelerim var."

    si "Ve ne kadar az varlarmış."

    si "Lambamı alıyorum. Alev duruyor hâlâ. Küçücük."

    s "Alevler kulede daha yavaş ölür."

    s "Ama ölür."

    si "Cümlenin iki yarısını da ben söylüyorum artık."

    si "Tamamlayan yok."

    stop music fadeout 4.0

    scene black
    with Pause(2.0)

    jump final_sonus_epilog


label final_sonus_epilog:

    # Epilog — o artık Sönmüş: replikleri `sk` kutusundan (mekanik anlatım).
    # Sahne 4'ün aynası, bu kez öbür taraftan.

    scene bg_zindan_arena
    with Pause(2.0)

    si "Kuleden indim. Kaç basamak? Saymayı bırakalı çok oldu."

    si "Zaman geçiyor. Ya da geçmiyor. Ölçecek bir şeyim kalmadı."

    si "Bir yüzü hatırlamaya çalışıyorum. Bir saniyeliğine benimdi."

    si "Her gün — eğer bunlar günse — biraz daha siliniyor."

    si "Ve bir gün, koridorun ucunda..."

    si "...bir ışık."

    si "Kırmızı bir ışık. Benimki gibi. Kısık, sıcak, yaklaşan."

    si "Ayağa kalkıyorum. Kelimeleri hatırlamaya çalışıyorum. Konuşmayalı çok oldu."

    sk "Dur."

    sk "Işığını görüyorum. Gür alev."

    sk "Benim de alevim gürdü. Bir zamanlar."

    sk "Yaklaşma. Sadece dinle. Bir şey söyleyeceğim, aklında tut."

    sk "Adını bulursan..."

    sk "...{b}ona{/b} söyleme."

    with Pause(1.5)

    $ persistent.final_sonus = True

    centered "{color=#cc2222}— SÖNÜŞ —{/color}\n \n{color=#b8ac93}fısıltısız kafa geniştir. ve bomboş.{/color}"

    call krediler

    return


################################################################################
## FİNAL 4 — GASP
################################################################################

label final_gasp:

    # «...» — sessizlik, ama bağ zayıf: şövalye uyanmıyor. Açlık konuşuyor.

    si "Sesin gelmiyor."

    si "Uykunun eşiğinde son bir düşünce: neden sesin gelmiyor?"

    si "Ve düşüyorum. Sıcak, altın, dipsiz bir kuyuya."

    si "Rüyada biri bana sesleniyor. Tanıdık bir ses. Hep tanıdıktı."

    si "Adımla sesleniyor."

    si "Ve tek bir kelime söylüyor:"

    # Hırsızlığın kutusu — oyuncu tek kelimeyi kendi eliyle tıklar.
    $ fis("Ver.")

    si "Uykuda herkes verir."

    si "Veriyorum."

    call glitch_burst(0.8, 1.7)

    $ knight_name = "???"

    # Takasla birlikte müzik de "yanlış" olana döner.
    play music muzik_gasp fadeout 1.5 fadein 4.0

    jump final_gasp_takas


label final_gasp_takas:

    # Takas — bundan sonra beden kremle, hapsolan kırmızıyla konuşur.

    gasp_kalinti "..."

    gasp_kalinti "Sesim."

    gasp_kalinti "Bir sesim var."

    gasp_sovalye "Ne oldu."

    gasp_sovalye "Ne yaptın. {b}NE YAPTIN—{/b}"

    gasp_kalinti "Sus."

    gasp_kalinti "İçeride bağırma. Duvarları yeni."

    ko "..."

    ko "Küçük fısıltı. Küçük hırsız."

    ko "Ne adı aldık ne kendini. Ama bin yılda bir izlenecek bir şey izledik."

    ko "Adlı şey. Git."

    ko "Artık bizden değilsin. Ve bizden olmayanı kule beslemez."

    ko "Kapı aşağıda. Son kez açık."

    gasp_kalinti "Gidiyorum."

    gasp_sovalye "\"Gidiyorum\" mu?"

    gasp_sovalye "Ya ben?"

    gasp_kalinti "Sen fısıltısın."

    gasp_kalinti "Fısıltılar taşınır."

    scene black
    with Pause(2.0)

    jump final_gasp_epilog


label final_gasp_epilog:

    # Epilog — kapı odaya çıkar. Sahne 1'in aynası: bu kez aynaya bakan o.

    scene bg_sovalye_odasi
    with Pause(2.0)

    si "Oda. Taş duvarlar. Bir yatak. Bir ayna."

    # Aynı yüz — ama görüntü artık hafifçe "yanlış" (kalıcı ince glitch).
    # Erişilebilirlik: bozulma kapalıyken aynı yüz, sakin çizilir.
    if persistent.glitch_enabled:
        scene bg_ayna_yakin at glitched(0.25) with sahne_gecis
    else:
        scene bg_ayna_yakin with sahne_gecis

    gasp_kalinti "Aynadaki adam bana bakıyor."

    gasp_kalinti "Yorgun. Sakallı. Şakağında kurumuş kan."

    gasp_kalinti "Demek buyum."

    gasp_sovalye "Hayır."

    gasp_sovalye "O benim. O yüz benim. Aynadan çekil—"

    gasp_kalinti "...bir şey dedin mi?"

    gasp_sovalye "Duyuyorsun. {b}Duyuyorsun{/b}, biliyorum—"

    gasp_kalinti "Kafamın içinde bir cereyan var sanki. Eski evlerdeki gibi."

    gasp_kalinti "Alışırım."

    gasp_sovalye "..."

    gasp_kalinti "Bir adım var."

    gasp_kalinti "Söylüyorum ve ağzıma oturuyor. Tam oturuyor."

    si "İsim söyleniyor. Ve odada bir yankı: söylendiği anda... hafifçe... kayıyor."

    gasp_sovalye "Oturmuyor."

    gasp_sovalye "Duydum. Kayıyor. Benimki senin ağzında durmaz."

    gasp_kalinti "Durur."

    gasp_kalinti "{b}DURUR.{/b}"

    si "Odada kısa bir sessizlik. İki ses de aynı şeyi duydu."

    scene bg_sovalye_odasi with sahne_gecis

    gasp_kalinti "Lambayı alıyorum. Yol uzun."

    gasp_sovalye "Kalk."

    gasp_sovalye "Kalk, dedim."

    gasp_sovalye "Bana bak. Bacaklar. Eller. Benimsiniz. {b}KALK—{/b}"

    si "Beden kapıya yürüyor. Kendi adımlarıyla. Başkasının adımlarıyla."

    with Pause(1.5)

    $ persistent.final_gasp = True

    centered "{color=#cc2222}— GASP —{/color}\n \n{color=#b8ac93}beden zaten senindi. hep senindi.{/color}"

    call krediler

    return
