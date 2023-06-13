#!/usr/bin/python3

"""Module defines a function"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a geometry class"""

    def __init__(self, width, height):
        """Initialises an instance"""

        BaseGeometry.integer_validator("width", width)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
