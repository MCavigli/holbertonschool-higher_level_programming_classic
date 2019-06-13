#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Runs tests for square.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.s1 = Square(5)
        cls.s2 = Square(7)
        cls.s3 = Square(2, 2)
        cls.s4 = Square(3, 1, 2)

    def test_10_00_create(self):
        """Checks to see if the creation of a square was successful"""

        self.assertTrue(self.s1)
        self.assertTrue(self.s2)
        self.assertTrue(self.s3)
        self.assertTrue(self.s4)

    def test_10_01_subclass(self):
        """Checks if Square is a subclass of Rectangle and Base"""

        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_10_02_check_attrs(self):
        """Check if the attributes of Square are set appropriately"""

        self.assertEqual(self.s4.width, 3)
        self.assertEqual(self.s4.height, 3)
        self.assertEqual(self.s4.x, 1)
        self.assertEqual(self.s4.y, 2)

    def test_10_03_area(self):
        """Makes sure the area method works"""

        self.assertEqual(self.s1.area(), 25)
        self.assertEqual(self.s2.area(), 49)
        self.assertEqual(self.s3.area(), 4)
        self.assertEqual(self.s4.area(), 9)

    def test_10_04_display(self):
        """Makes sure the display method works"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.s4.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n ###\n ###\n ###\n")

    def test_10_05_str(self):
        """Tests the __str__ method"""

        self.assertEqual(Square.__str__
                         (self.s1), "[Square] (11) 0/0 - 5")
        self.assertEqual(Square.__str__
                         (self.s2), "[Square] (12) 0/0 - 7")
        self.assertEqual(Square.__str__
                         (self.s3), "[Square] (13) 2/0 - 2")
        self.assertEqual(Square.__str__
                         (self.s4), "[Square] (14) 1/2 - 3")

    def test_10_06_dict(self):
        """Checks the dictionary method"""

        dict1 = self.s1.to_dictionary()
        self.assertDictEqual(dict1, {'size': 5, 'id': 11, 'x': 0, 'y': 0})
        dict2 = self.s2.to_dictionary()
        self.assertDictEqual(dict2, {'size': 7, 'id': 12, 'x': 0, 'y': 0})
        dict3 = self.s3.to_dictionary()
        self.assertDictEqual(dict3, {'size': 2, 'id': 13, 'x': 2, 'y': 0})
        dict4 = self.s4.to_dictionary()
        self.assertDictEqual(dict4, {'size': 3, 'id': 14, 'x': 1, 'y': 2})

    def test_10_07_x_check(self):
        """Checks x"""

        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 0)
        self.assertEqual(self.s3.x, 2)
        self.assertEqual(self.s4.x, 1)

    def test_10_08_y_check(self):
        """Checks y"""

        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 0)
        self.assertEqual(self.s4.y, 2)

    def test_10_09_id_check(self):
        """Check id"""

        self.assertEqual(self.s1.id, 11)
        self.assertEqual(self.s2.id, 12)
        self.assertEqual(self.s3.id, 13)
        self.assertEqual(self.s4.id, 14)

    def test_10_10_x_error(self):
        """Tests for errors with x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, 2.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, [2, 1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hi")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, (3, 2))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -2)
        with self.assertRaises(TypeError):
            s = Square(1, None)
        with self.assertRaises(TypeError):
            s = Square(1, float('inf'))

    def test_10_11_y_error(self):
        """Tests for errors with y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hi")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, (3, 2))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -2)
        with self.assertRaises(TypeError):
            s = Square(1, 1, None)
        with self.assertRaises(TypeError):
            s = Square(1, 1, float('inf'))

    def test_11_00_size_check(self):
        """Checks to make sure size method works"""

        s = Square(12)
        self.assertEqual(s.size, 12)
        s.size = 4
        self.assertEqual(s.size, 4)

    def test_11_01_size_error(self):
        """Tests for errors with size"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(2.2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([2, 1])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square({"hi": 3})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square((3, 2))
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-2)
        with self.assertRaises(TypeError):
            s = Square(None)
        with self.assertRaises(TypeError):
            s = Square(float('inf'))

    def test_11_02_size(self):
        """Checks the size method"""

        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 7)
        self.assertEqual(self.s3.size, 2)
        self.assertEqual(self.s4.size, 3)

    def test_12_0_update_args(self):
        """Tests the update function for *args"""

        s = Square(4, 3, 1, 98)
        s.update(22, 3, 4, 2)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 22)

    def test_12_1_update_args_with_kwargs(self):
        """Tests functionality when **kwargs are present"""

        s = Square(4, 3, 1, 98)
        s.update(22, 3, 4, 2, size=15, x=27)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 22)

    def test_12_2_update_kwargs(self):
        """Tests the update function for **kwargs"""

        s = Square(4, 3, 1, 98)
        s.update(size=15, y=20, x=12, id=8)
        self.assertEqual(s.width, 15)
        self.assertEqual(s.height, 15)
        self.assertEqual(s.x, 12)
        self.assertEqual(s.y, 20)

    def test_14_0_checks_toDictionary(self):
        """Checks the to_dictionary method works for Square"""

        s1_dict = self.s1.to_dictionary()
        self.assertTrue(type(s1_dict), dict)
        s = Square(1)
        self.assertEqual(Square.__str__
                         (s), "[Square] (16) 0/0 - 1")
        s.update(**s1_dict)
        self.assertEqual(Square.__str__
                         (s), "[Square] (11) 0/0 - 5")

    @classmethod
    def tearDownClass(cls):
        """Breaks down the testing environment"""

        pass
