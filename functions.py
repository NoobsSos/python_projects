import globalVariables
from app_setting import *


def calcOperations(a, b, op):
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b
        case '^': return a ** b
        case '√': return a ** (1 / b)
        case '%': return a % b
        case _: print("Invalid operator")

def checkInput(a):
    try:
        a = float(a)
        return a
    except ValueError:
        print("Invalid input")
        False


def errorChecker(b, op):
    try:
        if op not in ['+', '-', '*', '/', '^', '√', '%']:
            raise ValueError("Invalid operator")
        if op == '/' and b == 0:
            raise ZeroDivisionError("Division by zero")
    except (ValueError, ZeroDivisionError) as e:
        return str(e)
    return None

def getValidInput(error, b, op):
    while True:
        match error:
            case 'Invalid operator':
                print(error, "Enter a valid (+, -, *, /, ^, √, %) operator")
                op = input("Enter operator: ")
                error = errorChecker(b, op)
                if not error:
                    break
            case 'Division by zero':
                print(error, "Enter a non-zero number")
                b = float(input("Enter second number: "))
                error = errorChecker(b, op)
                if not error:
                    break;

    return b, op

def saveToMemory(a, b, op, result):
    globalVariables.savedResults.append(result)
    globalVariables.calculationHistory.append(f"{a} {op} {b} = {result}")

def recoverLastResult():
    if globalVariables.savedResults:
        return globalVariables.savedResults[-1]
    return None

def printHistory():
    if globalVariables.calculationHistory:
        print("Calculation History:")
        for entry in globalVariables.calculationHistory:
            print(entry)
    else:
        print("No calculations yet.")


def printSettingsMenuToConsole():
    while True:
        print("What would you like to change?")
        print("1. Numbers after decimal")
        print("2. Clear history")
        print("3. Clear memory")
        print("4. Auto save and recover mode on/off")
        print("5. Exit settings")
        choice = input("Enter choice: ")

        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid input")

def printMenuToConsole():
    print("Menu:")
    print(f"1. {'Continue' if globalVariables.savedResults else 'Start'} calculation")
    print("2. Settings")
    print("3. Exit")

    choice = input("Enter choice: ")
    return choice

def selectMenuChoice(choice):
    match choice:
        case '2':
            settingsChoice = printSettingsMenuToConsole()
            settings(settingsChoice)
            return 1
        case '3': return 0
        case _: return 1

def askToSave(a, b, op, result):
    if globalVariables.autoSave:
        saveToMemory(a, b, op, result)
    else:
        save = input("Save the result? (1/0): ")
        if save == '1':
            saveToMemory(a, b, op, result)

def checkHistory():
    view_history = input("View the calculation history? (1/0): ")
    if view_history == '1':
        printHistory()

def userCalculationInput():
    if globalVariables.savedResults and not globalVariables.autoRecover:
        recover_choice = input("Recover the last result? (1/0): ")
        if recover_choice == '1':
            a = recoverLastResult()
            print(f"Last recovered: {a}")
        else:
            a = checkInput(input("Enter first number: "))
    elif not globalVariables.savedResults:
        a = checkInput(input("Enter first number: "))
    elif not globalVariables.autoRecover:
        a = checkInput(input("Enter first number: "))

    if globalVariables.savedResults and globalVariables.autoRecover:
        a = recoverLastResult()
        print(f"Last recovered: {a}")

    b = checkInput(input("Enter second number: "))

    op = input("Enter operator: ")

    while not a or not b:
        print('You entered invalid input. Please try again. USE ONLY NUMBERS!!!')
        if not a:
            a = checkInput(input("Enter first number: "))

        if not b:
            b = checkInput(input("Enter second number: "))

    return a, b, op

def printResult(result):
    print(f"Result: {result}")


def settings(choice):
    match choice:
        case '1':
            globalVariables.numbersAfterDecimal = int(input("Enter numbers after decimal: "))
        case '2':
            globalVariables.calculationHistory = []
        case '3':
            globalVariables.savedResults = []
        case '4':
            globalVariables.autoRecover = not globalVariables.autoRecover
            globalVariables.autoSave = not globalVariables.autoSave
        case '5': return