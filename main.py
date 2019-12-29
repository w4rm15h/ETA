#Escape the Abyss
#6/02/19
#online word based game
#!/bin/bash

#Imports
import os
import os.path
import signal
import sys
import time
import pickle
import random
import shutil
import getpass 
import termcolor
from termcolor import colored
import configFiles.gameconfig
from configFiles.gameconfig import *
from configFiles.descriptions import *
from levels.level1 import *

#Creating User
def creatingUser():
    menuStart()
    print(colored("Please Enter Player Name...", 'green').center(93, " "))
    print()
    makeAccount = input(colored("                                     >", 'green'))
    print()
    
    if os.path.isfile("save/{0}.abyss".format(makeAccount)) == True:
        print(colored("Sorry, name already taken", 'green').center(93, " "))
        print()
        print(colored("Maybe try something", 'green').center(93, " "))
        print(colored("a little more... creative!", 'green').center(93, " "))
        time.sleep(2)
        creatingUser()
    else:
        print(colored("Are you happy with '{0}'".format(makeAccount), 'green').center(93, " "))
        nameConfirm = input(colored("                                     >", 'green'))
        if nameConfirm == "y":
            passwordSetup(makeAccount)
            time.sleep(2)
            loginPage()
        else:
            creatingUser()

def passwordSetup(makeAccount):
    print()
    print(colored("Enter your password: ", 'green').center(93, " "))
    passwordSetup1 = input(colored("                                     >", 'green'))
    print()
    print(colored("One more time:", 'green').center(93, " "))
    passwordSetupCheck = input(colored("                                     >", 'green'))

    if passwordSetup1 != passwordSetupCheck:
        print("sorry {0}, passwords do not match".format(makeAccount))
        time.sleep(1)
        passwordSetup()
    else:
        CMC.passHolder = passwordSetup1
        creatingUserProfile(makeAccount)
        
def creatingUserProfile(name):
    playerInvDict["playerattack"] = random.randint(12, 15)
    playerInvDict["playerdefence"] = random.randint(12, 15)
    playerInvDict["playername"] = name
    playerInvDict["playerphrase"] = CMC.passHolder
    with open("save/{0}.abyss".format(name), 'wb') as save1:
        pickle.dump(playerInvDict, save1)
    print()
    loadingScreen()
    print()
    print(colored("*Player Account Created*", 'green').center(93, " "))
    print()
    time.sleep(1)
    print(colored("*Time to login and play*", 'green').center(93, " "))
    time.sleep(2)
    loginPage()

#Login Page
def loginPage():
    menuStart()
    print(colored("1. Login         ", 'green').center(93, " "))
    print()
    print(colored("2. Create Account", 'green').center(93, " "))
    print()
    print(colored("3. Help          ", 'green').center(93, " "))
    print()
    print(colored("---------=---------", 'green').center(93, ' '))
    print(colored("User Name", 'green').center(93, " "))
    loginCtn()

def loginCtn():
    userName = input(colored("                                     > ", 'green'))

    if userName == "help" or userName == "3":
        menuStart()
        print(colored(helpText, 'green'))
        backToPage = input(colored(" Press enter to return to login", 'green').center(93, " " ))
        if backToPage == "":
            loginPage()
        else:
            loginPage()

    if userName == "create" or userName == "create account" or userName == "2":
        creatingUser()

    if os.path.isfile("save/{0}.abyss".format(userName)) != True:
        print()
        print(colored("*{0}* not found".format(userName), 'red').center(93, " "))
        errorFunctionLogin()
        loginCtn()
      
    else:
        passwordInputFunction(userName)

def passwordInputFunction(userName):
    with open("save/{0}.abyss".format(userName), 'rb') as open1:
        playerInvDict = pickle.load(open1)
    print()
    validPassword = playerInvDict["playerphrase"]
    print(colored("Password", 'green').center(93, " "))
    sys.stdout.write("\033[K") #clear line
    userPassword = input(colored("                                     > ", 'green'))

    #Validating the user password
    if userPassword == validPassword:
        if playerInvDict["playernew"] == True:
            playerInvDict["playernew"] = False
            with open("save/{0}.abyss".format(userName), 'wb') as update:
                pickle.dump(playerInvDict, update)
            introduction(userName)
        else:
            CMC.name = userName
            theHub(userName)
    else:
        print()
        print(colored("*Incorrect Password*", 'red').center(93, " "))
        errorFunctionPassword()
        passwordInputFunction(userName)

