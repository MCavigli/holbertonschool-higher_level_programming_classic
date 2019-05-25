#!/usr/bin/python3

"""Module for 0-add_integer.It contains the function add_integer
which adds two integers and returns their sum
"""


def add_integer(a, b=98):
    """returns the sum of two integers
    Args:
        a = the first integer
        b = the second integer
    Return:
        The sum of a and b
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
