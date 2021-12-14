"""Subtraction Class"""
import pprint

from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        try:
            for value in self.values[:1]:
                difference_of_values = value
            for value in self.values[1:]:
                difference_of_values = difference_of_values + (-1 * value)
                pprint.pprint(value)
            return difference_of_values
        except AttributeError:
            return "Attribute Error"
