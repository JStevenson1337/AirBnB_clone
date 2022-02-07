# !/usr/bin/python3
""" This module contains the Engine class. """
from models.engine.file_storage import FileStorage

""" Storage class for the engine. """
storage = FileStorage()
storage.reload()
