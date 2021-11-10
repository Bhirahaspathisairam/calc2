"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (4.0,2.0,2.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 16.0
