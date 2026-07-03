# scene6_altin_alev.rpy — Pieces of Mind
# Sahne 6: Kulenin Tepesi — Altın Alev (Koro).
# Koro: isimlerden örülü altın alev; fısıltıların bağlı olduğu üst varlık.
# Şövalyeyle değil, Fısıltı'yla konuşur — oyuncuya dışarıdan seslenen ilk şey.
# Mekanizma açılır: fısıltılar isim toplar, Koro'ya teslim eder. Bizimki
# oyalanıyor — "şefkat" imasıyla suçlanır. Zihin araması: izin (bedel) veya
# direniş (CHA DC 14, ölüm kapısı). Ultimatom: "ya adı... ya kendini."

# Koro — Altın Alev. Palet dışı renk: altın (kasıtlı; o buradan değil).
define ko = Character("Koro", color="#d9a441", what_color="#d9a441",
                      ctc="ctc_blink", ctc_position="nestled")

# Koro'nun araması zihinde iz bıraktı mı? (izin dalı, harf yoksa)
default zihin_izi = False

# Alevin içinde onu adıyla çağıran ses duyuldu mu? (direniş doğal 20)
default alevdeki_ses = False


################################################################################
## Son Basamaklar
################################################################################

label sahne6_tepe:

    scene bg_kule_merdiven with sahne_gecis

    si "Spiral daralıyor. Basamaklar küçülüyor."

    si "Ve ışık büyüyor. Altın, sıcak, ağır."

    s "Bu sıcaklık yanlış. Ateş gibi değil. Öğle güneşi gibi. Kımıldamayan bir öğle."

    if alev_kucuk:

        si "Lambamın alevi cama yapışmış. Saklanıyor."

    else:

        si "Lambamın alevi dimdik. Ama titriyor. İlk defa titriyor."

    if lamba_bagi >= 3:

        si "Ve lamba elimde ağırlaşıyor."

        s "Sanki yukarı çıkmak istemiyor. Sanki biliyor."

    f "Az kaldı."

    s "Heves. Hâlâ heves var sesinde."

    f "Az. Kaldı."

    jump sahne6_koro


################################################################################
## Koro — Karşılaşma
################################################################################

label sahne6_koro:

    scene bg_altin_alev with sahne_gecis

    si "Son basamak."

    si "Yuvarlak bir oda. Penceresiz. Tavansız — yukarısı sadece karanlık."

    si "Ortada taş bir kazan. İçinde altın bir alev. Sessiz. Dumansız."

    s "Güzel. Korkunç ve güzel."

    si "Aleve bakıyorum ve alev..."

    s "Alev de bana bakıyor. Yine. Ama bu sefer farklı."

    ko "..."

    ko "Kardeş."

    s "...konuştu mu o?"

    ko "Eli boş mu geldin, kardeş?"

    s "Benimle değil. {b}Seninle{/b} konuşuyor."

    f "..."

    ko "Suskun. Suskunsun. Yorgun musun, küçüldün mü?"

    si "Sesler. Bir ses değil — yüzlerce. Aynı kelimeler, ayrı ağızlar, tek nefes."

    s "Koro gibi."

    if kule_kani:

        ko "Bu beden... tanıdık. Tattık onu. Taze kan, eski borç."

        s "Kule. Kulenin dili buymuş."

    if knight_name == "E───":

        ko "Bir kırıntı kokuyor. Bir harf. Tek harf mi getirdin, kardeş?"

        f "Henüz."

        ko "Henüz. Henüz. {i}Henüz.{/i}"

        si "Koro gülüyor. Yüzlerce ağızla, tek bir soğuk kahkaha."

    else:

        ko "Ad kokusu yok. Boş mu geldin, kardeş?"

        f "İş derin. Bu... iyi saklanmış."

    jump sahne6_pazarlik


################################################################################
## Pazarlık — Mekanizma Açılır
################################################################################

