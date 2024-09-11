from globalVariables import *

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

def errorChecker(b, op):
    if op not in ['+', '-', '*', '/', '^', '√', '%']:
        return "Invalid operator"
    if op == '/' and b == 0:
        return "Division by zero"
    return None

def saveToMemory(a, b, op, result):
    global savedResults, calculationHistory
    savedResults.append(result)
    calculationHistory.append(f"{a} {op} {b} = {result}")

def recoverLastResult():
    if savedResults:
        return savedResults[-1]
    return None

def printHistory():
    if calculationHistory:
        print("Calculation History:")
        for entry in calculationHistory:
            print(entry)
    else:
        print("No calculations yet.")

def settings():
    print("What would you like to change?")
    print("1. Numbers after decimal")
    print("2. Clear history")
    print("3. Clear memory")
    print("4. Auto save and recover mode on/off")
    print("5. Exit settings")
    choice = input("Enter choice: ")

    if choice == '1':
        global numbersAfterDecimal
        numbersAfterDecimal = int(input("Enter the number of decimal places: "))
    elif choice == '2':
        global calculationHistory
        calculationHistory = []
    elif choice == '3':
        global savedResults
        savedResults = []
    elif choice == '4':
        global autoRecover
        autoRecover = not autoRecover

        global autoSave
        autoSave = not autoSave
        print(f"Auto recover is now {'on' if autoRecover and autoSave else 'off'}")  
    elif choice == '5':
        return
    else:
        print("Invalid choice")
        settings()
