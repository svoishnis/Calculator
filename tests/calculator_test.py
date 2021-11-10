"""Testing the calc"""
from calc.calculator import Calculator




def test_calculator_result():
    """testing calc result is 0"""
    calc = Calculator()
    assert calc.result == 0


def test_calculator_add():
    """Testing the Add function of the calc"""
    assert Calculator.result == 0


def test_calculator_get_result():
    """Testing the Get result method of the calc"""
    calc = Calculator()

    assert calc.get_result() == 0


def test_calculator_subtract():
    """Testing the subtract method of the calc"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1


def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator()
    result = calc.multiply_numbers(1, 2)
    assert result == 2
