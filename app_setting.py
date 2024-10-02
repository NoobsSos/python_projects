from Color_Console import *

from globalVariables import availavbleColours

def printAppSetting():
    print('Here you can change the colour of background or text')
    changes = input('To change background type 1, to change text type 2 or anything else to leave: ')
    print('Available Colours:')
    for entry in availavbleColours:
        print(entry)
    colour = input('Write some colour: ')

    isColourAvailable = colour.lower() in availavbleColours

    if isColourAvailable:
        return changes, colour
    else:
        return 0



def appSetting(changes, colour):
       match changes:
            case '1': color( bg = colour )
            case '2': color( text = colour )
            case _: return



