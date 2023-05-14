#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    rev = my_list[:]
    rev.reverse()
    for item in rev:
        print("{:d}".format(item))
