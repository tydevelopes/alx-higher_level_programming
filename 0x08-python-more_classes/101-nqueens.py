#!/usr/bin/python3
"""Module defines a function"""

if __name__ == "__main__":
    import sys

    args = len(sys.argv)

    if args != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if num < 4:
        print("N must be at least 4")
        exit(1)

        print([0, 1])
