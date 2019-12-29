NotesForSam = """
Hey sammy just edit the paragraphs here,
that way whatever you change will be instantly updated.
woop woop!!!
"""
#Generic Descriptions
title = """
▄▄▄ ..▄▄ ·  ▄▄·  ▄▄▄·  ▄▄▄·▄▄▄ .    ▄▄▄▄▄ ▄ .▄▄▄▄ .     ▄▄▄· ▄▄▄▄·  ▄· ▄▌.▄▄ · .▄▄ ·
▀▄.▀·▐█ ▀. ▐█ ▌▪▐█ ▀█ ▐█ ▄█▀▄.▀·    •██  ██▪▐█▀▄.▀·    ▐█ ▀█ ▐█ ▀█▪▐█▪██▌▐█ ▀. ▐█ ▀.
▐▀▀▪▄▄▀▀▀█▄██ ▄▄▄█▀▀█  ██▀·▐▀▀▪▄     ▐█.▪██▀▐█▐▀▀▪▄    ▄█▀▀█ ▐█▀▀█▄▐█▌▐█▪▄▀▀▀█▄▄▀▀▀█▄
▐█▄▄▌▐█▄▪▐█▐███▌▐█ ▪▐▌▐█▪·•▐█▄▄▌     ▐█▌·██▌▐▀▐█▄▄▌    ▐█ ▪▐▌██▄▪▐█ ▐█▀·.▐█▄▪▐█▐█▄▪▐█
 ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ .▀    ▀▀▀      ▀▀▀ ▀▀▀ · ▀▀▀      ▀  ▀ ·▀▀▀▀   ▀ •  ▀▀▀▀  ▀▀▀▀

"""

topBanner = "---------=---------"

swordImage = """
                                    /\
                                   // \
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                   || |
                                __ || | __
                               /____**____\
                                    XX
                                    XX
                                   _XX_
                                  (0000)
                                   \  /
                                    \/

"""

playerInvDict = {

    "playername": "Player 1",
    "playerhealth": 100,
    "playerprogress": "Empty",
    "playerweapon":{
            "weaponGrade": "Empty",
            "weaponName": "Empty",
            "weaponAttack": 0,
            "weaponColour": "green",
                },
    "playerarmor":{
            "armorGrade": "Empty",
            "armorName": "Empty",
            "armorDefence": 0,
            "armorColour": "green",
                },
    "playerattack": 0,
    "playerdefence": 0,
    "playerdeaths": 0,
    "playernew": True,
    "1. ": "Empty",
    "2. ": "Empty",
    "3. ": "Empty",
    "4. ": "Empty",
    "5. ": "Empty",
    "6. ": "Empty",
    "7. ": "Empty",
    "8. ": "Empty",
    "9. ": "Empty",
    "10. ": "Empty",
}

#Enemy Encounters_________________________________________
level1Enemys = {

    "1":{
        "name": "SPIDER",
        "health": 100,
        'attack': 20,
        "defence": 10,
        },
    "2":{
        "name": "IMP",
        "health": 100,
        'attack': 20,
        "defence": 11,
        },
    "3":{
        "name": "DEMON",
        "health": 100,
        'attack': 20,
        "defence": 12,
        }

}

# ACCEPTED INPUTS_________________________________________

yes = [

    "y",
    "Y",
    "yes",
    "yep",
    'fucking oath',
    "bring it on"
]

no = [

    "n",
    "N",
    "nope",
    "nah"
]

back = [

    "back",
    "head back",
    "go back",
    "backspace",
    "backwards",
    "return"
]

swear = [

    "fuck",
    "cunt",
    "ass",
    "butt",
    "tits",
    "motherfucker",
    "asscheese",
    "piss"

]

verbs = [

    "go",
    "kick",
    "check",
    "jump",
    "read",
    "take",
    "use",
    "exit",
    "move",
    "drop"
]

objects = [

    "north",
    "east",
    "south",
    "west",
    "door",
    "window",
    "wall",
    "brick",
    "note",
    "key",
    "playerInvDict"

]

hubChoices = [

    "start",
    "begin",
    "password"

]

startSword = {

    "common": (10,12),
    "rare": (12,14),
    "mystic": (14,16),
    "legendary": (16,20)

}

oneToTen = [

    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"

]

playerVerbs = [

    "use",
    "drop",
    "move",
    "exit"

]

healingtItems = {

    "potion" : 25,
    "strong potion": 50

}

