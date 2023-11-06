#!/usr/bin/python3
""" Inheriting from list type """


class MyList(list):
    """ Returning a list in sorted order """
    def print_sorted(self):
        print(sorted(self))
