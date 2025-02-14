# SCENE 32: At The Gym
# Locations: Outside the gym, inside the gym
# Characters: MC (Outfit 3when outside gym,Outfit 4 when inside gym ), Evelyn (Outfit 4)
# Time: Saturday Morning

init python:
    def v9s32_reply1():
        riley.messenger.newMessage(_("So you're coming?"))
        riley.messenger.addReply(_("I hope so ;)"))
        riley.messenger.newMessage(_("See you in a few!"))
        setattr(store, "v9_sex_with_riley", True)

    def v9s32_reply2():
        riley.messenger.newMessage(_("But? :o"))
        riley.messenger.addReply(_("But I have to stay focused on the Brawl. There's a lot riding on my fight."))
        riley.messenger.newMessage(_("Seriously?"))
        riley.messenger.addReply(_("I'm so sorry. You know I would any other day. Really."))
        riley.messenger.newMessage(_("Ok well, your loss."))

label v9_sat_gym:
    scene v9atg1 # TPP. Show MC outside the Gym, neutral face, mouth closed
    with fade
    u "(I should probably freshen up my skills.)"

    play music "music/v9/Track Scene 8_3.mp3" fadein 2

    menu:
        "Hit the gym":
            jump v9_sat_hit_gym
        "Skip the gym":
            jump v9_sat_skip_gym

label v9_sat_hit_gym:
    scene v9atg2 # FPP. Show Evelyn sat on a weight bench inside the gym (Camera from across room)
    with fade

    pause 1

    if evelyn.relationship >= Relationship.LIKES:
        scene v9atg3 # FPP. Show Evelyn sat on a weight bench inside the gym (now infront of MC), mouth closed
        with dissolve
        u "Hey, you seem to handle that bench pretty easy."

        scene v9atg3a # FPP. same camera as v9atg3, Show Evelyn sat on a weight bench inside the gym (now infront of MC), mouth open
        with dissolve
        ev "Yeah, I'm trying to focus on reps rather than increasing my weight endurance. The more times you do something the better, practice makes perfect. I'm sure you at least picked up on that in school."

        scene v9atg3
        with dissolve
        u "Ha, I did. So I guess that means I should be taking you out again soon."

        scene v9atg3a
        with dissolve
        ev "Is that so? I'm a very busy woman with a lot of responsibilities, I barely have enough time to workout and here you are interrupting that."

        menu:
            "Convince her":
                $ reputation.add_point(Reputations.BOYFRIEND)
                jump v9_sat_hit_gym_convince
            "Forget it":
                jump v9_sat_hit_gym_forget

        label v9_sat_hit_gym_convince:

            scene v9atg3
            with dissolve
            u "A wise woman once told me \"practice makes perfect\", I was just trying to follow her example."

            scene v9atg3c # FPP. same camera as v9atg3,Show Evelyn sat on a weight bench inside the gym (now infront of MC), mouth open, smiling
            with dissolve
            ev "Hmmm, this woman you speak of does sound pretty smart. What did you have in mind?"

            scene v9atg3b # FPP. same camera as v9atg3,Show Evelyn sat on a weight bench inside the gym (now infront of MC), closed, smiling
            with dissolve
            u "There's a cafe I just left and it was honestly amazing, wouldn't mind a nice breakfast would you?"

            scene v9atg3c
            with dissolve
            ev "That sounds nice."

            scene v9atg3b
            with dissolve

            $ grant_achievement("second_date")
            u "Great, I'll text you."

            scene v9atg4 # TPP. Show MC walking away from Evelyn, evelyn still on weight bench, MC walking towards punching bag, both smiling mouth closed
            with dissolve

            pause 1

            scene v9atg5 # TPP. Show MC Punching punching bag, neutral face, like this: https://www.featurepics.com/StockImage/20171103/man-and-punch-bag-stock-image-4549185.webp
            with dissolve

            pause 0.5

            scene v9atg5a # TPP. Same camera as v9atg5, show MC in boxing stance infront of punching bag, neutral face, like this: https://biomechanicsofboxing.weebly.com/uploads/2/5/2/3/25234795/8322860_orig.webp
            with dissolve

            scene v9atg5
            with dissolve

            pause 0.5 

            scene v9atg5a
            with dissolve
            u "(Okay, I think that's enough for today.)"

            scene v9atg6 # FPP. Show gym door as MC exits
            with dissolve
            
            jump v9_room_sat_aft

        label v9_sat_hit_gym_forget:
            scene v9atg3
            with dissolve
            u "Yeah, you're right. I'm pretty busy too. Talk to you later."

            scene v9atg3c
            with dissolve
            ev "Okay ummm, bye."

            jump v9_sat_hit_gym_train
    else:
        jump v9_sat_hit_gym_train
        
label v9_sat_hit_gym_train:
    scene v9atg5a
    with dissolve

    scene v9atg5
    with dissolve

    pause 0.5 

    scene v9atg5a
    with dissolve

    scene v9atg7 # FPP. Show punching bag, close to camera.
    with dissolve
    u "(Okay, I think that's enough for today.)"

    scene v9atg6
    with dissolve

    jump v9_room_sat_aft

label v9_sat_skip_gym:
    u "(Best that I don't push it.)"

    if riley.relationship >= Relationship.FWB:
        scene v9atg1a # TPP. Same camera as v9atg1, Show MC checking his phone.
        with dissolve

        play sound "sounds/vibrate.mp3"

        u "(Oh, who's that?)"

        $ riley.messenger.newMessage(_("Hey, what's up? Wanna come over?"), force_send=True)
        $ riley.messenger.addReply(_("I really shouldn't. Big day tomorrow. Stressed out"))
        $ riley.messenger.newMessage(_("Duh, that's why I'm asking ;)"))
        $ riley.messenger.addReply(_("Well you shoulda led with that!"), v9s32_reply1)
        $ riley.messenger.addReply(_("Man, I'd really love to but..."), v9s32_reply2)
        
        label s32_PhoneContinue:
            if riley.messenger.replies:
                call screen phone
            if riley.messenger.replies:
                u "(I should reply to Riley.)"
                jump s32_PhoneContinue

        if v9_sex_with_riley:
            stop music fadeout 3
            jump v9_ri_sex
        
        else:
            stop music fadeout 3
            jump v9_room_sat_aft

    else:
        stop music fadeout 3
        jump v9_room_sat_aft
