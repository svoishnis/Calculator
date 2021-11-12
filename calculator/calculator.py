""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Gets the First item from the list"""
        return Calculator.history[0].getresult()

    @staticmethod
    def clear_history():
        """Clears the history stored"""
        Calculator.history.clear()
        return True

    @staticmethod
    def history_count():
        """Returns the amount of Calculations Stored"""
        return len(Calculator.history)

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adds current item to the list"""
        Calculator.history.append(calculation)
        return True

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """gets the last item added to the list"""
        return Calculator.history[-1].getresult()

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result. Error thrown in python - unit test confirms"""
        if value_b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return value_a / value_b
