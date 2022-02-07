#!/usr/bin/python3
""" This module contains the class definition of a State and
    its public instance attributes and methods.
"""
from .engine.file_storage import FileStorage


class State(FileStorage):
    """ Class State that inherits from FileStorage """
    __name = ''

    def __init__(self, *args, **kwargs):
        """ Instantiation of a State object """
        super().__init__(*args, **kwargs)
        self.__name = args[0] if len(args) > 0 else kwargs.get('name')

    @property
    def name(self):
        """ Getter for the name attribute """
        return self.__name


class BaseModel:
    """ This class defines a base model for all future classes """

    def __init__(self, storage=None, *args, **kwargs):
        """ Initializes a BaseModel class instance """
        self.id = None
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            self.created_at = self.updated_at = None
            storage.new(self)
            storage.save()

    def __str__(self):
        """ Returns a string representation of a BaseModel class instance """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current
            datetime """
        self.updated_at = self.to_dict()['updated_at']
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict

    @classmethod
    def all(cls):
        """ Returns a list of all objects of a given class """
        return storage.all(cls)

    @classmethod
    def destroy(cls, id):
        """ Deletes an object based on the class name and id """
        storage.delete(cls, id)

    @classmethod
    def find(cls, id):
        """ Returns an object based on the class name and id """
        return storage.get(cls, id)

    @classmethod
    def count(cls):
        """ Returns the number of objects of a given class """
        return storage.count(cls)

    @classmethod
    def show_all(cls):
        """ Returns a string representation of all objects of a given class """
        return storage.show_all(cls)

    @classmethod
    def reset_all(cls):
        """ Deletes all objects of a given class """
        storage.delete_all(cls)

    @classmethod
    def save_to_file(cls):
        """ Serializes the object to a file """
        storage.save_to_file(cls)


