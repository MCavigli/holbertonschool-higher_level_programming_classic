#!/usr/bin/python3
"""Module that has an empty base class BaseGeometry and empty class function
"""


class BaseGeometry:
    """Class that defines a shape
    """

    pass

    def area(self):
        """Function that calculates the area of a shapre
        """

        raise Exception("area() is not implemented")
