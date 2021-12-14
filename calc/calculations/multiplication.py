"""Multiplication Class"""
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        try:
            for value in self.values:
                result = result * value
            return result
        except AttributeError:
            result = "Attribute Error"
