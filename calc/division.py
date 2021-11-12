"""This division calculation inherits values from parent"""

from calc.calculation import Calculation

class Division(Calculation):
    """Multiplication class has one method- get the result of calculation from parent class"""
    def getresult(self):
        """This is encapsulation example"""
        if self.value_b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.value_a / self.value_b
