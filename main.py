from globalVariables import *
from functions import *
from app_setting import *

def main():
    work = 1
    global savedResults

    while work:
        print("Menu:")
        print(f"1. {'Continue' if savedResults else 'Start'} calculation")
        print("2. Settings")
        print("3. App settings")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '2':
            settings()
            continue
        elif choice == '3':
            appSetting()
            continue
        elif choice == '4':
            break

        if savedResults and not autoRecover:
            recover_choice = input("Recover the last result? (1/0): ")
            if recover_choice == '1':
                a = recoverLastResult()
                print(f"Last recovered: {a}")
            else:
                a = float(input("Enter first number: "))
        elif not savedResults:
            a = float(input("Enter first number: "))
        elif not autoRecover:
            a = float(input("Enter first number: "))

        if savedResults and autoRecover:
            a = recoverLastResult()
            print(f"Last recovered: {a}")

        b = float(input("Enter second number: "))

        op = input("Enter operator: ")

        error = errorChecker(b, op)

        if error:
            while True:
                if error == "Invalid operator":
                    print(error, "Enter a valid (+, -, *, /, ^, √, %) operator")
                    op = input("Enter operator: ")
                    error = errorChecker(b, op)
                    if not error:
                        break
                elif error == "Division by zero":
                    print(error, "Enter a non-zero number")
                    b = float(input("Enter second number: "))
                    error = errorChecker(b, op)
                    if not error:
                        break

        result = round(calcOperations(a, b, op), numbersAfterDecimal)
        print(f"Result: {result}")

        if autoSave:
            saveToMemory(a, b, op, result)
        else:
            save = input("Save the result? (1/0): ")
            if save == '1':
                saveToMemory(a, b, op, result)

        view_history = input("View the calculation history? (1/0): ")
        if view_history == '1':
            printHistory()