#!/usr/bin/python3

"""
A rectangle with width and height
Area and perimeter included
Printing a rectangle with #
__repr__ reconstructs a rectangle with eval
Detects instance deletion
number_of_instances counts number of instances
print_symbol for various print cases
Checks if one rectangle is larger
classmethod square returns a square
"""


class Rectangle:
    """
    Rectangle with width and length
    Area and perimeter included
    print() and str() returns a rectangle built from #
    __repr__ reconstruction with eval
    Detects instance deletion
    number_of_instances counts number of instances
    print_symbol for various print cases
    Checks if one rectangle is larger
    classmethod square returns a square
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        result = []
        for i in range(self.height):
            result.append(str(self.print_symbol) * self.width)
        return "\n".join(result)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        if Rectangle.number_of_instances < 0:
            Rectangle.number_of_instances = 0
        print("Bye rectangle...")

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

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, (Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, (Rectangle)):
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()

        if rect_1_area > rect_2_area:
            return rect_1
        if rect_2_area > rect_1_area:
            return rect_2
        if rect_1_area == rect_2_area:
            return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
