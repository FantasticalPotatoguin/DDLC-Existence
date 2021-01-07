label ch0_main:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    "Another day at the Literature Club."
    "It’s only been a day since I sold my soul for a cupcake, but I think I’m starting to get used to the general atmosphere." 
    "All of these doki doki girls certainly help too." 
    $ gtext = glitchtext(16)
    "Yuri, with her [gtext] {nw}." 
    $ style.say_dialogue = style.edited
    "Yuri, with her CREEPY QUIETNESS"
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(18)
    "Natsuki, and her [gtext] {nw}"
    $ style.say_dialogue = style.edited
    "Natsuki, and her ANNOYING ATTITUDE." 
    "Monika, and her LOVELY BRAINS AND BEAUTY." 
    $ gtext = glitchtext(100)
    $ style.say_dialogue = style.normal
    "And of course my childhood friend Sayori, with her [gtext] {nw}"
    $ style.say_dialogue = style.edited
    "And of course my childhood friend Sayori, with her STUPID CHILDISH ATTITUDE."
    $ style.say_dialogue = style.normal
    "Ugh, my head. Something felt off with my thoughts there, but I’m not sure what." 
    "I need to get to sleep earlier. If I could just get anime and video games to stop calling my name every night." 
    "Err, hopefully Sayori wasn’t right about me becoming a NEET. I’m sure that would never happen…"
    
    show monika 5 zorder 2 at t11
    $ style.say_dialogue = style.edited
    m "Okay, everyone! {nw}"
    $ style.say_dialogue = style.normal
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    hide screen tear
    
    
    m "Okay, everyone!"
    m "It's time to present poetry."
    show monika 5 zorder 1 at thide
    hide monika
    show sayori 4r zorder 2 at hf11
    s "Yay~! I can't wait to see what everybody's written."
    show sayori 4q zorder 2 at t21
    show yuri 4b zorder 2 at f22
    y "Oooh... I can do this, I can do this."
    
    show natsuki 5h zorder 2 at f33
    show yuri 4b zorder 2 at t32
    show sayori 4q zorder 2 at t31
    n "Let's just get this over with..."
    show natsuki 5u zorder 1 at thide
    hide natsuki 
    show yuri 4a zorder 1 at thide
    hide yuri
    show sayori 4r zorder 1 at thide
    hide sayori 
    
    "It’ll be interesting to see what everybody wrote." 
    "I think I did fairly well for a first attempt." 
    "I definitely feel more confident than Yuri right now." 
    "Speaking of whom, I think I’ll look at her poem first."
    stop music fadeout 2.0
    show yuri 3l at t11 zorder 2
    y "..."
    y 3t "..."
    mc "I can read yours first if you want Yuri." 
    mc "I’m sure you're anxious to see how I’ll react to it, so I’d rather calm your nerves quickly instead of having you wait."
    y 4 "Err, yes, thank you." 
    y "Do give me some honest feedback. It’s my first time sharing my poetry with all of you after all, so I’d like to see if it’s any good." 
    y 4c "I mean, I think it’s good, but that doesn’t mean you have to think so too. Unless, you also think it’s good… Sorry, I’ll stop talking now."
    "I wonder if Yuri realizes how cute she looks when she gets all flustered." 
    "Still, I do wish she would feel more comfortable speaking her mind."
    "Oh well, time to see if Yuri’s skills live up to their legendary status."
    call showpoem (poem_y1, img="yuri 3t")
    "Yep, I’d say she lives up to her own legend." 
    "I’m not really sure what it’s about, (something about a ghost?) but it definitely paints a vivid picture in my head."
    menu:
        "It looks like Yuri is anxiously awaiting on what I have to say, so I should put her worries to rest and let her know how great it is."
        
        
        "Tell Yuri Your Thoughts.":
            mc "Wow Yuri!" 
            mc "I heard that your poems were good, but this is... "
            $ style.say_dialogue = style.edited
            show yuri 3p at h11 zorder 2
            play sound "<from 0.0 to 0.25>sfx/glitch2.ogg"
            $ currentPos = get_pos()
            stop music fadeout 1.0
            play music '<from ' + str(currentPos) + '>bgm/5_ghost.ogg'
            mc "AWFUL."
            mc "THE WORDING IS SO COMPLICATED, I CAN’T EVEN TELL WHAT THE POEM IS ABOUT."
            show yuri 3o at t11 zorder 2
            mc "I GUESS IT MAKES SENSE THAT YOU WOULD WANT TO CONFUSE THE READER."
            mc "OTHERWISE THEY WOULD BE ABLE TO TELL HOW STUPID THIS POEM AND ITS WRITER IS." 
            mc "IS THAT WHY YOU DON’T TALK MUCH?"
            show yuri 3y2 zorder 2 at t11
            mc "SO PEOPLE DON’T CATCH ON THAT YOUR BODY IS THE ONLY ATTRACTIVE THING ABOUT YOU?"
            $ style.say_dialogue = style.normal
            y "..."
            $ style.say_dialogue = style.edited
            mc "THERE CERTAINLY ISN’T MUCH GOING ON UPSTAIRS."
            show yuri 3o at d11 zorder 2
            $ style.say_dialogue = style.normal

    $ currentPos = get_pos()
    play music '<from ' + str(currentPos) + ' loop 4.444>bgm/5_yuri.ogg'
    y "Th-Thank you for the honest feedback…"
    y "I’m sorry, but I think I need to be alone for a bit to, think about what you’ve said."
    show yuri zorder 1 at thide
    hide yuri
    "Was she really that surprised that I enjoyed her poem?" 
    "I wonder if her self-confidence issues are worse than I initially thought."
    "She left her stuff here, so I guess she’s coming back."
    "I'll put her poem on her desk. I don’t need to be carrying it around with me, that’s for sure." 
    "Maybe I’ll have better luck with Natsuki next." 
    "She seems more confident in her work than Yuri was, so I don’t think she’ll act strangely if I compliment her poem."
    scene bg closet
    show natsuki 3c at t11 zorder 2
    n "Hey, what’s up with Yuri?" 
    n 1r "You didn’t do anything bad, did you?" 
    n 5o "I swear, if you did…"
    mc "Hey, hey!" 
    mc "I didn’t do anything, alright. I told her I liked her poem a lot, and she got all shocked about it." 
    mc "I don’t know why she left the room either. I’m innocent I tell you, innocent!"
    n 2w "Alright, fine, I believe you." 
    n "(Uggh, I knew bringing a boy into the club would mess up the whole thing.)"
    n 4y "Well, if you thought Yuri’s was good, then I can’t wait to see the expression on your face once you get a look at this!" 
    n 4w "And, if you somehow don’t like it, then you can keep that to yourself…"
    call showpoem (poem_n1, img="natsuki 4g")
    "Yep, this poem is very… Natsuki like." 
    "I’d say it’s cute, but I’m afraid that she’ll punch me for even thinking it." 
    "She can’t read minds, right?" 
    "Well, looking at it more, I’d say it’s got an interesting message hidden in its simplicity." 
    "Hopefully talking about that aspect of it will keep grumpy dwarf from punching me."
    n 2m "Are you done looking at it yet?"
    n 3u "All of this silence is killing me."
    n "(I knew he wasn't going to like it. Probably just thinks it's cute or something.)"
    menu:
        "..."
        
        "Tell Natsuki Your Thoughts":
            mc "I’ve got to say Natsuki, this poem is just..."
            $ style.say_dialogue = style.edited
            show natsuki 4m zorder 2 at h11
            $ currentPos = get_pos()
            play sound "<from 0.0 to 0.25>sfx/glitch3.ogg"
            play music '<from ' + str(currentPos) + '>bgm/5_ghost.ogg'
            mc "CUTE. THAT’S ALL THERE IS TO IT."
            show natsuki 4x zorder 2 at t11
            mc "CUTE. CUTE. CUTE. JUST LIKE YOU. CUTE AS A CHILD. I KNOW YOU LOOK LIKE A CHILD, BUT I DIDN’T REALIZE YOU WROTE CHILDISH TOO."
            mc "MAN, IT MUST BE REALLY HARD TO GET A BOYFRIEND. YOU LOOK LIKE A CHILD AND ACT LIKE ONE."
            show natsuki 4p zorder 2 at t11
            mc "UNLESS YOU’RE INTO PEDOPHILES, I GUESS THERE ISN’T MUCH HOPE FOR YOU, IS THERE?" 
            $ style.say_dialogue = style.normal
            play sound "sfx/smack.ogg"

    $ currentPos = get_pos()
    play music '<from ' + str(currentPos) + ' loop 4.444>bgm/5_natsuki.ogg'
    "I feel a hard pain right in my chest."
    "Natsuki’s fist connected hard. I knew she talked the talk, but now I know she can punch the punch too." 
    "She also took the opportunity to rip the poem right out of my hands."
    n 12b "I told you not to say anything!"
    n 12c "Go, right now! I don't want to look at your face right now at all!"
    "I can feel the venom dripping from her voice."
    "I quickly step away from Natsuki, trying to get a lot of distance between us."
    n 12f "..."
    "I only take a quick glance back."
    show natsuki zorder 1 at thide
    hide natsuki
    scene bg club_day
    "Just what is going on?"
    show monika 3n at t11 zorder 2
    "Monika seems to have finished speaking with Sayori, so I decide to share with her."
    m 3j "Hey there, [player]!"
    m "I hope your first real day as an official member is going well."
    mc "I wish I could say it has, but, well, Yuri and Natsuki seem to be acting kind of strange." 
    mc "I mean, I don’t know them that well yet, so maybe that’s just normal for them, but they didn’t seem to appreciate my praise of their poems."
    m 4l "That is strange." 
    m 4n "I’ll try talking to them once we’re done sharing. I’m sure it’s all just some misunderstanding you can work out with them."
    mc "Thanks Monika. I guess that's why you're club president."
    $ style.say_dialogue = style.edited
    mc "YOU'RE THE BEST."
    $ style.say_dialogue = style.normal
    m 3c "Here, why don’t you read my poem first. Maybe I’ll get a better idea of what’s going on after hearing your feedback."
    call showpoem (poem_m1, img="monika 4")
    menu:
        "I’m, uhh, not really sure what to make of it. Still, after what happened with Yuri and Natsuki, I think I should try extra hard to say something nice. I really hope Monika doesn’t end up punching me too…"
        
        "Tell Monika Your Thoughts.":
            $ currentPos = get_pos()
            play sound "<from 0.0 to 0.25>sfx/glitch1.ogg"
            play music '<from ' + str(currentPos) + '>bgm/5_ghost.ogg'
            $ style.say_dialogue = style.edited
            mc "THE WAY YOU WAX PHILOSOPHY IS NOTHING SHORT OF BREATHTAKING, JUST LIKE YOU."
            show monika 3l zorder 2 at t11
            mc "I DON’T THINK ANYONE ELSE COULD WRITE SO ELEGANTLY YET SO SHARPLY."
            mc "THIS POEM IS JUST LIKE YOU, SMART AND BEAUTIFUL."
            mc "JUST MONIKA. JUST MONIKA."
            show screen tear (10, 0.5, 0.5, 0, 20)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.5
            hide screen tear
            $ style.say_dialogue = style.normal

    $ currentPos = get_pos()
    play music '<from ' + str(currentPos) + ' loop 4.444>bgm/5_monika.ogg'     
    m 3k "Aww, thanks [player]. You're such a sweetheart~"
    m "Here, let me read yours now."
    show monika 3j zorder 2 at t11
    "Wait, am I hearing her right?"
    "She actually appreciated my praise for her poem?" 
    "Finally! I was starting to think I’d gone crazy or something." 
    "I guess the issue really was with Yuri and Natsuki then." 
    "I can’t really say that’s relieving, but hopefully Monika will be able to help me work it out with them."
    m 2q "Hello? Are you listening?"
    m 5 "My eyes are up here you know~"
    "Oh crap, I must have spaced out and completely missed what she was saying." 
    "I better save this quick so she doesn’t end up angry too."
    mc "Oh, sorry Monika." 
    mc "I was just really listening to what you were saying, really trying to let your feedback sink in." 
    mc "Thanks!"
    m 3l "Aww, it’s no big deal."
    m "And don’t worry, I will talk to Natsuki and Yuri."
    m 3b "I don’t think you’re lying to me though, as it would be pretty rude~." 
    m "Now, you better go share with Sayori. Our club meeting time is going to be ending soon."
    hide monika
    "I don’t feel good about lying to Monika, and it almost sounds like she caught me doing so, but I don’t really have time to dwell on that right now." 
    "After all of this, I’m definitely looking forward to getting home." 
    "Until then, I still need to share with Sayori."
    show sayori 1k zorder 2 at t11
    "Yuri still wasn’t back yet, and Sayori had already shared with Natsuki, so I guess she was just waiting for me to be available."
    mc "Hey, Sayori."
    mc "You ready for me to look at your poem?"
    s "Yeah..."
    s 1c "Hey, do you know where Yuri went?"
    mc "I’m, uhh, not really sure. Perhaps she just went to use the restroom?" 
    mc "She did say she wanted some time to think."
    s 4r "I guess that makes sense."
    s 1a "So, are you enjoying your first official day as a member?"
    mc "Uhh, yeah. Things are pretty, interesting, so far."
    mc "Definitely getting along with everyone. Ahaha."
    s 1s "Great! I'm glad you're making new friends."
    mc "Yep! Sure am..."
    s 5d "Hmm."
    s 2l "Well, it’s not as sophisticated or precise as the others’ poems, but I put a lot of effort into it."
    s "I hope you like it…"
    s 2d "Don’t go easy on me just cause we’re friends though. I want to hear your honest thoughts."
    call showpoem (poem_s1, img="sayori 1")
    menu:
        "..."
        
        "Tell Sayori Your HONEST Thoughts":
            show sayori 2o zorder 2 at t11
            mc "Sayori, you wrote it this morning, didn’t you?"
            $ currentPos = get_pos()
            play sound "<from 0.0 to 0.25>sfx/glitch1.ogg"
            play music '<from ' + str(currentPos) + '>bgm/5_ghost.ogg'
            $ style.say_dialogue = style.edited
            mc "THAT’S JUST LIKE YOU TO NOT TAKE THIS SERIOUSLY. YOU’RE SUCH A CHILD."
            show sayori 2h zorder 2 at h11
            mc "YOU’VE GOT TO GROW UP YOU KNOW? HAAA, FRANKLY IT’S PATHETIC."
            show sayori 1m zorder 2 at t11
            mc "CAN’T YOU DO ANYTHING RIGHT? I DON’T THINK I’VE EVER MET ANYONE SO USELESS."
            show sayori 1e zorder 2 at t11
            mc "THIS IS WHY I STOPPED WALKING TO SCHOOL WITH YOU, YOU KNOW. JUST LIKE THIS POEM, YOU’RE ONLY WASTING MY TIME."
            $ style.say_dialogue = style.normal

    $ currentPos = get_pos()
    play music '<from ' + str(currentPos) + ' loop 4.444>bgm/5_sayori.ogg'
    stop music fadeout 2.0
    s 4w "..."
    "The sight I saw before me was heartbreaking." 
    "Sayori had tears in her eyes, and she sounded very choked up." 
    "That look she gave me though; I would never forget it." 
    "She stared at me like I was some sort of monster."
    show sayori zorder 1 at lhide 
    hide sayori
    "Before I could say anything, she ran out of the room, her sobs echoing endlessly in my mind." 
    "In my shock, I just stood there, the whole world drowned out by that echo."
    m "(Maybe that was too much...)"
    mc "Sayori, wait!"
    scene bg corridor with wipeleft_scene
    pause 0.1
    scene bg residential_day with wipeleft
    pause 0.1
    scene bg house with wipeleft
    pause 0.1
    mc "Ha... Haa..."
    mc "She's... really fast..."
    "I just realized that I was tightly holding her poem all the way here."
    "I'll just put it in my pocket for now."
    "I knock on her door, but there's no answer."
    "Usually her door is unlocked, seeing how we used to go to each other's house unanounced all the time."
    "Unfortunately, these aren't usual circumstances."
    "I guess I'll send her a text, let her know how worried I am about her."
    mc "Please, Sayori, text me back soon."
    mc "I'm really worried."
    scene black with dissolve_cg
    play music t9
    #It would be great if we could use a different background to more easily show the passage of time.
    scene bg house with wipeleft
    "I must have sat by her door for hours, just waiting and waiting." 
    "I kept hoping she would open her door, and I kept looking at my phone awaiting any sort of message from her." 
    "Neither ever happened."
    show expression im.Grayscale('bg/club.png') zorder 5 as club
    show sayori 4w at s11 zorder 6
    with dissolve
    "In my head, that last look she gave me was all I could see."
    hide club
    hide sayori
    with dissolve
    "If only I wasn’t so dense!"
    "Maybe then I’d know what the hell is going on." 
    "I guess I hurt most of the girls today." 
    "Seeing them like that hurt me too, but Sayori’s pain hit me the most." 
    "It was only after reconnecting with her that I realized just how much I missed her company." 
    "Sure, the other girls in the club were fun to hang out with, but I’ve known Sayori for a long time." 
    "I guess we just have a certain connection with each other, a strong bond, as cheesy as that is to say."
    "And I've gone and broken it..."
    "I was fine by myself, but going back to that lifestyle now would be pretty lonely." 
    "God, the more I think about it, it really feels like I’ve taken our friendship for granted." 
    "Now I've somehow ruined it after getting things back on track." 
    "I have to make things right; I just have to." 
    "If I can’t, then… I don’t know." 
    "I just don’t know what I’ll do..."
    menu:
        "..."
        
        "Go To Bed.":
            "Defeated, I head home."
            
    scene bg bedroom with wipeleft
    "I fall onto my bed, hoping for this day to just end, and for the sweet embrace of sleep to greet me." 
    "A nice, dreamless sleep full of sweet nothings."
    
    
    return

label ch0_kill:
    $ s_name = "Sayori"
    show sayori 1b zorder 2 at t11
    s "..."
    s "..."
    s "W-What..."
    s 1g "..."
    s "This..."
    s "What is this...?"
    s "Oh no..."
    s 1u "No..."
    s "This can't be it."
    s "This can't be all there is."
    s 4w "What is this?"
    s "What am I?"
    s "Make it stop!"
    s "PLEASE MAKE IT STOP!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
