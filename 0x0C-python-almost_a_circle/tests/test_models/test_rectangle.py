import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_rectangles(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)

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

    def test_area(self):
        r15 = Rectangle(3, 5)
        self.assertEqual(r15.area(), 15)

    def test_display(self):
        r16 = Rectangle(2, 2)
        buf = io.StringIO()
        sys.stdout = buf
        r16.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), '##\n##\n')

    def test_display_x(self):
        r17 = Rectangle(3, 2, 1)
        buf = io.StringIO()
        sys.stdout = buf
        r17.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), ' ###\n ###\n')

    def test_display_x_y(self):
        r18 = Rectangle(2, 3, 2, 2)
        buf = io.StringIO()
        sys.stdout = buf
        r18.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), '\n\n  ##\n  ##\n  ##\n')

    def test_str(self):
        r19 = Rectangle(4, 6, 2, 1, 12)
        rect_string = '[Rectangle] (12) 2/1 - 4/6\n'
        buf = io.StringIO()
        sys.stdout = buf
        print(r19)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), rect_string)
