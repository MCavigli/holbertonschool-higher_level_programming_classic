#!/usr/bin/python3
"""Module holds a function that prints the number of lines
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file
    Args:
        filename: the file to read
    """

    counter = 0

    with open(filename) as f:
        for line in f:
            counter = counter + 1
    return counter
