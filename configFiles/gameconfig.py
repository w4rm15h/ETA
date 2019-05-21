import time
import sys
import random
import signal
import termcolor
from termcolor import *
import pickle

class CMCplayerIncvDict():
    playerIncvDictVerb = ""
    playerIncvDictNum = ""
    playerIncvDictMove = ""
    playerIncvDictCheck = False

class CMC():
    passHolder = ""
    choiceMaker = False
    iV = ""
    iO = ""
    playerIncvDictV = ""
    playerIncvDictN = 0
    word = ""
    number = 0
    roll = ""
    weaponLevel =  ""
    weaponAttack = 0
    cellKey = "false"
    cellDoor = "locked"
    hasItem = "false"

topBanner = ("---------=---------")

#SAVING FUNCTIONS

def playerLoad(name):
    with open("save/{0}.abyss".format(name), 'rb') as load:
        playerInvDict = pickle.load(load)

def playerSave(name):
    with open("save/{0}.abyss".format(name), 'wb') as save:
        pickle.dump(playerInvDict, save)



title = """
▄▄▄ ..▄▄ ·  ▄▄·  ▄▄▄·  ▄▄▄·▄▄▄ .    ▄▄▄▄▄ ▄ .▄▄▄▄ .     ▄▄▄· ▄▄▄▄·  ▄· ▄▌.▄▄ · .▄▄ · 
▀▄.▀·▐█ ▀. ▐█ ▌▪▐█ ▀█ ▐█ ▄█▀▄.▀·    •██  ██▪▐█▀▄.▀·    ▐█ ▀█ ▐█ ▀█▪▐█▪██▌▐█ ▀. ▐█ ▀.   
▐▀▀▪▄▄▀▀▀█▄██ ▄▄▄█▀▀█  ██▀·▐▀▀▪▄     ▐█.▪██▀▐█▐▀▀▪▄    ▄█▀▀█ ▐█▀▀█▄▐█▌▐█▪▄▀▀▀█▄▄▀▀▀█▄
▐█▄▄▌▐█▄▪▐█▐███▌▐█ ▪▐▌▐█▪·•▐█▄▄▌     ▐█▌·██▌▐▀▐█▄▄▌    ▐█ ▪▐▌██▄▪▐█ ▐█▀·.▐█▄▪▐█▐█▄▪▐█
 ▀▀▀  ▀▀▀▀ ·▀▀▀  ▀  ▀ .▀    ▀▀▀      ▀▀▀ ▀▀▀ · ▀▀▀      ▀  ▀ ·▀▀▀▀   ▀ •  ▀▀▀▀  ▀▀▀▀ 
                                        
"""
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
# Paragraphs_________________________________________

Help = """
                        Welcome to Escape the Abyss.

                        This game does not give you much help.
                        Figure it out for yourself... right?
                        Make your way through the Abyss to level
                        up and aquire stronger weapons and armor. 
                        Each time you fail you will arrive back
                        at the start, you keep your Weapons,
                        Armor and Key items to make the
                        next time a little easier.
                        There are lots of secrets and weapons 
                        hidden away, can you find them?

                        GOOD LUCK.
"""

