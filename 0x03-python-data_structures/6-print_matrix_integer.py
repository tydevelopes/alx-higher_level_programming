#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_len = 0
    if not matrix:
        print()
    for row in matrix:
        row_len = len(row)
        for idx, col in enumerate(row):
            if idx != row_len - 1:
                print("{:d}".format(col), end=" ")
            else:
                print("{:d}".format(col), end="")
        print()
