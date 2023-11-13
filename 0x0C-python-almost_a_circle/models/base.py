#!/usr/bin/python3
"Base class that is a subclass of object"
import json
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        f_name = cls.__name__ + '.csv'
        with open(f_name, mode="w", newline="",
                  encoding="utf-8") as cs_file:
            if list_objs is not None:
                writer = csv.writer(cs_file)
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.width, obj.height,
                                         obj.x, obj.y])
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        writer.writerow([obj.id, obj.size,
                                         obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        f_name = cls.__name__ + '.csv'
        try:
            with open(f_name, mode="r", encoding="utf-8") as cs_file:
                reader = csv.reader(cs_file)
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {"id": int(row[0]), "width": int(row[1]),
                                      "height": int(row[2]), "x": int(row[3]),
                                      "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {"id": int(row[0]), "size": int(row[1]),
                                      "x": int(row[2]), "y": int(row[3])}
                    list_objs.append(cls.create(**dictionary))
                return list_objs
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        window = turtle.Screen()
        window.bgcolor("white")
        t = turtle.Turtle()

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("blue")
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("green")
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        window.exitonclick()
