"""Division Class"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """divide calculation object"""

    def get_result(self):
        """get the quotient results"""
        result = 1.0
        try:
            for value in self.values[:1]:
                result = value
            for value in self.values[1:]:
                if value == 0:
                    return "Zero Division Error"
                result = result / value
            return result
        except AttributeError:
            return "Attribute Error"
