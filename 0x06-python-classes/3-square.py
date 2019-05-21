#!/usr/bin/python3
"""defines a class called Square"""


class Square:

    """Represents a square"""

    def __init__(self, size=0):

        """Initializes the data
        Args:
            size: size of the square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):

        """Returns the current square area"""

        return (self.__size * self.__size)
