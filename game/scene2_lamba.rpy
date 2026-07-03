# scene2_lamba.rpy — Pieces of Mind
# Sahne 2: Lambaya Yaklaşma.
# Üç dal: dokunma (DEX zarı) / izleme (CHA zarı) / inkâr (bedelli, geri döner).
# Sahnenin sonunda Fısıltı ilk kez "biz" der — niyetinin ilk sezdirilişi.

# Lamba bağı: şövalyenin lambayla kurduğu saplantının şiddeti.
# Lamba lehine her eylem/başarısızlık artırır. İleride sonuçları olacak.
default lamba_bagi = 0

# İnkâr fısıltısı denendi mi? (menüde bir kez görünür)
default sahne2_inkar = False


label sahne2_lamba:

    si "Lambaya doğru bir adım atıyorum."

    si "Sonra bir adım daha. Attığımı fark etmeden."

    s "Ne zaman yürümeye başladım?"

    $ fis("Önemi yok. Yaklaş.")

    si "Masa eski. Ahşabı çatlamış, boyası dökülmüş."

    si "Ama lambanın oturduğu halka tozsuz. Tertemiz."

    s "Ya biri onu her gün kaldırıyor... ya da lamba toz tutmuyor."

    si "Alev kısık. Ama sıcaklığını buradan hissediyorum."

    si "Hayır. Sıcaklık değil bu. Başka bir şey."

    s "Nabız gibi."

    jump sahne2_secim


label sahne2_secim:

    # Üç fısıltı — inkâr bile kurtarıcı değil (düşünceyi lanet ekti).
    menu:

        "«Dokun. Kaldır onu.»":
            jump sahne2_dokun

        "«Dokunma. Sadece izle.»":
            jump sahne2_izle

        "«Boş ver lambayı. O sadece bir lamba.»" if not sahne2_inkar:

            $ sahne2_inkar = True

            s "Sadece bir lamba."

            si "Cümleyi ağzımın içinde çeviriyorum. Tadı yanlış."

            s "Sadece bir... hayır. Değil. Neden değil?"

            si "Düşünce çengel gibi. Çektikçe derine giriyor."

            s "Sen ektin bunu, değil mi? Yoksa ben mi?"

            $ guven_degistir(-1)
            $ stres_degistir(1)

            jump sahne2_secim


################################################################################
## Dal A — Dokunma (DEX / ÇEVİKLİK zarı)
################################################################################

label sahne2_dokun:

    $ lamba_bagi += 1

    s "Elim kendiliğinden uzanıyor."

    si "Sanki karar benim değilmiş gibi. Sanki el başkasının."

    si "Parmaklarım kırmızı cama yaklaşıyor..."

    # --- DEX zarı — DC 12 ---
    call roll_dice("DEX", 12)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne2_dokun_krit_basari
    elif sonuc.crit_fail:
        jump sahne2_dokun_krit_fiyasko
    elif sonuc.success:
        jump sahne2_dokun_basari
    else:
        jump sahne2_dokun_basarisiz


label sahne2_dokun_krit_basari:

    # Doğal 20 — lamba onu kabul eder. Kazınmış yazı tamamen okunur.
    $ lamba_bagi += 1

    si "Parmaklarım sapı buluyor. Cam sıcak ama yakmıyor."

    si "Lambayı kaldırıyorum. Ağırlığı avucuma oturuyor."

    s "Bu ağırlığı tanıyorum."

    s "Bunu daha önce taşıdım. Uzun bir yol boyunca. Kilometrelerce."

    si "Tabanını çeviriyorum. Metale bir şey kazınmış."

    s "Tek kelime: {b}UYUMA{/b}."

    s "El yazısı... benimki. Bunu ben kazımışım."

    $ fis("Gördün mü? O sana ait.")

    jump sahne2_kapi


label sahne2_dokun_basari:

    # Başarı — dikkatli kaldırış, yarı silinmiş yazı.
    si "Parmaklarım sapı buluyor. Yavaş. Dikkatli."

    si "Lambayı kaldırıyorum. Beklediğimden ağır."

    si "Tabanında bir şey var. Kazınmış harfler. Çoğu silinmiş."

    s "...U... MA..."

    s "UYUMA mı? UNUTMA mı? DURMA mı?"

    s "Hangisi olursa olsun — biri bunu bir sebepten kazımış."

    si "Lambayı yerine koyuyorum. Halkasına. Tam oturuyor."

    jump sahne2_kapi


label sahne2_dokun_basarisiz:

    # Başarısızlık — cam yakar; lamba kımıldamaz bile.
    si "Parmaklarım cama değiyor ve—"

    s "Yanıyor!"

    si "Elimi geri çekiyorum. Parmak uçlarım zonkluyor, kızarmış."

    si "Ama asıl tuhafı bu değil."

    s "Lamba kılını bile kıpırdatmadı."

    s "Çarptım ona. Sarsılması gerekirdi. Devrilmesi gerekirdi."

    s "Sanki masaya vidalanmış. Hayır..."

    s "Sanki dünya {i}ona{/i} vidalanmış."

    $ stres_degistir(1)

    jump sahne2_kapi


