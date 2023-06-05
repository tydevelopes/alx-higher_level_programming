#!/usr/bin/python3

"""Module defines a test class"""


import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_no_arg(self):
        """function call with no argument"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """function call with empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_int_list(self):
        """function call with empty list"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_ints_unsorted(self):
        """function call all integers"""
        self.assertEqual(max_integer([2, -4, 65, 0, -100]), 65)

    def test_all_ints_sorted(self):
        """function call all integers"""
        self.assertEqual(max_integer([-100, -4, 0, 2, 65]), 65)

    def test_not_all_ints(self):
        """function call with integers and strings"""
        self.assertRaises(TypeError, max_integer, [1, 4, "hey", -4])

    if __name__ == "__main__":
        unittest.main()
