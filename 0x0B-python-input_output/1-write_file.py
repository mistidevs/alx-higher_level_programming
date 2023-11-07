#!/usr/bin/python3
""" Writing to a file and returning number
of characters written """


def write_file(filename="", text=""):
    """ Using write to write content to a file. 
    no error handling. """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
