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

    def test_update_args(self):
        s17 = Square(5)
        buf = io.StringIO()
        sys.stdout = buf
        s17.update()
        print(s17)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (37) 0/0 - 5\n')
        buf = io.StringIO()
        sys.stdout = buf
        s17.update(10)
        print(s17)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (10) 0/0 - 5\n')
        buf = io.StringIO()
        sys.stdout = buf
        s17.update(1, 2)
        print(s17)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (1) 0/0 - 2\n')
        buf = io.StringIO()
        sys.stdout = buf
        s17.update(1, 2, 3)
        print(s17)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (1) 3/0 - 2\n')
        buf = io.StringIO()
        sys.stdout = buf
        s17.update(1, 2, 3, 4)
        print(s17)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (1) 3/4 - 2\n')

    def test_update_kwargs(self):
        s18 = Square(1, 2, 3, 4)
        buf = io.StringIO()
        sys.stdout = buf
        s18.update(x=12)
        print(s18)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (4) 12/3 - 1\n')
        buf = io.StringIO()
        sys.stdout = buf
        s18.update(size=7, y=1)
        print(s18)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (4) 12/1 - 7\n')
        buf = io.StringIO()
        sys.stdout = buf
        s18.update(y=1, size=7, id=89)
        print(s18)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Square] (89) 12/1 - 7\n')
        
    def test_to_dictionary(self):
        s19 = Square(10, 2, 1)
        square_dict = {'id': 36, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s19.to_dictionary(), square_dict)
