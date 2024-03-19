import pytest
from main.recursion.Factorial import factorial


def testFactorial():
    assert factorial(3) == 6
    assert factorial(4) == 24
    # factorial(30000000) # Maximum Depth Exceed Error
