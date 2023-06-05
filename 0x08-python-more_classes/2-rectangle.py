#!/usr/bin/python3
""" Module defines a rectangle class """


class Rectangle:
    """Defines a rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialises class instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of rectangle instance"""

        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of rectangle instance"""

        return self.__width

    @height.setter
    def height(self, value):
        """set height of rectangle instance"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """return perimeter of rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
