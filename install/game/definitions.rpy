define persistent.demo = False
define persistent.steam = False
define config.developer = False

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("music_poem", mixer="music", tight=True)
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        if persistent.do_not_delete: return
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        try: renpy.file("../characters/monika.chr")
        except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        try: renpy.file("../characters/natsuki.chr")
        except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        try: renpy.file("../characters/yuri.chr")
        except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        try: renpy.file("../characters/sayori.chr")
        except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())
    def restore_relevant_characters():
        restore_all_characters()
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            delete_character("sayori")
        elif persistent.playthrough == 3:
            delete_character("sayori")
            delete_character("natsuki")
            delete_character("yuri")
        elif persistent.playthrough == 4:
            delete_character("monika")
    def pause(time=None):
        if not time:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            return
        if time <= 0: return
        renpy.pause(time)




# Music
define audio.t1 = "mod_assets/bgm/main_menu.mp3"  #Main theme (title)
define audio.t2 = "<loop 4.499>bgm/2.ogg"   #Sayori theme
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"   #Main theme (in-game)
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"  #Poem minigame
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"   #Sharing poems
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"  #Yuri/Natsuki theme
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"   #Causing trouble
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"   #Trouble resolved
define audio.t9 = "<loop 3.172>bgm/9.ogg"   #Emotional
define audio.t9g = "<loop 1.532>bgm/9g.ogg" #207% speed
define audio.t10 = "<loop 5.861>bgm/10.ogg"   #Confession
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.tmonika = "<loop 4.444>bgm/5_monika.ogg"
define audio.tsayori = "<loop 4.444>bgm/5_sayori.ogg"
define audio.tnatsuki = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.tyuri = "<loop 4.444>bgm/5_yuri.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

# Backgrounds
image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "mod_assets/gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_evening = "mod_assets/images/bg/gloomyclub.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg bedroom_night = "mod_assets/images/bg/bedroom_night.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg house_night = "mod_assets/images/bg/house_night.png"
image bg kitchen = "bg/kitchen.png"
image bg courtyard = "mod_assets/images/bg/courtyard.png"
image bg living_room = "mod_assets/images/bg/living_room.png"
image bg living_room_night = "mod_assets/images/bg/living_room_night.png"
image bg residential_snow = "mod_assets/images/bg/residential_snow.png"
image bg yuri_house_evening = "mod_assets/images/bg/house2evening.png"
image bg hallway = "mod_assets/images/bg/hallway.png"
image bg yuri_bedroom_day = "mod_assets/images/bg/bedroom3.png"
image bg yuri_bedroom_night = "mod_assets/images/bg/bedroom3night.png"
image bg yuri_house_day = "mod_assets/images/bg/house2.png"
image bg yuri_house_night = "mod_assets/images/bg/house2night.png"
image bg cafe = "mod_assets/images/bg/cafe.png"
image bg hospital = "mod_assets/images/bg/hospital.png"
image bg hospital_room = "mod_assets/images/bg/hospital_room.jpg"
image bg yuri_kitchen = "mod_assets/images/bg/kitchen2.png"
image bg bathroom = "mod_assets/images/bg/toilet_03.jpg"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0
        #1.0
        #linear 1.0 alpha 0.0

# Sayori

image sayori 1:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_010.png"
    pause 5
    repeat
image sayori 1a:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1/sayori_1_010.png"
    pause 5
    repeat
image sayori 1b:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1b/sayori_1b_010.png"
    pause 5
    repeat
image sayori 1c:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1c/sayori_1c_010.png"
    pause 5
    repeat
image sayori 1d:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1d/sayori_1d_010.png"
    pause 5
    repeat
image sayori 1e:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1e/sayori_1e_010.png"
    pause 5
    repeat
image sayori 1f:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1f/sayori_1f_010.png"
    pause 5
    repeat
image sayori 1g:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1g/sayori_1g_010.png"
    pause 5
    repeat
image sayori 1h:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1h/sayori_1h_010.png"
    pause 5
    repeat
image sayori 1i:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1i/sayori_1i_010.png"
    pause 5
    repeat
image sayori 1j:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1j/sayori_1j_010.png"
    pause 5
    repeat
image sayori 1k:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1k/sayori_1k_010.png"
    pause 5
    repeat
image sayori 1l:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1l/sayori_1l_010.png"
    pause 5
    repeat
image sayori 1m:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1m/sayori_1m_010.png"
    pause 5
    repeat
image sayori 1n:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1n/sayori_1n_010.png"
    pause 5
    repeat
image sayori 1o:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1o/sayori_1o_010.png"
    pause 5
    repeat
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1t/sayori_1t_010.png"
    pause 5
    repeat
image sayori 1u:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1u/sayori_1u_010.png"
    pause 5
    repeat
image sayori 1v:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1v/sayori_1v_010.png"
    pause 5
    repeat
image sayori 1w:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1w/sayori_1w_010.png"
    pause 5
    repeat
image sayori 1x:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1x/sayori_1x_010.png"
    pause 5
    repeat
image sayori 1y:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1y/sayori_1y_010.png"
    pause 5
    repeat

image sayori 2:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2/sayori_2_010.png"
    pause 5
    repeat
image sayori 2a:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2a/sayori_2a_010.png"
    pause 5
    repeat
image sayori 2b:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2b/sayori_2b_010.png"
    pause 5
    repeat
image sayori 2c:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2c/sayori_2c_010.png"
    pause 5
    repeat
image sayori 2d:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2d/sayori_2d_010.png"
    pause 5
    repeat
image sayori 2e:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2e/sayori_2e_010.png"
    pause 5
    repeat
image sayori 2f:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2f/sayori_2f_010.png"
    pause 5
    repeat
image sayori 2g:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2g/sayori_2g_010.png"
    pause 5
    repeat
image sayori 2h:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2h/sayori_2h_010.png"
    pause 5
    repeat
image sayori 2i:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2i/sayori_2i_010.png"
    pause 5
    repeat
image sayori 2j:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2j/sayori_2j_010.png"
    pause 5
    repeat
image sayori 2k:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2k/sayori_2k_010.png"
    pause 5
    repeat
image sayori 2l:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2l/sayori_2l_010.png"
    pause 5
    repeat
image sayori 2m:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2m/sayori_2m_010.png"
    pause 5
    repeat
image sayori 2n:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2n/sayori_2n_010.png"
    pause 5
    repeat
image sayori 2o:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2o/sayori_2o_010.png"
    pause 5
    repeat
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2t/sayori_2t_010.png"
    pause 5
    repeat
image sayori 2u:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2u/sayori_2u_010.png"
    pause 5
    repeat
image sayori 2v:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2v/sayori_2v_010.png"
    pause 5
    repeat
image sayori 2w:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2w/sayori_2w_010.png"
    pause 5
    repeat
image sayori 2x:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2x/sayori_2x_010.png"
    pause 5
    repeat
image sayori 2y:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2y/sayori_2y_010.png"
    pause 5
    repeat

image sayori 3:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3/sayori_3_010.png"
    pause 5
    repeat
image sayori 3a:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3a/sayori_3a_010.png"
    pause 5
    repeat
image sayori 3b:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3b/sayori_3b_010.png"
    pause 5
    repeat
image sayori 3c:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3c/sayori_3c_010.png"
    pause 5
    repeat
image sayori 3d:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3d/sayori_3d_010.png"
    pause 5
    repeat
image sayori 3e:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_010.png"
    pause 5
    repeat
image sayori 3f:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3e/sayori_3e_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_010.png"
    pause 5
    repeat
image sayori 3g:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_010.png"
    pause 5
    repeat
image sayori 3h:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3f/sayori_3f_010.png"
    pause 5
    repeat
image sayori 3i:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3h/sayori_3h_010.png"
    pause 5
    repeat
image sayori 3j:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3i/sayori_3i_010.png"
    pause 5
    repeat
image sayori 3k:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3k/sayori_3k_010.png"
    pause 5
    repeat
image sayori 3l:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3l/sayori_3l_010.png"
    pause 5
    repeat
image sayori 3m:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3m/sayori_3m_010.png"
    pause 5
    repeat
image sayori 3n:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3n/sayori_3n_010.png"
    pause 5
    repeat
image sayori 3o:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3o/sayori_3o_010.png"
    pause 5
    repeat
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3t/sayori_3t_010.png"
    pause 5
    repeat
image sayori 3u:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3u/sayori_3u_010.png"
    pause 5
    repeat
image sayori 3v:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3v/sayori_3v_010.png"
    pause 5
    repeat
