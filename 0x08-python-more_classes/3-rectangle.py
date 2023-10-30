#!/usr/bin/python3

"""
A rectangle with width and height
Area and perimeter included
Printing a rectangle with #
"""


class Rectangle:
    """
    Rectangle with width and length
    Area and perimeter included
    print() and str() returns a rectangle built from #
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        result = []
        for i in range(self.height):
            result.append("#" * self.width)
        return "\n".join(result)

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
