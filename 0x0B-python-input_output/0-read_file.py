#!/usr/bin/python3
""" Reading a file and printing to stdout """


def read_file(filename=""):
    """ Opening a file to read. No error handling. """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == '__main__':
    read_file()
