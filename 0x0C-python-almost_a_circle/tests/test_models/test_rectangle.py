#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Runs tests for rectangle.py"""

    @classmethod
    def setUpClass(cls):
        """Sets up the testing environment"""

        Base = _Base__nb_objects = 0
        cls.r1 = Rectangle(2, 3)
        cls.r2 = Rectangle(5, 5)
        cls.r3 = Rectangle(4, 5, 1)
        cls.r4 = Rectangle(6, 7, 1, 2, 98)
        cls.r5 = Rectangle(2, 5, 3, 4)

    """
    def test_2_0_id(self):


        self.assertEqual(self.r1.id, 3)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 3)
        self.assertEqual(self.r4.id, 98)
        self.assertEqual(self.r5.id, 4)
    """

    def test_2_1_width(self):
        """Tests when integers are added for width"""

        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r2.width, 5)
        self.assertEqual(self.r3.width, 4)
        self.assertEqual(self.r4.width, 6)
        self.assertEqual(self.r5.width, 2)

    def test_2_2_height(self):
        """Tests when integers are added for width"""

        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r2.height, 5)
        self.assertEqual(self.r3.height, 5)
        self.assertEqual(self.r4.height, 7)
        self.assertEqual(self.r5.height, 5)

    def test_2_3_x(self):
        """Tests when integers are added for x"""

        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 1)
        self.assertEqual(self.r4.x, 1)
        self.assertEqual(self.r5.x, 3)

    def test_2_4_y(self):
        """Tests when integers are added for y"""

        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r4.y, 2)
        self.assertEqual(self.r5.y, 4)

    def test_3_0_width_error(self):
        """Tests for errors with width"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(2.2, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([2, 1], 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({"hi": 3}, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((3, 2), 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, 1)

    def test_3_1_height_error(self):
        """Tests for errors with height"""

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, 2.2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [2, 1])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (3, 2))
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)

    def test_3_2_x_error(self):
        """Tests for errors with x"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, (3, 2))
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -2)

    def test_3_3_y_error(self):
        """Tests for errors with y"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, 2.2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, [2, 1])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, {"hi": 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, (3, 2))
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -2)

    def test_4_0_area(self):
        """Tests the area method"""

        self.assertEqual(Rectangle.area(self.r1), 6)
        self.assertEqual(Rectangle.area(self.r2), 25)
        self.assertEqual(Rectangle.area(self.r3), 20)
        self.assertEqual(Rectangle.area(self.r4), 42)
        self.assertEqual(Rectangle.area(self.r5), 10)

    def test_5_0_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r1.display()
        s = f.getvalue()
        self.assertEqual(s, "##\n##\n##\n")

    def test_5_1_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r2.display()
        s = f.getvalue()
        self.assertEqual(s, "#####\n#####\n#####\n#####\n#####\n")

    def test_6_0_str(self):
        """Tests the __str__ method"""

        self.assertEqual(Rectangle.__str__
                         (self.r1), "[Rectangle] (3) 0/0 - 2/3")
        self.assertEqual(Rectangle.__str__
                         (self.r2), "[Rectangle] (4) 0/0 - 5/5")
        self.assertEqual(Rectangle.__str__
                         (self.r3), "[Rectangle] (5) 1/0 - 4/5")
        self.assertEqual(Rectangle.__str__
                         (self.r4), "[Rectangle] (98) 1/2 - 6/7")
        self.assertEqual(Rectangle.__str__
                         (self.r5), "[Rectangle] (6) 3/4 - 2/5")

    def test_7_0_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r3.display()
        s = f.getvalue()
        self.assertEqual(s, " ####\n ####\n ####\n ####\n ####\n")

    def test_7_1_display(self):
        """Tests the display method"""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            self.r5.display()
        s = f.getvalue()
        self.assertEqual(s, "\n\n\n\n   ##\n   ##\n   ##\n   ##\n   ##\n")

    def test_8_0_update_args(self):
        """Tests the update function for *args"""

        r = Rectangle(4, 3, 1, 2, 98)
        r.update(22, 3, 4, 2, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 22)
