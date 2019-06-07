#!/usr/bin/python3
"""Module that holds a function to take in a class and return JSON
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.
    Args:
        obj: An instance of a class
    """

    return obj.__dict__
