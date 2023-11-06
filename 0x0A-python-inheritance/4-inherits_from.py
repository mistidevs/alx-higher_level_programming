#!/usr/bin/python3
""" Checking the subclasses an object belongs to
Returns the parent classes inherited from
"""


def inherits_from(obj, a_class):
    """ Using isinstance and type combination """
    return isinstance(obj, a_class) and type(obj) is not a_class

if __name__ == '__main__':
    inherits_from()
