#!/usr/bin/python3
""" This module contains the class definition of a State and
    its public instance attributes and methods.
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
