from shared.abstract_classes.BaseCalculator import BaseCalculator
from shared.functions.errorFunctions import checkInput, errorChecker, getValidInput

from ui.MenuItem import MenuItem
from ui.MenuBuilder import MenuBuilder

class Calculator(BaseCalculator):
    def __init__(self):
        super().__init__()

        self._savedResults = []
        self._calculationHistory = []
        self._numbersAfterDecimal = 2
        self._autoRecover = False
        self._autoSave = False

    @property
    def numbersAfterDecimal(self):
        return self._numbersAfterDecimal

    @numbersAfterDecimal.setter
    def numbersAfterDecimal(self, value):
        self._numbersAfterDecimal = value

    @property
    def autoRecover(self):
        return self._autoRecover

    @autoRecover.setter
    def autoRecover(self, value):
        self._autoRecover = value

    @property
    def autoSave(self):
        return self._autoSave

    @autoSave.setter
    def autoSave(self, value):
        self._autoSave = value

    def displayResult(self, result):
        print(f"Result: {result}")

    def askForAnotherCalculation(self):
        return input("Do you want to perform another calculation? (1/0): ") == '1'

    def userCalculationInput(self):
        if self._savedResults:
            match self._autoRecover:
                case True:
                    a = self.recoverLastResult()
                    print(f"Last recovered: {a}")
                case False:
                    recover_choice = input("Recover the last result? (1/0): ")
                    match recover_choice:
                        case '1':
                            a = self.recoverLastResult()
                            print(f"Last recovered: {a}")
                        case _:
                            a = checkInput(input("Enter first number: "))
        else:
            a = checkInput(input("Enter first number: "))

        b = checkInput(input("Enter second number: "))
        op = input("Enter operator: ")

        while not a or not b:
            print('You entered invalid input. Please try again. USE ONLY NUMBERS!!!')
            if not a:
                a = checkInput(input("Enter first number: "))
            if not b:
                b = checkInput(input("Enter second number: "))

        return a, b, op

    def calcOperations(self, a, b, op):
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return a / b
            case '^':
                return a ** b
            case '√':
                return a ** (1 / b)
            case '%':
                return a % b
            case _:
                print("Invalid operator")

    def saveToMemory(self, a, b, op, result):
        self._savedResults.append(result)
        self._calculationHistory.append(f"{a} {op} {b} = {result}")

    def askToSave(self, a, b, op, result):
        if self._autoSave:
            self.saveToMemory(a, b, op, result)
        else:
            save = input("Save the result? (1/0): ")
            if save == '1':
                self.saveToMemory(a, b, op, result)

    def recoverLastResult(self):
        if self._savedResults:
            return self._savedResults[-1]
        return None

    def askToShowHistory(self):
        choice = input("Do you want to show history? (1/0): ")
        match choice:
            case '1':
                self.printHistory()
            case _: return None

    def printHistory(self):
        if self._calculationHistory:
            print("Calculation History:")
            for entry in self._calculationHistory:
                print(entry)
        else:
            print("No calculations yet.")

    def start_or_continue_calculation(self):
        while True:
            a, b, op = self.userCalculationInput()

            error = errorChecker(b, op)

            if error:
                b, op = getValidInput(error, b, op)

            result = round(self.calcOperations(a, b, op), self._numbersAfterDecimal)
            self.displayResult(result)

            self.askToSave(a, b, op, result)

            if self._savedResults:
                self.askToShowHistory()

            if not self.askForAnotherCalculation():
                break

    def printMenuToConsole(self):
        menu_items = [
            MenuItem("1", f"{'Continue' if self._savedResults else 'Start'} calculation",
                     self.start_or_continue_calculation),
            MenuItem("2", "Settings", self.settings),
            MenuItem("3", "Exit", exit)
        ]

        menu_builder = MenuBuilder(menu_items)
        menu_builder.initialize()

    def printSettingsMenuToConsole(self):
        while True:
            print("What would you like to change?")
            print("1. Numbers after decimal")
            print("2. Clear history")
            print("3. Clear memory")
            print(f"4. Auto save and recover mode on/off. Current state: {self._autoSave}")
            print("5. Exit settings")
            choice = input("Enter choice: ")

            if choice in ['1', '2', '3', '4', '5']:
                return choice
            else:
                print("Invalid input")

    def settings(self):
        print("What would you like to change?")
        print("1. Numbers after decimal")
        print("2. Clear history")
        print("3. Clear memory")
        print(f"4. Auto save and recover mode on/off. Current state: {self._autoSave}")
        print("5. Exit settings")
        choice = input("Enter choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid input")

        match choice:
            case '1':
                self._numbersAfterDecimal = int(input("Enter numbers after decimal: "))
            case '2':
                self._calculationHistory = []
            case '3':
                self._savedResults = []
            case '4':
                self._autoRecover = not self._autoRecover
                self._autoSave = not self._autoSave
            case '5': return

    def selectMenuChoice(self, menuChoice):
        match menuChoice:
            case '2':
                while True:
                    settingsChoice = self.printSettingsMenuToConsole()
                    self.settings(settingsChoice)
                    if settingsChoice == '5':
                        break
            case '3':
                return 0
            case _:
                return 1

    def calculate(self):
        while True:
            choice = self.printMenuToConsole()
            self.selectMenuChoice(choice)

            a, b, op = self.userCalculationInput()

            error = errorChecker(b, op)

            if error:
                b, op = getValidInput(error, b, op)

            result = round(self.calcOperations(a, b, op), self._numbersAfterDecimal)
            self.displayResult(result)

            self.askToSave(a, b, op, result)

            if self._savedResults:
                self.askToShowHistory()

            if not self.askForAnotherCalculation():
                break