image sayori 3w:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3w/sayori_3w_010.png"
    pause 5
    repeat
image sayori 3x:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3x/sayori_3x_010.png"
    pause 5
    repeat
image sayori 3y:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3y/sayori_3y_010.png"
    pause 5
    repeat

image sayori 4:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4/sayori_4_010.png"
    pause 5
    repeat
image sayori 4a:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4a/sayori_4a_010.png"
    pause 5
    repeat
image sayori 4b:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4b/sayori_4b_010.png"
    pause 5
    repeat
image sayori 4c:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4c/sayori_4c_010.png"
    pause 5
    repeat
image sayori 4d:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4d/sayori_4d_010.png"
    pause 5
    repeat
image sayori 4e:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4e/sayori_4e_010.png"
    pause 5
    repeat
image sayori 4f:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4f/sayori_4f_010.png"
    pause 5
    repeat
image sayori 4g:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4g/sayori_4g_010.png"
    pause 5
    repeat
image sayori 4h:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4h/sayori_4h_010.png"
    pause 5
    repeat
image sayori 4i:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4i/sayori_4i_010.png"
    pause 5
    repeat
image sayori 4j:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4j/sayori_4j_010.png"
    pause 5
    repeat
image sayori 4k:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4k/sayori_4k_010.png"
    pause 5
    repeat
image sayori 4l:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4l/sayori_4l_010.png"
    pause 5
    repeat
image sayori 4m:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4m/sayori_4m_010.png"
    pause 5
    repeat
image sayori 4n:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4n/sayori_4n_010.png"
    pause 5
    repeat
image sayori 4o:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4o/sayori_4o_010.png"
    pause 5
    repeat
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4t/sayori_4t_010.png"
    pause 5
    repeat
image sayori 4u:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4u/sayori_4u_010.png"
    pause 5
    repeat
image sayori 4v:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4v/sayori_4v_010.png"
    pause 5
    repeat
image sayori 4w:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4w/sayori_4w_010.png"
    pause 5
    repeat
image sayori 4x:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4x/sayori_4x_010.png"
    pause 5
    repeat
image sayori 4y:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4y/sayori_4y_010.png"
    pause 5
    repeat

image sayori 5:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5/sayori_5_010.png"
    pause 5
    repeat
image sayori 5a:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5a/sayori_5a_010.png"
    pause 5
    repeat
image sayori 5b:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5b/sayori_5b_010.png"
    pause 5
    repeat
image sayori 5c:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5c/sayori_5c_010.png"
    pause 5
    repeat
image sayori 5d:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_5d/sayori_5d_010.png"
    pause 5
    repeat

image sayori 1ba:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1ba/sayori_1ba_010.png"
    pause 5
    repeat
image sayori 1bb:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bb/sayori_1bb_010.png"
    pause 5
    repeat
image sayori 1bc:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bc/sayori_1bc_010.png"
    pause 5
    repeat
image sayori 1bd:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bd/sayori_1bd_010.png"
    pause 5
    repeat
image sayori 1be:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1be/sayori_1be_010.png"
    pause 5
    repeat
image sayori 1bf:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bf/sayori_1bf_010.png"
    pause 5
    repeat
image sayori 1bg:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bg/sayori_1bg_010.png"
    pause 5
    repeat
image sayori 1bh:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bh/sayori_1bh_010.png"
    pause 5
    repeat
image sayori 1bi:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bi/sayori_1bi_010.png"
    pause 5
    repeat
image sayori 1bj:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bj/sayori_1bj_010.png"
    pause 5
    repeat
image sayori 1bk:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bk/sayori_1bk_010.png"
    pause 5
    repeat
image sayori 1bl:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bl/sayori_1bl_010.png"
    pause 5
    repeat
image sayori 1bm:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bm/sayori_1bm_010.png"
    pause 5
    repeat
image sayori 1bn:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bn/sayori_1bn_010.png"
    pause 5
    repeat
image sayori 1bo:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bo/sayori_1bo_010.png"
    pause 5
    repeat
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bt/sayori_1bt_010.png"
    pause 5
    repeat
image sayori 1bu:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bu/sayori_1bu_010.png"
    pause 5
    repeat
image sayori 1bv:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bv/sayori_1bv_010.png"
    pause 5
    repeat
image sayori 1bw:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bw/sayori_1bw_010.png"
    pause 5
    repeat
image sayori 1bx:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1bx/sayori_1bx_010.png"
    pause 5
    repeat
image sayori 1by:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_1by/sayori_1by_010.png"
    pause 5
    repeat

image sayori 2ba:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2ba/sayori_2ba_010.png"
    pause 5
    repeat
image sayori 2bb:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bb/sayori_2bb_010.png"
    pause 5
    repeat
image sayori 2bc:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bc/sayori_2bc_010.png"
    pause 5
    repeat
image sayori 2bd:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bd/sayori_2bd_010.png"
    pause 5
    repeat
image sayori 2be:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2be/sayori_2be_010.png"
    pause 5
    repeat
image sayori 2bf:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bf/sayori_2bf_010.png"
    pause 5
    repeat
image sayori 2bg:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bg/sayori_2bg_010.png"
    pause 5
    repeat
image sayori 2bh:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bh/sayori_2bh_010.png"
    pause 5
    repeat
image sayori 2bi:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bi/sayori_2bi_010.png"
    pause 5
    repeat
image sayori 2bj:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bj/sayori_2bj_010.png"
    pause 5
    repeat
image sayori 2bk:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bk/sayori_2bk_010.png"
    pause 5
    repeat
image sayori 2bl:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bl/sayori_2bl_010.png"
    pause 5
    repeat
image sayori 2bm:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bm/sayori_2bm_010.png"
    pause 5
    repeat
image sayori 2bn:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bn/sayori_2bn_010.png"
    pause 5
    repeat
image sayori 2bo:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bo/sayori_2bo_010.png"
    pause 5
    repeat
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bt/sayori_2bt_010.png"
    pause 5
    repeat
image sayori 2bu:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bu/sayori_2bu_010.png"
    pause 5
    repeat
image sayori 2bv:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bv/sayori_2bv_010.png"
    pause 5
    repeat
image sayori 2bw:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bw/sayori_2bw_010.png"
    pause 5
    repeat
image sayori 2bx:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2bx/sayori_2bx_010.png"
    pause 5
    repeat
image sayori 2by:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_2by/sayori_2by_010.png"
    pause 5
    repeat

image sayori 3ba:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3ba/sayori_3ba_010.png"
    pause 5
    repeat
image sayori 3bb:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bb/sayori_3bb_010.png"
    pause 5
    repeat
image sayori 3bc:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bc/sayori_3bc_010.png"
    pause 5
    repeat
image sayori 3bd:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bd/sayori_3bd_010.png"
    pause 5
    repeat
image sayori 3be:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3be/sayori_3be_010.png"
    pause 5
    repeat
image sayori 3bf:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bf/sayori_3bf_010.png"
    pause 5
    repeat
image sayori 3bg:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bg/sayori_3bg_010.png"
    pause 5
    repeat
image sayori 3bh:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bh/sayori_3bh_010.png"
    pause 5
    repeat
image sayori 3bi:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bi/sayori_3bi_010.png"
    pause 5
    repeat
image sayori 3bj:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bj/sayori_3bj_010.png"
    pause 5
    repeat
image sayori 3bk:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bk/sayori_3bk_010.png"
    pause 5
    repeat
image sayori 3bl:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bl/sayori_3bl_010.png"
    pause 5
    repeat
image sayori 3bm:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bm/sayori_3bm_010.png"
    pause 5
    repeat
image sayori 3bn:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bn/sayori_3bn_010.png"
    pause 5
    repeat
image sayori 3bo:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bo/sayori_3bo_010.png"
    pause 5
    repeat
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bt/sayori_3bt_010.png"
    pause 5
    repeat
image sayori 3bu:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bu/sayori_3bu_010.png"
    pause 5
    repeat
image sayori 3bv:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bv/sayori_3bv_010.png"
    pause 5
    repeat
image sayori 3bw:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bw/sayori_3bw_010.png"
    pause 5
    repeat
image sayori 3bx:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3bx/sayori_3bx_010.png"
    pause 5
    repeat
image sayori 3by:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_3by/sayori_3by_010.png"
    pause 5
    repeat

image sayori 4ba:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4ba/sayori_4ba_010.png"
    pause 5
    repeat
image sayori 4bb:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bb/sayori_4bb_010.png"
    pause 5
    repeat
