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
    print('Not sure if docked')
#evaluate if docked or not using ingame memory reading method / logic
else:
    print('Error @ "Am I docked?"')

# If I am docked then undock
evaluate_docked == '?'
while docked == 'y':
    print('execite undock feature')
    print('execute evaluate if docked / undocked feature')
    if evaluate_docked == 'n':
        docked == 'n'
    elif evaluate_docked =='y':
        docked == 'y'
    else:
        print('Error @ "If I am docked, then undock"')

# select destination
destination_selected ='?'
evaluate_destination_selected ='?'
while destination_selected != 'y':
    print('execute select destination feature')
    evaluate_destination_selected ='execute evaluate select destination feature'
    print(evaluate_destination_selected)
    if evaluate_destination_selected == 'y':
        destination_selected = 'y'
    elif evaluate_destination_selected == 'n':
        destination_selected = 'n'
    else:
        print('Error @ "select destination"')

# Enable auto pilot
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