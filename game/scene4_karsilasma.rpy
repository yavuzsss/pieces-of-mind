# scene4_karsilasma.rpy — Pieces of Mind
# Sahne 4: Karşılaşma — Sönmüş Şövalye.
# Fısıltısı gitmiş, alevi ölmek üzere olan eski bir taşıyıcı. Şövalyenin
# olası geleceği. Lore: fısıltılar "yer" bekler; isim fısıltıya verilmemeli.
# Yeni mekanikler: isyan (Fısıltı'ya karşı gelme), kılıç (ilk eşya),
# alev_kucuk (kalıcı kayıp). CHA zarı dramatik ilk kullanımını yapar.

# Sönmüş Şövalye — soluk, kuru ses.
define sk = Character("Sönmüş", color="#8a8378", what_color="#8a8378",
                      ctc="ctc_blink", ctc_position="nestled")

# Fısıltı'ya kaç kez açıkça karşı gelindi. İleride sonuçları olacak.
default isyan = 0

# Alev kalıcı olarak küçüldü mü? (dünya daralır; ileriki sahneler kullanır)
default alev_kucuk = False

# Paslı kılıç alındı mı?
default kilic_var = False

# Sönmüş'e "ne istiyor" sorusu soruldu mu? (menü tekrarı için)
default sahne4_soruldu = False


################################################################################
## Yaklaşma — Fısıltı hâlâ sessiz
################################################################################

label sahne4_karsilasma:

    si "Işık yaklaşıyor. Ben de ona."

    s "Neden yaklaşıyorum?"

    si "Fısıltı hâlâ sessiz. Kafamın içi ilk defa bu kadar boş."

    s "Yalnızlık böyle bir şeymiş demek."

    # Karşılaşma odası: yuvarlak, taş, lekeli zemin.
    scene bg_zindan_arena with sahne_gecis

    si "Işık köşeyi dönüyor. Ve ikimiz de duruyoruz."

    si "Burası bir oda. Yuvarlak, taş. Zeminindeki lekeler eski ve kahverengi."

    si "Bir adam. Zırhı paslı, kayışlarından dökülüyor."

    si "Elinde bir lamba. Benimkinin eşi."

    s "Ama alevi... avuç içi kadar. Ölmek üzere."

    si "Yüzü kurumuş toprak gibi çatlamış. Gözleri iki kör kuyu."

    sk "..."

    sk "Yeni."

    sk "Yenisin. Alevin gür."

    s "Kimsin?"

    si "Kuru bir ses çıkarıyor. Gülüyor olabilir."

    sk "Kim yok. Kim çoktan bitti."

    sk "Ben sadece... kaldım."

    jump sahne4_tanisma


label sahne4_tanisma:

    si "Başını yana eğiyor. Kulak kabartır gibi."

    sk "Kafan. Dolu mu hâlâ?"

    s "...ne?"

    sk "İçindeki. Konuşan. Tatlı sözler fısıldayan."

    s "Sen nereden—"

    sk "Bende de vardı."

    sk "Bir gün sustu. Ve bir daha konuşmadı."

    sk "Sustuğu gün... dökülmeye başladım."

    si "Çatlak yüzünü ışığa çeviriyor. Çatlakların içi boş."

    sk "İsmimi o götürdü. Yüzümü o götürdü."

    sk "Alevim de peşinden gitti."

    jump sahne4_istek


################################################################################
## İstek — Fısıltı geri döner
################################################################################

label sahne4_istek:

    si "Bir adım atıyor. Lambası titriyor."

    sk "Alevinden ver."

    sk "Bir nefes. Bir nefes yeter."

    si "Elini uzatıyor. Parmakları kavruk dallar gibi."

    call glitch_burst(0.3, 0.9, shake=False)

    f "Hayır."

    s "...döndün."

    f "Geri çekil. Alevler birbirine değmemeli."

    s "Neden?"

    f "Değmemeli."

    jump sahne4_secim


label sahne4_secim:

    menu:
        f "Ne fısıldayacaksın?"

        "«Geri çekil de. Alevi koru.»":
            jump sahne4_geri_cekil

        "«Ona alevden ver.»":
            jump sahne4_alev_ver

        "«Önce sor: içindeki şey ne istiyor?»" if not sahne4_soruldu:
            jump sahne4_sor


################################################################################
## Soru — Fısıltı'nın beklediği şey
################################################################################

label sahne4_sor:

    $ sahne4_soruldu = True

    s "İçimdeki şey... ne istiyor benden?"

    si "Sönmüş adam duruyor. Kör kuyular bana dönüyor."

    sk "İstemek."

    sk "Onlar istemez. Beklerler."

    s "Neyi bekler?"

    sk "Yer."

    sk "Senden geriye kalan yeri."

    f "Saçmalıyor. Aklı, alevinden önce sönmüş."

    s "İlk defa bu kadar hızlı cevap verdin."

    f "..."

    jump sahne4_secim


