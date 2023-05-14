#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    first_arg_a = 0
    first_arg_b = 0
    second_arg_a = 0
    second_arg_b = 0

    if len(tuple_a) == 1:
        first_arg_a = tuple_a[0]
    elif len(tuple_a) > 1:
        first_arg_a = tuple_a[0]
        first_arg_b = tuple_a[1]

    if len(tuple_b) == 1:
        second_arg_a = tuple_b[0]
    elif len(tuple_b) > 1:
        second_arg_a = tuple_b[0]
        second_arg_b = tuple_b[1]

    return (first_arg_a + second_arg_a, first_arg_b + second_arg_b)


