#!/usr/bin/python3

"""Module defines a base class"""

import json
import csv


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

    @classmethod
    def save_to_file(cls, list_objs):
        """save json rep of list_objs to file"""

        filename = f"{cls.__name__}.json"

        if list_objs is None:
            json_str = ""
        else:
            ld = [o.to_dictionary() for o in list_objs if isinstance(o, Base)]

            json_str = cls.to_json_string(ld)

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """deserialize json string"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        # create dummy object
        obj = None
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3, 1, 1)
        elif cls.__name__ == "Square":
            obj = cls(2, 3, 1)

        obj.update(**dictionary)

        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = f"{cls.__name__}.json"

        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                obj_list = cls.from_json_string(f.read())
                return [cls.create(**obj) for obj in obj_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save csv rep of list_objs to file"""

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", encoding="utf-8", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """save csv rep of list_objs to file"""

        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