################################################################################
## Dal A — Geri Çekil (CHA / ETKİ zarı)
################################################################################

label sahne4_geri_cekil:

    s "Geri çekil."

    si "Sesime, benim olmayan bir ağırlık biniyor."

    s "Alevimden uzak dur."

    # --- CHA zarı — DC 13 ---
    call roll_dice("CHA", 13)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne4_geri_krit_basari
    elif sonuc.crit_fail:
        jump sahne4_geri_krit_fiyasko
    elif sonuc.success:
        jump sahne4_geri_basari
    else:
        jump sahne4_geri_basarisiz


label sahne4_geri_krit_basari:

    # Doğal 20 — iki ses birden konuşur; Sönmüş dehşetle çekilir. Kılıç kalır.
    si "Sönmüş adam donuyor."

    sk "O ses."

    sk "İkiniz birden konuştunuz."

    si "Geri geri gidiyor. Kavruk eli göğsünde, kalkan gibi."

    sk "Bende de öyle başlamıştı."

    si "Karanlığa karışmadan önce duruyor. Kemerinden bir şey çözüyor."

    si "Taşın üstüne bırakıyor: bir kılıç. Paslı, kınsız. Ama kılıç."

    sk "Kuleye silahsız gidilmez. Bana artık... yük."

    $ kilic_var = True

    centered "{color=#f5e9d0}KILIÇ ALINDI{/color}"

    si "Kabzayı kavrıyorum. Ellerim onu tanıyor."

    jump sahne4_son


label sahne4_geri_basari:

    # Başarı — Sönmüş çekilir; kuleyi anar.
    si "Sönmüş adam sallanıyor. İleri... sonra geri."

    sk "Gür alev. Gür ses."

    sk "Benim de sesim gürdü. Bir zamanlar."

    si "Dönüyor. Sürüklenen adımlarla, karanlığa."

    sk "Kuleye gidiyorsan... acele et. Alevler kulede daha yavaş ölür."

    si "Işığı köşede kayboluyor. Küçük, kırmızı, yalnız."

    s "Bir gün o... ben miyim?"

    jump sahne4_son


label sahne4_geri_basarisiz:

    # Başarısızlık — üstüne atlar; zorunlu STR boğuşması.
    si "Kör kuyular kısılıyor."

    sk "Hayır. HAYIR. Beklemek bitti."

    si "Üstüme atılıyor. Kavruk parmaklar lambanın sapını buluyor."

    # --- Zorunlu STR zarı — DC 12 ---
    call roll_dice("STR", 12)
    $ sonuc2 = _return

    if sonuc2.crit_fail:
        jump sahne4_bogusma_olum
    elif sonuc2.success:
        jump sahne4_bogusma_zafer
    else:
        jump sahne4_bogusma_bedel


label sahne4_bogusma_zafer:

    si "Bileğini yakalıyorum. Kuru dal gibi — buruyorum."

    si "Çatırdıyor. İnsan sesi değil; eski kapı sesi."

    si "Geriliyor. İki büklüm, lambasını göğsüne bastırıyor."

    sk "Bekleyeceğim. Karanlıkta."

    sk "Hepiniz sonunda karanlığa iniyorsunuz."

    si "Karanlık onu geri alıyor."

    jump sahne4_son


label sahne4_bogusma_bedel:

    # Lambayı kurtarır ama alev kalıcı olarak küçülür.
    si "Parmaklar sapı kavrıyor. Çekiyor."

    si "Lamba aramızda. Alev savruluyor, küçülüyor—"

    s "Duvarlar. Duvarlar yaklaşıyor."

    si "Dizimi karnına gömüyorum. Katlanıyor. Lambayı göğsüme çekiyorum."

    si "Alev doğruluyor. Ama eski boyunda değil."

    s "Artık değil."

    $ alev_kucuk = True

    centered "{color=#cc2222}ALEV KÜÇÜLDÜ{/color}"

    si "Sönmüş adam, dökülen parçalarını toplaya toplaya karanlığa emekliyor."

    jump sahne4_son


label sahne4_bogusma_olum:

    # Doğal 1 — birlikte karanlığa.
    si "Parmaklar bileklerime kilitleniyor. Kuru. Ama demir gibi."

    sk "O zaman ikimiz de."

    sk "İkimiz de karanlıkta."

    si "Çekiyor. Işığın çemberi ayaklarımın altından kayıyor."

    s "Alevim. Alevim nerede—"

    f "Hayır. Hayır. {b}HAYIR—{/b}"

    call olum("sönmüş şövalye seni karanlığa çekti")


