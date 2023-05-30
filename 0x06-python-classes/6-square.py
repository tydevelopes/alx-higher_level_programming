#!/usr/bin/python3
""" Module defines a square class """


class Square:
    """Defines a sqaure class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises class instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (
            isinstance(position, tuple)
            and len(position) == 2
            and isinstance(position[0], int)
            and isinstance(position[1], int)
            and position[0] >= 0
            and position[1] >= 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    @property
    def position(self):
        """Return position of square"""

        return self.__size

    @position.setter
    def position(self, value):
        """Set the value of position"""

        self.__init__(value)

    def my_print(self):
        """Prints square using #"""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
                print(self.__size * "#")
