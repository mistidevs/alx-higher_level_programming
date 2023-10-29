#!/usr/bin/python3

"""
Module that prints a square
"""

def print_square(size):
    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    if size is None:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
            if j == size - 1:
                print()
