#!/usr/bin/python3
""" Rectangle class derived from the BaseGeometry class """


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """ Square sub class of Rectangle """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return (f"[Rectangle] {self.__size}/{self.__size}")
