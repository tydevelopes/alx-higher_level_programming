#!/usr/bin/python3

"""Module defines a function"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialises a square instance"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of square"""

        n = self.__class__.__name__
        i = self.id
        x = self.x
        y = self.y
        s = self.width

        return f"[{n}] ({i}) {x}/{y} - {s}"

    @property
    def size(self):
        """Returns size of a rectangle instance"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets size's value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates a square object"""

        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                return
        else:
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("size") is not None:
                self.width = kwargs.get("size")
                self.height = kwargs.get("size")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """returns dict rep of Square"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
