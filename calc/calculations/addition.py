"""Addition Class"""
from calc.calculations.calculation import Calculation


class Addition(Calculation):
    """ calculation addition class"""

    def get_result(self):
        """get the addition results"""
        sum_of_values = 0.0
        try:
            for value in self.values:
                sum_of_values = value + sum_of_values
            return sum_of_values
        except AttributeError:
            return "Attribute Error"
