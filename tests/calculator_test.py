"""Testing the Calculator"""
import pprint
import pytest
from calculator.calculator import Calculator
@pytest.fixture
def clear_history():
    """This method is created for Unit Testing Only"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1, 2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    """This tests the clearing history method defined above"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history()
    assert Calculator.history_count() == 0

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_divide(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.divide_numbers(2,3) == 0.6666666666666666

def test_calculator_divide_except(clear_history):
    """ tests the exception for the division of two numbers"""
    try:
        assert Calculator.divide_numbers(3, 0)
    except ZeroDivisionError:
        assert ZeroDivisionError
