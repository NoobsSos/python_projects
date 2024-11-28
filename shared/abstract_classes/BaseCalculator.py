from abc import abstractmethod

class BaseCalculator:
    def __init__(self, calculatorType="math"):
        calculatorType = calculatorType.lower()

    def calcOperations(self, a, b, op):
        raise NotImplementedError("Not implemented in BaseCalculator")

    @abstractmethod
    def calculate(self):
        pass
