#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_dup = my_list[:]
    if idx >= 0 and idx < len(my_list_dup):
        my_list_dup[idx] = element
        return my_list_dup
    return my_list_dup
