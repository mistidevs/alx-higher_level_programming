#!/usr/bin/python3
"Base class that is a subclass of object"


class Base:
    "Base class which other classes will inherit from"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
