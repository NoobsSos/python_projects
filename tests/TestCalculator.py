import unittest

import sys
sys.path.append('C:/Users/$MNH400-P2NKHD8RVQGL/Desktop/python_labs')

from classes.calculatorClasses.Calculator import Calculator
from shared.functions.errorFunctions import errorChecker

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calcOperations(5, 3, '+'), 8)

        self.assertEqual(self.calculator.calcOperations(-5, -3, '+'), -8)

        self.assertEqual(self.calculator.calcOperations(-5, 3, '+'), -2)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calcOperations(10, 3, '-'), 7)

        self.assertEqual(self.calculator.calcOperations(-5, -3, '-'), -2)

        self.assertEqual(self.calculator.calcOperations(5, 10, '-'), -5)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calcOperations(5, 3, '*'), 15)

        self.assertEqual(self.calculator.calcOperations(5, 0, '*'), 0)

        self.assertEqual(self.calculator.calcOperations(-5, -3, '*'), 15)

        self.assertEqual(self.calculator.calcOperations(5, -3, '*'), -15)

    def test_division(self):
        self.assertEqual(self.calculator.calcOperations(10, 2, '/'), 5)

        self.assertEqual(self.calculator.calcOperations(-10, -2, '/'), 5)

        self.assertEqual(self.calculator.calcOperations(-10, 2, '/'), -5)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.calcOperations(10, 0, '/')

    def test_error_handling(self):
        error = errorChecker(10, '#')
        self.assertEqual(error, "Invalid operator")

        error = errorChecker(0, '/')
        self.assertEqual(error, "Division by zero")