#!/usr/bin/python3

"""Module defines a function"""

import json


def to_json_string(my_str):
    """deserialize json string"""

    return json.loads(my_str)