#PRINTING THE HUB
def theHub(playerName):
    menuStart()
    with open("save/{0}.abyss".format(playerName), 'rb') as loading:
        playerInvDict = pickle.load(loading)
    CMC.name = playerName
    weaponName = (playerInvDict["playerweapon"]["weaponName"])
    armorName = (playerInvDict["playerarmor"]["armorName"])
    weaponAttack = (playerInvDict["playerweapon"]["weaponAttack"])
    armorDefence = (playerInvDict["playerarmor"]["armorDefence"])
    weaponColour = (playerInvDict["playerweapon"]["weaponColour"])
    armorColour = (playerInvDict["playerarmor"]["armorColour"])
    playerHealth = playerInvDict["playerhealth"]
    playerAttack = playerInvDict["playerattack"]
    playerDefence = playerInvDict["playerdefence"]
    playerProgress = playerInvDict["playerprogress"]
    playerDeaths = playerInvDict["playerdeaths"]
    playerAttackTotal = (playerAttack + weaponAttack)
    playerDefenceTotal = (playerDefence + armorDefence)
    weaponPrint = (colored(weaponName, '{0}'.format(weaponColour)).center(93, " "))
    armorPrint = (colored(armorName, '{0}'.format(armorColour)).center(93, " "))

    print(colored("{0}".format(playerName), 'green').center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(weaponPrint)
    print(colored("Damage: {0}".format(weaponAttack), "green").center(93, " "))
    print()
    print(armorPrint)
    print(colored("Defence: {0}".format(armorDefence), "green").center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(colored("Health: {0}".format(playerHealth), 'green').center(92, " "))
    print(colored("Attack: {0}".format(playerAttackTotal), 'green').center(92, " "))
    print(colored("Defence: {0}".format(playerDefenceTotal), 'green').center(90, " "))
    print(colored("Progress: {0}".format(playerProgress), 'green').center(92, " "))
    print(colored("Deaths: {0}".format(playerDeaths), 'green').center(90, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    printingInventory()
    print()
    print(colored("---------=---------", 'green').center(93, ' '))
    print(colored("Type 'start' to begin your adventure.", 'green').center(93, ' '))
    hubInput()

def hubInput():
    hubChoice = input(colored("                                        > ", 'green'))

    while hubChoice in hubChoices:
        if hubChoice == "start":
            cell()
    else:
        errorFunction()
        hubInput()

#INTRO FUNCTION_______________________________________________________

def introduction(playerName):
    menuStart()

    print(colored('"Well, well, well."', 'green').center(93, " "))
    print(colored('"look who we have here?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Lost... pity."', 'green').center(93, " "))
    print(colored('"Wondering where?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"I guess i could tell you"', 'green').center(93, " "))
    print(colored('...', 'green').center(93, " "))
    print(colored('"Lets just say..."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Deep into the abyss!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Will you find your way out?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"OR"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Will you get lost,', 'green').center(93, " "))
    print(colored('in the dark?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(2)

    menuStart()
    print(colored('"Are you ready?"', 'green').center(93, " "))
    print(colored("Press enter to start.", 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    with open("save/{0}.abyss".format(playerName), 'rb') as update:
        playerInvDict = pickle.load(update)
    playerInvDict["playernew"] = False
    with open("save/{0}.abyss".format(playerName), 'wb') as addUpdate:
        pickle.dump(playerInvDict, addUpdate)
    process = input()
    if process == " ":
        theHub(playerName)
    else:
        theHub(playerName)

#HELP MENU______________________________________________________________________

def helpMenu():
    menuStart()
    print(colored("H E L P", 'green').center(93, ' '))
    print()
    time.sleep(0.4)
    print(colored("   ---=---     ", 'green').center(95, ' '))
    print(colored(Help.center(100, " "), 'green'))
    print(colored("---------=---------", 'green').center(93, ' '))
    returnToMenu = input(colored("                                        > ", 'green'))

    if returnToMenu in back:
        mainMenu()

    else:
        print(colored("Not a valid input, seriously come on dude.", 'green').center(93, " "))
        time.sleep(1)
        helpMenu()

#RUNNING FUNCTIONS_________________________________________
loginPage()


