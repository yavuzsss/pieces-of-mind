# script.rpy — Pieces of Mind
# Karakter tanımları + Sahne 1: Uyanış — siyah ekran, sadece metin.
# Fısıltı'nın TÜM replikleri fis() kutularıyla oyuncu tarafından seçilir
# (fisilti.rpy — Milk mekaniği). İlk ZEKÂ zarı burada atılır.

################################################################################
## Karakterler
################################################################################

# Şövalye henüz adını bilmiyor; adı hatırladıkça değişecek.
default knight_name = "???"

# Fısıltı — oyuncunun sesi. Şövalyenin zihnindeki lanet. Kırmızı, italik.
# Sahne içinde konuşmaz: replikleri fis() kutularından seçilir. Bu tanım
# ölüm monoloğu (death.rpy) ve geçmiş (history) kayıtları için durur.
define f = Character("Fısıltı", color="#cc2222", what_color="#cc2222",
                     what_italic=True,
                     ctc="ctc_blink", ctc_position="nestled")

# Yorgun Şövalye — krem tonunda.
define s = Character("[knight_name]", color="#f5e9d0", what_color="#f5e9d0",
                     ctc="ctc_blink", ctc_position="nestled")

# Şövalyenin iç sesi / algısı — soluk krem, isimsiz.
define si = Character(None, what_color="#b8ac93", what_italic=True,
                      ctc="ctc_blink", ctc_position="nestled")


################################################################################
## Sahne 1 — Uyanış
################################################################################

label start:

    # Yeni koşu: permadeath kimliği (death.rpy).
    $ run_id = yeni_kosu_id()

    # Ölüm görmüş oyuncu görülmüş metni geçebilir (tekrar.rpy).
    $ gec_uygula()

    play music muzik_karanlik fadein 3.0

    scene black
    with Pause(1.0)

    si "...soğuk."

    si "Taş. Sırtımın altında taş var."

    si "Ne kadar zamandır buradayım?"

    s "..."

    s "Kalkmalıyım."

    # Fısıltı ilk kez konuşur — oyuncunun ilk kutusu.
    # Lanet geçmiş ölümleri hatırlar; şövalye hatırlamaz.
    call glitch_burst(0.15, 0.6, shake=False)
    if persistent.olum_sayisi > 0:
        $ fis("Kalk. Yeniden.")
    else:
        $ fis("Kalk.")

    s "...?"

    s "Bu... benim sesim miydi?"

    si "Elbette benim sesimdi. Başka kimin olacak?"

    si "Ayağa kalkıyorum. Eklemlerim paslı menteşeler gibi gıcırdıyor."

    # Göz alışıyor: oda görünür olur.
    scene bg_sovalye_odasi with sahne_gecis

    si "Oda küçük. Duvarlar taş. Pencere yok."

    si "Köşede bir yatak — az önce üstünde değildim. Yerde uyumuşum."

    si "Ve karşımda... bir ayna."

    jump sahne1_ayna


label sahne1_ayna:

    # Ayna yakın planı — oyunun ilk yüzü.
    scene bg_ayna_yakin with sahne_gecis

    s "Aynadaki adam bana bakıyor."

    s "Yorgun. Sakallı. Şakağında kurumuş kan."

    s "Demek buyum. Daha kötüsü olabilirdi."

    s "Nasıl olabilirdi bilmiyorum. Ama olabilirdi."

    s "Bu yüzü tanıyorum. Tanımam gerekiyor."

    s "Ama... ismi yok. Yüzün ismi yok."

    s "Kimim ben?"

    s "Neden buradayım?"

    # Dikkat dağılması — Fısıltı'nın ektiği düşünce.
    si "Odaklanmalıyım. Kim olduğumu—"

    call glitch_burst(0.2, 0.7, shake=False)
    $ fis("Lamba.")

    # Dikkat aynadan kopar — oda geri gelir.
    scene bg_sovalye_odasi with sahne_gecis

    si "...masanın üstünde bir gaz lambası var."

    si "Camı kırmızı. Alevi kısık ama sönmüyor."

    s "Bu lamba... özel."

    s "Neden özel olduğunu bilmiyorum ama özel. Bundan eminim."

    s "Bu odada önemli olan tek şey o. Belki de dünyada önemli olan tek şey."

    si "...ne?"

    si "Bu düşünce nereden geldi? Ben... ben aynaya bakıyordum."

    s "Kim olduğumu bulmaya çalışıyordum."

    jump sahne1_hatirlama


