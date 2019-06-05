#!/usr/bin/python3
""" Module that has a function to return a list of availble attributes and
methods
"""


def lookup(obj):
    """Function that returns the list of available attributes and methods of an
    object
    Args:
        obj - the object to check
    """

    return dir(obj)
