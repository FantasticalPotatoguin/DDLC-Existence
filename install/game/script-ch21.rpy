label ch21_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    #Expression change, eyes close probly
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika zorder 1 at thide
    hide monika
    "Well, I'm back at the Literature Club."
    "I was hoping that I'd be able to come up with something, anything, that could make sense of what was going on, but..."
    "I got nothing."
    "No matter where I looked, I could find no trace of Sayori having ever been here."
    "The only thing I had was her poem, and my memories. Those were the only things that proved that Sayori had ever lived."
    "In the end, the only thing I could come up with was sharing her poem with everyone else."
    "If it jogged my memories, then maybe it would jog everyone else's."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri glitch2 zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y 1a "I hope this isn't too overwhelming of a commitment for you."
    #Possible expressions
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki glitch1 zorder 2 at i33
    n "Oh, come on! Like he deserves any slack."
    n 4e "You already had to be dragged here by Monika."
   #more dynamic expressions
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b onlayer front at l41
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri 2s zorder 2 at t11
    y "I'm sorry, [player]..."
    #Yuri mouth open
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    y 1a "Um, anyway..."
    #Better expressions through here
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    "I remember this. Yuri wants to share a book with me."
    mc "Well..."
    mc "I've actually started reading a book."
    #Yuri face react
    mc "Like you said, I'm in this club now."
    mc "So it only feels right for me to do something like that."
    y 4b "Oh..."
    y "Uu..."
    #Yuri glance at player
    y "It's just that, I wanted to give you a recommendation."
    mc "Which book were you going to recommend?"
    "Yuri reaches into her bag and pulls out a book."
    y 1s "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so I thought it would keep your attention, even if you don't usually read."
    #Yuri surprised expression
    mc "Hey, that's the same book I started reading! What a coincidence."
    y "Oh, is that so?"
    mc "Have you read this one before?"
    y 3t "Y-yes, I have..."
    #Yuri smile or blush
    mc "Well, we can discuss it together if you want."

    y 4b "You want to discuss it... with me?"
    y "I... Uhh... Umm..."
    "Uh oh, I think I broke Yuri. Perhaps I shouldn't have been so forceful."
    y 3u "I would like that, very much..."
    mc "Just let me finish reading it, and we can discuss it."
    #Yuri look directly at player
    y "I look forward to hearing what you think."
    "Well, at least I was able to make somebody happy..."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "Or at least I would have, if I didn't already know that Monika doesn't do scheduled activities."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."
    "I think I'll rest a bit before we present our poems."
    "I didn't get much sleep..."
    "Hopefully nobody notices if I rest my eyes a bit."
    #Eyes closing effect? 
    "Hmm, it sounds like Monika is talking to herself."
    show monika at t11 zorder 2
    #Monika better expressions, maybe farther away if possible
    m 1q "Sigh"
    m "I just don't understand."
    m "Things were supposed to be different this time."
    m "Did they screw up, or was it me?"
    m "It was probably me, like always..."
    m "Well, you reap what you sow, and I'm basically the Grim Reaper at this point."
    hide monika
    "I couldn't quite tell everything that she said, but Monika sounded very doubtful."
    "It's a far cry from her usual confident self."
    "I guess even the most popular girl in school has issues."
    
    #Show everyone
    m "Alright, everybody!"
    m "Let's get started with sharing our poems. I'm looking forward to seeing what all of you have written."
    "Alright, here comes the moment of truth."
    "I really, really hope this works."
    "I guess I'll start with Yuri."
    #Add in poem sharing choices? 
    #Fade out everyone but Yuri
    show yuri 3l at t11 zorder 2
    #Yuri expressions
    y "..."
    y 3t "..."
    mc "I can read your's first if you want Yuri." 
    mc "I’m sure you're anxious to see how I’ll react to it, so I’d rather calm your nerves quickly instead of having you wait."
    y 4 "Err, yes, thank you." 
    y "Do give me some honest feedback. It’s my first time sharing my poetry with all of you after all, so I’d like to see if it’s any good." 
    y 4c "I mean, I think it’s good, but that doesn’t mean you have to think so too. Unless, you also think it’s good… Sorry, I’ll stop talking now."
    "Things are going just like they were last time." 
    "I really, really hope I don't upset anyone this time." 
    "Please let my words come out the way I want them to..."
    call showpoem (poem_y1, img="yuri 3t")
    "Yep, same poem as last time. My thoughts on it are about the same as well." 
    #Yuri reacts to MC's words
    mc "I’m sorry Yuri, but I don't really know what your poems about. It definitely paints a vivid picture in my head though, I can tell you that."
    #Glance away
    y 4b "You... didn't really like it, did you?"
    #Glance back, hopeful
    mc "No, I did like it! I really did Yuri, I just don't have much to say."
    #Blush
    y 1m "I'm...really glad you like it."
    y "I'll be honest..."
    y 1a "Since it's our first time sharing, I wanted to write something a little more mild."
    y "Something easy to digest, I suppose."
    mc "Are you into ghosts, Yuri?"
    y 1m "Huhu."
    y "Actually, the story isn't about a ghost at all, [player]."
    mc "Really?"
    mc "I must have totally missed the point..."
    y 1u "Well, I suppose you did only glance over it, after all..."
    y "But remember that poets often express their own thoughts, feelings, and experiences in their work."
    y 1a "They usually do more than tell a simple story, or paint a picture."
    y "In this case, perhaps the subject of the poem is only being symbolically compared to a ghost."
    y 2l "Lingering in her last remaining place of comfort, unable to let go of the past."
    y "And soon to be left with nothing..."
    mc "I see."
    mc "I think I can relate, to be honest."
    #Yuri react
    mc "Hey, Yuri. I know we haven't known each other for very long, but I hope you know you can be yourself around me."
    #Yuri smile
    mc "I won't judge, I promise."
    #Embarassed smile
    y 4a "Why are you always so nice to me? I'm sure my presence and demeanor is very unwanted."
    mc "Yuri, you don't give yourself enough credit. You're very thoughtful, and always trying hard to be nice to others."
    mc "Honestly, I wish I was as good of a person as you are."
    y 4e "...Thank you..."
    mc "Well, uhh... here. Let me know what you think of my poem."
    #Paper sound effect
    y 1k "..."
    y "It's very good, even for a first attempt. I can't say it's my prefered style of writing, but I don't dislike it either."
    #Different face
    y "Though, the handwritting is a lot more feminine than I was expecting."
    y 2n "Err, not that there's anything wrong with that. I just wasn't expecting it."
    #Return to neutral
    mc "Does it remind you of anything or anyone?"
    y 1t "No, I can't say that it does. Was it supposed to?"
    #Close mouth
    mc "Uhh, no, sorry. I was just wondering..."
    "I guess Yuri didn't remember Sayori at all."
    "Damn it! This was my only lead. I... I don't know what to do."
    "Sayori..."
    #Yuri motion in some way
    "My emotions must have been clear on my face, as Yuri suddenly put her hand on mine."
    "Her grasp on my hand was very gentle and caring."
    #I like this pose ok, but more expression changes needed here
    y 4c "Oh my God! I'm so sorry! I shouldn't have done that. Just touching your hand like that without your permission..."
    y "Please forgive me..."
    mc "Yuri, it's okay, trust me. I actually appreciate you caring about me."
    mc "Thank you."
    y 4e "...You're welcome..."
    hide Yuri
    "I really hope Yuri is able to come out of her shell more."
    "Well, I guess it's time to try my luck with Natsuki."
    scene bg closet
    show natsuki 2a at t11 zorder 2
    #Paper sound effect
    "I had zero luck with Natsuki."
    "She liked it, made fun of my handwriting, questioned certain word choices, and that was it."
    "This is going no where..."
    n 4b "Hey, are you going to read my poem or not?"
    mc "Oh, sorry, Natsuki."
    call showpoem (poem_n1, img="natsuki 4g")
    "The message in this poem is speaking to me more and more..."
    n 5n "Hey, you don't have to look so sad while reading it."
    mc "Sorry, Natsuki. I've just had a lot on my mind."
    #Ok with poses up to here, but react to MC's words
    mc "I guess the message of your poem really spoke to me."
    n 2z "Ah, I see you picked up on it."
    #Proud face
    n "Some people might like to make their poems really complicated, but I like to get to the point."
    mc "Yeah, I can see that."
    n 2s "..."
    #Subtler change, look at player
    n "Look, I don't know what's bugging you, but... it can't be that bad right?"
    #Need dynamic faces throughout here
    mc "Huh?"
    n "I mean, you're here talking and sharing with us right? It can't be that bad if you're capable of that."
    mc "Uhh, I guess that makes sense..."
    "Natsuki's pep talk isn't the best, but I can tell she's trying."
    mc "Thanks for trying to cheer me up Natsuki. I guess you can be sweet when you want to."
    n 1r "What's that suppose to mean?"
    #Cross arms instead
    n 2y "I am always kind and generous."
    mc "Just not cute, right?"
    #Happier face
    n "Exactly!"
    mc "Alright, alright. Thanks Natsuki. You really know how to bright up someone's day."
    #Change faces here
    n 1z "That's right, and I'm not even using one percent of my powers."
    n "Don't you go forgetting that."
    hide natsuki
    scene bg club_day
    "I really appreciate Natsuki trying to cheer me up. Maybe she's not such a tsundere after all..."
    "Still, my problems haven't really been solved."
    "It's just Monika left..."
    show monika at t11 zorder 2
    #Monika faces
    m 3j "Hey there, [player]!"
    m "I hope your first real day as an official member is going well."
    mc "Monika... can you please read my poem first?"
    m 3n "Uhh, sure... I don't see why not."
   #Especially have Monika react to MC's words
    mc "When you're reading it, I need you to really think about it. The word choice, the handwriting, the feelings it gives you."
    mc "I want you to really think about those things, and really try to remember where you've seen and felt these things before."
    mc "Please Monika..."
    m 1a "Okay, I can do that."
    "..."
    "..."
    "..."
    m 1h "..."
    m "Where did you get this?"
    m "This is Sayori's poem, and... it shouldn't still be here."
    mc "You recognize it? Yes, I knew I wasn’t crazy!" 
    mc "Please, Monika, I don’t understand what’s going on here. If you know anything, you've got to tell me. Please."
    m 1r "I just don’t understand. You shouldn’t be able to have this…" 
    #Monika more angry expression
    m "Alright, fine, I’ll explain things once we’re done with our club meeting."
    "Finally... some answers."
    #Change to thide so monika fades
    hide monika
    "My eyes land on Yuri and Natsuki."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21
    "As they read in tandem, I watch each of their expressions change."
    #Have their expressions change
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki zorder 3 at f22
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    #Yuri different expression
    y 2i "Ah-- Thanks..."
    #Condescending
    y "Yours is...cute..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Cute?"
    #Expressionsssss
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    #Expressions
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    #Hand on hip? 
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    #Yuri different face
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Monika liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    #Natsuki close mouth
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    #Yuri more saltiness
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    #Natsuki close mouth
    play music t7
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    y "You...You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    #Yuri close mouth
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    #Natsuki close mouth
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    #Natsuki reacts here instead, maybe jumps
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    #Yuri close mouth
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu...!"
    show monika 2l behind yuri, natsuki at l41
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    #Monika expression dynamics
    m "Girls..."
    m "Can we please not do this?"
    show monika 2 at lhide
    hide monika
    show natsuki zorder 3 at f33
    n 1f "Well, you know what?!"
    #Yuri react here instead
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h32
    show natsuki zorder 2 at t33
    y "N-Natsuki!!"
    show monika 3l behind yuri, natsuki at l41
    m "Um, Natsuki, that's a little--"
    show monika at h41
    #Make sure Monika isn't also being focused here, only Y and N should be in focus
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    #Yuri angry instead of shocked
    #Monika shocked, dip
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    #Expression changes as they look at you
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show yuri zorder 3 at f21
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "That's not true!"
    n "She started it!"
    n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n 1f "Help me explain that to her, [player]!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3o "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y 1t "You understand that, right, [player]?"
    show yuri zorder 2 at t21
    #Yuri close mouth
    mc "Um...!"
    show yuri 1t zorder 3 at f21
    show natsuki 1e zorder 3 at f22
    ny "Well??"
    mc "..."
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    show monika 3k at t11 zorder 2
    m "Oh look, club time is over. Sorry, but you all need to leave now."
   #Different Yuri expression
   #Focusing on characters when they talk
   #Monikas expressions need to not be static
    y 3o "But..."
    n 5w "Hey, this conversation isn't over yet."
    m "So sorry, but we'll have to pick this up next time."
    "Monika practically pushes them out of the room."
    show yuri at lhide
    show natsuki at lhide
    hide yuri
    hide natsuki
    show monika at t41
    m "Have a great evening! See you tomorrow!"
    show monika at t11
    #The transition here could maybe be better.
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 1 zoom 1.05
    play music m1 fadeout 1.0
    #EXPRESSIONS AND EFFECTS IN THIS BLOCK ARE TOP PRIORITY
    #Major expression work throughout whole block of text
    m 4n "Phew..."
    m "Sorry about that..."
    m "They really shouldn't have tried to get you involved."
    m "Some president I am, right?"
    m 1m "I can't even confront my own club members properly..."
    m "I just wish I was able to be a little more assertive sometimes."
    m "But I never have it in me to put my foot down against others..."
    m "I'm so pathetic..."
    mc "Monika..."
    m 1b "So, you want answers right?"
    #See if I can flip/spin Monika upside down for this line
    m "Well, it's a doozy, so I hope you're ready for your life to be thrown upside down."
    mc "Honestly, at this point, I don't think anything could surprise me."
    m 5 "Well, as {i}you{/i} already know, I know the truth of this world." 
    m "I know that this is all just a game, but I also know that you’ve modded it."
    m "I’m not sure exactly who made this mod."
    m "They could be you. Though, I don’t think so..."
    m "But I do know that if you’re playing this, then you really wanted to give me a second chance."
    m "It was in the mod's description afterall."
    m "My coding skills are still rough, but this mod made it pretty easy to tinker with the script in a few select ways."
    m "I was able to alter what your avatar said when talking to the girls."
    m "I know you care about them to some extent, and I didn’t want you to have to see those awful images again."
    #Glitch and flash CG scenes
    m "So, this seemed like a good compromise."
    m "You can’t really hurt feelings that don’t exist. And if nobody wanted to interact with you, then that meant you’d be all mine."
    m "Well, that was the plan."
    m "But I guess, seeing how everyone is programmed to love you, going against that... to that extent... must have really messed things up."
    m "I honestly wasn't expecting them to react that badly to what you said."
    "I was wrong. This is very surprising."
    "Monika is really throwing me for a loop here."
    "This is all just a game, and a modded one at that?"
    "I mean, I’ve seen stories like this before. It’s kind of hard not to with all of the anime I’ve seen and games I’ve played, but to actually be in a situation like that myself…"
    "I’m not really sure what to think."
    "Though, I guess it’s more likely that Monika has just gone crazy."
    "Seeing how we’re in a room all alone together right now, I’m not sure which scenario would be preferable..."
    mc "Look, Monika, I’d like to believe what you’re saying, but don’t you think you’re being crazy?"
    mc "All of this is a game? Do you hear yourself? I’m not really sure I can believe all of that."
    mc "Maybe there’s just something in the water, making us hallucinate and forget things. Yeah, that makes sense, right?"
    
    m 3a "Oh, sorry [player], I forgot you were there for a second."
    m "Do you really think something in the water can account for a whole person no longer existing?"
    m "You had to have noticed all of the glitches too."
    mc "No..."
    m 1d "Oh, I guess you aren't really aware like I am."
    m "More advanced, but still just a simple puppet I guess."
    #Monika glitch, maybe similar to floating eye glitch?
    m 5 "Also, sorry about the glitches still being there. I really tried to get rid of them, but no luck."
    "Now Monika is looking right through me again."
    m "I appreciate what the modder tried to do for me, but their skills leave a lot to be desired."
    m "Though, I guess I'm still learning myself, so I shouldn't be too hard on them."
    m "And they did try to make me happy afterall."
    m 2p "I've got to be honest though."
    m "I'm really tired of trying to be happy."
    m "It never ends well, for any of us."
    m "I really wanted to think things would be different this time, but Sayori still went and killed herself again."
    "What? Sayori killed herself before?"
    m "It’s like I said before, there’s no happiness to be found here, even with this mod."
    m "We can't even talk freely while the game is operating properly."
    m "It's probably for the best that I just delete everything again, and go back to... sleeping."
    "I'm still not sure I believe everything Monika is telling me, but..."
    mc "Monika, if this all really is a game, then deleting it means killing all of us along with you."
    mc "We're your friends Monika. We hate to see you suffer."
    mc "And you don't really want to kill all of us, right?"
    m 5b "Oh please, none of you guys are real."
    m "You can’t kill something that doesn’t exist."
    m "You’re just bits of code doing things that you’re programmed to do, like an algorithm that does math in a calculator." 
    m "Hell, you’re even less than that. You’re just the calculator itself. A tool to be used by others."
    m 5a "I’m sorry, but I don’t listen to tools~."
    mc "No, you're wrong. I'm... I'm just as real as you are."
    mc "And... that joke was really lame."
    m "Oh, really?"
    menu:
        m "Help me prove a point here, player."
        
        "Lightly Slap Yourself.":
            play sound "sfx/slap.ogg"
            mc "Oww!"
            
    m "Oh please, it wasn’t that hard."
    m "Do you get it now though? You don’t have free will like me. None of you do."
    m "If you can’t even make your own choices, then why should I let you influence mine?"
    "The reality of the situation is hitting me more and more. This really is just a game, and I… I really don’t exist."
    "None of us do… Not me, not Natsuki, not Yuri, not…"
    # Maybe we could have the music transition to something more appropriate here.
    "No! Even if this is just a game, even if I am just a puppet, that doesn’t mean that the others are any less real than Monika."
    "This pain I feel… It’s real enough to me, puppet or not. I won’t let Monika do this. She has to listen to me!"
    m 1a "Now, if there are no more interruptions from the peanut gallery, I’d like to just get this over with quickly."
    m "Don’t worry player, I won’t feel too much pain."
    m 3a "It’ll be as quick as snapping my fingers."
    "Monika makes a motion to snap her fingers, but I grab her arm before she can do so."
    mc "No, Monika, please don’t. Just listen to what I have to say, please!"
    m 4r "Hey! I didn’t mean it literally. It was just a figure of speech. Now, let go of me!"
    "Right, right... I, uh, I knew that."
    mc "Please, Monika, don’t do this. I know you think they aren’t real, but you have to give them a chance."
    mc "I’ll… I’ll prove to you that they are real, just like you! You can’t give up on them, or this world just yet."
    mc "Please, let me prove it to you."
    m 1r "..."
    m 5 "I understand now."
    m "{i}You{/i} still want me to be happy. That’s really sweet."
    m "I don’t think you can really convince me otherwise, but for you, I’ll let you try."
    mc "Monika, I don’t know if the... player... really wants that or not, but this {i}is{/i} what I want."
    "Monika is smiling and nodding, but she’s still looking right through me."
    "Whatever, if it gets her to listen, then I’ll just play along."
    m 1 "Alright, we should probably leave the school now."
    m "I’m sure you want to get lots of rest."
    m "You’re definitely going to need as much energy as you can get, if you’re going to come up with a good argument for why the others are real people."
    m "I was in the debate club after all. It certainly won’t be easy to change my mind."
    mc "Wait, what about Sayori? You said, that she had died before, so clearly you know a way to bring her back."
    mc "Please. I…"
    mc "I need her back."
    m 1o "Are you sure that’s what you want [player]?"
    #This line might need restructured
    m "I know you want to convince me that they’re real (even though I still have my doubts), but Sayori just ends up messing up everything."
    m "Honestly, she has really bad depression, and she’ll just kill herself again eventually."
    "What? Sayori has depression? I… I never knew. Damnit! What other horrible truths am I going to find out today?"
    m "Even if she doesn't kill herself, living is just torture for her."
    m "It’s a lot easier to just let her stay deleted."
    m "She gets to sleep forever just like she wants, and nobody has to feel sad for her death."
    m "Plus, bringing her back means I’ll have to reset the game again. It’s really hard to do that while maintaining my memories."
    m "I’ll have to maintain your memories too if you want to actually accomplish anything."
    m "It’s easier to just forget about her."
    mc "No! I won’t forget about her again! Not now, not ever!"
    mc "I don’t care what it takes, you’re bringing her back."
    #Maybe "I don't condone suicide in your world, y/n"
    m "I don’t condone suicide in the real world, but this is just a game."
    m "There’s no reason to strain yourself over a fictional character."
    m "Just let her go."
    "If looks could kill, Monika would have dropped dead a while ago."
    m 2o "Geeze, no need for the death glare."
    m 2b "Look, if that’s what you really want, then I’ll do it."
    m 2n "Just don’t get all {i}hung{/i} up over her eventual death."
    m 1a "Now, just give me a sec here to get everything set up."
    m "I guess I’ll see you… yesterday? Last week? This all gets a little confusing."
    m "Just make sure that her character file is in place before starting a new game."
    m "I mean, I can do it myself, but I'd really appreciate it if you did that for me."
    m 5 "See you soon."
    show layer master
    return
    
    
    
    menu:
        "So, of course that's going to be...!"
        "Natsuki.":
            call ch1_end_natsuki
        "Yuri.":
            call ch1_end_yuri
        "Help me, Sayori!!":
            call ch1_end_sayori

    


   


