"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()
#You have to add the fixture function as a parameter to the test that you want to use it with
def test_calculator_add_static(clear_history_fixture):
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0,2.0,5.0)
    Calculator.addition(my_tuple)
    assert Calculator.get_last_result_value() == 8.0

def test_calculator_subtract_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.subtraction(my_tuple)
    assert Calculator.get_last_result_value() == -6.0

def test_calculator_multiply_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 2.0, 3.0)
    Calculator.multiplication(my_tuple)
    assert Calculator.get_last_result_value() == 6.0

def test_calculator_divide_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 2.0, 1)
    Calculator.division(my_tuple)
    assert Calculator.get_last_result_value() == 0.5

def test_calculator_divide_error_static(clear_history_fixture):
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 0, 1)
    Calculator.division(my_tuple)
    assert Calculator.get_last_result_value() == "ZeroDivisionError"
