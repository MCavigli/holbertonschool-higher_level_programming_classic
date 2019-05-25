#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Runs tests for 6-max_integer
    """

    def test_if_empty(self):
        """Checks to make sure a list is empty"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_unordered(self):
        """Checks an unordered list"""
        un_list = [1, 5, 2, 8, 3]
        self.assertEqual(max_integer(un_list), 8)

    def test_ordered(self):
        """Checks an ordered list"""
        o_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(o_list), 5)

    def test_neg_unordered(self):
        """Checks an unordered list of negatives"""
        nun_list = [-1, -5, -2, -8, -3]
        self.assertEqual(max_integer(nun_list), -1)

    def test_neg_ordered(self):
        """Checks an ordered list of negatives"""
        no_list = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(no_list), -1)

    def test_single(self):
        """Checks a list with a single element"""
        single = [5]
        self.assertEqual(max_integer(single), 5)

    def test_float_list(self):
        """Checks a list of floats"""
        f_list = [3.2, 5.6, 7.3, 9.9, 12.7]
        self.assertEqual(max_integer(f_list), 12.7)

    def test_float_int(self):
        """Checks a list of floats and ints"""
        f_and_i = [2.2, 1, 7.4, 8, 3.4]
        self.assertEqual(max_integer(f_and_i), 8)

    def test_string_list(self):
        """Checks a list of strings"""
        s_list = ["oh", "hello", "neato", "burrito"]
        self.assertRaises(TypeError, max_integer, "neato", s_list)

    def test_single_string(self):
        """Checks a single string"""
        single_string = ["burrito"]
        self.assertRaises(TypeError, max_integer, "t", single_string)

    def test_same(self):
        """Checks through a list of the same ints"""
        same_int = [22, 22, 22, 22]
        self.assertEqual(max_integer(same_int), 22)

    def test_mixed_types(self):
        """Checks to see if numbers are mixed with strings"""
        mixed = [1, 2, 3, "neat", 5]
        self.assertRaises(TypeError, max_integer, mixed)

if __name__ == '__main__':
    unittest.main()
