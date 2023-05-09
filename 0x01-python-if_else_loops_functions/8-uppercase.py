#!/usr/bin/python3
def uppercase(str):
    i = 0
    ch = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            ch = chr(ord(i) - 32)
        else:
            ch = i
        print(f"{ch}", end="")
    print()
