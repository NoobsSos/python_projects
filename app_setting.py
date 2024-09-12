from Color_Console import *

availavbleColours = [
    'black',
    'blue',
    'aqua',
    'red',
    'purple',
    'yellow',
    'white',
    'gray',
]

def appSetting():
    while True:
        print('Here you can change the colour of background or text')
        changes = input('To change background type 1, to change text type 2: ')
        print('Available Colours:')
        for entry in availavbleColours:
            print(entry)
        colour = input('Write some colour: ')

        isColourAvailable = colour.lower() in availavbleColours

        if isColourAvailable:
            if changes == '1':
                color( bg = colour )
                print('done')
                break
            elif changes == '2':
                color( text = colour )
                print('done')
                break
        else:
            print('Try again')



