#!/usr/bin/python3
"""Module holds a function that reads lines and prints to stdout
"""

def read_lines(filename="", nb_lines=0):
    """Reads a specified number of lines and prints them to stdout
    Args:
        filename: the file to read
        nb_lines: the number of lines to read in filename
    """

    count = 0
    with open(filename) as f:
        for lines in f:
            count = count + 1

    if nb_lines <= 0:
        nb_lines = count
    if nb_lines > count:
        nb_lines = count

    i = 0
    with open(filename) as f:
        for lines in f:
            if i == nb_lines:
                break
            print(lines, end="")
            i = i + 1
