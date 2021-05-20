label fight_tutorialLabel:
    scene tomstancekick
    with dissolve

    show screen fight_tutorial

    tut "In every fight, you'll have positions from which you can attack and positions from which you'll need to defend."
    tut "In attacking positions you'll have a set of offensive actions, as shown on the left."
    tut "Since you're new to fighting, you only have 3 simple attacks:"

    show screen fight_tutorial(highlight='q')

    tut "{b}Q{/b}: a quick, left-handed jab to create distance and attack the opponent's face from the front."

    show screen fight_tutorial(highlight='w')

    tut "{b}W{/b}: a strong, right-handed hook to attack the opponent's head from the side."

    show screen fight_tutorial(highlight='r')

    tut "And {b}R{/b}: a right-footed kick to attack the opponent's legs."

    show screen fight_tutorial

    tut "As you learn more about fighting, you'll gain new attack moves."

    tut "When attacking, look at the opponent's stance and try to identify possible points of attack."

    show targets

    tut "With your three actions, there are three possible points of attack."

    show screen fight_tutorial(highlight='r')

    tut "Since Tom has his guard up and could probably block both a jab and a hook, try to kick him by pressing {b}R{/b} in the upcoming screen."

    hide screen fight_tutorial
    hide targets
    with dissolve

    return

label fight_changeKeybinds:
    scene jab1pic
    with dissolve

    $ w = renpy.input("Which button should be hook / block face?", default="w").strip() or "w"

    scene hook1pic
    with dissolve

    $ q = renpy.input("Which button should be hook / block face?", default="q").strip() or "q"

    scene kick1pic
    with dissolve

    $ r = renpy.input("Which button should be hook / block face?", default="r").strip() or "r"

    return