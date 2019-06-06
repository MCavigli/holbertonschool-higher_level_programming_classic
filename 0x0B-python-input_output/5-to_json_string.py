#!/usr/bin/python3
"""Module holds a function that returns JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object (string)
    Args:
        my_obj: object to return as JSON representation
    """

    return (json.dumps(my_obj))
