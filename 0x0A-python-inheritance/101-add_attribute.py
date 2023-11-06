#!/usr/bin/python3
""" Adds a new attribute if possible """


def add_attribute(obj, name, value):
    """ Adding an attribute if possible """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)

    else:
        raise TypeError("can't add new attribute")


if __name__ == "__main__":
    add_attribute()
