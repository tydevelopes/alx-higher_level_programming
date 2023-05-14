#!/usr/bin/python3
def no_c(my_string):
    no_c_str = ""
    if not my_string:
        return
    for ch in my_string:
        if ch != "c" and ch != "C":
            no_c_str += ch
    return no_c_str
