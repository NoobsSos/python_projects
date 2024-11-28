from shared.logger import Logger

def checkInput(a):
    try:
        a = float(a)
        return a
    except ValueError:
        Logger.log('Someone entered an invalid input value')
        print("Invalid input")
        return False


def errorChecker(b, op):
    try:
        if op not in ['+', '-', '*', '/', '^', '√', '%']:
            Logger.log('Someone entered an invalid operator')
            raise ValueError("Invalid operator")
        if op == '/' and b == 0:
            Logger.log('Someone tried to divide by zero')
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

import re

def isValidUrl(input_str):
    url_pattern = re.compile(
        r'^(https?|ftp)://'                           
        r'(?:(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'       
        r'(?:\/[^\s]*)?$',
        re.IGNORECASE
    )
    return re.match(url_pattern, input_str) is not None


