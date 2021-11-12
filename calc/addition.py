"""Addition calculation inherits value A and value B from the calculation class"""
from calc.calculation import Calculation

class Addition(Calculation):
    """Gets result of the calculation A and B in parent class"""
    def getresult(self):
        """Example of encapsulation"""
        return self.value_a + self.value_b
