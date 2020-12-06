label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."
    "No, wait, that doesn't sound right."
    "Wasn't I waiting on something? Something, annoying..."
    "Ugh, my head's starting to hurt."
    "It was probably just some dream I'm forgetting about. Nothing to worry over."
    "As I'm walking towards school, I take a look at a house that's near mine."
    mc "Still for sale, huh? It sure would be nice if somebody moved in."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Wait, why am I thinking about clubs?"
    "I have no desire to join one."
    "But, didn't I promise I'd think about joining one?"
    "I don't know who I'd make that promise to though."
    "It certainly wasn't to myself."

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "...Monika?"
    $ m_name = "Monika"
    m 1b "I was hoping to find you here!"
    m 5 "It's good to see you again."
    mc "Ah..."
    mc "It's good to see you too, Monika."
    "Am I hearing her right?"
    "One of the most popular girls in school is happy to see me?"
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Did I really leave that much of an impression on her?"

    #Change Monika poses here? Is this section original game code?
    mc "What did you come in here for, anyway?"
    m 1i "Let me just cut to the chase." 
    m 3b "I've been looking for new members for my club, and I think you'd fit right in."
    show monika 3a zorder 2 at t11
    mc "...You're in the debate club, right?"
    m 1l "Ahaha, about that..."
    m 1n "I actually quit the debate club."
    show monika 1m zorder 2 at t11
    mc "Really? You quit?"
    show monika 1n zorder 2 at t11
    m "Yeah..."
    m 2e "To be honest, I can't stand all of the politics around the major clubs."
    m 1b "That's why I decided to make my own club."
    m 5a "A literature club!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "A literature club!{fast}"
    window auto
    mc "Literature...?"
    show monika 5b
    "That sounds kind of...dull?"
    mc "How many members do you have so far?"
    
    m 2n "Um..."
    m 2m "Ahaha..."
    m 2l "It's kind of embarrassing, but there are only three of us so far."
    m 1j "That's why I'd really appreciate it if you decided to join us."
    m 4b "We need at least four members to become an official club."
    m 2m"I know being part of a literature club sounds boring."
    m 2k "But it's really not boring at all, you know!"
    m 2a"Literature can be anything. Reading, writing, poetry..."
    m 3e "I mean, one of my members even keeps her manga collection in the clubroom..."
    mc "Wait...really?"
    m 2k "Yeah, it's funny, right?"
    m 2e "She always insists that manga is literature, too."
    "...Did Monika say \"she\"?"
    "Hmm..."
    m 1e "Hey, [player]..."
    m 1d "I know we don't really know each other all that well, but I just know that my club is the club for you."
    m 2a "I would appreciate it so, so much if you would join."
    m 2e "Please?"
    mc "Um..."
    "Well, I guess I have no reason to refuse..."
    show monika 2j zorder 2 at t11
    "Besides, how could I ever refuse someone like Monika?"
    mc "Sure, I guess I could check it out."
    m 1k "Aah, awesome!"
    m 1b "You're really sweet, [player], you know that?"
    show monika 1a zorder 2 at t11
    mc "I-It's nothing, really..."
    mc "Like you said, it just feels right."
    mc "I don't know if you believe in fate, but it kinda feels like that."
    m "{i}(Yeah, I guess free will would be a foreign concept for you.){/i}"
    mc "Hmm?"
    m 1l "Oh, nothing! I'm just musing to myself."
    m 1b "Shall we go, then?"
    show monika 1a zorder 2 at t11
    mc "Yes, let's."
    show monika 1j zorder 2 at thide
    hide monika

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul for a cupcake, err, to Monika and her irresistible smile."
    "Not sure why I was starting to think about cupcakes."
    "I timidly follow Monika across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Monika, full of energy, swings open the classroom door."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
        show monika g1 at f31
    else:
        show monika 3b at l31
        show monika 3b at f31

    #shocker, more poses to make fancy so that stuff doesn't mismatch
    m "I'm back~!"
    m 3k "And I brought a guest with me!"
    show monika 3k zorder 2 at t31
    show yuri 2e zorder 2 at f33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "Eh?"
    y 2t "Oh, this must be the new member you were talking about."
    show yuri 2s zorder 2 at t33
    show natsuki 4e zorder 2 at f32
    n "Seriously? You brought a boy?"
    n 4q "Way to kill the atmosphere."
    show natsuki 4s zorder 2 at t32
    show monika 3n zorder 2 at f31
    m "Don't be mean, Natsuki..."
    m 3b "...But anyway, welcome to the club, [player]!"
    show monika 3e zorder 2 at t31
    mc "..."
    "All words escape me in this situation."
    "This club..."
    show monika 1j zorder 2 at h31
    "{i}...is full of incredibly cute girls!!{/i}"

    show natsuki 5c zorder 3 at f32
    n "So, let me guess..."
    show yuri 2e zorder 2 at t33
    show monika 1d zorder 2 at t31
    n 5k "You're Monika's boyfriend, right?"
    show natsuki 5a zorder 2 at t32
    mc "Wha--"
    show monika 2h zorder 2 at t31
    mc "No, I'm not!"
    show monika 2q zorder 2 at t31
    show yuri 2q zorder 2 at f33
    y  "Natsuki..."
    show yuri 2u zorder 2 at t33
    $ n_name = 'Natsuki'
    "The girl with the sour attitude, whose name is apparently Natsuki, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."

    show yuri zorder 2 at t33
    show monika zorder 2 at f31
    m 2l "A-Anyway, this is Natsuki, energetic as usual..."
    m 2b "And this is Yuri, the Vice President!"
    $ y_name = 'Yuri'
    show monika 2a zorder 2 at t31
    show yuri zorder 2 at f33
    y 4 "I-It's nice to meet you..."
    "Yuri, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Natsuki."
    "It's kind of weird, but I was expecting the Vice President to be someone else."
    show yuri zorder 2 at t33
    mc "Yeah... It's nice to meet both of you."
    show monika zorder 2 at f31
    m 1a "So, I ran into [player] in a classroom, and he decided to come check out the club."
    m "Isn't that great?"
    show monika zorder 2 at t31
    show natsuki zorder 2 at f32
    n 4e "Wait! Monika!"
    n "If you just ran into them, then why did you tell me to prepare cupcakes?"
    n 4q "It sounds like you knew he was going to join..."
    n 4y "Did you make him an offer he couldn't refuse?"
    show natsuki zorder 2 at t32
    # Change pose to make Monika more shocked, less embarassed
    show monika zorder 2 at f31
    m 1e "Hey, what's that suppose to mean?"
    # Change Natsuki's pose here
    n 4y "Don't worry Monika, I see how it is. You're secret is safe with me."
    m 2n "It's really not like that..."
    show monika zorder 2 at t31
    #Yuri comes into focus a line too early
    #Don't like that the other girl's faces stay exactly the same
    #while Yuri is talking, change to resting pose
    show yuri zorder 2 at f33
    "A slightly uncomfortable silence is starting to fill the room."
    y 1a "In any case, I should at least make some tea, right?"
    show yuri zorder 2 at t33
    show monika zorder 2 at f31
    m 1b "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    #Change to thide poses so they fade instead of disappear
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "Natsuki and Yuri walk over to the corner of the room, where Natsuki grabs a wrapped tray and Yuri opens the closet."
    "Still feeling awkward, I take a seat next to Monika."
    #More expressive Monika
    show monika 1a zorder 2 at t11
    m "So, I know you didn't really plan on coming here..."
    m "But we'll make sure you feel right at home, okay?"
    m 1j "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    mc "I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m 3b "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Though, now that we have enough members to be an official club, I'm not too worried about gaining new members."
    m 2k "It was hard enough to find you guys as it is..."
    #ask about this line, if shifting to the right is intentional
    #90% sure this shift is an accident
    show monika zorder 2 at t22
    "Monika must have worked really hard just to find these three, err, two."
    "Come on me, I'm better at counting than that."
    "Natsuki proudly marches back to the table, tray in hand."
    show natsuki 2z zorder 2 at t32
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show monika 2d zorder 2 at t33
    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show monika zorder 2 at f33
    m 2b "Your cupcakes are always a delight Natsuki!"
    show monika zorder 2 at t33
    show natsuki zorder 2 at f32
    n 2m "Huh? This is the first time I've made cupcakes for you guys."
    #some sort of minor glitch here would be cool
    m 3k "Oh, well, I'm sure they're still a delight either way."
    #Natsuki needs an expression change here
    n " Whatever, just hurry and take one!"
    "Monika takes one, and I follow."
    show natsuki zorder 2 at t32
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show monika zorder 1 at thide
    hide monika
    #Change Natsuki's face here
    show natsuki 1c zorder 2 at t32
    "Natsuki is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    #Have Natsuki's face react to this line
    mc "This is really good."
    mc "Thank you, Natsuki."
    n 5h "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show natsuki at s32
    n 5s "...Made them for you or anything."
    #minor reaction from Natsuki here
    mc "Eh? I thought you technically did."
    show natsuki zorder 2 at t32
    n 12c "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    #Natsuki arm cross or something
    mc "Alright, alright..."
    show natsuki zorder 1 at thide
    hide natsuki
    "I give up on Natsuki's weird logic and dismiss the conversation."
    #Show Yuri here instead, dip sprite when placing teacups
    "Yuri returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show yuri 1a zorder 2 at t21
    mc "You keep a whole tea set in this classroom?"
    #Yuri expressions
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show monika 4a zorder 2 at f22
    #Possible split into two lines for expression purposes
    m "Ehehe, don't let yourself get intimidated, Yuri's just trying to impress you."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "Eh?! T-That's not..."
    #Have Yuri look away directly with this line
    "Insulted, Yuri looks away."
    #Have Yuri peek back at player
    y 4b "I meant that, you know..."
    show yuri zorder 2 at t21
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    show yuri zorder 2 at f21
    y 2u "I'm glad..."
    show yuri zorder 2 at t21
    "Yuri faintly smiles to herself in relief."
    show monika zorder 1 at thide
    hide monika
    #Change Yuri's t number
    show yuri 1a zorder 2 at t32
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    #Yuri eyebrow raise
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show natsuki 1c zorder 2 at t41
    #Natuski jump
    "Natsuki's head suddenly perks up."
    #Natsuki mouth close
    "It looks like she wants to say something, but she keeps quiet."
    "I guess she's the manga reader who Monika was telling me about."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Yuri's sad smile."
    mc "Anyway, what about you, Yuri?"
    y 1l "Well, let's see..."
    "Yuri traces the rim of her teacup with her finger."
    #Don't like poses through here but might leave cuz they're original I think
    y 1a "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y 1f "And telling a good story in such a foreign world is equally impressive."
    "I had a feeling she'd say something like that."
    "Yuri goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y 2m "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y 2a "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Yuri might as well be having a conversation with a rock."
    show monika 1j zorder 2 at f33
    m "Ahaha. I'd expect that from you, Yuri."
    m 1a "It suits your personality."
    show monika zorder 2 at t33
    show yuri zorder 2 at f32
    #Change pose I think
    y 1a "Oh, is that so?"
    y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 2 at f31
    n "Ugh, I hate horror..."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at f32
    y 1f "Oh? Why's that?"
    #Yuri's face does literally nothing through this segment, have her react to things
    show yuri zorder 2 at t32
    show natsuki zorder 2 at f31
    n 5c "Well, I just..."
    "Natsuki's eyes dart over to me for a split second."
    n 5q "Never mind."
    show natsuki zorder 2 at t31
    show monika zorder 2 at f33
    m 1a "That's right, you usually like to write about cute things, don't you, Natsuki?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 2 at f31
    n "W-What?"
    n "What gives you that idea?"
    show natsuki zorder 2 at t31
    show monika zorder 2 at f33
    m 3b "Your poems always come out being super cute."
    m "Plus, you're as cute as a button too."
    show monika zorder 2 at t33
    show natsuki 1p zorder 2 at f31
    n "I am not cute!!"
    #Shift in reaction
    n "And don't be looking at my poems! Those are for my eyes only."
    #Natsuki return to neutral
    show natsuki zorder 2 at t31

    #Don't like Monika's pose here
    show monika zorder 2 at f33
    m 1j "Fine, fine~"
    show monika 1a zorder 2 at t33
    mc "Natsuki, you write your own poems?"
    show natsuki zorder 2 at f31
    n 1c "Eh? Well, I guess sometimes."
    n "Why do you care?"
    show natsuki zorder 2 at t31
    #Natsuki surprise
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    show natsuki zorder 2 at f31
    n 5q "N-No!"
    #Change so averting eyes is in sync
    "Natsuki averts her eyes."
    #Peek back at player
    n "You wouldn't...like them..."
    show natsuki zorder 2 at t31
    #Natsuki return to neutral
    mc "Ah...not a very confident writer yet?"
    show yuri zorder 2 at f32
    y 2f "I understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y 2k "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show yuri zorder 2 at t32
    show monika 2a zorder 2 at f33
    #Monika better expressions
    m "I'm sure you have lots of writing experience Yuri."
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    show yuri at s32
    y 3o "..."
    mc "I guess it's the same for Yuri..."
    "We all sit in silence for a moment."
    show monika zorder 2 at f33
    #Don't like this pose, do the finger in the air one
    m 5a "Hey, I just got an idea!"
    m "How about this?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 2 at f32
    ny "...?"
    "Natsuki and Yuri look quizzically at Monika."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 2 at f33
    m 2b "Let's all go home and write a poem of our own!"
    #Background poses for other girls
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 2 at f31
    n 5q "U-Um..."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 2 at f32
    y "..."
    show yuri zorder 2 at t32
    show monika 2m zorder 2 at f33
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show monika zorder 2 at t33
    show yuri zorder 2 at f32
    y 2l "Well..."
    y "...I think you're right, Monika."
    y 2f "We should probably start finding activities for all of us to participate in together."
    y 2h "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    #These poses could be better
    y 2a "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    #This one especially needs changed
    #Have Natsuki and Monika look at player here
    y "Do you agree as well, [player]?"
    #Drop Yuri out of focus
    mc "Umm, sure, I guess."
    mc "I have no experience writing poems though."
    #Monika focus
    m 3b "That's completely fine."
    m "This club is for those who are interested in literature, whether you're a pro or not."
    m "We can all grow our skills together."
    m 5 "Besides, we won't make fun of you."
    #Expression change at "much", possible pose change to accomodate
    m "Much~."
    #Drop Monika out of focuse
    #Yuri focus
    y 3w "Monika..."
    #Defocus Yuri, focus Monika
    #Monika better expressions
    m 1a "I'm joking, I'm joking."
    m "So, what do you say [player]?"
    #All react in bg
    mc "Yeah, I can take a shot at writing poetry."
    mc "I did say I'd join after all, so it would be pretty lame of me to drop out at the first sign of trouble."
    m 1e "Thank you so much for this. You're really amazing."
    #See about glitching the word "everything", idk that I want Glitch Text but something
    m "I'll do everything I can to give you a great time, okay?"
    show monika zorder 2 at t33
    mc "Ah...thanks, I guess."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    #More dynamic poses through here
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    #Monika's face should change with this line
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika zorder 1 at thide
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Yuri cleans up the tea set."
    "It's kind of weird though. There's something that's been nagging at me all day."
    "I feel like it's right on the tip of my tongue, but I'm not sure what."
    
    show monika 4k at i21 zorder 2
    m "Say, Yuri..."
    stop music fadeout 5.0
    #Either a fade to silence or a slightly melancholy song.
    show sayori 1s at t11 zorder 2
    mc "...!{nw}"
    show screen invert(0.15,0.01) # Added in a invert just before Sayori is hidden
    pause 0.05
    hide sayori
    mc "Did you just say \"Sayori\"?"
    #maybe different face for Monika here
    m 1p "..."
    "I’m not sure why, but that name felt very important to me. Who was she?"
    #Yuri expressions
    show yuri 1a at t22 zorder 2
    y "Oh, no, Monika was just trying to get my attention." 
    y "I’m sure she wanted to discuss our plans for the upcoming festival." 
    y "As Vice President, it’s important that I do what I can to help Monika keep the club interesting."
    #Monika slightly different expressions, embarassed/angry
    m 4k "Yes, that’s right, I just wanted to discuss with Yuri on what we can do to make the festival fun for everyone."
    m "Besides, there isn’t anyone named Sayori that’s part of this club."
    m "Trust me, you already met all of us. Why, I don’t even know anyone named Sayori. Ahaha…"
    "Something seemed off with what Monika was saying, but my thoughts were too jumbled to really pick up on anything specific."
    "Sayori… Why did I recognize that name? And… Why did thinking about it bring me such a sharp pain in my chest?"
    mc "I guess I'll be on my way, then..."
    #Now we fade back to the previous tune.
    play music t3 fadein 2.0
    #Remove this fade
    show monika 5a zorder 2 at t11
    m "Okay!"
    m "I'll see you tomorrow, then."
    m "I can't wait!"
    #Expressions change as girls fade together

    scene bg residential_day
    with wipeleft_scene

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    
    #Make these sprites black and white or sepia, since reminiscing? 
    show natsuki 4a zorder 2 at t31
    "Natsuki,"
    show yuri 1a zorder 2 at t32
    "Yuri,"
    show monika 1a zorder 2 at t33
    "Monika,"
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    show sayori 1a zorder 2 at t11
    "and... her."
    
    scene bg kitchen with wipeleft
    # We don't really need a different song here, but if you think something else would be good here, I'll trust your judgement.
    "Finally, home again. I can’t wait to get out of these clothes." 
    "It feels like I’ve been wearing them for days. Nothing a warm shower can’t fix."
    #Split this line, add rustling sound effect
    mc "Hmm? What’s in my pocket? Paper? No, wait, this is a poem."
    "Who wrote this, and why do I have this?"
    call showpoem (poem_s1, img="sayori 1")
    mc "This is..."
    
    $ s_name = "Sayori"
    
    scene bg club_day
    with wipeleft
    #I'm not sure if the music coming suddenly is better or not. Your call.
    play music t6 fadein 2.0
    #Definitely going with black and white/sepia for these sprites
    #Black and white background as well, with vignettes
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a \"new member--\""
    scene bg residential_day with wipeleft
    show sayori 1a zorder 2 at t11
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    #Add better expression for Sayori here
    s "I guess you don't have it in you to be mean even if you want to~"
    scene bg house with wipeleft
    show sayori 4p at t11 zorder 2
    play music t9
    #Don't like Sayori's expressions here
    s "Highschool is kind of scary, huh?"
    s "All this new stuff to learn... I think my brain's going to burst!"
    mc "Come on Sayori, just because you're a bit of an airhead doesn't mean you can't get used to all of this new stuff."
    s 1j "Hey, that's mean!"
    s 1o "I think..."
    mc "Well, I'll see you tomorrow then."
    s 1k "Hey, [player]..."
    mc "Hmm?"
    #Sayori looks into player's eyes
    s "Do you think, we'll always be like this? Close friends, who walk and talk on their way to school and from?"
    mc "Well, I don't see why not."
    mc "We've been doing it this long."
    #Sayori hopeful
    s "Really?"
    mc "Well, I certainly like to think we'll be there for each other, at least when we really need help."
    s 1 "So you won't forget me?"
    "Yeesh, I don't know why Sayori is being so sentimental all of a sudden."
    mc "Yes, Sayori, I won't forget about you."
    s 4s "It makes me really happy to hear you say that."
    scene black with dissolve_scene_full
    hide sayori
    mc "Sayori..."
    mc "You deserved so much better."
    mc "I wasn't there for you. I forgot about you. I treated our friendship like it was nothing."
    mc "And still, you worried about me."
    mc "I'm sorry. I'm so, so sorry."
    mc "Nothing in my life was more important than yours."
    scene bg kitchen with wipeleft
    #Split this line
    "I hunched over my counter, head in my arms, for a good while. Strangely, it felt good to cry, like a tremendous pressure inside of me was finally coming loose."
    "Still, all of my regrets lingered."
    scene bg bedroom with wipeleft
    "I barely had the energy to shower and change my clothes."
    "Honestly, I don't know if I'll be able to attend school tomorrow, let alone the Literatrue Club."
    stop music fadeout 2.0
    #Split this line
    mc "Wait, didn't I just join the club today? That can't be right. I've already shared poems with everyone. No, wait, we're suppose to do that tomorrow..."
    "In my grief, I failed to realize something very important."
    "This week had restarted itself."
    "But this time, it was like Sayori was never there."
    "Sayori wasn't part of the club. Yuri was Vice President, not her. Nobody even knew Sayori."
    "For the second time this evening, I felt a maelstrom of emotions."
    "This time though, it wasn't sadness, but utter confusion."
    mc "What... is going on?"
    mc "It's like Sayori never existed at all, but I know that can't be right. I remember her now, and I have her poem."
    mc "I'm just... so confused. I just don't know anymore."
    "With all of this confusion, on top of my tiredness, I just couldn't keep my eyes open anymore."
    "I quickly fell asleep, hoping that I could figure something out tomorrow."
    

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
