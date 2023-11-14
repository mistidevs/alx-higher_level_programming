import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_valid_squares(self):
        s1 = Square(2)
        s2 = Square(2, 7)
        s3 = Square(3, 7, 8)
        s4 = Square(3, 7, 8, 9)
        self.assertEqual(s4.id, 9)

    def test_invalid_squares(self):
        with self.assertRaises(TypeError):
            s5 = Square("2")
        with self.assertRaises(ValueError):
            s6 = Square(0)
        with self.assertRaises(ValueError):
            s7 = Square(-1)
        with self.assertRaises(TypeError):
            s8 = Square(4, "5")
        with self.assertRaises(ValueError):
            s9 = Square(4, -1)
        with self.assertRaises(TypeError):
            s10 = Square(4, 5, "8")
        with self.assertRaises(ValueError):
            s11 = Square(4, 5, -2)
        
    def test_area(self):
        s12 = Square(3)
        self.assertEqual(s12.area(), 9)

    def test_display(self):
        s13 = Square(2)
        buf = io.StringIO()
        sys.stdout = buf
        s13.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), '##\n##\n')

    def test_display_x(self):
        s14 = Square(2, 2)
        buf = io.StringIO()
        sys.stdout = buf
        s14.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), '  ##\n  ##\n')

    def test_display_x_y(self):
        s15 = Square(3, 1, 3)
        buf = io.StringIO()
        sys.stdout = buf
        s15.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), '\n\n\n ###\n ###\n ###\n')

    def test_str(self):
        s16 = Square(3, 1, 3, 20)
        square_string = '[Square] (20) 1/3 - 3\n'
        buf = io.StringIO()
        sys.stdout = buf
        print(s16)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(), square_string)
