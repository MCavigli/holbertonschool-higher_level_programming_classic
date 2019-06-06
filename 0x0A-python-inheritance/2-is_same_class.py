#!/usr/bin/python3
"""This module holds a function that checks if an object is an instance
or a specified class
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified
    class; otherwise False
    Args:
        obj: the object to check
        a_class: The class to check against
    """

    return True if type(obj) is a_class else False
