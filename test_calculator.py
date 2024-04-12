from calculator import addition
from calculator import soustraction
from calculator import division



def test_addition():
    assert addition(1, 2) == 3

def test_soustraction():
    assert soustraction(2, 2) == 0

def test_division():
    assert division(5, 5) == 1



