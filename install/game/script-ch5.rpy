image exception_bg = "#dadada"
image fake_exception = Text("An exception has occurred.", size=40, style="_default")
image fake_exception2 = Text("File \"game/script-ch5.rpy\", line 307\nSee traceback.txt for details.", size=20, style="_default")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    #add music to this scene? 

    "Eventually I woke up. I don’t think I slept well, but I’m not sure." 
    "I hadn’t set my alarm, so I woke up later than I normally would."
    scene bg kitchen with wipeleft_scene
    "I didn’t care. I grabbed a quick breakfast, and walked outside. I was still wearing my clothes from yesterday."
    scene bg residential_day with wipeleft_scene
    "I waited for Sayori, but she never came to greet me. I hoped that she had gone to school already, without me." 
    "Unfortunately, I didn’t have the luxury of waiting there forever, and had to make my way to school as well."

    scene bg corridor with wipeleft_scene
    show monika 2b zorder 2 at t11
    m "Hey there [player]! How's it going?"
    m 2e "You're kind of late today."
    mc "I'm... okay..."
    m 1l "No Sayori? I guess you really left her hanging this morning."
    m 1m "Not used to seeing that so early in the week..."
    mc "Huh?"
    m 1k "I guess she's going to sleep forever at this rate."
    m 4j "I thought things would be different this time, but I guess she's just a lost cause."
    m 2i "Hey... No matter what happens, don't blame yourself, okay?"
    m 2g "It's not your fault."
    show monika 2h zorder 1 at thide
    hide monika 
    "Something about what Monika said sent a shiver down my spine. A terror that I couldn’t quite explain started to grip me." 
    "I pulled out my phone to try and get ahold of Sayori, to make sure that she was okay." 
    "A simple text should do it." 
    "Wait... what the hell is this?" 
    "The last message I had sent her…"
    #add phone screen image? 
    "I DON'T WANT TO TALK TO YOU EVER AGAIN"
    "That... that's not what I sent."
    "What the hell?!"
    mc "Monika, I... I have to go. Right now!"
    m "Okay, but don't strain yourself~"
    scene bg corridor with wipeleft
    scene bg residential_day with wipeleft
    scene bg house with wipeleft
    "I ran as fast as I could to Sayori's house."
    mc "Sayori, open up, please!"
    "I banged, and banged, and banged on her door, desperate to get in."
    "All rational thought was starting to leave me."
    #Knocking sound effect? 
    "I banged on the door so hard, my hands were starting to feel broken."
    mc "I need to change tactics."
    "I picked up the biggest rock I could find nearby."
    "I was getting in, even if I had to break through a window."
    "Thankfully, my eyes caught a glare beneath me."
    "As luck would have it, there was a spare key under that rock." 
    #Door opening sound effect?
    "I frantically unlocked the door, and stumbled inside."
    scene black with wipeleft
    "No sign of her."
    "I hurried to her room." 
    "This was starting to feel like an invasion of privacy, but I couldn’t care at the moment." 
    "I had to make sure she was okay. I had to." 
    "Her door… I gently… No!" 
    "I kick the door down, with all of my might."
    mc "{cps=30}.......Sayo--{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ renpy.save_persistent()
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    $ pause(3.75)
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    $ pause(0.01)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    $ pause(2.0)
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    $ pause(1.5)
    show white zorder 2
    show splash_glitch zorder 2
    $ pause(1.5)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    $ pause(4.0)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.2)
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    $ pause(0.75)
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("Oh jeez...I didn't break anything, did I? Hold on a sec, I can probably fix this...I think...\nActually, you know what? This would probably be a lot easier if I just deleted her. She's the one who's making this so difficult. Ahaha! Well, here goes nothing.", False)
        except: pass
    $ pause(6.0)


    "..."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "This couldn’t be real…"
    "No, I refuse to accept this…"
    "She can’t be…"
    "I was going to make things right."
    "I was!"
    "But now… I never can."
    "I just got her back in my life, and now she’s gone again, forever."
    scene black with dissolve_cg
    "No, this is just a nightmare, it has to be."
    "I’m still in my bed, sleeping."
    "I’m going to wake up any minute now."
    "..."
    "Come on, wake up!"
    "Wake up!!"
    "Please... Just wake up..."

    
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
