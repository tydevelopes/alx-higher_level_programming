#!/usr/bin/python3

"""Module defines a function"""


def print_square(size):
    """prints square with #"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
