#!/usr/bin/python3
"""Module with a function that creates an Object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.
    Args:
        filename: The name of the file
    """

    with open(filename, encoding='utf-8') as f:
        for line in f:
            new_obj = json.loads(line)
    return new_obj
