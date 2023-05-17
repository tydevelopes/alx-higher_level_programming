#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # list(map(lambda x : 89 if x == 2 else x, my_list))
    return [89 if x == 2 else x for x in my_list]
