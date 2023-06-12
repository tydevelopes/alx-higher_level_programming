#!/usr/bin/python3

"""Module defines a class"""


class MyList(list):
    """Extends list class"""

    def __init__(self):
        """Initialises class instance"""

        super().__init__(self)

    def print_sorted(self):
        """Prints sorted list"""

        print(sorted(self))
