#!/usr/bin/python3

"""Module defines a function"""

from models.base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialises a rectangle instance"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns width of a rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets width's value"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return height of rectangle instance"""

        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle instance"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return x of rectangle instance"""

        return self.__x

    @x.setter
    def x(self, value):
        """set x of rectangle instance"""

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return y of rectangle instance"""

        return self.__y

    @y.setter
    def y(self, value):
        """set y of rectangle instance"""

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height

    def display(self):
        """string representation of rectangle"""

        # print position
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(self.__x * " ", end="")
            print(f"{self.__width * '#'}")

    def __str__(self):
        """string representation of rectangle"""

        n = self.__class__.__name__
        i = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height

        return f"[{n}] ({i}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """Updates a rectangle object"""

        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                return
        else:
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("width") is not None:
                self.width = kwargs.get("width")
            if kwargs.get("height") is not None:
                self.height = kwargs.get("height")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """returns dict rep of Rectangle"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
