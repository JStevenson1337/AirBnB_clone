#!/usr/bin/python3
"""Unittest for city class"""
import unittest
import models
from genericpath import exists
from models.city import City
import pep8


class TestCityClass(unittest.TestCase):
    """class for testing city"""
    def setUp(self):
        self.city = City()

    def testInit(self):
        """tests the init method"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(City.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main
