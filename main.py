#Escape the Abyss
#6/02/19
#online word based game
#!/bin/bash

import os
import os.path
import signal
import sys
import time
import pickle
import random
import shutil
import termcolor
from termcolor import colored
import configFiles.gameconfig
from configFiles.gameconfig import *
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
        print(CMC.passHolder)
        creatingUserProfile(makeAccount)
        
def creatingUserProfile(name):
    playerInvDict["playerattack"] = random.randint(12, 15)
    playerInvDict["playerdefence"] = random.randint(12, 15)
    playerInvDict["playername"] = name
    playerInvDict["playerphrase"] = CMC.passHolder
    with open("save/{0}.abyss".format(name), 'wb') as save1:
        pickle.dump(playerInvDict, save1)
    print(colored("*Player Account Created*", 'green').center(93, " "))
    print(colored("*Time to login and play*", 'green').center(93, " "))
    print(colored("*...*", 'green').center(93, " "))
    time.sleep(2)
    loginPage()

#Login Page
def loginPage():
    menuStart()
    print(colored("Player Login", 'green').center(93, " "))
    print()
    print(colored("-----=-----", 'green').center(93, ' '))
    print(colored("User Name", 'green').center(93, " "))
    
    #Creating User Name
    userName = input(colored("                                     >", 'green'))

    #Trying Something Different
    if os.path.isfile("save/{0}.abyss".format(userName)) != True:
        print()
        print(colored("*{0}*' not found".format(userName), 'red').center(93, " "))
        print()
        print(colored("Create a new account?", 'green').center(93, " "))
        userName = input(colored("                                     >", 'green'))
        if userName == "y":
            creatingUser()
        else:
            loginPage()
    else:
        with open("save/{0}.abyss".format(userName), 'rb') as open1:
            playerInvDict = pickle.load(open1)
        validPassword = playerInvDict["playerphrase"]
        print(validPassword)
        print(colored("Password", 'green').center(93, " "))
        userPassword = input(colored("                                     >", 'green'))
        #Validating the user password
        if userPassword == validPassword:
            if playerInvDict["playernew"] == True:
                playerInvDict["playernew"] = False
                playerSave(userName)
                introduction(userName)
            else:
                theHub(userName)
        else:
            print(colored("Incorrect Password", 'green').center(93, " "))
            loginPage()
               
#PRINGTING PLAYER INV____________________________________

def printingInventory(playerName):
    with open("save/{0}.abyss".format(playerName), 'rb') as save1:
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
    print(colored(item1, 'green').center(93, " "))
    print(colored(item2, 'green').center(93, " "))
    print(colored(item3, 'green').center(93, " "))
    print(colored(item4, 'green').center(93, " "))
    print(colored(item5, 'green').center(93, " "))
    print(colored(item6, 'green').center(93, " "))
    print(colored(item7, 'green').center(93, " "))
    print(colored(item8, 'green').center(93, " "))
    print(colored(item9, 'green').center(93, " "))
    print(colored(item10, 'green').center(93, " "))

#PRINTING THE HUB_________________________________________

def theHub(playerName):
    menuStart()
    with open("save/{0}.abyss".format(playerName), 'rb') as loading:
        playerInvDict = pickle.load(loading)

    print(colored("{0}".format(playerInvDict["playername"]), 'green').center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print()
    print(colored("Equipped Weapon:", 'green').center(93, " "))
    print(colored("{0}".format(playerInvDict["playerweapon"]), 'green').center(93, " "))
    print()
    print(colored("Equipped Armor:", 'green').center(93, " "))
    print(colored(playerInvDict["playerarmor"], 'green').center(93, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(colored("Health: {0}".format(playerInvDict["playerhealth"]), 'green').center(93, " "))
    print(colored("Attack: {0}".format(playerInvDict["playerattack"]), 'green').center(93, " "))
    print(colored("Defence: {0}".format(playerInvDict["playerdefence"]), 'green').center(93, " "))

    print()
    print(colored(topBanner, 'green').center(93, " "))
    print()
    print(colored("Progress: {0}".format(playerInvDict["playerprogress"]), 'green').center(93, " "))
    print(colored("Deaths: {0}".format(playerInvDict["playerdeaths"]), 'green').center(92, " "))
    print()
    print(colored(topBanner, 'green').center(93, " "))
    printingInventory(playerName)
    print()
    print(colored("---------=---------", 'green').center(93, ' '))
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
    time.sleep(5)

    menuStart()
    print(colored('"Lost... pity."', 'green').center(93, " "))
    print(colored('"Wondering where?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)

    menuStart()
    print(colored('"I guess i could tell you"', 'green').center(93, " "))
    print(colored('...', 'green').center(93, " "))
    print(colored('"Lets just say..."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)

    menuStart()
    print(colored('"Deep into the abyss!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)

    menuStart()
    print(colored('"Will you find your way out?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(3)

    menuStart()
    print(colored('"OR"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(1)

    menuStart()
    print(colored('"Will you get lost,', 'green').center(93, " "))
    print(colored('in the dark?"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)

    menuStart()
    print(colored('"Are you ready?"', 'green').center(93, " "))
    print(colored("Press enter to start.", 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))

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
signal.signal(signal.SIGINT, signal_handler)