errorOutputs = [

    "Pity, such a simple creation",
    "That is not possible right now",
    "Maybe choose an option that will help...",
    "Shame... can't even perform such a simple task",
    "Come on, Focus!"

]

helpText = """
                            Welcome to Escape the Abyss.

                            Make your way through the levels by solving
                            the puzzles to either escape a room or
                            progress further into the Abyss.

                            Keep the inputs simple, if you want
                            to jump for a window use "jump window".
                            For picking up items use "take <item>".
                            Most general terms will be accepted for
                            yes and no e.g. Yeah, yes and yep.

                            If you die during the game, you will
                            be placed back at the start.
                            You will keep the weapons, armor and
                            items you collect along the way to make
                            progressing the next time that little
                            bit easier, though this will still be a
                            challenge.

                            You are assigned an attack and defence
                            number decided by a dice roll.
                            To increase these values seek and find
                            weapons through-out the levels.

                            GOOD LUCK.
"""
#LEVEL1 - CELL _________________________________________

drinkingPotionText = """
                            You pull the cork off the small vile,
                            The smell is unpleasent,
                            you open your mouth and empty the
                            vile. You almost instantly feel
                            refreshed and healthy.
                            Let's continue...
"""

cellParagraph = """
You wake to find yourself in a small,
dark jailcell.
Terrible things have happened here,
faint sounds of screams haunt the long, narrow,
stone hallways. The old cell doors
lie direcetly NORTH, their bars rusty,
weakened with age.
Fingernail scratchings, torn deep into the EAST wall,
casting warped, disturbing shadows.
To the SOUTH, a small WINDOW, providing
an ominious blue glow, that helps illuminate
the small cell but also provides a chilling breeze.
A wooden desk is chained and bolted to
the shadowy WEST wall.
Despite the rot in the old wood,
The dust on top was fresh.
Someone was in here... Recently.
"""
cellNorth = """
                            You walk up to the cell door and wrap your
                            hands around the old bars.
                            You can feel the rust digging into your
                            skin, all you see is darkness.
                            Screams and groans echoing through the
                            hallways.
"""
cellEast = """
                            You slowly walk up to the wall
                            and run your fingers down the
                            scrathes. They somewhat resemble
                            an arrow pointing to a odd
                            looking brick in the wall.
"""
cellSouth = """
                            You turn around and look at the
                            window.
                            The bars looked cold, frozen.
                            The window is high, though it
                            seems it might be in reach.
"""
cellWest = """
                            The desk, just sitting there,
                            Rotting and beaten by old age.
                            The dust on top, fresh.
                            Someone was in here, recently.
"""
cellBrick = """
                            You grip the edge of the
                            odd looking brick.
                            You pull out the brick,
                            revealing a note and a key.
"""
cellNote = """
                            A quick TIP to help you
                            along your travels.
                            Keep the text lowercase.
                            Use words like:
                            go north,
                            kick door,
                            Use key,
                            to interact with your
                            surroundings.
                            You fold the note and
                            place it back in the hole.
                            Just incase...
"""
cellWindow = """
                            You jump and hold the glaciated
                            bars blocking the window.
                            Your hands can't get a good grip,
                            but you manage to get a look outside.
                            It's a giant lake, frozen over.
                            souls are frozen in the lake,
                            with only thier necks and heads
                            pertruding the surface.
                            The souls here, stuck, without
                            even the small comfort of thier
                            own tears.
"""

cellDoorOpen = """
                            You walk up to the door
                            and place the key in the lock.
                            you twist the key slowly trying
                            not to make to much noise,
                            trying to avoid alerting any
                            potential enemys.
                            The cell door unlocks.
                            You put the key back and
                            place the brick back into
                            the exposed hole.
                            It seems like the right
                            thing to do.
                            You step out of the cell,
                            closing the door behind
                            you.
"""


#LEVEL 1 - PART 2 ________________________________________________________________

level1Hallway1 = """

                            The air whistles past your ears flowing
                            fast to the NORTH, it was a long hallway,
                            leading off the right.
                            the walls leading high up into the darkness.
                            Behind you to the SOUTH is the small, dark
                            cell you just excaped from.
                            You hear a whisper 'Thisssssss wayyyyyy',
                            pulling your head to the WEST.
                            The hallway was narrow, eary and dark,
                            very dark. There is a light at the end
                            though, though is does seem far,
                            it

"""
