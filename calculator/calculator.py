""" This is the increment function"""
from calc.addition import Addition

class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        # create an addition object using the factory we created on the calculation class
        addition = Addition.create(value_a, value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result. Error thrown in python - unit test confirms"""
        if value_b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return value_a / value_b

    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """gets the last item added to the list"""
        return Calculator.history[-1].getresult()

    @staticmethod
    def add_calculation_to_history(calculation):
        """Adds current item to the list"""
        Calculator.history.append(calculation)
        return True
