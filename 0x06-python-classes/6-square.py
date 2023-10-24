#!/usr/bin/python3

""" Define a class Square"""""


class Square:
    """ Holds the size of a square with error handling
        Uses getters and setters
        Prints the size ofthe square using hash"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 \
           or type(value[0]) is not int or type(value[1]) is not int \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of two postive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for k in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
