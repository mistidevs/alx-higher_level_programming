#!/usr/bin/python3
""" Function that checks the type of an instance """


def is_same_class(obj, a_class):
    """ Using type """
    if type(obj) is a_class:
        return True
    return False


if __name__ == '__main__':
    is_same_class()
