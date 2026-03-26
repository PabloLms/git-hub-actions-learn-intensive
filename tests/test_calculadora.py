import pytest
from calculator import calculator

def test_calculator():
    a = 1
    b = 2
    result=calculator(a,b)
    assert 8,result
