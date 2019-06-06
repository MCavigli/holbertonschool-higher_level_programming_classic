#!/usr/bin/python3
"""Module with function that writes object to text file
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation
    Args:
        my_obj: The object
        filename: File to save my_obj to
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
