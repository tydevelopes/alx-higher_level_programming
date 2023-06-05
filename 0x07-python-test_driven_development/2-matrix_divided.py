#!/usr/bin/python3

"""Module defines a function"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div"""

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