image sayori 4bc:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bc/sayori_4bc_010.png"
    pause 5
    repeat
image sayori 4bd:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bd/sayori_4bd_010.png"
    pause 5
    repeat
image sayori 4be:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4be/sayori_4be_010.png"
    pause 5
    repeat
image sayori 4bf:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bf/sayori_4bf_010.png"
    pause 5
    repeat
image sayori 4bg:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bg/sayori_4bg_010.png"
    pause 5
    repeat
image sayori 4bh:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bh/sayori_4bh_010.png"
    pause 5
    repeat
image sayori 4bi:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bi/sayori_4bi_010.png"
    pause 5
    repeat
image sayori 4bj:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bj/sayori_4bj_010.png"
    pause 5
    repeat
image sayori 4bk:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bk/sayori_4bk_010.png"
    pause 5
    repeat
image sayori 4bl:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bl/sayori_4bl_010.png"
    pause 5
    repeat
image sayori 4bm:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bm/sayori_4blm_010.png"
    pause 5
    repeat
image sayori 4bn:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bn/sayori_4bn_010.png"
    pause 5
    repeat
image sayori 4bo:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bo/sayori_4bo_010.png"
    pause 5
    repeat
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bt/sayori_4bt_010.png"
    pause 5
    repeat
image sayori 4bu:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bu/sayori_4bu_010.png"
    pause 5
    repeat
image sayori 4bv:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bv/sayori_4bv_010.png"
    pause 5
    repeat
image sayori 4bw:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bw/sayori_4bw_010.png"
    pause 5
    repeat
image sayori 4bx:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4bx/sayori_4bx_010.png"
    pause 5
    repeat
image sayori 4by:
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_000.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_001.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_002.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_003.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_004.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_005.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_006.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_007.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_008.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_009.png"
    pause 0.01666
    "mod_assets/images/sayori/Live2D/Final Products/sayori_4by/sayori_4by_010.png"
    pause 5
    repeat



image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat

# Natsuki

image natsuki 1:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_010.png"
    pause 5
    repeat
image natsuki 1a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1a/natsuki_1a_010.png"
    pause 5
    repeat
image natsuki 1b:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1b/natsuki_1b_010.png"
    pause 5
    repeat
image natsuki 1c:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1c/natsuki_1c_010.png"
    pause 5
    repeat
image natsuki 1d:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1d/natsuki_1d_010.png"
    pause 5
    repeat
image natsuki 1e:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1e/natsuki_1e_010.png"
    pause 5
    repeat
image natsuki 1f:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1f/natsuki_1f_010.png"
    pause 5
    repeat
image natsuki 1g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1g/natsuki_1g_010.png"
    pause 5
    repeat
image natsuki 1h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1h/natsuki_1h_010.png"
    pause 5
    repeat
image natsuki 1i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1i/natsuki_1i_010.png"
    pause 5
    repeat
image natsuki 1j:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1j/natsuki_1j_010.png"
    pause 5
    repeat
image natsuki 1k:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1k/natsuki_1k_010.png"
    pause 5
    repeat
image natsuki 1l:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1l/natsuki_1l_010.png"
    pause 5
    repeat
image natsuki 1m:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1m/natsuki_1m_010.png"
    pause 5
    repeat
image natsuki 1n:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1n/natsuki_1n_010.png"
    pause 5
    repeat
image natsuki 1o:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1o/natsuki_1o_010.png"
    pause 5
    repeat
image natsuki 1p:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1p/natsuki_1p_010.png"
    pause 5
    repeat
image natsuki 1q:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1q/natsuki_1q_010.png"
    pause 5
    repeat
image natsuki 1r:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1r/natsuki_1r_010.png"
    pause 5
    repeat
image natsuki 1s:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1s/natsuki_1s_010.png"
    pause 5
    repeat
image natsuki 1t:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1t/natsuki_1t_010.png"
    pause 5
    repeat
image natsuki 1u:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1u/natsuki_1u_010.png"
    pause 5
    repeat
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1/natsuki_1_010.png"
    pause 5
    repeat
image natsuki 2a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2a/natsuki_2a_010.png"
    pause 5
    repeat
image natsuki 2b:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2b/natsuki_2b_010.png"
    pause 5
    repeat
image natsuki 2c:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2c/natsuki_2c_010.png"
    pause 5
    repeat
image natsuki 2d:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2d/natsuki_2d_010.png"
    pause 5
    repeat
image natsuki 2e:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2e/natsuki_2e_010.png"
    pause 5
    repeat
image natsuki 2f:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2f/natsuki_2f_010.png"
    pause 5
    repeat
image natsuki 2g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2g/natsuki_2g_010.png"
    pause 5
    repeat
image natsuki 2h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2h/natsuki_2h_010.png"
    pause 5
    repeat
image natsuki 2i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2i/natsuki_2i_010.png"
    pause 5
    repeat
image natsuki 2j:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2j/natsuki_2j_010.png"
    pause 5
    repeat
image natsuki 2k:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2k/natsuki_2k_010.png"
    pause 5
    repeat
image natsuki 2l:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2l/natsuki_2l_010.png"
    pause 5
    repeat
image natsuki 2m:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2m/natsuki_2m_010.png"
    pause 5
    repeat
image natsuki 2n:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2n/natsuki_2n_010.png"
    pause 5
    repeat
image natsuki 2o:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2o/natsuki_2o_010.png"
    pause 5
    repeat
image natsuki 2p:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2p/natsuki_2p_010.png"
    pause 5
    repeat
image natsuki 2q:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2q/natsuki_2q_010.png"
    pause 5
    repeat
image natsuki 2r:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2r/natsuki_2r_010.png"
    pause 5
    repeat
image natsuki 2s:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2s/natsuki_2s_010.png"
    pause 5
    repeat
image natsuki 2t:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2t/natsuki_2t_010.png"
    pause 5
    repeat
image natsuki 2u:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2u/natsuki_2u_010.png"
    pause 5
    repeat
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3/natsuki_3_010.png"
    pause 5
    repeat
image natsuki 3a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3a/natsuki_3a_010.png"
    pause 5
    repeat
image natsuki 3b:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3b/natsuki_3b_010.png"
    pause 5
    repeat
image natsuki 3c:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3c/natsuki_3c_010.png"
    pause 5
    repeat
image natsuki 3d:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3d/natsuki_3d_010.png"
    pause 5
    repeat
image natsuki 3e:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3e/natsuki_3e_010.png"
    pause 5
    repeat
image natsuki 3f:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3f/natsuki_3f_010.png"
    pause 5
    repeat
image natsuki 3g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3g/natsuki_3g_010.png"
    pause 5
    repeat
image natsuki 3h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3h/natsuki_3h_010.png"
    pause 5
    repeat
image natsuki 3i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3i/natsuki_3i_010.png"
    pause 5
    repeat
image natsuki 3j:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3j/natsuki_3j_010.png"
    pause 5
    repeat
image natsuki 3k:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3k/natsuki_3k_010.png"
    pause 5
    repeat
image natsuki 3l:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3l/natsuki_3l_010.png"
    pause 5
    repeat
image natsuki 3m:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3m/natsuki_3m_010.png"
    pause 5
    repeat
image natsuki 3n:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3n/natsuki_3n_010.png"
    pause 5
    repeat
image natsuki 3o:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3o/natsuki_3o_010.png"
    pause 5
    repeat
image natsuki 3p:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3p/natsuki_3p_010.png"
    pause 5
    repeat
image natsuki 3q:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3q/natsuki_3q_010.png"
    pause 5
    repeat
image natsuki 3r:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3r/natsuki_3r_010.png"
    pause 5
    repeat
image natsuki 3s:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3s/natsuki_3s_010.png"
    pause 5
    repeat
image natsuki 3t:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3t/natsuki_3t_010.png"
    pause 5
    repeat
image natsuki 3u:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3u/natsuki_3u_010.png"
    pause 5
    repeat
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4/natsuki_4_010.png"
    pause 5
    repeat
image natsuki 4a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4a/natsuki_4a_010.png"
    pause 5
    repeat
image natsuki 4b:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4b/natsuki_4b_010.png"
    pause 5
    repeat
image natsuki 4c:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4c/natsuki_4c_010.png"
    pause 5
    repeat
image natsuki 4d:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4d/natsuki_4d_010.png"
    pause 5
    repeat
image natsuki 4e:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4e/natsuki_4e_010.png"
    pause 5
    repeat
image natsuki 4f:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4f/natsuki_4f_010.png"
    pause 5
    repeat
