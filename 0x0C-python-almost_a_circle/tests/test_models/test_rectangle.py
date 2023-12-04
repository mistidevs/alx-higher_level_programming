import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_valid_rectangles(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r4.id, 5)

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

    def test_update_args(self):
        r20 = Rectangle(10, 10, 10, 10)
        buf = io.StringIO()
        sys.stdout = buf
        r20.update()
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (29) 10/10 - 10/10\n')
        buf = io.StringIO()
        sys.stdout = buf
        r20.update(89)
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 10/10 - 10/10\n')
        buf = io.StringIO()
        sys.stdout = buf
        r20.update(89, 2)
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 10/10 - 2/10\n')
        buf = io.StringIO()
        sys.stdout = buf
        r20.update(89, 2, 3)
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 10/10 - 2/3\n')
        buf = io.StringIO()
        sys.stdout = buf
        r20.update(89, 2, 3, 4)
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 4/10 - 2/3\n')
        buf = io.StringIO()
        sys.stdout = buf
        r20.update(89, 2, 3, 4, 5)
        print(r20)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 4/5 - 2/3\n')

    def test_update_kwargs(self):
        r21 = Rectangle(10, 10, 10, 10)
        buf = io.StringIO()
        sys.stdout = buf
        r21.update(height=1)
        print(r21)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (30) 10/10 - 10/1\n')
        buf = io.StringIO()
        sys.stdout = buf
        r21.update(width=1, x=2)
        print(r21)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (30) 2/10 - 1/1\n')
        buf = io.StringIO()
        sys.stdout = buf
        r21.update(y=1, width=2, x=3, id=89)
        print(r21)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 3/1 - 2/1\n')
        buf = io.StringIO()
        sys.stdout = buf
        r21.update(x=1, height=2, y=3, width=4)
        print(r21)
        sys.stdout = sys.__stdout__
        self.assertEqual(buf.getvalue(),
                         '[Rectangle] (89) 1/3 - 4/2\n')

    def test_to_dictionary(self):
        r22 = Rectangle(10, 2, 1, 9)
        rect_dict = {'x': 1, 'y': 9, 'id': 28, 'height': 2, 'width': 10}
        self.assertEqual(r22.to_dictionary(), rect_dict)
