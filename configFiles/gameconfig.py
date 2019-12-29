#imports
import time
import sys
import random
import signal
import termcolor
from termcolor import *
import pickle
from gameconfig import *
from descriptions import *

#Class to store variables for player
class CMC():
    name = ""
    passHolder = ""
    choiceMaker = False
    iV = ""
    iO = ""
    playerInvDictV = ""
    playerInvDictN = 0
    word = ""
    number = 0
    weaponAttack = 0
    cellKey = "false"
    cellDoor = "locked"
    hasItem = "false"
    encounter = False
    level = 0
    text = ""
    txt = ""
    eb = False
    playerVerb = ""
    playerNum = ""
    playerMove = ""
    playerCheck = False

#Clearing screen
def menuStart():
    os.system("clear")
    print(colored(title, 'green'))
    time.sleep(0.2)
    print(colored("---------=---------", 'green').center(93, ' '))
    print()

#Pressing CTRL + C
import signal
def signal_handler(sig, frame):
    pass

signal.signal(signal.SIGINT, signal_handler)

#CONTINUE FUNCTION
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

#Loading screen for creating player profile
def loadingScreen():
    for i in range(5):
        sys.stdout.write(colored("\r" + "                                 Creating Profile" + "." * i, 'green'))
        time.sleep(1)
        sys.stdout.flush()
    print()

