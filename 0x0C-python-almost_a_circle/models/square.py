#!/usr/bin/python3
"Square class that inherits from Rectangle"
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square class inheriting from Rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        "Constructor class initialising Square"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "Returning a string representation of Square"
        return (f"[Square] ({self.id}) {self.x}/{self.y} - \
{self.width}")

    @property
    def size(self):
        "Return size of Square"
        return self.width

    @size.setter
    def size(self, value):
        "Set the size of Square"
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "Update the values of Square"
        if len(args) == 0:
            for key in kwargs:
                if key == 'x':
                    self.x = kwargs['x']
                if key == 'y':
                    self.y = kwargs['y']
                if key == 'id':
                    self.id = kwargs['id']
                if key == 'size':
                    self.size = kwargs['size']
        else:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

    def to_dictionary(self):
        "Returning Square as a dictionary"
        return {
            'id': self.id,
            'x': self.x,
            'size': self.width,
            'y': self.y
            }
