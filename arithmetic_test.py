"""
Unit tests for the arithmetic library
"""

# import the code to be tested
from arithmetic import add

def describe_an_arithmetic_library():

  def it_can_add_two_numbers():
    """
    The add() function can add two numbers, a and b
    """
    assert add(3, 4) == 7
    assert add(5, 23) == 28
    assert add(-5, -7) == -12
    assert add(-5, 5) == 0
