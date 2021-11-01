# SCENE 49: Make sure Chloe is distracted with concert tickets for $100
# Locations: Sidwalk to Chick's house, Lindsey's room
# Characters: MC (Outfit: 1), LINDSEY (Outfit: x)
# Time: 


label v14s49:
    scene v14s49_1 # TPP. Show MC walking down the sidewalk towards the Chick's house, slight smile, mouth closed.
    with dissolve

    play sound "sounds/vibrate.mp3"

    u "(What do we have here?)"

    if v14_money_theft_concert_distraction: #Placeholder for concert distraction
        scene v14s49_2 # TPP. MC stopped walking looking at his phone, slight smile, mouth closed.
        with dissolve

        $ Lindsey.messenger.newMessage(_("Chloe just left the house with some other blonde girl. On their way to the concert!"), queue =False)
        $ Lindsey.messenger.addReply(_("It worked! How did you send the tickets without making her suspicious? Also, blonde girl?"))
        $ Lindsey.messenger.newMessage(_("I just sent the e-tickets anonymously. She has plenty of admirers these days. Probably just assumed it was a gift from one of them. Easy, huh?"))
        $ Lindsey.messenger.newMessage(_("Oh, she said they used to know each other when they were kids. That's all I know."))
        $ Lindsey.messenger.addReply(_("Very smooth, Linds. Money well spent."))
        $ Lindsey.messenger.newMessage(_("You've got to spend money to make money :P"))
        $ Lindsey.messenger.addReply(_("Or in this case, steal it."))
        $ Lindsey.messenger.newMessage(_("Haha, exactly!"))
        $ Lindsey.messenger.addReply(_("I'm on my way."))

        label s49Lindsey_PhoneContinue:
            if Lindsey.messenger.replies:
                call screen phone
            if Lindsey.messenger.replies:
                "(I should reply to Lindsey.)"
                jump s49Lindsey_PhoneContinue

    elif v14_money_theft_date_ditch: #Placeholder for date ditch distraction

        scene v14s49_2a # TPP. MC holding the phone to his ear, slight smile, mouth open.
        with dissolve

        u "Hey, Lindsey."

        scene v14s49_3 # TPP. Lindsey standing in her room with her phone to her ear, slight smile, mouth open.
        with dissolve

        li "Hey, now is the perfect time. Text Chloe and tell her to meet you at Classico Cuisine."

        if chloegf:
            scene v14s49_3a # TPP. Same as v14s49_3, Lindsey slight smile, mouth closed.
            with dissolve

            u "Oh, right. Yeah."

        scene v14s49_3
        with dissolve

        li "I'll stay on the phone while you do it so we can make sure she actually takes the bait. *Chuckles*"

        scene v14s49_3a
        with dissolve

        u "Okay, I'm texting her now."

        scene v14s49_2
        with dissolve

        if chloegf:
            $ Chloe.messenger.addReply(_("Hey… Think I'm in the mood for a little Italian cuisine and a beautiful woman across from me…"), queue =False)
            $ Chloe.messenger.newMessage(_("Haha, hi there Mr Sweet Talk…"))
            $ Chloe.messenger.newMessage(_("I could definitely eat, and… I suppose I’m down to see you ;)"))
            $ Chloe.messenger.addReply(_("Well then, I suppose I’ll see you soon :)"))
        else:
            $ Chloe.messenger.addReply(_("Hey… Think we can meet at that new Italian place, Classico Cuisine? I'm hungry and need some company."), queue =False)
            $ Chloe.messenger.newMessage(_("What am I, just a lunch buddy?"))
            $ Chloe.messenger.addReply(_("Sorry, these are hungry person texts, haha."))
            $ Chloe.messenger.newMessage(_("Haha, okay. Let's go now?"))
            $ Chloe.messenger.addReply(_("Yeah, sounds great"))

        label s49Chloe_PhoneContinue:
                if Chloe.messenger.replies:
                    call screen phone
                if Chloe.messenger.replies:
                    "(I should reply to Chloe.)"
                    jump s49Chloe_PhoneContinue

        scene v14s49_3a
        with dissolve

        u "Okay, seems to me like she took the bait."

        scene v14s49_3
        with dissolve

        li "Okay, hang on."

        li "..."

        li "Oh! I can hear her heading to the door now. I'm just checking out the window."

        li "She's getting into an Uber! Nice!"

        scene v14s49_3a
        with dissolve

        u "Success!"

        scene v14s49_3
        with dissolve

        li "Hurry here. Don't be long."

        scene v14s49_3a
        with dissolve

        u "Okay, boss lady. *Chuckles*"

        play sound "sounds/rejectcall.mp3"
     
    scene v14s49_2a # TPP. Same as v14s49_2, MC putting his phone away.
    with dissolve

    pause .25

    scene v14s49_4 # TPP. Show Mc further up the sidewalk walking towards the chick house.
    with dissolve

    u "(Time to commit the perfect crime.)"

    jump v14s50