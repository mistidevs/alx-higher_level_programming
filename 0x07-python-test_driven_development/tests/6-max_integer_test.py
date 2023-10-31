#!/usr/bin/python3

"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Defining all test cases """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertIsNone(max_integer([]))


if __name__ == '__main__':
    unittest.main()
