""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    history = []

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        return value_a + value_b
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
        return value_a / value_b
