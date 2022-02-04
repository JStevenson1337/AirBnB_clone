#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):
    """Tests BaseModel"""
    def test_init(self):
        """tests init"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIn('id', base.__dict__)
        self.assertIn('created_at', base.__dict__)
        self.assertIn('updated_at', base.__dict__)
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
