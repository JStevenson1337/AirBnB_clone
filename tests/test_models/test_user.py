#!/usr/bin/python3
"""Unittest for user class"""
import unittest
import models
from genericpath import exists
from models.user import User
import pep8


class TestUserClass(unittest.TestCase):
    """class for testing user"""
    def setUp(self):
        self.user = User()

    def testInit(self):
        """tests the init method"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(User.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main
