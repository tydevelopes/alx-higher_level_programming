#!/usr/bin/python3

"""Module defines a function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""

    new_str_list = text.replace("?", ".").replace(":", ".").split(".")

    length = len(new_str_list)
    for index, string in enumerate(new_str_list):
        if index != length - 1:
            print(string.strip())
            print()
        else:
            print(string.strip(), end="")
