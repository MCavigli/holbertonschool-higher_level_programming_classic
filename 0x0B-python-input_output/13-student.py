#!/usr/bin/python3
"""Module that holds class Student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""

        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if attr in self.__dict__.keys():
                my_dict[attr] = self.__dict__[attr]
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""

        old_dict = self.__dict__
        for attr in json.keys():
            for old_attr in old_dict.keys():
                if attr == old_attr:
                    old_dict[old_attr] = json[attr]
        return old_dict
