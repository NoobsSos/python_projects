from functions import *
from app_setting import *

from clases.Calculator import Calculator
import globalVariables
def main():
    work = 1

    while work:
        calc = Calculator()
        work = calc.calculate()

        if work == 0:
            break
        a, b, op = userCalculationInput()

        error = errorChecker(b, op)

        if error:
            b, op = getValidInput(error, b, op)

        result = round(calcOperations(a, b, op), globalVariables.numbersAfterDecimal)
        printResult(result)

        askToSave(a, b, op, result)

        checkHistory()