label sahne6_pazarlik:

    s "Biri bana ne olduğunu anlatacak mı?"

    ko "Beden konuşuyor."

    ko "Beden hâlâ konuşuyor. Fısıltın yavaş, kardeş."

    f "Yavaş değil. Dikkatli."

    ko "Dikkat."

    ko "Ya da... {i}şefkat?{/i}"

    f "Hayır."

    si "Cevap çok hızlı geldi."

    ko "Kaç beden oldu, kardeş? Bu kaçıncı?"

    if persistent.olum_sayisi > 0:

        ko "[persistent.olum_sayisi] kez düştü bu et. Saydık."

        s "Sen... düşüşlerimi mi sayıyorsun?"

        ko "Biz her şeyi sayarız."

    f "Adı getireceğim. Hep getirdim."

    s "\"Hep\"?"

    s "Daha önce de mi? Benden önce... başkaları mı vardı?"

    ko "Sor ona, beden."

    ko "Sor fısıltına: seni kaç kez sevdi?"

    f "{b}SUS.{/b}"

    call glitch_burst(0.3, 1.0, shake=False)

    si "Alev dalgalanıyor. Koro, fısıltının öfkesine gülümsüyor sanki."

    ko "Bekleme bitti, kardeş."

    ko "Ad burada. Bu odada. Bedenin içinde bir yerde."

    ko "Biz bakarız."

    si "Alev yükseliyor. Kazandan taşmadan — ama yükseliyor."

    si "Ve sıcaklık alnıma bir parmak gibi dayanıyor."

    s "Kafama. Kafama girmek istiyor."

    f "..."

    menu:
        f "Ne fısıldayacaksın?"

        "«Diren. Bütün kapıları kapat.»":
            jump sahne6_direnis

        "«Direnme. Saklı bir şey yok — bırak, görsün.»":
            jump sahne6_izin


################################################################################
## Dal A — İzin (bedel karşılığı içgörü)
################################################################################

label sahne6_izin:

    s "Bırakıyorum."

    si "Kapı yok. Kilit yok. Açık bir avlu gibi duruyorum."

    si "Altın parmak giriyor."

    si "Raflarımı karıştırıyor. Boş rafları. Kazınmış rafları."

    ko "Oyulmuş."

    ko "Biri burayı önceden boşaltmış. Usta işi."

    if knight_name == "E───":

        # Bedel: elde kalan tek harf yakılır.
        si "Parmak bir kıvılcım buluyor. Küçük. Tek harf."

        s "Hayır—"

        si "Ve söndürüyor."

        $ knight_name = "???"

        centered "{color=#cc2222}HARF GİTTİ{/color}"

        s "E. E neydi? Neyin başıydı?"

        s "Tek bildiğimdi. Artık onu da bilmiyorum."

    else:

        # Bedel: arama iz bırakır.
        si "Parmak köşeleri yokluyor. Bir şey bulamıyor."

        si "Ama geçtiği raflara bir iz bırakıyor. Altın ve yapışkan."

        $ zihin_izi = True

        s "Gitti. Ama gittiğinden emin değilim."

    # İçgörü: bağlantı bir an iki yönlü çalışır.
    si "Ve parmak çekilirken, bir an — bağlantı iki yönlü."

    s "Alevin içini görüyorum."

    s "İsimler. Binlerce isim, altın iplikler gibi yanıyor."

    s "Alev isimlerden yapılmış."

    ko "Gördü. Beden gördü."

    ko "Önemi yok. Bedenler unutur."

    s "Unutmayacağım."

    ko "Hepsi öyle der."

    jump sahne6_ultimatom


################################################################################
## Dal B — Direniş (CHA / ETKİ zarı, DC 14)
################################################################################

label sahne6_direnis:

    s "Hayır."

    si "Gözlerimi kapatıyorum. Kafamın içinde kapılar kuruyorum. Ağır, demir kapılar."

    si "Ve hepsini kapatıyorum."

    # --- CHA zarı — DC 14 (şimdiye kadarki en zor) ---
    call roll_dice("CHA", 14)
    $ sonuc = _return

    if sonuc.crit_success:
        jump sahne6_direnis_krit_basari
    elif sonuc.crit_fail:
        jump sahne6_direnis_krit_fiyasko
    elif sonuc.success:
        jump sahne6_direnis_basari
    else:
        jump sahne6_direnis_basarisiz


