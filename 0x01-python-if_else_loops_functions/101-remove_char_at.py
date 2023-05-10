#!/usr/bin/python3
def remove_char_at(str, n):
    str_dup = ""
    i = 0
    length = len(str)

    if n >= length or n < 0:
        return str
    while i < length:
        if i != n:
            str_dup += str[i]
        i += 1
    return str_dup
