#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    args = len(sys.argv)
    argv = sys.argv
    ops = "+-*/"

    if args != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    if ops.find(argv[2]) == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == "+":
        print(f"{argv[1]} + {argv[3]} = {add(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "-":
        print(f"{argv[1]} - {argv[3]} = {sub(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "*":
        print(f"{argv[1]} * {argv[3]} = {mul(int(argv[1]), int(argv[3]))}")
    elif argv[2] == "/":
        print(f"{argv[1]} / {argv[3]} = {div(int(argv[1]), int(argv[3]))}")