image natsuki 4g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4g/natsuki_4g_010.png"
    pause 5
    repeat
image natsuki 4h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4h/natsuki_4h_010.png"
    pause 5
    repeat
image natsuki 4i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4i/natsuki_4i_010.png"
    pause 5
    repeat
image natsuki 4j:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4j/natsuki_4j_010.png"
    pause 5
    repeat
image natsuki 4k:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4k/natsuki_4k_010.png"
    pause 5
    repeat
image natsuki 4l:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4l/natsuki_4l_010.png"
    pause 5
    repeat
image natsuki 4m:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4m/natsuki_4m_010.png"
    pause 5
    repeat
image natsuki 4n:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4n/natsuki_4n_010.png"
    pause 5
    repeat
image natsuki 4o:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4o/natsuki_4o_010.png"
    pause 5
    repeat
image natsuki 4p:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4p/natsuki_4p_010.png"
    pause 5
    repeat
image natsuki 4q:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4q/natsuki_4q_010.png"
    pause 5
    repeat
image natsuki 4r:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4r/natsuki_4r_010.png"
    pause 5
    repeat
image natsuki 4s:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4s/natsuki_4s_010.png"
    pause 5
    repeat
image natsuki 4t:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4t/natsuki_4t_010.png"
    pause 5
    repeat
image natsuki 4u:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4u/natsuki_4u_010.png"
    pause 5
    repeat
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12/natsuki_12_010.png"
    pause 5
    repeat
image natsuki 12a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12a/natsuki_12a_010.png"
    pause 5
    repeat
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12g/natsuki_12g_010.png"
    pause 5
    repeat
image natsuki 12h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12h/natsuki_12h_010.png"
    pause 5
    repeat
image natsuki 12i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12i/natsuki_12i_010.png"
    pause 5
    repeat

image natsuki 42:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42/natsuki_42_010.png"
    pause 5
    repeat
image natsuki 42a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42a/natsuki_42a_010.png"
    pause 5
    repeat
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42g/natsuki_42g_010.png"
    pause 5
    repeat
image natsuki 42h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42h/natsuki_42h_010.png"
    pause 5
    repeat
image natsuki 42i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42i/natsuki_42i_010.png"
    pause 5
    repeat

image natsuki 51:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5/natsuki_5_010.png"
    pause 5
    repeat
image natsuki 5a:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5a/natsuki_5a_010.png"
    pause 5
    repeat
image natsuki 5b:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5b/natsuki_5b_010.png"
    pause 5
    repeat
image natsuki 5c:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5c/natsuki_5c_010.png"
    pause 5
    repeat
image natsuki 5d:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5d/natsuki_5d_010.png"
    pause 5
    repeat
image natsuki 5e:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5e/natsuki_5e_010.png"
    pause 5
    repeat
image natsuki 5f:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5f/natsuki_5f_010.png"
    pause 5
    repeat
image natsuki 5g:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5g/natsuki_5g_010.png"
    pause 5
    repeat
image natsuki 5h:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5h/natsuki_5h_010.png"
    pause 5
    repeat
image natsuki 5i:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5i/natsuki_5i_010.png"
    pause 5
    repeat
image natsuki 5j:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5j/natsuki_5j_010.png"
    pause 5
    repeat
image natsuki 5k:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5k/natsuki_5k_010.png"
    pause 5
    repeat
image natsuki 5l:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5l/natsuki_5l_010.png"
    pause 5
    repeat
image natsuki 5m:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5m/natsuki_5m_010.png"
    pause 5
    repeat
image natsuki 5n:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5n/natsuki_5n_010.png"
    pause 5
    repeat
image natsuki 5o:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5o/natsuki_5o_010.png"
    pause 5
    repeat
image natsuki 5p:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5p/natsuki_5p_010.png"
    pause 5
    repeat
image natsuki 5q:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5q/natsuki_5q_010.png"
    pause 5
    repeat
image natsuki 5r:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5r/natsuki_5r_010.png"
    pause 5
    repeat
image natsuki 5s:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5s/natsuki_5s_010.png"
    pause 5
    repeat
image natsuki 5t:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5t/natsuki_5t_010.png"
    pause 5
    repeat
image natsuki 5u:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5u/natsuki_5u_010.png"
    pause 5
    repeat
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")
#image natsuki 52 = im.Composite((960, 960), (0, 0), "natsuki/3.png", (0, 0), "natsuki/4t.png")

image natsuki 1ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1ba/natsuki_1ba_010.png"
    pause 5
    repeat
image natsuki 1bb:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bb/natsuki_1bb_010.png"
    pause 5
    repeat
image natsuki 1bc:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bc/natsuki_1bc_010.png"
    pause 5
    repeat
image natsuki 1bd:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bd/natsuki_1bd_010.png"
    pause 5
    repeat
image natsuki 1be:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1be/natsuki_1be_010.png"
    pause 5
    repeat
image natsuki 1bf:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bf/natsuki_1bf_010.png"
    pause 5
    repeat
image natsuki 1bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bg/natsuki_1bg_010.png"
    pause 5
    repeat
image natsuki 1bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bh/natsuki_1bh_010.png"
    pause 5
    repeat
image natsuki 1bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bi/natsuki_1bi_010.png"
    pause 5
    repeat
image natsuki 1bj:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bj/natsuki_1bj_010.png"
    pause 5
    repeat
image natsuki 1bk:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bk/natsuki_1bk_010.png"
    pause 5
    repeat
image natsuki 1bl:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bl/natsuki_1bl_010.png"
    pause 5
    repeat
image natsuki 1bm:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bm/natsuki_1bm_010.png"
    pause 5
    repeat
image natsuki 1bn:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bn/natsuki_1bn_010.png"
    pause 5
    repeat
image natsuki 1bo:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bo/natsuki_1bo_010.png"
    pause 5
    repeat
image natsuki 1bp:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bp/natsuki_1bp_010.png"
    pause 5
    repeat
image natsuki 1bq:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bq/natsuki_1bq_010.png"
    pause 5
    repeat
image natsuki 1br:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1br/natsuki_1br_010.png"
    pause 5
    repeat
image natsuki 1bs:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bs/natsuki_1bs_010.png"
    pause 5
    repeat
image natsuki 1bt:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bt/natsuki_1bt_010.png"
    pause 5
    repeat
image natsuki 1bu:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_1bu/natsuki_1bu_010.png"
    pause 5
    repeat
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2ba/natsuki_2ba_010.png"
    pause 5
    repeat
image natsuki 2bb:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bb/natsuki_2bb_010.png"
    pause 5
    repeat
image natsuki 2bc:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bc/natsuki_2bc_010.png"
    pause 5
    repeat
image natsuki 2bd:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bd/natsuki_2bd_010.png"
    pause 5
    repeat
image natsuki 2be:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2be/natsuki_2be_010.png"
    pause 5
    repeat
image natsuki 2bf:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bf/natsuki_2bf_010.png"
    pause 5
    repeat
image natsuki 2bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bg/natsuki_2bg_010.png"
    pause 5
    repeat
image natsuki 2bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bh/natsuki_2bh_010.png"
    pause 5
    repeat
image natsuki 2bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bi/natsuki_2bi_010.png"
    pause 5
    repeat
image natsuki 2bj:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bj/natsuki_2bj_010.png"
    pause 5
    repeat
image natsuki 2bk:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bk/natsuki_2bk_010.png"
    pause 5
    repeat
image natsuki 2bl:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bl/natsuki_2bl_010.png"
    pause 5
    repeat
image natsuki 2bm:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bm/natsuki_2bm_010.png"
    pause 5
    repeat
image natsuki 2bn:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bn/natsuki_2bn_010.png"
    pause 5
    repeat
image natsuki 2bo:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bo/natsuki_2bo_010.png"
    pause 5
    repeat
image natsuki 2bp:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bp/natsuki_2bp_010.png"
    pause 5
    repeat
image natsuki 2bq:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bq/natsuki_2bq_010.png"
    pause 5
    repeat
image natsuki 2br:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2br/natsuki_2br_010.png"
    pause 5
    repeat
image natsuki 2bs:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bs/natsuki_2bs_010.png"
    pause 5
    repeat
image natsuki 2bt:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bt/natsuki_2bt_010.png"
    pause 5
    repeat
image natsuki 2bu:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_2bu/natsuki_2bu_010.png"
    pause 5
    repeat
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3ba/natsuki_3ba_010.png"
    pause 5
    repeat
