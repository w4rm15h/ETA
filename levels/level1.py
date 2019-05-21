# ESCAPE THE ABYSS
# LEVEL 1
import random
import time
import os
import sys
import pickle
import termcolor
from termcolor import *
import configFiles.gameconfig
from configFiles.gameconfig import *
import configFiles.descriptions
from configFiles.descriptions import * 

#CLEAR SCREEN FUNCTION_____________________________________
def menuStart():
    os.system("clear")
    print(colored(title, 'green'))
    time.sleep(0.2)
    print(colored("---------=---------", 'green').center(93, ' '))
    print()

#CELL OPTIONS______________________________________________
def cellFunction():

    CMC.choiceMaker = False
    UserInputFunction()
    CMC.choiceMaker = True
    
    if CMC.choiceMaker == True:

        if CMC.word == "gonorth" and CMC.cellDoor == "locked":
            print(colored(cellNorth, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == 'gonorth' and CMC.celldoor == "open":
            print(colored(cellNorth, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "goeast":
            print(colored(cellEast, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "gosouth":
            print(colored(cellSouth, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "gowest":
            print(colored(cellWest, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "readnote" and CMC.cellBrick == "true":
            print(colored(cellNote, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "jumpwindow":
            print(colored(cellWindow, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
        
        if CMC.word == "checkbrick":
            print(colored(cellBrick, 'green'))
            print(colored("---=---", 'green').center(93, ' '))
            CMC.cellBrick = "true"
            cellFunction()
        
        if CMC.word == "takekey":
            invItem = "Cell Key"
            addingInv(invItem)
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()

        if CMC.word == "usekey":
            keyItem = "Cell Key"
            usingItem(keyItem)
            if CMC.hasItem == "false":
                print(colored("You don't have the correct key."))
                cellFunction()

            if CMC.hasItem == "true":
                print(colored(cellDoorOpen, 'green'))
                time.sleep(5)
                level1()

        else:

            print(colored("Now is not the time for that!", 'green').center(93, " "))
            print()
            print(colored("---=---", 'green').center(93, ' '))
            cellFunction()
    
    else:
        print(colored("** ERROR **", 'green'))
        time.sleep(3)
        UserInputFunction()

#LEVEL 1 FUNCTION________________________________________
def level1Function():

    CMC.choiceMaker = False
    UserInputFunction()
    CMC.choiceMaker = True
    
    if CMC.choiceMaker == True:
        None

#CELL DESCRIPTION________________________________________
def cell():
    menuStart()

    print(colored(cellParagraph, 'green'))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    cellFunction()

#LEVEL 1 DESCRIPTION____________________________________
def level1():
    menuStart()

    print(colored(level1Hallway1, 'green'))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    level1Function()

#LEVEL 1 INTRO TEXT______________________________________
def level1intro():
    menuStart()

    print(colored('"Just going to lay there?"', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"pity, such a pathetic, lazy, disappointment."', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    menuStart()

    print(colored('"Open your eyes."', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"Show me you are worthy"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    menuStart()

    print(colored('"Good... good, thats right."', 'green').center(93, " "))
    print()
    time.sleep(2)
    print(colored('"RISE!"', 'green').center(93, " "))
    print()
    print(colored("---=---", 'green').center(93, ' '))
    time.sleep(5)
    cell()


