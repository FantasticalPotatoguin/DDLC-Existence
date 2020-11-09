image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ s_name = "Sayori"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.sayori_back:
            try:
                renpy.file("../characters/sayori.chr")
                renpy.call_screen("dialog", message="Thanks for putting Sayori back.\nI love how thoughtful you are.", ok_action=Return())
                persistent.monika_back = True
            except:
                pass
                
    $ restore_all_characters()
    "Wait, did it work? I'm outside my house."
    play music t2
    s "Heeey!"
    "It's... It's..."
    show sayori 4r at t11 zorder 2
    s "Hehe. I caught up to you this time!"
    #Could use a better transition to something sad here.
    stop music fadeout 1.0
    s 4w "Huh? [player], why are you crying? What's wrong?"
    play music t10 fadein 4.0
    "I can’t help myself. The tears just keep flowing."
    "I thought I’d never…" 
    "I give Sayori a tight hug. I can feel her warmth. She’s really here, alive…"
    # play music t9
    "She seems surprised and unsure of what to do at first, but she gives me a hug in return."
    mc "I thought, that I would never see you again."
    s 1y "Hey, it's okay. I'm right here."
    "For the first time in a while, everything feels... good."
    "I wish this moment could last forever."
    "Unfortunately, that's just wishful thinking."
    "Eventually, we had to break up our hug and start making our way towards school."
    s 1b "I'm surprised you missed me so much."
    s 2b "It's only been a few months..."
    mc "I... had an awful dream."
    mc "I did something horrible, or said something horrible to you."
    mc "I'm not sure what exactly I did, but..."
    mc "I hurt you so bad, and you... you..."
    mc "Went and killed yourself."
    s 2n "Huh?"
    mc "It was awful..."
    stop music fadeout 2.0
    s 4x "There's no need to feel bad, okay?"
    play music t9 fadein 2.0
    s "It was just a nightmare."
    "I really wish that were true. I really do."
    s "I'm right here safe and sound."
    mc "Yeah..."
    s "Besides, I'm not going to kill myself over something like that."
    s "This isn't some kind of soap opera."
    s "You can have more faith in me than that."
    mc "I know."
    "This is just some weird dating sim type game."
    "Well, I think so anyway. Why else would I be the only guy in a club full of cute girls?"
    "Wait, does that mean Sayori was supposed to be a romance option too?"
    "I... don't want to think about that right now."
    s 5d "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "Actually, yes, I have."
    s 1k "Huh? Oh..."
    s "Which one?"
    mc "I'll tell you later."
    s 1h "Oh, come on [player]."
    s "It's not nice to keep secrets."
    mc "Haha."
    mc "You're like a big child sometimes."
    s 5d "Hey, that's mean. Meanie..."
    mc "Aww, but I like that about you."
    s 4m "What?"
    s 4y "Geeze, what are you saying?"
    "I probably look silly with this big grin on my face, but I can't help it."
    "Bantering with Sayori like this..."
    "I've really missed it."
    "I've really missed her."
    scene bg corridor with wipeleft
    stop music fadeout 2.0
    show sayori 1b at t11 zorder 2
    play music t3 fadein 2.0
    mc "Hey, Sayori..."
    s "Hmm?"
    mc "I'm sorry for neglecting you."
    mc "Dream or not, it made me realize just how much I've taken our friendship for granted."
    s "..."
    s "It's not your fault."
    s "I'm the one who started sleeping in more and more."
    s "I never blamed you for leaving me behind."
    s 1a "I know you have much more important things to be doing than hanging out with me."
    mc "Sayori, almost nothing in my life is more important than you."
    s "..."
    mc "I promise you, I'll never take our friendship for granted again."
    s "Okay..."
    mc "I'll see you later, alright?"
    s "Uhuh..."
    "I give Sayori a smile before I leave for class."
    
    scene bg class_day with wipeleft_scene
    play music m1
    "Another ordinary day of school, I guess."
    "The teacher's droning on and on."
    "Most of the class is struggling to pay attention."
    "It's hard to believe that this is all just a game, that none of this is real."
    "This boredom certainly feels real..."
    "I look at my hands, and tightly grasp them together."
    "My hands feel real. I feel real."
    "..."
    "I shouldn't overthink this."
    "I need to convince Monika that all of this is real anyway, not have my own existential crisis."
    stop music fadeout 2.0
    scene bg class_day with wipeleft_scene
    pause 1.0
    play music t2 fadein 1.0
    "Finally, lunch time."
    "The nice thing about going to a Japanese school is that we get to eat in the classroom."
    "Err, wait, this is Japan, right?"
    "There I go again, overthinking things."
    "Maybe I should start writing all of this down."
    "Well, that can wait for after lunch."
    "Oh great, I forgot to pack a drink with me. I guess I'll just get one from a vending machine."
    "I should have enough money for that."
    scene bg corridor with wipeleft_scene
    "Yeah, I guess some lemonade will do."
    "Wait, is that?"
    show yuri 3m at t11 zorder 2
    "Oh, I didn't know Yuri had the same lunch block as me."
    mc "Hey, how's it going?"
    y 3n "Huh?"
    y 3o "I'm sorry, are you talking to me?"
    mc "Yeah..."
    y "It's just that..."
    y "You're acting very cordial with me, even though I don't believe we've met yet."
    "Oh crap, I'm an idiot."
    "Of course Yuri is confused. We {i}haven't{/i} met yet."
    mc "Oh, uh, sorry about that. I guess I came on a little too strong."
    mc "It's just that, I hadn't seen you around before, so I figured I'd say hi."
    y 3w "Okay..."
    mc "Sorry. I know I'm coming across as strange. I'll leave you alone now."
    y 3n "Oh, no! You're fine!"
    y "You were just trying to be nice. I'm the one that made things awkward."
    y 4b "I'm sorry. I'm sure I've made a horrible first impression."
    mc "Hey, no, you're fine. I don't think badly of you or anything."
    y "..."
    mc "Here, let's start over. I'm [player]."
    y 3q "My name is Yuri."
    mc "It's very nice to meet you Yuri."
    y 3s "It's nice to meet you too, [player]."
    mc "So, do you usually eat out here in the hallway?"
    y 3g "Umm, sometimes."
    y "It's usually nice and quiet out here, which makes it easier to read."
    mc "Oh, sorry, I hope I'm not taking away from your reading time."
    y 3t "No, you're fine."
    y "I actually just finished my book, so I'll probably just focus on eating for the rest of lunch."
    mc "Would you mind if I joined you?"
    y 3p "Huh!?"
    y "You... want to eat with me?"
    mc "Sure, if you don't mind. Though, I don't want to take away from your quiet time."
    y 3v "The peace and quiet is nice, though I suppose it can get a bit lonely..."
    mc "I usually just eat by myself too."
    mc "So, why not be lonely together, huh?"
    y 4c "Umm... I guess that would be okay."
    "I went and grabbed my lunch, and took a seat next to Yuri."
    y 2u "..."
    "We mostly just made small talk, otherwise it was a pretty quiet lunch."
    "It was a bit awkward to be honest..."
    "Soon, lunch came to an end."
    mc "Well, this was nice."
    y "Was it? I know I didn't have much to say. Sorry..."
    mc "Nah, you're fine. Sure, it was quiet, but it was still nice."
    mc "Certainly better than eating alone."
    y 3v "..."
    mc "We should do this again."
    y 3n "Huh? But, why?"
    y 4b "I know I made very poor company..."
    mc "I mean, I know we didn't have much to say, but I still enjoyed eating with you."
    mc "Quiet or not, you made good company, trust me."
    y 4a "...okay."
    mc "I'll see you later, Yuri."
    stop music fadeout 2.0
    scene bg class_day with wipeleft
    "And I'm back to boring classtime."
    "I couldn't be the protagonist of a cool action game or something, nooo."
    "It just had to be a highschool slice of life type game."
    "Well, at least it's not a horror game."
    scene bg class_day with wipeleft_scene
    "Finally, the school day is over."
    "Well, I guess I better make my way towards the clubroom."
    scene bg corridor with wipeleft_scene
    "And thus, today marks the day I joined the Literature Club for the third time."
    "Hmm... How do I want to go about doing this?"
    play music t3
    scene bg club_day with wipeleft
    "Hello, beautiful ladies! I'm here to write the way into your hearts."
    show natsuki 4x at t11 zorder 2
    n "Yeah, no, I don't think so."
    n 4o "I suggest you leave now while you can still walk out."
    stop music
    scene bg corridor
    "Well, that was a stupid idea."
    "I guess I'll just go in and see what happens."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Hello? Is this the room for the Literature Club?"
    show sayori 2m at t11 zorder 2
    s "Huh? [player], what are you doing here?"
    hide sayori
    show yuri 1f zorder 2 at t11
    y "Oh, so {i}you're{/i} the [player] Sayori is always talking about!"
    y 1a "Sayori always says nice things about you."
    y "(I can certainly see why.)"
    mc "Well, I'm here to join the club."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "Seriously? A boy?"
    n "There goes the atmosphere..."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a
    mc "..."
    "I really shouldn't be surprised at this point, but..."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"
    "Hehe. Saying that never gets old."

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at f32
    hide monika
    hide yuri

    n 2c "What are you looking at?"
    n "If you want to say something, say it."
    mc "S-Sorry..."
    show natsuki zorder 2 at t32
    show yuri 2l zorder 2 at f33
    y "Natsuki..."
    $ n_name = 'Natsuki'
    show yuri zorder 2 at t33
    show natsuki zorder 2 at f32
    n 5s "Hmph."
    show natsuki zorder 2 at t32
    show sayori 2o zorder 2 at f31
    s "So, wait, you're here to join the club?"
    mc "Well, yeah. You said I should join a club, and which one would be better than the one my best friend's a part of?"
    s 4r "Eeeeehhh! I'm so excited!"
    s "You're going to have so much fun here."
    show natsuki 2z zorder 2 at t32
    n "Well, at least the cupcakes won't go to waste now."
    hide sayori
    hide natsuki
    hide yuri
    "The rest of the club meeting goes how it usually does."
    "The cupcakes taste great, Yuri gets flustered, and Sayori seems really happy."
    "It's great and all, especially the cupcakes, but..."
    "I don't want to go through this day again."
    "It's pretty tiring to go through the same day again and again, especially if everything is exactly the same each time."
    "Eventually, the day comes to an end, and everybody starts to leave."
    show sayori 1a at t21 zorder 2
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Of course, Sayori."
    s 4q "Yaay~"
    show monika 1a at t22 zorder 2
    m "You two have fun~"
    m "Oh, and [player]?"
    "Monika gets close to me and whispers into my ear."
    m 5 "Don't think I've forgotten what you've promised me."
    m "We will talk more tomorrow."
    "With that, Monika waves us bye as we leave."
    scene bg residential_day
    with wipeleft_scene
    "The whole way, what Monika said lingers in my mind."
    "I still need to convince Monika that this world is just as real as she is."
    "This is going to be very hard..."
    "Maybe Yuri can help me. She's read a lot of books, and is clearly smart."
    show sayori 1a at t11 zorder 2
    s "So, what are you thinking about?"
    mc "Huh?"
    s "You seemed really deep in thought."
    s 1x "Thinking about all of the cute girls in the club~?"
    mc "What are you trying to get at?"
    s 1d "Come on [player]. I saw how Monika whispered into your ear before we left. You already know each other too."
    mc "Sayori, there's nothing between me and Monika. That was just... something club related."
    s 2l "What about you and Yuri then? You certainly seemed familiar with each other."
    s "You and Natsuki have a lot in common too. Plus, she's super cute."
    s 3n "Oh, don't tell her I said that."
    mc "Yuri and I just happend to run into each other during lunch. That's why we were familiar with each other."
    mc "Natsuki and I may have things in common, but that doesn't really mean anything either."
    s 3l "If you say so..."
    mc "Come on Sayori, there's no need to be jealous."
    s 2h "Huh?"
    mc "I'm walking home with you, aren't I?"
    s 1k "That's... not really what I mean."
    mc "Besides, you're way cuter than Natsuki."
    s 1x "Now you're just being silly."
    mc "Uh oh. I guess you've rubbed off on me too much."
    s 5c "Meanie..."
    "I give Sayori's hair a little ruffle."
    mc "Well, I'll see you tomorrow Sayori."
    s 2r "See ya!"
    hide sayori
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."
    
    
    call ch1_main
    
    return
    
    
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "I wanted to thank you for getting rid of Monika."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "That's right..."
        s "I know everything that she did."
        s 1x "Maybe it's because I'm the President now."
        s "But I really know everything, [player]."
        s 1q "Ehehe~"
        s 1d "I know how hard you tried to make everyone happy."
        s "I know about all of the awful things that Monika did to make everyone really sad..."
        s 1b "But none of that matters anymore."
        s "It's just us now.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "It's just us now.{fast}"
        hide room_glitch
        s 1d "And you made me the happiest girl in the whole world."
        s "I can't wait to spend every day like this..."
        s "With you."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        $ pause(0.3)
        stop sound
        s 1q "Forever and ever..."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "F"
        s "o"
        s "r"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        s "e"
        s "v"
        s "e"
        window show(None)
        stop music
        call screen dialog("No...", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "...Eh?"
        s "W-What's happening...?"
        call screen dialog("I won't let you hurt him.", ok_action=Return())
        s "Who..."
        s "I-It hurts--"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        $ pause(0.35)
        stop sound
        hide screen tear
        window show(None)
        s "Ah--"
        call screen dialog("I'm sorry... I was wrong.", ok_action=Return())
        call screen dialog("There's no happiness here after all...", ok_action=Return())
        call screen dialog("Goodbye, Sayori.", ok_action=Return())
        call screen dialog("Goodbye, [player].", ok_action=Return())
        call screen dialog("Goodbye, Literature Club.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.35)
        stop sound
        hide screen tear
        scene black
        $ pause(3.0)
        return

    label ch40_clearall:
        s "I wanted to thank you for spending so much time with us all."
        play music mend
        s 2d "You worked so hard to make each and every one of us happy."
        s "You comforted us through our hard times."
        s "And you helped us all get along with each other."
        s 1a "Do you get it, [player]?"
        s "Because I'm President now, I understand everything."
        s 1q "You really didn't want to miss a single thing in this game, did you?"
        s 1a "You saved and loaded so many times, just to make sure you could spend time with everyone."
        s "Only someone who truly cares about the Literature Club would go that far."
        s "But..."
        s 4d "All along, that's all I ever wanted."
        s "For everyone to be happy and care about each other."
        s 4q "Ahaha..."
        s 1t "It's kind of sad, you know?"
        s "After all you've done for us, there isn't much I can do for you in return."
        s "We've already reached the end of the game."
        s 1y "So..."
        s "This is where we say goodbye."
        s 1d "Thank you for playing {i}Doki Doki Literature Club{/i}."
        s "I'm going to miss you, [player]."
        s "Come visit sometime, okay?"
        s "We'll always be here for you."
        s 1t "We..."
        scene black with dissolve_cg
        s "We all love you."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
