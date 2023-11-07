#!/usr/bin/python3
""" Return dict version of serializable object """


def class_to_json(obj):
    """ Using var to the effect """
    return vars(obj)


if __name__ == '__main__':
    class_to_json()
