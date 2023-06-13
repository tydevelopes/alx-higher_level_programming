#!/usr/bin/python3

"""Module defines a function"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Initialises an instance"""

        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """a dictionary representation of a Student instance"""

        return self.__dict__
