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
        
