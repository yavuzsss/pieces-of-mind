# effects.rpy — Pieces of Mind
# CRT ve glitch efektleri. Görsel varlık gerektirmez; hepsi GLSL shader.
#
# Kullanım:
#   - CRT katmanı otomatik olarak her zaman açıktır (persistent.crt_enabled).
#   - Anlık glitch patlaması:   call glitch_burst(0.4)
#   - Bir görseli glitch'lemek: show lamba at glitched(1.0)   (ileride)


################################################################################
## Ayarlar
################################################################################

# CRT katmanı açık/kapalı (ayarlar menüsüne düğme eklenebilir).
default persistent.crt_enabled = True

# Arka plan geçişleri için standart yavaş çözülme.
define sahne_gecis = Dissolve(1.2)


################################################################################
## Shader'lar
################################################################################

init python:

    ## CRT katmanı — altını örneklemez; tarama çizgisi, vinyet, titreme ve
    ## paraziti yarı saydam siyah olarak üstüne çizer.
    renpy.register_shader("pom.crt",
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;

            // Vinyet: köşeler kararır.
            float d = distance(uv, vec2(0.5));
            float vig = smoothstep(0.40, 0.90, d) * 0.55;

            // Tarama çizgileri (~3 piksellik periyot).
            float pix_y = uv.y * u_model_size.y;
            float scan = (0.5 + 0.5 * sin(pix_y * 2.094)) * 0.16;

            // Düşük frekanslı tüp titremesi.
            float flick = 0.015 * sin(u_time * 47.0)
                        + 0.015 * sin(u_time * 13.7);

            // Film paraziti.
            float n = fract(sin(dot(uv + fract(u_time),
                                    vec2(12.9898, 78.233))) * 43758.5453);
            float noise = n * 0.05;

            float a = clamp(vig + scan + flick + noise, 0.0, 0.85);
            gl_FragColor = vec4(0.0, 0.0, 0.0, a);
        """)

    ## Glitch barları — altını örneklemez; rastgele satırlarda kırmızı/krem
    ## parazit bantları çakar. u_pom_strength ile şiddeti ayarlanır.
    renpy.register_shader("pom.glitchbars",
        variables="""
            uniform float u_time;
            uniform float u_pom_strength;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;
            float t = floor(u_time * 24.0);
            float row = floor(uv.y * 28.0);

            float r1 = fract(sin(dot(vec2(row, t),
                                     vec2(12.9898, 78.233))) * 43758.5453);
            float r2 = fract(sin(dot(vec2(row, t),
                                     vec2(39.3468, 11.135))) * 24634.6345);

            vec3 col = vec3(0.0);
            float a = 0.0;

            if (r1 > 0.82) {
                // Kırmızı bant.
                col = vec3(0.80, 0.13, 0.13);
                a = 0.40 * r2;
            } else if (r1 < 0.06) {
                // Krem bant.
                col = vec3(0.96, 0.91, 0.82);
                a = 0.30 * r2;
            }

            a *= u_pom_strength;
            gl_FragColor = vec4(col * a, a);   // premultiplied alpha
        """)

    ## Görüntü bozma — ALTINI ÖRNEKLER (tex0): yatay dilim kaydırma + RGB
    ## kanal ayrışması. Sprite/arka plan görsellerine uygulanır.
    renpy.register_shader("pom.glitch",
        variables="""
            uniform sampler2D tex0;
            uniform float u_time;
            uniform float u_pom_strength;
            attribute vec2 a_tex_coord;
            varying vec2 v_tex_coord;
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 uv = v_tex_coord;
            float t = floor(u_time * 20.0);
            float band = floor(uv.y * 16.0);

            float r = fract(sin(dot(vec2(band, t),
                                    vec2(12.9898, 78.233))) * 43758.5453);

            // Bazı bantlar yana kayar.
            float shift = (r - 0.5) * 0.08 * u_pom_strength * step(0.72, r);
            vec2 uv2 = vec2(clamp(uv.x + shift, 0.0, 1.0), uv.y);

            // RGB kanal ayrışması.
            float sp = 0.005 * u_pom_strength;
            vec4 c = texture2D(tex0, uv2);
            c.r = texture2D(tex0, vec2(clamp(uv2.x + sp, 0.0, 1.0), uv2.y)).r;
            c.b = texture2D(tex0, vec2(clamp(uv2.x - sp, 0.0, 1.0), uv2.y)).b;

            gl_FragColor = c;
        """)


################################################################################
## Transformlar
################################################################################

# 'pause 0.02 / repeat' döngüsü ekranın sürekli yeniden çizilmesini sağlar;
# u_time'a bağlı shader'ların akması için gereklidir.

transform crt_fx:
    mesh True
    shader "pom.crt"
    block:
        pause 0.03
        repeat

transform glitchbars_fx(strength=1.0):
    mesh True
    shader "pom.glitchbars"
    u_pom_strength strength
    block:
        pause 0.02
        repeat

# Herhangi bir görseli glitch'lemek için: show lamba at glitched(1.0)
transform glitched(strength=1.0):
    mesh True
    shader "pom.glitch"
    u_pom_strength strength
    block:
        pause 0.02
        repeat


################################################################################
## Ekranlar
################################################################################

# Sürekli açık CRT katmanı — her şeyin üstünde (zar paneli dahil).
screen crt_overlay():
    zorder 1000
    if persistent.crt_enabled:
        add Solid("#ffffff") at crt_fx

init python:
    config.overlay_screens.append("crt_overlay")


# Anlık glitch patlaması (glitch_burst etiketi gösterir/gizler).
screen glitch_flash(strength=1.0):
    zorder 1100
    add Solid("#ffffff") at glitchbars_fx(strength)


################################################################################
## Yardımcı Etiket
################################################################################

# Kısa glitch patlaması: parazit bantları + yatay sarsıntı.
#     call glitch_burst           -> varsayılan 0.35s
#     call glitch_burst(0.6, 1.5) -> daha uzun, daha şiddetli
label glitch_burst(duration=0.35, strength=1.0, shake=True):

    play sound glitch_sfx
    show screen glitch_flash(strength)
    if shake:
        with hpunch
    $ renpy.pause(duration, hard=True)
    hide screen glitch_flash

    return