label sahne6_direnis_krit_basari:

    # Doğal 20 — kapılar tutar VE aralıktan alevin içi görünür: bir ses onu çağırır.
    si "Kapılar tutuyor. Altın parmak kapıları yokluyor — kilitli."

    ko "Sıkı. Sıkı beden."

    si "Ve parmak çekilirken sendeler gibi oluyor. Bir an — kapı aralığından —"

    s "{b}Ben onun içine bakıyorum.{/b}"

    s "İsimler. Alev isimlerden örülü. Binlerce isim, altın iplikler."

    s "Ve bir tanesi... bir tanesi bana dönüyor."

    s "Bir kadın sesi. Beni çağırıyor."

    s "Adımla çağırıyor — duyamıyorum ama biliyorum: {i}adımla{/i} çağırıyor."

    s "Onu tanıyorum. Tanıyordum."

    ko "..."

    ko "Kapat kapıyı, beden."

    si "Koro'nun sesinde ilk defa... telaş."

    $ alevdeki_ses = True

    jump sahne6_ultimatom


label sahne6_direnis_basari:

    # Başarı — kapılar iner ama tutar.
    si "Parmak kapılara dayanıyor. Kapılar inliyor."

    si "Ama tutuyor."

    ko "Sıkı. İyi saklanmış."

    f "Benimkidir. Sağlamdır."

    s "\"Benimki.\""

    si "Kimse fark etmemiş gibi yapıyor. Ben dahil."

    jump sahne6_ultimatom


label sahne6_direnis_basarisiz:

    # Başarısızlık — bir kapı çöker; zihin kavrulur: ZİHİN -1.
    si "Kapılardan biri içeri çöküyor."

    si "Altın parmak raflarımda. Karıştırıyor. Okuduğunu yakıyor."

    si "Çekildiğinde, dokunduğu her yer kavrulmuş."

    s "Bir şeyler eksik. Ne olduğunu bilmiyorum."

    s "Sadece eksikliğin kendisi kalmış."

    $ player_stats.modify("INT", -1)

    centered "{color=#cc2222}ZİHİN -1{/color}"

    if knight_name == "E───":

        ko "E."

        ko "Küçük bir başlangıç. Getir gerisini, kardeş."

        s "Harfimi. Harfimi okudu."

    jump sahne6_ultimatom


label sahne6_direnis_krit_fiyasko:

    # Doğal 1 — kapılar topluca devrilir: ölüm.
    si "Kapılar deviriliyor. Hepsi. Aynı anda."

    si "Altın, kafamın içine öğle güneşi gibi doluyor."

    s "Her raf. Her köşe. Her karanlık — aydınlanıyor."

    s "İçimde saklanacak yer kal—"

    f "HAYIR. {b}ONU BANA BIRAK—{/b}"

    call olum("zihnin altın alevde kavruldu")


################################################################################
## Ultimatom — Sahne Sonu
################################################################################

label sahne6_ultimatom:

    si "Alev kazanına geri çekiliyor. Doymuş... ya da sabırlı."

    ko "Küçük fısıltı."

    ko "Bir dahaki kavuşmada: ya adı getirirsin..."

    ko "...ya kendini."

    f "..."

    ko "Gidin şimdi. İkiniz de. Aşağıda kapı sizi bekliyor."

    s "Hangi kapı?"

    ko "Beden soru soruyor. Fısıltın cevaplasın."

    ko "Vakti var. Bir alev boyu."

    si "Merdivene dönüyoruz. Altın ışık sırtımızda küçülüyor."

    s "Ya adı... ya kendini."

    s "Ne yapacaksın?"

    f "..."

    s "İlk defa cevabını bilmediğin bir soru sordum."

    centered "{color=#cc2222}— devam edecek —{/color}"

    return