label sahne1_hatirlama:

    # Üç fısıltı — hiçbiri kurtarıcı değil.
    menu:

        "«Hatırla. Ellerine bak. Ellerin bilir.»":

            s "Ellerim..."

            si "Avuçlarım nasır içinde. Parmaklarım bir şeyi kavramaya alışkın."

            si "Bir şeyin... kabzasını."

        "«Hatırla. Kan. Şakağındaki kan nereden geldi?»":

            s "Kan..."

            si "Şakağıma dokunuyorum. Kurumuş, pul pul."

            si "Bir darbe. Düşüş. Metalin metale çarptığı bir ses... uzakta."

            $ stres_degistir(1)

        "«Boş ver. Kim olduğun önemli değil.»":

            s "..."

            s "Önemli değil mi?"

            si "Cümle göğsümde bir yere oturuyor. Soğuk bir taş gibi."

            s "Belki haklısın. Belki isimsiz de yürünür."

            s "Ama yine de deneyeceğim. Sana rağmen."

            $ guven_degistir(-1)
            $ stres_degistir(1)

    s "Hatırlamaya çalışıyorum."

    si "Zihnimin karanlık bir dehlizine uzanıyorum. Parmak uçlarımda bir şey var, kıpırdıyor..."

    # --- İLK ZAR: ZEKÂ — DC 12 --- (görsel panel: dice.rpy)
    call roll_dice("ZEKA", 12)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne1_hatirlama_krit_basari
    elif sonuc.crit_fail:
        jump sahne1_hatirlama_krit_fiyasko
    elif sonuc.success:
        jump sahne1_hatirlama_basari
    else:
        jump sahne1_hatirlama_basarisiz


label sahne1_hatirlama_krit_basari:

    # Doğal 20 — canlı, sarsıcı bir anı parçası.
    si "Dehliz aydınlanıyor."

    s "Bir savaş alanı. Çamur. Yağmur."

    s "Sırtımda zırh var — ağırlığını hatırlıyorum, omuzlarımı nasıl çökerttiğini."

    s "Biri bana bağırıyor. Bir isim. Benim ismim."

    s "Duyamıyorum ama... bir yemin ettiğimi biliyorum. Birine. Bir şey için."

    s "Ben bir şövalyeyim. Ya da... öyleydim."

    $ fis("Güzel. Hatırlıyorsun.")

    s "Bu ses yine geldi. İçimden ama... içimden değil."

    jump sahne1_son


label sahne1_hatirlama_basari:

    # Normal başarı — küçük ama gerçek bir kırıntı.
    si "Karanlıkta bir şey parlıyor."

    s "Metal. Soğuk metal, avucumun içinde."

    s "Bir kılıç kabzası. Ona sarılmışım, saatlerce, günlerce."

    s "Ben... savaşan biriydim. Bir asker? Bir şövalye?"

    s "Kesin değil. Ama ellerim kılıç tutmayı unutmamış."

    $ fis("Bu bir başlangıç.")

    jump sahne1_son


label sahne1_hatirlama_basarisiz:

    # Başarısızlık — dehliz boş, sadece uğultu.
    si "Uzanıyorum... uzanıyorum..."

    s "Hiçbir şey."

    s "Karanlık dehliz sadece uğultuyla dolu. Arı kovanı gibi."

    s "Başım zonkluyor. Zorladıkça uğultu büyüyor."

    si "Bırakıyorum. Şimdilik."

    $ fis("Zorlamayacağız. Henüz.")

    $ stres_degistir(1)

    jump sahne1_son


label sahne1_hatirlama_krit_fiyasko:

    # Doğal 1 — lanet kıpırdanır. Rahatsız edici bir an.
    si "Uzanıyorum ve—"

    s "Bir şey uzandığım yerden {b}geri{/b} uzanıyor."

    s "Soğuk. Islak. Parmaklarımı sayıyor."

    s "GERİ ÇEK. GERİ ÇEK. GERİ—"

    si "...duvara yaslanmışım. Nefes nefeseyim."

    s "Bir daha oraya bakmayacağım."

    si "Gözlerim kendiliğinden lambaya kayıyor. Kırmızı cam. Kısık alev."

    s "Lamba güvenli. Lamba... özel."

    jump sahne1_son


label sahne1_son:

    si "Oda hâlâ aynı. Taş duvarlar, yatak, ayna."

    si "Ve masanın üstünde, kısık alevli kırmızı lamba."

    si "Sanki bekliyor."

    $ fis("Devam edeceğiz.")

    # Sahne 2: Lambaya Yaklaşma (scene2_lamba.rpy)
    jump sahne2_lamba