image natsuki 3bb:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bb/natsuki_3bb_010.png"
    pause 5
    repeat
image natsuki 3bc:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bc/natsuki_3bc_010.png"
    pause 5
    repeat
image natsuki 3bd:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bd/natsuki_3bd_010.png"
    pause 5
    repeat
image natsuki 3be:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3be/natsuki_3be_010.png"
    pause 5
    repeat
image natsuki 3bf:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bf/natsuki_3bf_010.png"
    pause 5
    repeat
image natsuki 3bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bg/natsuki_3bg_010.png"
    pause 5
    repeat
image natsuki 3bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bh/natsuki_3bh_010.png"
    pause 5
    repeat
image natsuki 3bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bi/natsuki_3bi_010.png"
    pause 5
    repeat
image natsuki 3bj:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bj/natsuki_3bj_010.png"
    pause 5
    repeat
image natsuki 3bk:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bk/natsuki_3bk_010.png"
    pause 5
    repeat
image natsuki 3bl:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bl/natsuki_3bl_010.png"
    pause 5
    repeat
image natsuki 3bm:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bm/natsuki_3bm_010.png"
    pause 5
    repeat
image natsuki 3bn:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bn/natsuki_3bn_010.png"
    pause 5
    repeat
image natsuki 3bo:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bo/natsuki_3bo_010.png"
    pause 5
    repeat
image natsuki 3bp:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bp/natsuki_3bp_010.png"
    pause 5
    repeat
image natsuki 3bq:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bq/natsuki_3bq_010.png"
    pause 5
    repeat
image natsuki 3br:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3br/natsuki_3br_010.png"
    pause 5
    repeat
image natsuki 3bs:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bs/natsuki_3bs_010.png"
    pause 5
    repeat
image natsuki 3bt:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bt/natsuki_3bt_010.png"
    pause 5
    repeat
image natsuki 3bu:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_3bu/natsuki_3bu_010.png"
    pause 5
    repeat
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4ba/natsuki_4ba_010.png"
    pause 5
    repeat
image natsuki 4bb:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bb/natsuki_4bb_010.png"
    pause 5
    repeat
image natsuki 4bc:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bc/natsuki_4bc_010.png"
    pause 5
    repeat
image natsuki 4bd:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bd/natsuki_4bd_010.png"
    pause 5
    repeat
image natsuki 4be:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4be/natsuki_4be_010.png"
    pause 5
    repeat
image natsuki 4bf:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bf/natsuki_4bf_010.png"
    pause 5
    repeat
image natsuki 4bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bg/natsuki_4bg_010.png"
    pause 5
    repeat
image natsuki 4bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bh/natsuki_4bh_010.png"
    pause 5
    repeat
image natsuki 4bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bi/natsuki_4bi_010.png"
    pause 5
    repeat
image natsuki 4bj:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bj/natsuki_4bj_010.png"
    pause 5
    repeat
image natsuki 4bk:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bk/natsuki_4bk_010.png"
    pause 5
    repeat
image natsuki 4bl:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bl/natsuki_4bl_010.png"
    pause 5
    repeat
image natsuki 4bm:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bm/natsuki_4bm_010.png"
    pause 5
    repeat
image natsuki 4bn:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bn/natsuki_4bn_010.png"
    pause 5
    repeat
image natsuki 4bo:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bo/natsuki_4bo_010.png"
    pause 5
    repeat
image natsuki 4bp:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bp/natsuki_4bp_010.png"
    pause 5
    repeat
image natsuki 4bq:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bq/natsuki_4bq_010.png"
    pause 5
    repeat
image natsuki 4br:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4br/natsuki_4br_010.png"
    pause 5
    repeat
image natsuki 4bs:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bs/natsuki_4bs_010.png"
    pause 5
    repeat
image natsuki 4bt:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bt/natsuki_4bt_010.png"
    pause 5
    repeat
image natsuki 4bu:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_4bu/natsuki_4bu_010.png"
    pause 5
    repeat
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12ba/natsuki_12ba_010.png"
    pause 5
    repeat
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bg/natsuki_12bg_010.png"
    pause 5
    repeat
image natsuki 12bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bh/natsuki_12bh_010.png"
    pause 5
    repeat
image natsuki 12bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_12bi/natsuki_12bi_010.png"
    pause 5
    repeat

image natsuki 42ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42ba/natsuki_42ba_010.png"
    pause 5
    repeat
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bg/natsuki_42bg_010.png"
    pause 5
    repeat
image natsuki 42bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bh/natsuki_42bh_010.png"
    pause 5
    repeat
image natsuki 42bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_42bi/natsuki_42bi_010.png"
    pause 5
    repeat

image natsuki 5ba:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5ba/natsuki_5ba_010.png"
    pause 5
    repeat
image natsuki 5bb:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bb/natsuki_5bb_010.png"
    pause 5
    repeat
image natsuki 5bc:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bc/natsuki_5bc_010.png"
    pause 5
    repeat
image natsuki 5bd:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bd/natsuki_5bd_010.png"
    pause 5
    repeat
image natsuki 5be:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5be/natsuki_5be_010.png"
    pause 5
    repeat
image natsuki 5bf:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bf/natsuki_5bf_010.png"
    pause 5
    repeat
image natsuki 5bg:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bg/natsuki_5bg_010.png"
    pause 5
    repeat
image natsuki 5bh:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bh/natsuki_5bh_010.png"
    pause 5
    repeat
image natsuki 5bi:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bi/natsuki_5bi_010.png"
    pause 5
    repeat
image natsuki 5bj:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bj/natsuki_5bj_010.png"
    pause 5
    repeat
image natsuki 5bk:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bk/natsuki_5bk_010.png"
    pause 5
    repeat
image natsuki 5bl:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bl/natsuki_5bl_010.png"
    pause 5
    repeat
image natsuki 5bm:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bm/natsuki_5bm_010.png"
    pause 5
    repeat
image natsuki 5bn:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bn/natsuki_5bn_010.png"
    pause 5
    repeat
image natsuki 5bo:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bo/natsuki_5bo_010.png"
    pause 5
    repeat
image natsuki 5bp:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bp/natsuki_5bp_010.png"
    pause 5
    repeat
image natsuki 5bq:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bq/natsuki_5bq_010.png"
    pause 5
    repeat
image natsuki 5br:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5br/natsuki_5br_010.png"
    pause 5
    repeat
image natsuki 5bs:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bs/natsuki_5bs_010.png"
    pause 5
    repeat
image natsuki 5bt:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bt/natsuki_5bt_010.png"
    pause 5
    repeat
image natsuki 5bu:
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_000.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_001.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_002.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_003.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_004.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_005.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_006.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_007.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_008.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_009.png"
    pause 0.01666
    "mod_assets/images/natsuki/Live2D/Final Products/natsuki_5bu/natsuki_5bu_010.png"
    pause 5
    repeat
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")



# Natsuki legacy
image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki mouth = LiveComposite((960, 960), (0, 0), "natsuki/0.png", (390, 340), "n_rects_mouth", (480, 334), "n_rects_mouth")

image n_rects_mouth:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    size (20, 25)

image n_moving_mouth:
    "images/natsuki/mouth.png"
    pos (615, 305)
    xanchor 0.5 yanchor 0.5
    parallel:
        choice:
            ease 0.10 yzoom 0.2
        choice:
            ease 0.05 yzoom 0.2
        choice:
            ease 0.075 yzoom 0.2
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        pass
        choice:
            ease 0.10 yzoom 1
        choice:
            ease 0.05 yzoom 1
        choice:
            ease 0.075 yzoom 1
        pass
        choice:
            0.02
        choice:
            0.04
        choice:
            0.06
        choice:
            0.08
        repeat
    parallel:
        choice:
            0.2
        choice:
            0.4
        choice:
            0.6
        ease 0.2 xzoom 0.4
        ease 0.2 xzoom 0.8
        repeat

image natsuki_ghost_blood:
    "#00000000"
    "natsuki/ghost_blood.png" with ImageDissolve("images/menu/wipedown.png", 80.0, ramplen=4, alpha=True)
    pos (620,320) zoom 0.80

image natsuki ghost_base:
    "natsuki/ghost1.png"
image natsuki ghost1:
    "natsuki 11"
    "natsuki ghost_base" with Dissolve(20.0, alpha=True)
image natsuki ghost2 = Image("natsuki/ghost2.png")
image natsuki ghost3 = Image("natsuki/ghost3.png")
image natsuki ghost4:
    "natsuki ghost3"
    parallel:
        easeout 0.25 zoom 4.5 yoffset 1200
    parallel:
        ease 0.025 xoffset -20
        ease 0.025 xoffset 20
        repeat
    0.25
    "black"
