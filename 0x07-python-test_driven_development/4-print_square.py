#!/usr/bin/python3
"""This module holds a function that prints a square
"""


def print_square(size):
    """Prints a square using the # character of a size of the size arg
    Args:
        size: The size of the square
    Return:
        Nothing
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("")
    for row in range(size):
        for col in range(size):
            print("#", end='')
        print("")
