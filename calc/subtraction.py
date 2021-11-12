"""This subtraction calculation inherits values from parent"""

from calc.calculation import Calculation

class Subtraction(Calculation):
    """Subtraction class has one method- get the result of calculation from parent class"""
    def getresult(self):
        """Example of Encapsulation"""
        return self.value_a - self.value_b
