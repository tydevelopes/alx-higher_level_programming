#!/usr/bin/python3

"""Module defines a function"""

import sys

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
args = []

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        args.append(sys.argv[i])

content = load_from_json_file(filename)
new_content = content + args

save_to_json_file(new_content, filename)
