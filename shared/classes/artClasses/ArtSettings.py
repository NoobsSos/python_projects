from shared.functions.errorFunctions import checkInput

class ArtSettings():
    availableFonts = ['tty', 'banner', 'rozzo', 'standard', 'slant', 'big', 'doom', 'alligator', 'digital', 'cybermedium']
    availableColors = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    availableSymbols = ['#', '@', '/', '.', '*']
    availableAlignment = ['left', 'center', 'right']
    def __init__(self):
        self.font = "rozzo"
        self.width = 1
        self.height = 1
        self.symbol = '@'
        self.color = 37
        self.align = "left"

    def changeFont(self):
        print(self.availableFonts)
        chosen_font = input("Choose one: ")
        if chosen_font in self.availableFonts:
            self.font = chosen_font
        else:
            self.font = "tty"

    def changeWidthAndHeight(self):
        self.width = checkInput(input("Enter number"))
        self.height = checkInput(input("Enter number"))
        if self.width == False or self.height == False:
            self.width = 1
            self.height = 1


    def changeSymbol(self):
        print(self.availableSymbols)
        symbol = input("Choose one: ")
        if symbol in self.availableSymbols:
            self.symbol = symbol

    def changeColor(self):
        print(self.availableColors)
        color = input("Enter color")
        if color in self.availableColors:
            match color:
                case 'black':
                    self.color = 30
                case 'red':
                    self.color = 31
                case 'green':
                    self.color = 32
                case 'yellow':
                    self.color = 33
                case 'blue':
                    self.color = 34
                case 'magenta':
                    self.color = 35
                case 'cyan':
                    self.color = 36
                case 'white':
                    self.color = 37

        else:
            self.color = 30

    def changeAlignment(self):
        print(self.availableAlignment)
        align = input("Choose one: ")
        if align in self.availableAlignment:
            self.align = align
        else:
            self.align = "left"

    def menu(self):
        while True:
            print("1. Change font")
            print("2. Change width and height")
            print("3. Change symbol")
            print("4. Change colour")
            print("5. Exit")

            choice = input("Choose option: ")

            match choice:
                case "1":
                    self.changeFont()
                case "2":
                    self.changeWidthAndHeight()
                case "3":
                    self.changeSymbol()
                case "4":
                    self.changeColor()
                case _:
                    break