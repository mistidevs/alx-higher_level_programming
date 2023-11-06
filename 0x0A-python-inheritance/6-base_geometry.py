#!/usr/bin/python3
""" Base Geomotry with Exception for area function """


class BaseGeometry:
    """ Base Geometry with Exception for area function """
    def area(self):
        raise Exception("area() is not implemented")
