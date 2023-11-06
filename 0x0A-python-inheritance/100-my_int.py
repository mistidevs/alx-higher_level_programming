#!/usr/bin/python3
""" Rebel int class with == and != inverted """


class MyInt(int):
    """ Rebel class inverting equality operators """
    def __eq__(self, other):
        if True:
            return False
        return True

    def __ne__(self, other):
        if MyInt.__eq__ is True:
            return False
        return True
