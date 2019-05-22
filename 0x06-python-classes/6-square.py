#!/usr/bin/python3
"""defines a class called Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data
        Args:
            size: size of the square
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size"""

        return self.__size

    @property
    def position(self):
        """Retrieves the position"""

        return self.__position

    @size.setter
    def size(self, value):
        """Sets the size value
        Args:
            value: the size of the square
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @position.setter
    def position(self, value):
        """Sets the position value
        Args:
            value: the position
        """
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """prints out the square with the character # in stdout"""

        if self.__size == 0:
            print("")
            return

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()

        for i in range(self.__size):
            if self.__position[0] > 0:
                for i in range(self.__position[0]):
                    print(" ", end='')
            for j in range(self.__size):
                print("#", end='')
            print("")
