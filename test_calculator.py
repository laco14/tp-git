from calculator import addition
from calculator import soustraction, division


def test_addition():
    assert addition(1, 2) == 3

def test_soustraction():
    assert soustraction(4, 2) == 2
    
def test_soustraction_variant():
    """Test another case for the soustraction function."""
    assert soustraction(6, 2) == 4

def test_division():
    assert division(10, 2) == 5
    assert division(10, 0) == "Cannot divide by zero"
    
