"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """divide calculation object"""
    def get_result(self):
        """get the quotient results"""
        result = 1.0
        for value in self.values:
            if value == 0:
                return "ZeroDivisionError"
            result = result / value
        return result
