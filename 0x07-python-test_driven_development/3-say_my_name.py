#!/usr/bin/python3
"""Contains a function that takes in two arguments and prints out a statement
"""


def say_my_name(first_name, last_name=""):
    """Combines both arguments and prints out a statement
    Args:
        first_name: the first string
        last_name: the second string
    Return:
        Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
