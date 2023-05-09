#!/usr/bin/python3
def uppercase(str):
    i = 0
    ch = ""
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            ch = chr(ord(str[i] + 32))
        else:
            ch = str[i]
        print("{0}".format(ch), end="")
    print("")
