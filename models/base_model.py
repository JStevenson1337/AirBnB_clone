#!/usr/bin/env python3
""" Base Model """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ BaseModel for AirBnB project """
    def __init__(self, *args, **kwargs):
        """ Initialize the instance """
        if kwargs:
            for key in kwargs:
                if key in ('created_at', 'updated_at'):
                    kwargs[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                if key != ('__class__'):
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the instance """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Update the public instance attribute updated_at with current
        datetime """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ of the
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
