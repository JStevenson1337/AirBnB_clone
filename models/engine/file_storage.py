#!/usr/bin/python3
""" File storage engine for the API """
# -*- coding: utf-8 -*-
import json


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
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                self.__objects = json.load(f)
                print(self.__objects)

                for key, value in FileStorage.__objects.items():
                    self.__objects[key] = eval(
                        value.__class__.__name__ + "(**" + str(value) + ")"
                    )
        except FileNotFoundError:
            pass

    def new(self, obj):
        """
        new method
        """
        if obj:
            FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """
        save method
        """
        try:
            with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
                json.dump(FileStorage.__objects, f)
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
