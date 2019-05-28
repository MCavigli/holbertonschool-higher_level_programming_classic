#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the data for the rectangle
        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.width = width
        self.height = height

    def __str__(self):
        """Prints a string representation of a rectangle with #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ''
        for row in range(self.__height):
            for col in range(self.__width):
                rect += "#"
            if row == self.__height - 1:
                break
            else:
                rect += "\n"
        return rect

    def __repr__(self):
        """Returns the name of the class with attributes"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    @property
    def width(self):
        """Retrieves the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width of the rectangle
        Args:
            value: the integer that represents the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height of the rectangle
        Args:
            value: the integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimiter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
