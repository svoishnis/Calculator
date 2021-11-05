"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator()
    calc.add_number(4)
    assert calc.result == 4

def test_calculator_subtract():
    calc = Calculator()
    calc.subtract_number(4)
    assert calc.result == 4

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    calc.multiple_numbers(4)
    assert calc.result == 4

def test_calculator_divide():
    """ tests division of two numbers"""
    calc = Calculator()
    calc.divide_numbers(4)
    assert calc.result == 4
