#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = list(a_dictionary.keys())[0]
    max = a_dictionary[best_key]
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            best_key = key
    return best_key
