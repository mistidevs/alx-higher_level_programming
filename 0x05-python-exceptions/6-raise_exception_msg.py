#!/usr/bin/python3

def raise_exception_msg(message=""):
    print(message, end="")
    raise NameError


if __name__ == '__main__':
    raise_exception_msg()
