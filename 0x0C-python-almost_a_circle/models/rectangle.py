#!/usr/bin/python3
"""Class Rectangle that inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes class Rectangle"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Overrides the __str__ method so it returns something else"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                        self.__y, self.__width,
                                                        self.__height))

    def to_dictionary(self):
        """Returns a dictionary representation of Rectangle"""

        d = {"id": self.id, "width": self.__width, "height": self.__height,
             "x": self.__x, "y": self.__y}

        return d

    def update(self, *args, **kwargs):
        """Takes in multiple arguments and updates attributes
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """

        attrs = ["id", "width", "height", "x", "y"]
        for elem in range(len(args)):
            for attr in range(len(attrs)):
                if attr == elem:
                    setattr(self, attrs[attr], args[elem])
                    break

        if not args or len(args) == 0:
            for key, val in kwargs.items():
                for attr in range(len(attrs)):
                    if key == attrs[attr]:
                        setattr(self, attrs[attr], val)
                        break

    def area(self):
        """Returns the area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """Prints a representation of the rectangle with '#'"""

        for space in range(self.__y):
            print("")

        for row in range(self.__height):
            for move in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print("")

    @property
    def width(self):
        """Returns width as a private attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Defines the width
        Args:
            value: integer that represents the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height as a private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the height
        Args:
            value: integer that represents the height
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x as a private attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Defines the x
        Args:
            value: integer that represents the x
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y as a private attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Defines the y
        Args:
            value: integer that represents the y
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
