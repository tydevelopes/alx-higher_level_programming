#!/usr/bin/python3

"""Module defines a function"""


def read_file(filename=""):
    """reads a text file"""

    with open(filename, mode="r", encoding="utf-8") as f:
        content = f.read()
        print(content)
