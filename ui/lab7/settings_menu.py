from shared.functions.httpFunctions import printHistory

def settingsMenu(settings):
    while True:
        print("1. Change API")
        print("2. Change colour")
        print("3. Print history")
        print("5. Exit")

        choice = input("Choose option: ")

        match choice:
            case "1":
                settings.setUrl()
            case "2":
                settings.changeColor()
            case "3":
                printHistory(settings)
            case _:
                break