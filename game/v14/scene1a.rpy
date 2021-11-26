# SCENE 01a: Wake Up From Fever Dream
# Locations: Hotel Bathroom, Hotel Room, Hotel Corridor, Hotel Lobby
# Characters: LINDSEY (Outfit: 1), MC (Outfit: 3)
# Time: Night

label v14s01a:
    play music "music/v14/Track Scene 1a_1.mp3" fadein 2

    scene v14s01a_1 # TPP. Same positioning as v13s62a_10a, MC moving in for a kiss on Lindsey (not kissing yet), Lindsey smiling, mouth closed
    with dissolve

    pause

    call screen VoiceActing_Toggle()

    scene v14s01a_1a # TPP. Same as v14s01a_1, Lindsey putting a finger on MC's lips (as if telling him to be quiet), MC confused, mouth closed, Lindsey smiling, mouth open
    with dissolve

    li "Wait... Open your eyes..."

    scene v14s01a_1b # TPP. Same as v14s01a_1a, Lindsey mouth closed, MC mouth open, LIndsey finger no longer on MC mouth
    with dissolve

    u "Huh?"

    stop music fadeout 3
    play music "music/v14/Track Scene 1a_2.mp3" fadein 2

    scene v14s01a_2 # TPP. Show MC startled, waking up (still night time), he is laying on his bed, mouth open
    with flash

    u "What the- holy shit...!"

    scene v14s01a_3 # TPP. Show MC sitting up on his bed, slightly annoyed, mouth closed, hands on head
    with dissolve

    u "(A fucking dream?! Ugh! I need to get up and do something. I can't sleep right now, I don't care what time it is.)"

    scene v14s01a_4 # TPP. Show MC leaving the hotel room door, slightly annoyed, mouth closed
    with fade

    u "(No more dreaming for me.)"

    scene v14s01a_5 # TPP. Show MC walking in hotel corridor, slightly annoyed, mouth closed
    with dissolve

    pause 0.75

    scene v14s01a_6 # TPP. Show MC arriving in hotel lobby, neutral expression, mouth closed
    with dissolve

    pause 0.75

    stop music fadeout 3

    jump v14s02