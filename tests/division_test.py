"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (1.0,2.0)
    divsion = Division(mynumbers)
    #Act
    #Assert
    assert divsion.get_result() == 0.5