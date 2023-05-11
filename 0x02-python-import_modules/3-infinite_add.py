#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv)
    sum = 0

    if args == 1:
        sum = 0

    for value in sys.argv[1:]:
        sum += int(value)
    print(sum)
