#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = (number * -1) % 10
    else:
        ld = number % 10
    print("{0}".format(ld), end="")

    return ld
