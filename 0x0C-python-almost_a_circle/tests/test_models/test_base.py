#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Runs tests for base.py"""

    def setUp(self):
        """Sets up the testing environment"""

        Base._Base__nb_objects = 0

    def test_create(self):
        """Tests the creation of a Base class"""

        b = Base()
        print(b.id)
        self.assertTrue(b)

    def test_create_id(self):
        """Tests the creation of class Base with a specified id"""

        b = Base()
        b.id = 5
        self.assertEqual(b.id, 5)

    def test_id_inc(self):
        """Test to see if id is incrementing correctly"""

        b = Base()
        test = b.id
        b2 = Base()
        test2 = b2.id
        self.assertEqual(test, test2 - 1)

    def test_id_inc2(self):
        """More id incrementation tests"""

        b = Base()
        test = b.id
        b2 = Base(88)
        test2 = b2.id
        b3 = Base()
        test3 = b3.id
        self.assertEqual(test, test3 - 1)
        self.assertEqual(test2, 88)