image natsuki glitch1:
    "natsuki/glitch1.png"
    zoom 1.25
    block:
        yoffset 300 xoffset 100 ytile 2
        linear 0.15 yoffset 200
        repeat
    time 0.75
    yoffset 0 zoom 1 xoffset 0 ytile 1
    "natsuki 4e"

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"

# Yuri
image yuri 1:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1/yuri_1_010.png"
    pause 5
    repeat
image yuri 2:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2/yuri_2_010.png"
    pause 5
    repeat
image yuri 3:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3/yuri_3_010.png"
    pause 5
    repeat
image yuri 4:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4/yuri_4_010.png"
    pause 5
    repeat

image yuri 1a:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1a/yuri_1a_010.png"
    pause 5
    repeat
image yuri 1b:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1b/yuri_1b_010.png"
    pause 5
    repeat
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1e/yuri_1e_010.png"
    pause 5
    repeat
image yuri 1f:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1f/yuri_1f_010.png"
    pause 5
    repeat
image yuri 1g:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1g/yuri_1g_010.png"
    pause 5
    repeat
image yuri 1h:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1h/yuri_1h_010.png"
    pause 5
    repeat
image yuri 1i:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1i/yuri_1i_010.png"
    pause 5
    repeat
image yuri 1j:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1j/yuri_1j_010.png"
    pause 5
    repeat
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1n/yuri_1n_010.png"
    pause 5
    repeat
image yuri 1o:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1o/yuri_1o_010.png"
    pause 5
    repeat
image yuri 1p:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1p/yuri_1p_010.png"
    pause 5
    repeat
image yuri 1q:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1q/yuri_1q_010.png"
    pause 5
    repeat
image yuri 1r:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1r/yuri_1r_010.png"
    pause 5
    repeat
image yuri 1s:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1s/yuri_1s_010.png"
    pause 5
    repeat
image yuri 1t:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1t/yuri_1t_010.png"
    pause 5
    repeat
image yuri 1u:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1u/yuri_1u_010.png"
    pause 5
    repeat
image yuri 1v:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1v/yuri_1v_010.png"
    pause 5
    repeat
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2a/yuri_2a_010.png"
    pause 5
    repeat
image yuri 2b:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2b/yuri_2b_010.png"
    pause 5
    repeat
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2e/yuri_2e_010.png"
    pause 5
    repeat
image yuri 2f:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2f/yuri_2f_010.png"
    pause 5
    repeat
image yuri 2g:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2g/yuri_2g_010.png"
    pause 5
    repeat
image yuri 2h:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2h/yuri_2h_010.png"
    pause 5
    repeat
image yuri 2i:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2i/yuri_2i_010.png"
    pause 5
    repeat
image yuri 2j:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2j/yuri_2j_010.png"
    pause 5
    repeat
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2n/yuri_2n_010.png"
    pause 5
    repeat
image yuri 2o:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2o/yuri_2o_010.png"
    pause 5
    repeat
image yuri 2p:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2p/yuri_2p_010.png"
    pause 5
    repeat
image yuri 2q:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2q/yuri_2q_010.png"
    pause 5
    repeat
image yuri 2r:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2r/yuri_2r_010.png"
    pause 5
    repeat
image yuri 2s:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2s/yuri_2s_010.png"
    pause 5
    repeat
image yuri 2t:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2t/yuri_2t_010.png"
    pause 5
    repeat
image yuri 2u:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2u/yuri_2u_010.png"
    pause 5
    repeat
image yuri 2v:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2v/yuri_2v_010.png"
    pause 5
    repeat
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3a/yuri_3a_010.png"
    pause 5
    repeat
image yuri 3b:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3b/yuri_3b_010.png"
    pause 5
    repeat
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3e/yuri_3e_010.png"
    pause 5
    repeat
image yuri 3f:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3f/yuri_3f_010.png"
    pause 5
    repeat
image yuri 3g:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3g/yuri_3g_010.png"
    pause 5
    repeat
image yuri 3h:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3h/yuri_3h_010.png"
    pause 5
    repeat
image yuri 3i:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3i/yuri_3i_010.png"
    pause 5
    repeat
image yuri 3j:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3j/yuri_3j_010.png"
    pause 5
    repeat
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3n/yuri_3n_010.png"
    pause 5
    repeat
image yuri 3o:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3o/yuri_3o_010.png"
    pause 5
    repeat
image yuri 3p:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3p/yuri_3p_010.png"
    pause 5
    repeat
image yuri 3q:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3q/yuri_3q_010.png"
    pause 5
    repeat
image yuri 3r:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3r/yuri_3r_010.png"
    pause 5
    repeat
image yuri 3s:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3s/yuri_3s_010.png"
    pause 5
    repeat
image yuri 3t:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3t/yuri_3t_010.png"
    pause 5
    repeat
image yuri 3u:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3u/yuri_3u_010.png"
    pause 5
    repeat
image yuri 3v:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3v/yuri_3v_010.png"
    pause 5
    repeat
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4a/yuri_4a_010.png"
    pause 5
    repeat
image yuri 4b:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4b/yuri_4b_010.png"
    pause 5
    repeat
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4d/yuri_4d_010.png"
    pause 5
    repeat
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ba/yuri_1ba_010.png"
    pause 5
    repeat
image yuri 1bb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bb/yuri_1bb_010.png"
    pause 5
    repeat
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1be/yuri_1be_010.png"
    pause 5
    repeat
image yuri 1bf:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bf/yuri_1bf_010.png"
    pause 5
    repeat
image yuri 1bg:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bg/yuri_1bg_010.png"
    pause 5
    repeat
image yuri 1bh:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bh/yuri_1bh_010.png"
    pause 5
    repeat
image yuri 1bi:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bi/yuri_1bi_010.png"
    pause 5
    repeat
image yuri 1bj:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bj/yuri_1bj_010.png"
    pause 5
    repeat
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bn/yuri_1bn_010.png"
    pause 5
    repeat
image yuri 1bo:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bo/yuri_1bo_010.png"
    pause 5
    repeat
image yuri 1bp:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bp/yuri_1bp_010.png"
    pause 5
    repeat
image yuri 1bq:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bq/yuri_1bq_010.png"
    pause 5
    repeat
image yuri 1br:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1br/yuri_1br_010.png"
    pause 5
    repeat
image yuri 1bs:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bs/yuri_1bs_010.png"
    pause 5
    repeat
image yuri 1bt:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bt/yuri_1bt_010.png"
    pause 5
    repeat
image yuri 1bu:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bu/yuri_1bu_010.png"
    pause 5
    repeat
image yuri 1bv:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1bv/yuri_1bv_010.png"
    pause 5
    repeat
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ba/yuri_2ba_010.png"
    pause 5
    repeat
image yuri 2bb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bb/yuri_2bb_010.png"
    pause 5
    repeat
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2be/yuri_2be_010.png"
    pause 5
    repeat
image yuri 2bf:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bf/yuri_2bf_010.png"
    pause 5
    repeat
image yuri 2bg:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bg/yuri_2bg_010.png"
    pause 5
    repeat
image yuri 2bh:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bh/yuri_2bh_010.png"
    pause 5
    repeat
image yuri 2bi:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bi/yuri_2bi_010.png"
    pause 5
    repeat
image yuri 2bj:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bj/yuri_2bj_010.png"
    pause 5
    repeat
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bn/yuri_2bn_010.png"
    pause 5
    repeat
image yuri 2bo:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bo/yuri_2bo_010.png"
    pause 5
    repeat
image yuri 2bp:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bp/yuri_2bp_010.png"
    pause 5
    repeat
image yuri 2bq:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bq/yuri_2bq_010.png"
    pause 5
    repeat
image yuri 2br:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2br/yuri_2br_010.png"
    pause 5
    repeat
image yuri 2bs:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bs/yuri_2bs_010.png"
    pause 5
    repeat
image yuri 2bt:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bt/yuri_2bt_010.png"
    pause 5
    repeat
image yuri 2bu:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bu/yuri_2bu_010.png"
    pause 5
    repeat
image yuri 2bv:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2bv/yuri_2bv_010.png"
    pause 5
    repeat
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3ba/yuri_3ba_010.png"
    pause 5
    repeat
image yuri 3bb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bb/yuri_3bb_010.png"
    pause 5
    repeat
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3be/yuri_3be_010.png"
    pause 5
    repeat
