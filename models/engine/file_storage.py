#!/usr/bin/python3
""" File storage engine for the API """
# -*- coding: utf-8 -*-
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import models


class FileStorage:
    """
    FileStorage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all method
        """
        return self.__objects

    def reload(self):
        """
        reload method
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                all_json = json.load(f)
                for key in all_json:
                    self.__objects[key] = getattr(
                        models, all_json[key]['__class__'])(**all_json[key])
        except FileNotFoundError:
            pass

    def new(self, obj):
        """
        new method
        """
        name = obj.__class__.__name__
        key = name + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        save method
        """
        json_dict = {}
        try:
            with open(self.__file_path, 'w', encoding="utf-8") as f:
                for k, v in self.__objects.items():
                    json_dict[k] = v.to_dict()
                json.dump(json_dict, f)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete method
        """
        if obj:
            del FileStorage.__objects[obj.id]
        else:
            FileStorage.__objects = {}

    def close(self):
        """
        close method
        """
        self.save()
