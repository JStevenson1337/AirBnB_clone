#!/usr/bin/env python3
""" File storage engine for the API """
# -*- coding: utf-8 -*-
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        all method
        """
        return FileStorage.__objects

    def reload(self):
        """
        reload method
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    FileStorage.__objects[key] = eval(
                        value['__class__'])(**value)
        except FileNotFoundError:
            pass

    def new(self, obj):
        """
        new method
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        save method
        """
        my_dict = {
            key: value.to_dict()
            for key, value in FileStorage.__objects.items()
        }

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def delete(self, obj=None):
        """
        delete method
        """
        if obj:
            del FileStorage.__objects[obj.id]
        else:
            FileStorage.__objects.clear()

    def close(self):
        """
        close method
        """
        self.save()
