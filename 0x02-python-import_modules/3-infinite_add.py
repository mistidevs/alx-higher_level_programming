#!/usr/bin/python3
from sys import argv

len = len(argv) - 1

def add_infinite():
    result = 0
    for i in range(1, len + 1):
        result += int(argv[i])
    print("{:d}".format(result))

if __name__ == '__main__':
    add_infinite()
