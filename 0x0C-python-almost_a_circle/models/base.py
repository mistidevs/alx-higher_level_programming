#!/usr/bin/python3
"Base class that is a subclass of object"
import json


class Base:
    "Base class which other classes will inherit from"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(cls.__name__ + '.json', mode="w", encoding="utf-8") as f:
                  f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        f_name = cls.__name__ + '.json'
        try:
            with open(f_name, mode="r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dicti) for dicti in list_dicts]
        except FileNotFoundError:
            return []
