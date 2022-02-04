#!/usr/bin/env python3
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ BaseModel for AirBnB project """
    id = ""
    created_at = datetime.utcnow()
    updated_at = datetime.utcnow()

    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """ Return a string representation of the instance """
        pass

    def save(self):
        """ Update the public instance attribute updated_at with current
        datetime """
        pass

    def to_dict(self):
        """ Return a dictionary containing all keys/values of __dict__ of the
        """
        pass
