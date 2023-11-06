#!/usr/bin/python3
""" Checking the classes an object belongs to
Returns the parent classes and the actual class
"""


def is_kind_of_class(obj, a_class):
    """ Using isinstance """
    if isinstance(obj, a_class):
        return True
    return False


if __name__ == '__main__':
    is_kind_of_class()
