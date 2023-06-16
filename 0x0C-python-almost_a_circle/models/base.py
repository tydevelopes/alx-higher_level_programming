#!/usr/bin/python3

"""Module defines a base class"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Creates an instance of a base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
