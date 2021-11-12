"""Testing the Calculator"""
from calculator.calculator import Calculator

def test_calculator_add():
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_divide():
    """ tests multiplication of two numbers"""
    assert Calculator.divide_numbers(2,3) == 0.6666666666666666

def test_calculator_divide_except():
    """ tests the exception for the division of two numbers"""
    try:
        result = Calculator.divide_numbers(3, 0)
    except ZeroDivisionError:
        result = "Cannot divide by zero"
    assert result == "Cannot divide by zero"
