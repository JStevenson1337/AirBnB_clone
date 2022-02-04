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

    def new(self, obj):
        """
        new method
        """
        FileStorage.__objects[obj.id] = obj

    def save(self):
        """
        save method
        """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        reload method
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
            for key, value in my_dict.items():
                value = value['__class__'](**value)
                FileStorage.__objects[key] = value
        except FileNotFoundError:
            pass

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
