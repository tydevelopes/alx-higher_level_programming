#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = len(sys.argv) - 1

    print(f"{args} {'argument' if args == 1 else 'arguments'}", end="")
    print(f"{'.' if args == 0 else ':'}")

    for index, value in enumerate(sys.argv):
        if index == 0:
            continue
        print(f"{index}: {value}")
