import pytest
from hslaupackage import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 5) == -5

def test_multiply():
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-2, 3) == -6

def test_divide():
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(9, 3) == 3
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calculator.divide(5, 0)

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1

def test_sqrt():
    assert calculator.sqrt(9) == 3
    assert calculator.sqrt(0) == 0
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calculator.sqrt(-4)

def test_factorial():
    assert calculator.factorial(0) == 1
    assert calculator.factorial(1) == 1
    assert calculator.factorial(5) == 120
    with pytest.raises(ValueError, match="Cannot take the factorial of a negative number."):
        calculator.factorial(-3)

def test_mod():
    assert calculator.mod(10, 3) == 1
    assert calculator.mod(20, 5) == 0