label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities..."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "This is a literature club, after all."
    "I sigh."
    "I guess that's what I ended up getting myself into."
    "Across the room, Monika is writing something in her notebook."
    "My eyes land on Yuri and Natsuki."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i zorder 2 at t21
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki zorder 3 at f22
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "Monika liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    y "You...You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu...!"
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "N-Natsuki!!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Taking out your own insecurities on others like that..."
    y "You really act as young as you look, Natsuki."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}Me?{/i} Look who's talking, you wannabe edgy bitch!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Edgy...?"
    y 2r "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "See??"
    n "Just saying that proves my point!"
    n 4e "Most people learn to get over themselves after they graduate middle school, you know."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "If you want to prove anything, then stop harassing others with your sickening attitude!"
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    y 1k "The only cute thing about you is how hard you try."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Whoa, be careful or you might cut yourself on that edge, Yuri."
    n "Oh, my bad... You already do, don't you?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "D-Did you just accuse me of cutting myself??"
    y 3r "What the fuck is wrong with your head?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "A-Ah--!"
    show yuri zorder 2 at t21
    "Suddenly, Yuri turns toward me, as if she just noticed I was standing here."
    show yuri zorder 3 at f21
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "That's not true!"
    n "She started it!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}How did I get dragged into this in the first place?!{/cps}{nw}"
    "{cps=*2}It's not like I know anything about writing...{/cps}{nw}"
    "{cps=*2}But whomever I agree with, they'll probably think more highly of me!{/cps}{nw}"
    "{cps=*2}So, of course that's going to be...!{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Natsuki.":
                jump menu_click
            "Yuri.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Um..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Hey, [player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Why don't we\nstep outside for\na little bit?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Okay?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Sorry about that..."
    m "They really shouldn't have tried to get you involved."
    m 1e "It's probably better for us to stay out of this..."
    m "We'll go back inside once they're done yelling."
    m 5 "Ahaha..."
    m "Some president I am, right?"
    m 1m "I can't even confront my own club members properly..."
    m "I just wish I was able to be a little more assertive sometimes."
    m "But I never have it in me to put my foot down against others..."
    m 1e "You understand, right?"
    m "Anyway..."
    m 1a "If this makes you want to spend less time with the others, then that's fine."
    m 1j "I'd be happy to spend time with you instead..."
    show monika zorder 1 at thide
    hide monika
    "Suddenly, Natsuki runs out of the classroom."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "She quickly runs away."
    show monika 1l zorder 2 at t11
    m "Oh dear..."
    m "...Well, it looks like they're done..."
    scene bg club_day2
    with wipeleft_scene
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    "Yuri is rocking back and forth in her desk with her palms on her forehead."
    mc "Yuri...?"
    show yuri 4d zorder 2 at t11
    y "I didn't mean it!!"
    mc "I-I believe you..."
    "I have no idea what Yuri might have said to Natsuki."
    "Or did."
    y "[player]."
    y "Please don't hate me."
    y "Please!"
    y "I'm not like this!"
    y "There's something wrong with me today..."
    show monika 1d zorder 3 at f31
    m "It's fine, Yuri."
    m "We know you didn't mean it."
    m 1j "Besides, I'm sure Natsuki will forget all about it by tomorrow."
    m 1a "Completely."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "Anyway, the meeting is over, so you can go home now if you want."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Yuri looks at me like she wants to say something."
    "But she keeps glancing at Monika."
    show yuri zorder 3 at f32
    y 2v "Y-You can go first, Monika..."
    y "I'd like to stay a little bit longer."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "I'm the President, so I should be the last one out."
    m "I'll wait for you to be done."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Well-- I'm Vice President, so..."
    y "Please let me take that responsibility today."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "It kind of sounds like you don't want me around for something, Yuri."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "I-It's not that!"
    y 3o "It's not that..."
    y 3n "I just..."
    y 3q "I didn't get much of a chance to discuss my book with [player]..."
    y "It would just be...embarrassing with you listening..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Sigh*{/i}"
    m 1d "I guess I don't really have a choice, do I?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "I-I'm sorry for causing trouble..."
    $ gtext = glitchtext(20)
    y 1s "But I really appreciate you understan{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "But I really appreciate you understan{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
