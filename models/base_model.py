#!/usr/bin/env python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ BaseModel for AirBnB project """
    id = ""
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    def __init__(self, *args, **kwargs):
        """Initialize the base class"""
        if kwargs:
            self.__dict__ = kwargs
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    self.updated_at = datetime.strptime(value,
                                                        "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the instance """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Update the public instance attribute updated_at with current
        datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ of the
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return
