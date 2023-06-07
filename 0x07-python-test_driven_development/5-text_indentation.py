#!/usr/bin/python3

"""Module defines a function"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""

    new_str_list = (
        text.replace("?", "?\n\n").replace(":", ":\n\n").replace(".", ".\n\n")
    )

    print(new_str_list, end="")