image yuri 3bf:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bf/yuri_3bf_010.png"
    pause 5
    repeat
image yuri 3bg:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bg/yuri_3bg_010.png"
    pause 5
    repeat
image yuri 3bh:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bh/yuri_3bh_010.png"
    pause 5
    repeat
image yuri 3bi:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bi/yuri_3bi_010.png"
    pause 5
    repeat
image yuri 3bj:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bj/yuri_3bj_010.png"
    pause 5
    repeat
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bn/yuri_3bn_010.png"
    pause 5
    repeat
image yuri 3bo:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bo/yuri_3bo_010.png"
    pause 5
    repeat
image yuri 3bp:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bp/yuri_3bp_010.png"
    pause 5
    repeat
image yuri 3bq:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bq/yuri_3bq_010.png"
    pause 5
    repeat
image yuri 3br:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3br/yuri_3br_010.png"
    pause 5
    repeat
image yuri 3bs:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bs/yuri_3bs_010.png"
    pause 5
    repeat
image yuri 3bt:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bt/yuri_3bt_010.png"
    pause 5
    repeat
image yuri 3bu:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bu/yuri_3bu_010.png"
    pause 5
    repeat
image yuri 3bv:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_3bv/yuri_3bv_010.png"
    pause 5
    repeat
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4ba/yuri_4ba_010.png"
    pause 5
    repeat
image yuri 4bb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bb/yuri_4bb_010.png"
    pause 5
    repeat
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_4bd/yuri_4bd_010.png"
    pause 5
    repeat
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

#Hospital gown
image yuri 1ha:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ha/yuri_1ha_010.png"
    pause 5
    repeat
image yuri 1hb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hb/yuri_1hb_010.png"
    pause 5
    repeat
image yuri 1hc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")
image yuri 1hd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")
image yuri 1he:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1he/yuri_1he_010.png"
    pause 5
    repeat
image yuri 1hf:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hf/yuri_1hf_010.png"
    pause 5
    repeat
image yuri 1hg:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hg/yuri_1hg_010.png"
    pause 5
    repeat
image yuri 1hh:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hh/yuri_1hh_010.png"
    pause 5
    repeat
image yuri 1hi:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hi/yuri_1hi_010.png"
    pause 5
    repeat
image yuri 1hj:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hj/yuri_1hj_010.png"
    pause 5
    repeat
image yuri 1hk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")
image yuri 1hl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")
image yuri 1hm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")
image yuri 1hn:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hn/yuri_1hn_010.png"
    pause 5
    repeat
image yuri 1ho:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ho/yuri_1ho_010.png"
    pause 5
    repeat
image yuri 1hp:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hp/yuri_1hp_010.png"
    pause 5
    repeat
image yuri 1hq:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hq/yuri_1hq_010.png"
    pause 5
    repeat
image yuri 1hr:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hr/yuri_1hr_010.png"
    pause 5
    repeat
image yuri 1hs:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hs/yuri_1hs_010.png"
    pause 5
    repeat
image yuri 1ht:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1ht/yuri_1ht_010.png"
    pause 5
    repeat
image yuri 1hu:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hu/yuri_1hu_010.png"
    pause 5
    repeat
image yuri 1hv:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_1hv/yuri_1hv_010.png"
    pause 5
    repeat
image yuri 1hw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1hl.png", (0, 0), "yuri/1hr.png")

image yuri 2ha:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ha/yuri_2ha_010.png"
    pause 5
    repeat
image yuri 2hb:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hb/yuri_2hb_010.png"
    pause 5
    repeat
image yuri 2hc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")
image yuri 2hd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")
image yuri 2he:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2he/yuri_2he_010.png"
    pause 5
    repeat
image yuri 2hf:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hf/yuri_2hf_010.png"
    pause 5
    repeat
image yuri 2hg:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hg/yuri_2hg_010.png"
    pause 5
    repeat
image yuri 2hh:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hh/yuri_2hh_010.png"
    pause 5
    repeat
image yuri 2hi:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hi/yuri_2hi_010.png"
    pause 5
    repeat
image yuri 2hj:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hj/yuri_2hj_010.png"
    pause 5
    repeat
image yuri 2hk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")
image yuri 2hl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")
image yuri 2hm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")
image yuri 2hn:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hn/yuri_2hn_010.png"
    pause 5
    repeat
image yuri 2ho:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ho/yuri_2ho_010.png"
    pause 5
    repeat
image yuri 2hp:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hp/yuri_2hp_010.png"
    pause 5
    repeat
image yuri 2hq:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hq/yuri_2hq_010.png"
    pause 5
    repeat
image yuri 2hr:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hr/yuri_2hr_010.png"
    pause 5
    repeat
image yuri 2hs:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hs/yuri_2hs_010.png"
    pause 5
    repeat
image yuri 2ht:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2ht/yuri_2ht_010.png"
    pause 5
    repeat
image yuri 2hu:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hu/yuri_2hu_010.png"
    pause 5
    repeat
image yuri 2hv:
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_000.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_001.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_002.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_003.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_004.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_005.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_006.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_007.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_008.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_009.png"
    pause 0.01666
    "mod_assets/images/yuri/Live2D/Final Products/yuri_2hv/yuri_2hv_010.png"
    pause 5
    repeat
image yuri 2hw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2hl.png", (0, 0), "yuri/2hr.png")



image y_glitch_head:
    "images/yuri/za.png"
    0.15
    "images/yuri/zb.png"
    0.15
    "images/yuri/zc.png"
    0.15
    "images/yuri/zd.png"
    0.15
    repeat

image yuri stab_1 = "yuri/stab/1.png"
image yuri stab_2 = "yuri/stab/2.png"
image yuri stab_3 = "yuri/stab/3.png"
image yuri stab_4 = "yuri/stab/4.png"
image yuri stab_5 = "yuri/stab/5.png"
image yuri stab_6 = LiveComposite((960,960), (0, 0), "yuri/stab/6-mask.png", (0, 0), "yuri stab_6_eyes", (0, 0), "yuri/stab/6.png")

image yuri stab_6_eyes:
    "yuri/stab/6-eyes.png"
    subpixel True
    parallel:
        choice:
            xoffset 0.5
        choice:
            xoffset 0
        choice:
            xoffset -0.5
        0.2
        repeat
    parallel:
        choice:
            yoffset 0.5
        choice:
            yoffset 0
        choice:
            yoffset -0.5
        0.2
        repeat
    parallel:
        2.05
        easeout 1.0 yoffset -15
        linear 10 yoffset -15


image yuri oneeye = LiveComposite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/oneeye.png", (0, 0), "yuri oneeye2")
image yuri oneeye2:
    "yuri/oneeye2.png"
    subpixel True
    pause 5.0
    linear 60 xoffset -50 yoffset 20

image yuri glitch:
    "yuri/glitch1.png"
    pause 0.1
    "yuri/glitch2.png"
    pause 0.1
    "yuri/glitch3.png"
    pause 0.1
    "yuri/glitch4.png"
    pause 0.1
    "yuri/glitch5.png"
    pause 0.1
    repeat
image yuri glitch2:
    "yuri/0a.png"
    pause 0.1
    "yuri/0b.png"
    pause 0.5
    "yuri/0a.png"
    pause 0.3
    "yuri/0b.png"
    pause 0.3
    "yuri 1"

image yuri eyes = LiveComposite((1280, 720), (0, 0), "yuri/eyes1.png", (0, 0), "yuripupils")

image yuri eyes_base = "yuri/eyes1.png"

image yuripupils:
    "yuri/eyes2.png"
    yuripupils_move

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"

# Monika

image monika 1a:
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_010.png"
    pause 5
    repeat
image monika 1b:
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_010.png"
    pause 5
    repeat
image monika 1c:
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_010.png"
    pause 5
    repeat
image monika 1d:
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_010.png"
    pause 5
    repeat
image monika 1e:
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_010.png"
    pause 5
    repeat
image monika 1f:
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_010.png"
    pause 5
    repeat
image monika 1g:
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_010.png"
    pause 5
    repeat
image monika 1h:
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_010.png"
    pause 5
    repeat
image monika 1i:
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_010.png"
    pause 5
    repeat
image monika 1j:
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1j/monika_1j_010.png"
    pause 5
    repeat
image monika 1k:
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1k/monika_1k_010.png"
    pause 5
    repeat
image monika 1l:
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1l/monika_1l_010.png"
    pause 5
    repeat
