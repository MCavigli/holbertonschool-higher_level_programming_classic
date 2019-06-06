#!/usr/bin/python3
"""Module that holds a function that writes a file
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number
    of characters written.
    Args:
        filename: The file to write to
        text: The text to write to filename
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        char_count = f.write(text)

    return (char_count)