label sahne2_dokun_krit_fiyasko:

    # Doğal 1 — alev söner. Karanlıkta başka bir şey vardır.
    # (roll_dice doğal 1'de otomatik glitch + stres ekler; devamı buraya düşer.)

    si "Parmaklarım cama değiyor ve alev—"

    si "Sönüyor."

    s "Karanlık. Mutlak karanlık."

    si "Kendi nefesimi duyuyorum. Hızlı. Sığ."

    si "Ve başka bir nefes daha. Yavaş. Derin. Odanın köşesinden."

    s "Karanlıkta biri fısıldadı."

    call glitch_burst(0.5, 1.2)

    s "Ama o... {b}sen değildin{/b}."

    si "Alev, hiçbir şey olmamış gibi yeniden yanıyor."

    si "Oda aynı. Köşe boş. Nefes yok."

    s "Bir daha dokunmayacağım."

    jump sahne2_kapi


################################################################################
## Dal B — İzleme (CHA / ETKİ zarı)
################################################################################

label sahne2_izle:

    si "Ellerimi iki yanıma sabitliyorum. Sadece bakıyorum."

    si "Alev hiç titremiyor."

    s "Odada cereyan var — tozlar uçuşuyor. Ama alev dimdik."

    si "Bakmaya devam ediyorum. Alev de bana bakıyor."

    s "...alev de bana bakıyor?"

    # --- CHA zarı — DC 12 --- (irade: bakışını alevden koparabilmek)
    call roll_dice("CHA", 12)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne2_izle_krit_basari
    elif sonuc.crit_fail:
        jump sahne2_izle_krit_fiyasko
    elif sonuc.success:
        jump sahne2_izle_basari
    else:
        jump sahne2_izle_basarisiz


label sahne2_izle_krit_basari:

    # Doğal 20 — bakışını koparır VE aynadaki sırrı görür.
    si "Bakışımı koparıyorum. Zor oluyor — bataklıktan bacak çeker gibi."

    si "Ve gözüm aynaya takılıyor."

    s "Aynada oda var. Masa var. Ben varım."

    s "Lamba yok."

    si "Aynadaki masanın üstünde, lambanın olması gereken yerde..."

    s "Bir anahtar deliği var. Havada asılı, kapkara bir anahtar deliği."

    $ fis("Bunu görmemeliydin.")

    s "...ne?"

    $ fis("Henüz. Henüz görmemeliydin.")

    # Şövalye, Fısıltı'nın bir şey sakladığını ilk kez duyar.
    $ guven_degistir(-1)

    jump sahne2_kapi


label sahne2_izle_basari:

    # Başarı — bakışını koparır; aynada lambanın yansımadığını fark eder.
    si "Bakışımı koparıyorum. Boynum tutulmuş — ne kadar süre baktım?"

    si "Gözüm aynaya kayıyor. Ve o zaman fark ediyorum."

    s "Aynada oda var. Masa var. Ben varım."

    s "Lamba yok."

    s "Aynadaki masa boş. Alevin ışığı bile yansımıyor."

    si "Aynaya göre bu oda karanlık."

    jump sahne2_kapi


label sahne2_izle_basarisiz:

    # Başarısızlık — trans; kayıp zaman.
    si "Sadece bir dakika izleyeceğim. Sadece bir—"

    si "Gözümü kırpıyorum."

    s "...diz üstündeyim."

    si "Masanın önünde diz çökmüşüm. Elim lambanın camında. Cam sıcak."

    s "Ne zaman yürüdüm? Ne zaman diz çöktüm?"

    si "Ayağa kalkıyorum. Bacaklarım uyuşmuş. Uzun süre öyle kalmışım."

    s "Ve alev... az önce olduğundan bir parmak daha uzun."

    $ lamba_bagi += 1
    $ stres_degistir(1)

    jump sahne2_kapi


label sahne2_izle_krit_fiyasko:

    # Doğal 1 — derin trans: bir anlığına alevin içinden bakar.
    # (roll_dice doğal 1'de otomatik glitch + stres ekler; devamı buraya düşer.)

    si "İzliyorum. İzliyorum. İzli—"

    s "Oda ters."

    s "Hayır. Ters değil. {b}Dışarıdan{/b} bakıyorum."

    s "Alevin içinden. Kırmızı camın arkasından."

    s "Masanın önünde bir adam duruyor. Gözleri boş. Ağzı yarı açık."

    s "O adam benim."

    call glitch_burst(0.6, 1.4)

    si "...duvara yaslanmışım. Kalbim kaburgalarımı dövüyor."

    si "Lamba masasında. Alev kısık. Her şey normal."

    s "Hiçbir şey normal değil."

    $ lamba_bagi += 2

    jump sahne2_kapi


################################################################################
## Birleşme — Kapı ve "biz"
################################################################################

label sahne2_kapi:

    si "Geri çekiliyorum. Bir adım. İki."

    si "İşte o zaman görüyorum."

    s "Duvarda bir kapı var."

    s "Az önce orada değildi. Ya da hep oradaydı da... ben mi görmüyordum?"

    si "Ahşap, demir kuşaklı, sıradan bir kapı. Sıradanlığı rahatsız edici."

    $ fis("Kapı. Gitme vakti.")

    s "Dışarıda ne olduğunu bilmiyorum."

    $ fis("Lambayı al. Onsuz gidemeyiz.")

    s "..."

    s "\"Gidemeyiz\"?"

    call glitch_burst(0.25, 0.8, shake=False)

    s "Biz... kaç kişiyiz?"

    # Şövalye çoğulu yakalar; Fısıltı cevap yerine bastırır.
    $ guven_degistir(-1)
    $ stres_degistir(1)

    $ fis("Al onu.")

    si "Sorumun cevabı gelmiyor. Sadece o iki kelime, kafamın içinde, kendi sesimden daha yüksek."

    si "Elim lambanın sapına uzanıyor."

    # Sahne 3: Kapı ve Koridor (scene3_koridor.rpy)
    jump sahne3_koridor