#Error function
def invError():
    errorOutput = random.choice(errorOutputs)
    print(colored("---=---", 'green').center(93, ' '))
    print(colored(errorOutput, 'green').center(93, " "))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def errorFunction():
    errorOutput = random.choice(errorOutputs)
    print(colored("---=---", 'green').center(93, ' '))
    print(colored(errorOutput, 'green').center(93, " "))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def errorFunctionLogin():
    print(colored("---=---", 'green').center(93, ' '))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def errorFunctionPassword():
    print(colored("---=---", 'green').center(93, ' '))
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[F") #back to previous line
    sys.stdout.write("\033[K") #clear line

def areaUpdate(text):
    CMC.text = (text)

#Global function for input
def UserInputFunction():
    while CMC.choiceMaker == False:
        UserInput = input(colored("                                     > ", 'green'))
        instruction = UserInput.split(" ")
        wordLength = len(instruction)

        if UserInput == "inv":
                CMC.checkplayerInvDict = True
                playerInvInputFunction()

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
                    return(CMC.iV, CMC.iO)
                    break

#Inventory functions
#Printing Inventory
def printingInventory():
    with open("save/{0}.abyss".format(CMC.name), 'rb') as save1:
        playerInvDict = pickle.load(save1)
    item1 = playerInvDict["1. "]
    item2 = playerInvDict["2. "]
    item3 = playerInvDict["3. "]
    item4 = playerInvDict["4. "]
    item5 = playerInvDict["5. "]
    item6 = playerInvDict["6. "]
    item7 = playerInvDict["7. "]
    item8 = playerInvDict["8. "]
    item9 = playerInvDict["9. "]
    item10 = playerInvDict["10. "]
    print()
    print(colored("Inventory", 'green').center(93, ' '))
    print()
    print(colored("                                      1. " + item1, 'green'))
    print(colored("                                      2. " + item2, 'green'))
    print(colored("                                      3. " + item3, 'green'))
    print(colored("                                      4. " + item4, 'green'))
    print(colored("                                      5. " + item5, 'green'))
    print(colored("                                      6. " + item6, 'green'))
    print(colored("                                      7. " + item7, 'green'))
    print(colored("                                      8. " + item8, 'green'))
    print(colored("                                      9. " + item9, 'green'))
    print(colored("                                     10. " + item10, 'green'))

#Adding items to inventory
def addingplayerInvDict(item):
    with open("save/{0}.abyss".format(CMC.name), 'rb') as loading:
        playerInvDict = pickle.load(loading)
        printingInventory()
        print()
        print(colored("---=---", 'green').center(93, ' '))
        print(colored("Where do you want to place the item?", 'green').center(93," "))
        userInput = input(colored("                                     > ", 'green'))
        num = userInput
        if num not in oneToTen:
            errorFunction()()
        else:
            playerInvDict["{0}. ".format(num)] = item
            print(colored("{0} added to inventory".format(item), 'green').center(93, " "))
            with open("save/{0}.abyss".format(CMC.name), 'wb') as save2:
                pickle.dump(playerInvDict, save2)

#In Game inventory functions
def playerInvInputFunction():
    menuStart()
    with open("save/{0}.abyss".format(CMC.name), 'rb') as save2:
        playerInvDict = pickle.load(save2)
    printingInventory()
    print(colored("---=---", 'green').center(93, ' '))
    print(colored("DROP, MOVE, USE or EXIT follow by the playerInvDict number", 'green').center(93, " "))
    print(colored("---=---", 'green').center(93, ' '))

    while CMC.checkplayerInvDict == True:
        playerInvInput = input(colored("                                     >", 'green'))
        playerInvWord = playerInvInput.split(" ")

        if playerInvWord[0] == "exit":
            CMC.checkplayerInvDict == False
            menuStart()
            print(colored(CMC.text, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            break

        if len(playerInvWord) == 2:
            CMC.playerVerb = (playerInvWord[0])
            CMC.playerNum = (playerInvWord[1])
        else:
            if len(playerInvWord) != 2:
                errorFunction()

        verb = CMC.playerVerb
        num = CMC.playerNum

    #Checking to see if word is valid
        if verb not in playerVerbs or num not in oneToTen:
            invError()

        if verb == "drop":
            playerInvDict["{0}. ".format(num)] = "Empty"

            with open("save/{0}.abyss".format(CMC.name), 'wb') as save2:
                pickle.dump(playerInvDict, save2)

        if verb == "move" and num in oneToTen:
            print(colored("---=---", 'green').center(93, ' '))
            print(colored("Move where?", 'green').center(93, " "))
            playerMove = input(colored("                                     > ", 'green'))

            if playerMove not in oneToTen:
                invError()

            else:
                playerInvDictStore = playerInvDict["{0}. ".format(num)]
                playerInvDict["{0}. ".format(num)] = playerInvDict["{0}. ".format(playerMove)]
                playerInvDict["{0}. ".format(playerMove)] = playerInvDictStore
                with open("save/{0}.abyss".format(CMC.name), 'wb') as save2:
                    pickle.dump(playerInvDict, save2)
                invError()

    #Using Item
        if verb == "use":
            healingItem = playerInvDict["{0}. ".format(num)]

            if healingItem not in healingtItems:
                invError()

            else:
                with open("save/{0}.abyss".format(CMC.name), 'rb') as save1:
                    playerInvDict = pickle.dump(save1)

                typePotion = playerInvDict["{0}. ".format(num)]

                if typePotion not in healingItems:
                    invError()

                heal = (healingItems["{0}".format(typePotion)] * playerInvDict[playerhealth]) / 100.0

            #If player health is not already full
                if playerInvDict["playerhealth"] < 100:
                    playerInvDict["playerhealth"] += heal

            #making sure health does not go over max amount
                if playerInvDict["playerhealth"] > 100:
                    playerInvDict["playerhealth"] = 100

                with open("save/{0}.abyss".format(CMC.name), 'wb') as save1:
                    pickle.dump(playerInvDict, save1)

def usingItem(item):
    with open("save/{0}.abyss".format(CMC.name), 'rb') as save2:
        playerInvDict = pickle.load(save2)
    for item in playerInvDict:
        CMC.hasItem = "true"
        break
    else:
        CMC.hasItem = "False"

#Picking up WEAPON function
def pickUpWeapon(weaponName):
#Rolling the dice
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    total = (number1 + number2)
#Legendary grade
    if total < 4:
        grade = "legendary"
        name = (weaponName)
        score = 30
        colour = "magenta"
        weaponScore(grade, name, score, colour)
#Mystic grade
    if total > 4 and total < 10:
        grade = "mystic"
        name = (weaponName)
        score = 25
        colour = "cyan"
        weaponScore(grade, name, score, colour)
#Uncommon grade
    if total > 10 and total < 20:
        grade = "uncommon"
        name = (weaponName)
        score = 23
        colour = "blue"
        weaponScore(grade, name, score, colour)
#Common Grade
    if total > 20 and total < 40:
        grade = "common"
        name = (weaponName)
        score = 21
        colour = "green"
        weaponScore(grade, name, score, colour)

#Equipping or passing on WEAPON
def weaponScore(grade, name, score, colour):
    menuStart()
#Loading Dictionary
    with open("save/{0}.abyss".format(CMC.name), 'rb') as loading:
        playerInvDict = pickle.load(loading)
#Displaying Weapon and givinge choice to equip
    menuStart()
    print()
    print(colored("**********", 'green').center(93, " "))
    print(colored("Chest contains", 'green').center(93, " "))
    print(colored("**********", 'green').center(93, " "))
    print()
    print(colored("{0}".format(name), '{0}'.format(colour)).center(93, " "))
    print(colored("Damage: {0}".format(score), '{0}'.format(colour)).center(93, " "))
    print()
    print(colored("-----=-----", 'green').center(93, ' '))
    print(colored("Would you like to equip", 'green').center(93, " "))
    print(colored("'{0}'?".format(name), 'green').center(93, " "))
    yesNo = input("                                         > ")
#Picking Up Weapon
    if yesNo == "y" or yesNo == "yes":
        playerInvDict["playerweapon"]["weaponGrade"] = grade
        playerInvDict["playerweapon"]["weaponName"] = name
        playerInvDict["playerweapon"]["weaponAttack"] = score
        playerInvDict["playerweapon"]["weaponColour"] = colour
        with open("save/{0}.abyss".format(CMC.name), 'wb') as saving:
            pickle.dump(playerInvDict, saving)
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You have equipped the weapon", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
#Leaving weapon behind
    if yesNo == "n" or yesNo == "no":
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You left the weapon behind", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()

#Picking up ARMOR function
def pickUpArmor(armorName):
#Rolling the dice
    number1 = random.randint(1,20)
    number2 = random.randint(1,20)
    total = (number1 + number2)
#Legendary grade
    if total < 4:
        grade = "legendary"
        name = (armorName)
        score = 50
        colour = "magenta"
        armorScore(grade, name, score, colour)
#Mystic grade
    if total > 4 and total < 10:
        grade = "mystic"
        name = (armorName)
        score = 40
        colour = "cyan"
        armorScore(grade, name, score, colour)
#Uncommon grade
    if total > 10 and total < 20:
        grade = "uncommon"
        name = (armorName)
        score = 35
        colour = "blue"
        armorScore(grade, name, score, colour)
#Common Grade
    if total > 20 and total < 40:
        grade = "common"
        name = (armorName)
        score = 30
        colour = "green"
        armorScore(grade, name, score, colour)

#Equipping or passing on ARMOR
def armorScore(grade, name, score, colour):
    menuStart()
    with open("save/{0}.abyss".format(CMC.name), 'rb') as loading:
        playerInvDict = pickle.load(loading)
#Displaying ARMOR and giving choice to equip
    menuStart()
    print()
    print(colored("**********", 'green').center(93, " "))
    print(colored("Chest contains", 'green').center(93, " "))
    print(colored("**********", 'green').center(93, " "))
    print()
    print(colored("{0}".format(name), '{0}'.format(colour)).center(93, " "))
    print(colored("Defence: {0}".format(score), '{0}'.format(colour)).center(93, " "))
    print()
    print(colored("-----=-----", 'green').center(93, ' '))
    print(colored("Would you like to equip", 'green').center(93, " "))
    print(colored("'{0}'?".format(name), 'green').center(93, " "))
    yesNo = input("                                         > ")
#Picking Up armor
    if yesNo == "y" or yesNo == "yes":
        playerInvDict["playerarmor"]["armorGrade"] = grade
        playerInvDict["playerarmor"]["armorName"] = name
        playerInvDict["playerarmor"]["armorDefence"] = score
        playerInvDict["playerarmor"]["armorColour"] = colour
        with open("save/{0}.abyss".format(CMC.name), 'wb') as saving:
            pickle.dump(playerInvDict, saving)
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You put on the Armor", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
#Leaving armor behind
    if yesNo == "n" or yesNo == "no":
        print(colored("-----=-----", 'green').center(93, ' '))
        print()
        print(colored("You left the armor behind", 'green').center(93, " "))
        print()
        print(colored("-----=-----", 'green').center(93, ' '))
        time.sleep(3)
        menuStart()