playerInvDict = {

    "playername": "Player 1",
    "playerhealth": 100,
    "playerprogress": "Empty",
    "playerweapon": "Empty",
    "playerarmor": "Empty",
    "playerattack": 0,
    "playerdefence": 0,
    "playerdeaths": 0,
    "playernew": False,
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

loginNames = {

    "justcause": "Justcause",

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
    "playerIncvDictentory"

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

playerIncvDictVerbs = [

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
    "Shame... can't even perform such a simple task"

]

#CLEARING SCREEN
def menuStart():
    os.system("clear")
    print(colored(title, 'green'))
    time.sleep(0.2)
    print(colored("---------=---------", 'green').center(93, ' '))
    print()

#CTRL + C ____________________________________________
def signal_handler(sig, frame):
    print()
    print(colored('You pressed Ctrl+C!', 'green').center(93, " "))
    pass

signal.signal(signal.SIGINT, signal_handler)

#SAVING FUNCTIONS____________________________________





#ERROR FUNCTION______________________________________
def errorFunction():
    errorOutput = random.choice(errorOutputs)
    print(colored("---=---", 'green').center(93, ' '))
    print(colored(errorOutput, 'green').center(93, " "))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def playerIncvDictErrorFunction():
    errorOutput = random.choice(errorOutputs)
    print(colored("---=---", 'green').center(93, ' '))
    print(colored(errorOutput, 'green').center(93, " "))

    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")  #clear line
    sys.stdout.write("\033[F")
    
    #playerIncvDictENTORY____________________________________________
def printingplayerIncvDictentory():
    print()
    print(colored("playerIncvDictentory", 'green').center(93, " "))
    print(colored("---=---", 'green').center(93, ' '))
    print()

    with open("save2.abyss", 'rb') as save2:
        playerInvDict = pickle.load(save2)

    for i in playerInvDict:
        print(colored("%s: %s" % (i, playerInvDict[i]), 'green').center(93, " "))

def playerIncvDictentoryFunction():
    
    with open("save2.abyss", 'rb') as save2:
        playerInvDict = pickle.load(save2)

    printingplayerIncvDictentory()
    print(colored("---=---", 'green').center(93, ' '))
    print(colored("move, drop, use items.", 'green').center(93," "))
    print(colored("type exit to head back.", 'green').center(93, " "))
 

def addingplayerIncvDict(item):

    with open("save2.abyss", 'rb') as save2:
        playerInvDict = pickle.load(save2)

        printingplayerIncvDictentory()
        print()
        print(colored("---=---", 'green').center(93, ' '))
        print(colored("Where do you want to place the item?", 'green').center(93," "))
        userInput = input(colored("                                     > ", 'green'))
        num = userInput

        if num not in oneToTen:
            playerIncvDictErrorFunction()
            
        else:

            playerInvDict["{0}. ".format(num)] = item

            print(colored("{0} added to playerIncvDictentory".format(item), 'green').center(93, " "))
            
            with open("save2.abyss", 'wb') as save2:
                pickle.dump(playerInvDict, save2)
            
#playerInvDict INPUT FUNCTION________________________________
def playerIncvDictInputFunction():

    while CMCplayerIncvDict.checkplayerIncvDict == True:

        with open("save2.abyss", 'rb') as save2:
            playerInvDict = pickle.load(save2)

        printingplayerIncvDictentory()
        print(colored("---=---", 'green').center(93, ' '))
        print(colored("DROP, MOVE, USE or EXIT follow by the playerInvDict number", 'green').center(93, " "))
        print(colored("---=---", 'green').center(93, ' '))
        playerIncvDictInput = input(colored("\r                                     >", 'green'))
        playerIncvDictInputWord = playerIncvDictInput.split(" ")
        
        if len(playerIncvDictInputWord) == 2:
            CMCplayerIncvDict.playerIncvDictVerb = (playerIncvDictInputWord[0])
            CMCplayerIncvDict.playerIncvDictNum = (playerIncvDictInputWord[1])
        else:
            CMCplayerIncvDict.playerIncvDictVerb = (playerIncvDictInputWord[0])

        verb = CMCplayerIncvDict.playerIncvDictVerb
        num = CMCplayerIncvDict.playerIncvDictNum 
        

        if verb == "drop":
            playerInvDict["{0}. ".format(num)] = "Empty"

            with open("save2.abyss", 'wb') as save2:
                pickle.dump(playerInvDict, save2)

        if verb == "move" and num in oneToTen:

            print(colored("---=---", 'green').center(93, ' '))
            print(colored("Move where?", 'green').center(93, " "))
            playerIncvDictMove = input(colored("                                     > ", 'green'))

            if playerIncvDictMove not in oneToTen:
                playerIncvDictErrorFunction()

            else:
                playerIncvDictStore = playerInvDict["{0}. ".format(num)]
                playerInvDict["{0}. ".format(num)] = playerInvDict["{0}. ".format(playerIncvDictMove)]
                playerInvDict["{0}. ".format(playerIncvDictMove)] = playerIncvDictStore

                with open("save2.abyss", 'wb') as save2:
                    pickle.dump(playerInvDict, save2) 
        
        if verb == "use":
            healingItem = playerInvDict["{0}. ".format(num)]

            if healingItem not in healingtItems:
                playerIncvDictErrorFunction()

            
            else:
                with open("save1.abyss", 'rb') as save1:
                    playerInvDict = pickle.dump(save1)
                
                typePotion = playerInvDict["{0}. ".format(num)]

                if typePotion not in healingItems:
                    playerIncvDictErrorFunction()


                heal = (healingItems["{0}".format(typePotion)] * playerInvDict[playerhealth]) / 100.0

                #If player health is not already full
                if playerInvDict["playerhealth"] < 100:
                    playerInvDict["playerhealth"] += heal



                #making sure health does not go over max amount    
                if playerInvDict["playerhealth"] > 100:
                    playerInvDict["playerhealth"] = 100

                with open("save1.abyss", 'wb') as save1:
                    pickle.dump(playerInvDict, save1)

        if verb == "exit":
            break

        if verb not in playerIncvDictVerbs or num not in oneToTen:
            playerIncvDictErrorFunction()

#CONTINUE FUNCTION__________________________________
def pressEnter():

    print(colored("Press Enter", 'green').center(93, " "))
    print(colored("---=---", 'green').center(93, ' '))
    cnt = input(colored("> ", 'green').center(93, " "))
    while cnt != " ":
        print(colored("I said Enter, pity... Fool."))
        time.sleep(2)
        break
    
    else:
        None

#GLOBAL FUNCTION FOR CHOICES__________________________
def UserInputFunction():

    while CMC.choiceMaker == False:

        UserInput = input(colored("                                     > ", 'green'))
        instruction = UserInput.split(" ")
        wordLength = len(instruction)

        if wordLength == 2:

            CMC.iV = (instruction[0])
            CMC.iO = (instruction[1])
            CMC.word = (CMC.iV + CMC.iO)

            if CMC.iV not in verbs:

                print(colored("{0}?".format(CMC.iV), 'green').center(93, " "))
                print()
                print(colored("---=---", 'green').center(93, ' '))
                CMC.choiceMaker = False
                
            else:

                if CMC.iO not in objects:

                    print(colored("{0}?".format(CMC.iO), 'green').center(93, " "))
                    print()
                    print(colored("---=---", 'green').center(93, ' '))
                    CMC.choiceMaker = False
                
                else:
                    if CMC.word == "checkplayerIncvDictentory":
                        CMCplayerIncvDict.checkplayerIncvDict = True
                        playerIncvDictInputFunction()
                    
                    else:
                        return(CMC.iV, CMC.iO)
                        break
                    
    else:

        print(colored("Two words please", 'green').center(93, " "))
        CMC.choiceMaker = False
        time.sleep(1)



def diceRoll():

    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    total = (number1 + number2)

    if total < 4:
        CMC.roll = "legendary"
        CMC.weaponLevel = "legendary"

    if total > 4 and total < 10:
        cmc.roll = "mystic"
        CMC.weaponLevel = "mystic"
    
    if total > 10 and total < 20:
        CMC.roll = "uncommon"
        MC.weaponLevel = "uncommon"

    if total > 20 and total < 40:
        CMC.roll = "common"
        CMC.weaponLevel = "common"

def weaponStats():
    
    if CMC.weaponLevel == "legendary":

        CMC.weaponAttack = random.randint(startSword["legendary"])
        weaponDamge = random.randint(startSword["legendary"])
        print(colored(swordImage, 'yellow'))
        print(colored("Weapon Damage: {0}".format(weaponDamage), 'yellow'))
        print(colored("Do you want to equip this item?"))
        yesOrNo = input(colored("> ", 'green').center(93, " "))
        while yesOrNo not in yes or yesOrNo not in no:

            print(colored('"YES OR NO?"', "green").center(93, " "))

        else: 
            if yesOrNo in yes:
                print("This is were we equip the item. should make a function for that though")

            if yesOrNo in no:
                print("Back to it then.")
            
    if CMC.weaponLevel == "mystic":
        None

    if CMC.WeaponLevel == "uncommon":
        None

    if CMC.weaponLevel == "common":
        None

def printWeaponStats():
    None
           
def pickingUpSword():
    print(colored("You hold the sword in your hands",'green').center(93," "))
    diceRoll()
    weaponStats()

def usingItem(playerIncvDictItem):

    with open("save2.abyss", "rb") as save2:
        playerInvDict = pickle.load(save2)
    
    for playerIncvDictItem in playerInvDict:
        CMC.hasItem = "true"
        break

    else:
        CMC.hasItem = "False"


