#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    exist = False
    for x in list(a_dictionary.values()):
        if x == value:
            exist = True
    if not exist:
        return a_dictionary
    pairs = list(a_dictionary.items())
    for key, val in pairs:
        if val == value:
            del a_dictionary[key]
    return a_dictionary
