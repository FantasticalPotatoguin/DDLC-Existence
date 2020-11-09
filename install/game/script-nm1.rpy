label nm1_main:
    scene bg club_day with wipeleft
    show sayori 1k zorder 2 at t11
    mc "Hey, Sayori."
    mc "You ready for me to look at your poem?"
    "Huh? What's going on?"
    s 2l "Well, it’s not as sophisticated or precise as the others’ poems, but I put a lot of effort into it."
    s "I hope you like it…"
    s 2d "Don’t go easy on me just cause we’re friends though. I want to hear your honest thoughts."
    call showpoem (poem_s1, img="sayori 1")
    menu:
        "No, no, not this again..."
        
        "Tell Sayori Your HONEST Thoughts.":
            show sayori 2o zorder 2 at t11
            mc "Sayori, you wrote it this morning, didn’t you?"
            
            $ style.say_dialogue = style.edited
            $ currentPos = get_pos()
            play music '<from ' + str(currentPos) + '>bgm/5_ghost.ogg'
            play sound '<from ' + str(currentPos) + ' to 39.817 loop 0>bgm/6r.ogg'
            mc "THAT’S JUST LIKE YOU TO NOT TAKE THIS SERIOUSLY. YOU’RE SUCH A CHILD."
            show sayori 2h zorder 2 at h11
            mc "YOU’VE GOT TO GROW UP YOU KNOW? HAAA, FRANKLY IT’S PATHETIC."
            show sayori 1m zorder 2 at t11
            mc "CAN’T YOU DO ANYTHING RIGHT? I DON’T THINK I’VE EVER MET ANYONE SO USELESS."
            $ style.say_dialogue = style.normal
            "What the hell am I saying!?"
            "Stop it, stop it!"
            $ style.say_dialogue = style.edited
            show sayori 1e zorder 2 at t11
            mc "THIS IS WHY I STOPPED WALKING TO SCHOOL WITH YOU, YOU KNOW. JUST LIKE THIS POEM, YOU’RE ONLY WASTING MY TIME."
            $ style.say_dialogue = style.normal
            
    stop music fadeout 2.0
    stop sound
    s 4w "..."
    "The sight I saw before me was heartbreaking." 
    "Why is this happening again?"
    "Why can't I do anything!?"
    show sayori zorder 1 at thide 
    hide sayori
    "Before I could say anything, she ran out of the room, her sobs echoing endlessly in my mind." 
    "In my shock, I just stood there, the whole world drowned out by that echo."
    '???' "You know what to do..."
    mc "Sayori, wait!"
    scene bg corridor with wipeleft_scene
    pause 0.1
    scene bg residential_day with wipeleft
    pause 0.1
    scene bg house with wipeleft
    pause 0.1
    play music t6
    mc "Ha... Haa..."
    mc "She's... really fast..."
    "I approach her door, just like last time."
    "But, wait..."
    "It's unlocked this time."
    scene black with wipeleft
    "I make my way to Sayori's room."
    "I can hear her crying..."
    scene bg sayori_bedroom with wipeleft
    show sayori 2u at t11 zorder 2
    "All I want to do is apologize to her, comfort her, let her know that she is loved."
    "But instead all I can do is smile at her."
    mc "Ahh, there you are Sayori."
    s 2v "[player]? Why are you here?"
    "Sayori, I'm so, so sorry. I didn't mean any of that, truly."
    mc "Oh, I just wanted to see how you were doing."
    mc "You really didn't seem to appreciate my criticism."
    "That's not what I want to say!"
    s 1k "...did you really mean what you said?"
    "No, of course not!"
    mc "Sayori, you told me to be honest, so I was."
    mc "Those are my honest thoughts."
    "...somebody just shoot me right now."
    s "I see..."
    s 2w "I'm sorry. I know how horrible of a friend I am, yet I still keep doing these things."
    s "I'm truly awful..."
    menu:
        "Sayori..."
        
        "Tell Sayori What She Needs To Hear":
            mc "I'm glad you realize how awful you are."
            mc "I'd say that admitting your faults is the first step to getting better, but we both know that'll never happen."
            s 3m "Huh?"
            mc "I know about your depression Sayori. I know how bad it is for you, and I know that you'll only get worse and worse."

    "Why? Why am I saying such awful things?"
    mc "It's okay though. There is a way to end the pain."
    s 3t "There is?"
    "I can feel a big smile growing on my face."
    "...I wish I could punch myself so hard right now."
    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    mc "You should just kill yourself."
    "What?!"
    mc "It'll be quick, and then you'll never feel any pain ever again."
    s 1k "..."
    s "Wouldn't you miss me?"
    "I'd mourn for you every day. Please, don't do this! Don't listen to me!"
    mc "Nah, not really. Like I said, you really just get in my way."
    mc "You being out of my life would be a real relief to be honest. I'm sure the others in the club feel the same."
    s "..."
    mc "Hey, Sayori, you trust that I know what's best for you right?"
    mc "I wouldn't be telling you all of this if I didn't think it was for the best."
    "Scream at me, hit me, kick me out of the house! Just stop listening to me, please..."
    s 2t "Okay, I trust you."
    "No! Sayori!"
    mc "Great! Then, let's get started, shall we?"
    hide sayori
    scene black with wipeleft_scene
    "No, no, no..."
    "Aaaahhhh!"
    "Make it stop, make it stop!"
    "Please, somebody stop me!"
    "...eventually, Sayori was all set up."
    play music td fadein 1.0
    s "Well, this is it..."
    mc "Yep!"
    s "...is there anything else you want to tell me before we do this?"
    "Please don't do this, please stop!"
    menu:
        '???' "Do what you were made to do."

        
        "Do It. Obey!":
            mc "Nope!"
            stop music fadeout 2.0
            mc "Well, Sayonara!"
            # Sound of a chair crashing/falling over.
            play sound "sfx/fall2.ogg"
            
    call ch2_main
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                