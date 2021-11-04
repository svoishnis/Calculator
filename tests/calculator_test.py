"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3

def test_calculator_subtract():

    assert Calculator.subtract_number(1,2) == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiple_numbers(1,2) == 2

def test_calculator_divide():
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(1,2) == 0.5