image monika 1m:
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_010.png"
    pause 5
    repeat
image monika 1n:
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_010.png"
    pause 5
    repeat
image monika 1o:
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_010.png"
    pause 5
    repeat
image monika 1p:
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_010.png"
    pause 5
    repeat
image monika 1q:
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1q/monika_1q_010.png"
    pause 5
    repeat
image monika 1r:
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1r/monika_1r_010.png"
    pause 5
    repeat

image monika 1:
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1/monika_1_010.png"
    pause 5
    repeat
image monika 2:
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2/monika_2_010.png"
    pause 5
    repeat
image monika 3:
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3/monika_3_010.png"
    pause 5
    repeat
image monika 4:
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4/monika_4_010.png"
    pause 5
    repeat
image monika 5:
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5/monika_5_010.png"
    pause 5
    repeat

image monika 1a:
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1a/monika_1a_010.png"
    pause 5
    repeat
image monika 1b:
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1b/monika_1b_010.png"
    pause 5
    repeat
image monika 1c:
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1c/monika_1c_010.png"
    pause 5
    repeat
image monika 1d:
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1d/monika_1d_010.png"
    pause 5
    repeat
image monika 1e:
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1e/monika_1e_010.png"
    pause 5
    repeat
image monika 1f:
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1f/monika_1f_010.png"
    pause 5
    repeat
image monika 1g:
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1g/monika_1g_010.png"
    pause 5
    repeat
image monika 1h:
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1h/monika_1h_010.png"
    pause 5
    repeat
image monika 1i:
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1i/monika_1i_010.png"
    pause 5
    repeat
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m:
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1m/monika_1m_010.png"
    pause 5
    repeat
image monika 1n:
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1n/monika_1n_010.png"
    pause 5
    repeat
image monika 1o:
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1o/monika_1o_010.png"
    pause 5
    repeat
image monika 1p:
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_1p/monika_1p_010.png"
    pause 5
    repeat
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a:
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2a/monika_2a_010.png"
    pause 5
    repeat
image monika 2b:
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2b/monika_2b_010.png"
    pause 5
    repeat
image monika 2c:
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2c/monika_2c_010.png"
    pause 5
    repeat
image monika 2d:
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2d/monika_2d_010.png"
    pause 5
    repeat
image monika 2e:
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2e/monika_2e_010.png"
    pause 5
    repeat
image monika 2f:
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2f/monika_2f_010.png"
    pause 5
    repeat
image monika 2g:
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2g/monika_2g_010.png"
    pause 5
    repeat
image monika 2h:
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2h/monika_2h_010.png"
    pause 5
    repeat
image monika 2i:
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2i/monika_2i_010.png"
    pause 5
    repeat
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m:
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2m/monika_2m_010.png"
    pause 5
    repeat
image monika 2n:
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2n/monika_2n_010.png"
    pause 5
    repeat
image monika 2o:
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2o/monika_2o_010.png"
    pause 5
    repeat
image monika 2p:
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_2p/monika_2p_010.png"
    pause 5
    repeat
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a:
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3a/monika_3a_010.png"
    pause 5
    repeat
image monika 3b:
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3b/monika_3b_010.png"
    pause 5
    repeat
image monika 3c:
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3c/monika_3c_010.png"
    pause 5
    repeat
image monika 3d:
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3d/monika_3d_010.png"
    pause 5
    repeat
image monika 3e:
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3e/monika_3e_010.png"
    pause 5
    repeat
image monika 3f:
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3f/monika_3f_010.png"
    pause 5
    repeat
image monika 3g:
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3g/monika_3g_010.png"
    pause 5
    repeat
image monika 3h:
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3h/monika_3h_010.png"
    pause 5
    repeat
image monika 3i:
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3i/monika_3i_010.png"
    pause 5
    repeat
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m:
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3m/monika_3m_010.png"
    pause 5
    repeat
image monika 3n:
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3n/monika_3n_010.png"
    pause 5
    repeat
image monika 3o:
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3o/monika_3o_010.png"
    pause 5
    repeat
image monika 3p:
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_3p/monika_3p_010.png"
    pause 5
    repeat
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a:
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4a/monika_4a_010.png"
    pause 5
    repeat
image monika 4b:
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4b/monika_4b_010.png"
    pause 5
    repeat
image monika 4c:
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4c/monika_4c_010.png"
    pause 5
    repeat
image monika 4d:
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4d/monika_4d_010.png"
    pause 5
    repeat
image monika 4e:
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4e/monika_4e_010.png"
    pause 5
    repeat
image monika 4f:
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4f/monika_4f_010.png"
    pause 5
    repeat
image monika 4g:
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4g/monika_4g_010.png"
    pause 5
    repeat
image monika 4h:
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4h/monika_4h_010.png"
    pause 5
    repeat
image monika 4i:
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4i/monika_4i_010.png"
    pause 5
    repeat
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m:
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4m/monika_4m_010.png"
    pause 5
    repeat
image monika 4n:
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4n/monika_4n_010.png"
    pause 5
    repeat
image monika 4o:
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4o/monika_4o_010.png"
    pause 5
    repeat
image monika 4p:
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_4p/monika_4p_010.png"
    pause 5
    repeat
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a:
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5a/monika_5a_010.png"
    pause 5
    repeat
image monika 5b:
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_000.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_001.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_002.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_003.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_004.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_005.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_006.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_007.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_008.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_009.png"
    pause 0.01666
    "mod_assets/images/monika/Live2D/Final Products/monika_5b/monika_5b_010.png"
    pause 5
    repeat


image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat

#MC
image mc = im.Composite((960, 960), (0, 0), "mod_assets/images/player/2l.png", (0, 0), "mod_assets/images/player/2r.png", (0, 0), "mod_assets/images/player/error.png")

# Character variables
define narrator = Character(ctc="ctc", ctc_position="fixed")
define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ny = Character('Nat & Yuri', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")

# Other characters
define b = DynamicCharacter('b_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default b_name = "Barista"
define t = DynamicCharacter('t_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default t_name = "Teacher"
define q = DynamicCharacter('q_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default q_name = "???"
define nu = DynamicCharacter('nu_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default nu_name = "Nurse"
define d = DynamicCharacter('d_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
default d_name = "Doctor"



define _dismiss_pause = config.developer

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default persistent.yuri_kill = 0
default persistent.seen_eyes = None
default persistent.seen_sticker = None
default persistent.ghost_menu = None
default persistent.seen_ghost_menu = None
default seen_eyes_this_chapter = False
default persistent.anticheat = 0
default persistent.clear = [False, False, False, False, False, False, False, False, False, False]
default persistent.special_poems = None
default persistent.clearall = None
default persistent.menu_bg_m = None
default persistent.first_load = None
default persistent.first_poem = None
default in_sayori_kill = None
default in_yuri_kill = None
default anticheat = 0
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default currentpos = 0
default faint_effect = None

default s_name = "Sayori"
default m_name = "Monika"
default n_name = "Natsuki"
default y_name = "Yuri"

# Instantiating variables for poem appeal. This is how much each character likes the poem for each day.
# -1 = Dislike, 0 = Neutral, 1 = Like
default n_poemappeal = [0, 0, 0]
default s_poemappeal = [0, 0, 0]
default y_poemappeal = [0, 0, 0]
default m_poemappeal = [0, 0, 0]

# The last winner of the poem minigame.
default poemwinner = ['sayori', 'sayori', 'sayori']

# Keeping track of who read your poem when you're showing it to each of the girls.
default s_readpoem = False
default n_readpoem = False
default y_readpoem = False
default m_readpoem = False

# Used in poemresponse_start because it's easier than checking true/false on everyone's read state.
default poemsread = 0

# The main appeal points. Whoever likes your poem the most gets an appeal point for that chapter.
# Appeal points are used to keep track of which exclusive scene to show each chapter.
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# We keep track of whether we watched Natsuki's and sayori's second exclusive scenes
# to decide whether to play them in chapter 3.
default n_exclusivewatched = False
default y_exclusivewatched = False

# Yuri runs away after the first exclusive scene of playthrough 2.
default y_gave = False
default y_ranaway = False

# We choose who to side with in chapter 1.
default ch1_choice = "sayori"

# If we choose to help Sayori in ch3, some of the dialogue changes.
default help_sayori = None
default help_monika = None

# We choose who to spend time with in chapter 4.
default ch4_scene = "yuri"
default ch4_name = "Yuri"
default sayori_confess = True

# We read Natsuki's confession poem in chapter 23.
default natsuki_23 = None
