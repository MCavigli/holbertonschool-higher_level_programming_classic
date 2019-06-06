#!/usr/bin/python3
"""Module that contains a class MyList that inherits from list
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that prints the list but sorted
        """

        print(sorted(self))
