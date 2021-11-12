"""This multiplication calculation inherits values from parent"""

from calc.calculation import Calculation

class Multiplication(Calculation):
    """Multiplication class has one method- get the result of calculation from parent class"""
    def getresult(self):
        """This is encapsulation example"""
        return self.value_a * self.value_b
