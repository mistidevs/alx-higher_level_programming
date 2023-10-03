#!/usr/bin/python3
def uppercase(str):
    for w in str:
        if ord(w) in range(97, 123):
            w = chr(ord(w) - 32)
        print("{}".format(w), end="")
    print("", end="\n")
