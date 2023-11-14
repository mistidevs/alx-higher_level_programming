import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_rectangles(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 90)

    def test_invalid_rectangles(self):
        with self.assertRaises(TypeError):
            r5 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, "2")
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            r8 = Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            r9 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r10 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r11 = Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            r12 = Rectangle(1, -1)
        with self.assertRaises(ValueError):
            r13 = Rectangle(1, 2, -1)
        with self.assertRaises(ValueError):
            r14 = Rectangle(1, 2, 3, -1)
