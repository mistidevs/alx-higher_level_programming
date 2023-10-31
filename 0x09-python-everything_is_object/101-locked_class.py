#!/usr/bin/python3

"""
Prevents creation of new instance attributes
unless first_name is called
"""


class LockedClass:
    """ A locked class that only accepts first name """
    __slots__ = ['first_name']
