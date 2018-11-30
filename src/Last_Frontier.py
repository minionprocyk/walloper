from EveWindowManager import EveWindowManager
window_manager = EveWindowManager()

import time
import pyautogui

# create main
# --- Nothing Above this line ---
# -- Navigation --
# - Macro Navigation -
def macro_navigation():
    print("macro_navigation")

#FIX ME IM BROKEN
# Am I docked? (Updated 11/11/2018)
def docked():
    docked = window_manager.image_exist('undock_2.png')
    if docked == False:
        print('Currently Undocked')
    elif docked == True:
        print('Currently Docked')
    elif docked == '?':
        print('Not sure if docked')
    #evaluate if docked or not using ingame memory reading method / logic
    else:
        print('Error @ "Am I docked?"')
    return docked

#FIX ME IM BROKEN
# If I am docked then undock
def undock():
    docked = '?'
    docked()
    while docked != False:
        window_manager.click_image('undock_2.png')
        time.sleep(3)
        docked()
    else:
        print('Error @ "If I am docked, then undock"')


# select destination
def select_destination():
    n = 1 # TEMPORARY IN PLACE OF INPUT PARAMETER
    pl_variable = 1
    xt = 12 + 12
    yt = 123 + (16 * pl_variable) + 4

    # right click
    pyautogui.rightClick() # VALUES HERE PUT MOUSE IN CENTER OF SCREEN FOR EASY MENU
    time.sleep(1)
    # mouse x value = XO
    # mouse y value = YO
    x, y = pyautogui.position()
    # tabs = N (number of menue tabs to go through)
    tabs = n
    # while tabs != 0
        # tabs = tabs -1
        # mouse x value = XO + XT
        # mouse y value = YO + YT
        # move mouse to (XO + XT, YO + YT)
        # if tabs = 0 then left click
    while tabs != 0:
        tabs = tabs -1
        x = x +xt
        y = y + yt
        pyautogui.moveTo(x ,y)
        time.sleep(1)
        if tabs == 0:
            pyautogui.click()

def select_destination2():
    destination_selected ='?'
    evaluate_destination_selected ='?'
    while destination_selected != True:
        print('execute select destination feature')
        evaluate_destination_selected ='execute evaluate select destination feature'
        print(evaluate_destination_selected)
        if evaluate_destination_selected == True:
            destination_selected = True
        elif evaluate_destination_selected == False:
            destination_selected = False
        else:
            print('Error @ "select destination"')

# Enable auto pilot
def auto_pilot():
    auto_pilot = '?'
    while auto_pilot != 'on':
        print('execite enable_auto_pilot')
        evaluate_auto_pilot='execute evaluate_enable_auto_pilot'
        if evaluate_auto_pilot == 'y':
            auto_pilot = 'on'
        elif evaluate_auto_pilot == 'n':
            auto_pilot ='off'
        else:
            print('Error @ Enable autopilot')

# Have I reached my destiniation? or Am I Docked?
# - Micro Navigation -
def micro_navigation():
    print("text")
    print("new text here")
# Select destination
# Do I APROACH / ORBIT / MAINTAIN DISTANCE / HALT?
# Have I reached my destination? if yes do I HALT or continue?
# --- Nothing Below this line ---
# execute main
def main():
    print('Starting this bad boy')
    time.sleep(5)
    select_destination()
    print('This bad boy is take a rest')

main()