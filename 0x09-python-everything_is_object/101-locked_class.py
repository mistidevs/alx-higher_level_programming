#!/usr/bin/python3

"""
Prevents creation of new instance attributes
unless first_name is called
"""


class LockedClass:
    __slots__ = ['first_name']
