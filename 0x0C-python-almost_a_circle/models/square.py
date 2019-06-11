#!/usr/bin/python3
"""Class Square that inherits from class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes class Square"""

        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """Returns a dictionary representation of Square"""

        d = {"id": self.id, "size": self.width,
             "x": self.x, "y": self.y}

        return d

    def update(self, *args, **kwargs):
        """Updates multiples attributes as either args or dicts
        Args:
            *args: multiple arguments
            **kwargs: dictionary arguments
        """

        attrs = ["id", "size", "x", "y"]
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

    @property
    def size(self):
        """Returns size as a private attribute"""

        return self.width

    @size.setter
    def size(self, value):
        """Defines width and height of square
        Args:
            value: integer that represents width and height
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Overwrites the __str__ magic method"""

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
