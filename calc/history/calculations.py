"""Calculation history Class"""
from calc.calculations.addition import Addition
from calc.calculations.division import Division
from calc.calculations.multiplication import Multiplication
from calc.calculations.subtraction import Subtraction


class Calculations:
    """Create a storage for calculation history"""
    history = []
    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clears history of calculations"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """Method returns the amount of calculations stored"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """Returns the oldest calculation stored"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        """Returns a specific calculation stored"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """get a generic calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """ Add a addition calculation to the history"""
        Calculations.add_addition_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        # Get the result of the calculation
        return True
