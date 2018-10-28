# create main
# --- Nothing Above this line ---
# -- Navigation --
# - Macro Navigation -
def macro_navigation():
    print("macro_navigation")

# Am I docked?
docked = '?'
if docked == 'n':
    print('Currently Undocked')
elif docked == "y":
    print('Currently Docked')
elif docked == '?':
    #evaluate if docked or not using ingame memory reading method / logic
else:
    print('Error @ "Am I docked?"')

# If I am docked then undock
while docked == 'y':
    print('execite undock feature')
    print('execute evaluate if docked / undocked feature')
    if evaluate_docked == 'n':
        docked == 'n'
    elif evaluate_docked =='y':
        docked == 'y'
    else:
        [print('Error @ "If I am docked, then undock"')


if docked == 'y':
    print('execute undock feature')
    print('execute ')

# select destination
# Enable auto pilot
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