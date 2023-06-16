#!/usr/bin/python3

"""Module defines a base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json rep of list_dictionaries"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
