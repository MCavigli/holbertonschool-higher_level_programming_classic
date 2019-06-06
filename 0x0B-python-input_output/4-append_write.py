#!/usr/bin/python3
"""Module holds function that appends to a file
"""


def append_write(filename="", text=""):
    """Function appends text to a file and returns the number of characters
    added.
    Args:
        filename: The filename to append to
        text: The text to append to filename
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        char_count = f.write(text)

    return char_count
