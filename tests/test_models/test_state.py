#!/usr/bin/python3
"""Unittest for state class"""
import unittest
import models
from genericpath import exists
from models.state import State
import pep8


class TestStateClass(unittest.TestCase):
    """class for testing state class"""
    def test_setup(self):
        """sets state to state"""
        self.state = State()

    def test_init(self):
        """tests init method"""
        self.assertEqual(self.state.name, "")

    def test_pep8(self):
        """
        Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings).")

    def test_documentation(self):
        """
        tests for module, class, & method documentation.
        """
        # Class docstring
        self.assertTrue(len(State.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main
