#!/usr/bin/python3

"""Module defines a function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for value in row:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    num_rows_in_a = len(m_a)
    num_cols_in_a = len(m_a[0])
    num_rows_in_b = len(m_b)
    num_cols_in_b = len(m_b[0])

    if num_cols_in_a != num_rows_in_b:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_result = [[0] * num_cols_in_b for _ in range(num_rows_in_a)]

    for i in range(num_rows_in_a):
        for j in range(num_cols_in_b):
            for k in range(num_cols_in_a):
                mul_result[i][j] += m_a[i][k] * m_b[k][j]

    return mul_result
