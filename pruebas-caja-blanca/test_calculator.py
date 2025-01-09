from Calculator import Calculator
from TemperatureConverter import TemperatureConverter
import pytest

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator):
    assert calculator.add(3, 4) == 7

def test_subtract(calculator):
    assert calculator.subtract(10, 5) == 5

def test_multiply(calculator):
    assert calculator.multiply(3, 4) == 12

def test_divide(calculator):
    assert calculator.divide(10, 2) == 5

def test_divide_by_zero(calculator):
    with pytest.raises(ValueError) as error:
        calculator.divide(10, 0)
    assert str(error.value) == "Cannot divide by zero"