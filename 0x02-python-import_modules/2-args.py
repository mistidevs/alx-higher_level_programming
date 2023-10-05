#!/usr/bin/python3
from sys import argv

len = len(argv) - 1


def print_args():
    if len != 1:
        print("{} arguments".format(len), end="")
    else:
        print("1 argument", end="")
    if len == 0:
        print(".")
    else:
        print(":")
        for i in range(1, len + 1):
            print("{}: {}".format(i, argv[i]))


if __name__ == '__main__':
    print_args()
