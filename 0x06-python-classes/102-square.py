#!/usr/bin/python3
""" Module defines a square class """


class Square:
    """Defines a sqaure class"""

    def __init__(self, size=0):
        """Initialises class instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square"""

        return self.__size * self.__size

    @property
    def size(self):
        """Return size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the value of size"""

        self.__init__(value)

    def __eq__(self, other):
        """compare two square areas with =="""

        return self.area() == other.area()

    def __ne__(self, other):
        """compare two square areas with !="""

        return self.area() != other.area()

    def __gt__(self, other):
        """compare two square areas with >"""

        return self.area() > other.area()

    def __ge__(self, other):
        """compare two square areas with >="""

        return self.area() >= other.area()

    def __lt__(self, other):
        """compare two square areas with <"""

        return self.area() < other.area()

    def __le__(self, other):
        """compare two square areas with <="""

        return self.area() <= other.area()
