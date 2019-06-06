#!/usr/bin/python3
"""Module holds a function returning JSON string representation
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string.
    Args:
        my_str: The object
    """

    return (json.loads(my_str))
