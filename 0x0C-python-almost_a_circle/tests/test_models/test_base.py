import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)

    def test_to_json_string(self):
        list_dictionaries = [{'x': 2, 'width': 10, 'id': 1,
                              'height': 7, 'y': 8}]
        js_string = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        b3 = Base()
        json_string = b3.to_json_string(list_dictionaries)
        self.assertEqual(json_string, js_string)
        None_dict = None
        none_string = b3.to_json_string(None_dict)
        self.assertEqual(none_string, "[]")
        Empty_dict = []
        empty_string = b3.to_json_string(Empty_dict)
        self.assertEqual(empty_string, "[]")

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            json_string_r1 = file.read()

        js_string_r1 = '[{"x": 2, "y": 8, "id": 2, \
"height": 7, "width": 10}, {"x": 0, "y": 0, \
"id": 3, "height": 4, "width": 2}]'
        self.assertEqual(json_string_r1, js_string_r1)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            empty_string = file.read()

        empty_str = '[]'
        self.assertEqual(empty_string, empty_str)

    def test_from_json_string(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
    ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        None_string = None
        none_list = Rectangle.from_json_string(None_string)
        self.assertEqual(none_list, [])
        Empty_string = '[]'
        empty_list = Rectangle.from_json_string(Empty_string)
        self.assertEqual(empty_list, [])

    def test_create(self):
        r3 = Rectangle.create(**{'id': 501})
        r4 = Rectangle.create(**{'id': 502, 'width': 1})
        r5 = Rectangle.create(**{'id': 503, 'width': 1, 'height': 2})
        r6 = Rectangle.create(**{'id': 504, 'width': 1, 'height': 2, 'x': 3})
        r7 = Rectangle.create(**{'id': 505, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        s1 = Square.create(**{'id': 201})
        s2 = Square.create(**{'id': 202, 'size': 1})
        s3 = Square.create(**{'id': 204, 'size': 1, 'x': 3})
        s4 = Square.create(**{'id': 205, 'size': 1, 'x': 3, 'y': 4})
        
if __name__ == '__main__':
    unittest.main()
