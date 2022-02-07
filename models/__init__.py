# !/usr/bin/python3
""" init file for models package """
from models.engine.file_storage import FileStorage

""" define storage """
storage = FileStorage()
storage.reload()
