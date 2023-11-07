#!/usr/bin/python3
""" Appending to a file """


def append_write(filename="", text=""):
    """ Appending to a file with write """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
