#!/usr/bin/python3
"""Unittest for amenity class"""
import unittest
import models
from genericpath import exists
from models.amenity import Amenity
import pep8


class TestAmenityClass(unittest.TestCase):
    """class for testing amenity"""
    def setUp(self):
        self.amenity = Amenity()

    def testInit(self):
        """tests the init method"""
        self.assertEqual(self.amenity.name, "")

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(Amenity.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main
