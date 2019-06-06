#!/usr/bin/python3
"""Module contains a class that inherits from 'int'
"""


class MyInt(int):
    """Subclass that inherits from int but reverses == and !=
    """

    def __init__(self, num):
        """Initializes MyInt
        Args:
            num: int that's passed through
        """

        self.num = num

    def __eq__(self, value):
        """Changes == to !=
        """

        if not isinstance(value, MyInt):
            return False

    def __ne__(self, value):
        """Changes != to ==
        """

        if not isinstance(value, MyInt):
            return True
