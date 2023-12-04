#!/usr/bin/python3
"Class rectangle that inherits from Base"
from models.base import Base


class Rectangle(Base):
    "Rectangle class inheriting from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        "Constructor initialiser"
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        "String function that returns Rectangle"
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    @property
    def width(self):
        "Return the width of self"
        return self.__width

    @width.setter
    def width(self, value):
        "Sets the value of width"
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "Return the height of self"
        return self.__height

    @height.setter
    def height(self, value):
        "Set the height of self"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        "Return the value of x"
        return self.__x

    @x.setter
    def x(self, value):
        "Set the value of x"
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        "Return the value of y"
        return self.__y

    @y.setter
    def y(self, value):
        "Set the value of y"
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        "Return the area of the Rectangle"
        return self.__width * self.__height

    def display(self):
        "Display Rectangle using #"
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        "Updating the variables in Rectangle"
        if len(args) == 0:
            for key in kwargs:
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']
                if key == 'id':
                    super().__init__(kwargs['id'])
                if key == 'width':
                    self.width = kwargs['width']
                if key == 'height':
                    self.height = kwargs['height']
        else:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

    def to_dictionary(self):
        "Returning Rectangle in dictionary form"
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