label sahne4_geri_krit_fiyasko:

    # CHA doğal 1 — lambaya değil, kafaya saldırır: içindekini ister.
    si "Kör kuyular... genişliyor."

    sk "Ses."

    sk "SESİ DUYDUM. İçindekini duydum."

    sk "Onu istiyorum. VER. ONU. BANA."

    si "Lambaya değil. {b}Kafama{/b} atılıyor."

    # --- Zorunlu STR zarı — DC 15 ---
    call roll_dice("STR", 15)
    $ sonuc2 = _return

    if sonuc2.success:

        si "Onu kendimden söküp fırlatıyorum."

        si "Taşa çarpıyor. Parçaları dökülüyor — kuru, gri parçalar."

        si "Doğrulmuyor. Sürünerek, karanlığa."

        sk "Verecektin."

        sk "Bir gün sen de vermek isteyeceksin. O zaman hatırla: verecektin."

        jump sahne4_son

    else:

        si "Parmakları şakaklarıma yapışıyor."

        s "Kafamın içinde bir şey ÇEKİLİYOR—"

        f "BIRAK. O BENİM. {b}O BENİM.{/b}"

        call glitch_burst(0.7, 1.6)

        call olum("içindeki koparılırken beden dayanamadı")


################################################################################
## Dal B — Alevden Ver (isyan: Fısıltı'ya ilk karşı geliş)
################################################################################

label sahne4_alev_ver:

    $ isyan += 1

    s "Yaklaş."

    f "Ne yapıyorsun?"

    s "Bir nefes. Sadece bir nefes."

    f "Değmemeli diyorum. Dur."

    s "Sen sustuğunda ben durmadım. Şimdi de durmuyorum."

    call glitch_burst(0.3, 1.0)

    f "{b}DUR.{/b}"

    si "Durmuyorum."

    si "Lambamı uzatıyorum. Sönmüş adam kendi lambasının camını açıyor."

    si "İki alev birbirine uzanıyor. Ve değiyor."

    call glitch_burst(0.5, 1.2)

    # Vizyon — alevler değince: bütün taşıyıcılar aynı odada uyandı.
    si "Bir an — tek bir an — başka bir yerdeyim."

    s "Bir oda. Taş duvarlar. Bir ayna. Yerde uyanan bir adam."

    s "Adam o. Genç. Yüzü bütün. Ve kafasının içinde bir ses: {i}Kalk.{/i}"

    s "Aynı oda. Benim odam."

    s "{b}Aynı ses.{/b}"

    si "Alevler ayrılıyor."

    si "Onunki artık bir kıvılcım değil; küçük, dik bir alev. Benimki... eksik."

    $ alev_kucuk = True

    centered "{color=#cc2222}ALEV KÜÇÜLDÜ{/color}"

    si "Sönmüş adam alevine bakıyor. Çatlak yüzünde bir şey kıpırdıyor."

    si "Belki bir yüz ifadesiydi. Bir zamanlar."

    sk "Sıcak."

    sk "Unutmuşum."

    jump sahne4_hediye


label sahne4_hediye:

    # Nefese karşılık: uyarı ve kılıç.
    si "Bana doğru eğiliyor. Sesi düşüyor. Fısıltıdan da alçağa."

    sk "Dinle. İçindeki uyurken dinle."

    sk "Adın. Hâlâ bir yerde saklı mı?"

    s "Bilmiyorum. Hatırlamıyorum."

    sk "Bulduğunda... ona söyleme."

    sk "Adını aldığı gün, kalmak için sebebi kalmaz."

    f "Yeter. Gidiyoruz."

    si "Sönmüş adam kemerinden paslı bir kılıç çözüyor. İki eliyle uzatıyor."

    sk "Nefese karşılık. Kuleye silahsız gidilmez."

    $ kilic_var = True

    centered "{color=#f5e9d0}KILIÇ ALINDI{/color}"

    si "Karanlığa dönüyor. Ama adımları... daha az sürükleniyor."

    jump sahne4_son


################################################################################
## Sahne Sonu — Kule
################################################################################

label sahne4_son:

    scene bg_zindan_koridoru with sahne_gecis

    si "Yürümeye devam ediyorum."

    if isyan > 0:

        f "Bana bir daha karşı gelme."

        s "Gelirsem?"

        f "..."

        si "Cevap yok. Ama kafamın içinde bir yerde, bir şey not alıyor."

    elif alev_kucuk:

        f "Alev küçüldü. Daha dikkatli olmalıyız."

        s "Biz. Yine biz."

    else:

        f "İyi iş çıkardın."

        s "İltifat mı bu? Senden?"

        f "Alışma."

    # Merdiven/kule görseli henüz yok — karanlığa dönülür.
    scene black with sahne_gecis

    si "Koridor bir eşiğe açılıyor: geniş, taş bir merdiven. Yukarı."

    si "Ve çok yukarıda, karanlığın inceldiği yerde: pencereler. Sıra sıra, sönük pencereler."

    s "Bir kule. İçindeyiz. Ya da altındayız."

    s "Kule ne, biliyor musun?"

    f "Evet."

    s "Söyleyecek misin?"

    f "Hayır."

    centered "{color=#cc2222}— devam edecek —{/color}"

    return
