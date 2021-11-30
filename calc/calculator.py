""" This is the increment function"""
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """This gets the result of the calculation"""
        return Calculations.get_last_calculation_result_value()
    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ adds list of numbers"""
        #create an addition object using the factory we created on the calculation class
        # pylint: disable=maybe-no-member
        Calculator.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    #this is an example of a calling method
    def subtract_numbers(tuple_values: tuple):
        """ subtract list of numbers from result"""
        # create an subtraction object using the factory we created on the calculation class
        # pylint: disable=maybe-no-member
        Calculator.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiply numbers from the result"""
        # pylint: disable=maybe-no-member
        Calculator.add_multiplication_calculation(tuple_values)
        return True

    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ divide numbers from the result"""
        # pylint: disable=maybe-no-member
        Calculator.add_division_calculation(tuple_values)
        return True
