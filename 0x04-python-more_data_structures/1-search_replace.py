#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # list(map(lambda x : replace if x == search else x, my_list))
    return [replace if x == search else x for x in my_list]
