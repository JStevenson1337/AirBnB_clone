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
        """ Constructor """
        pass

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
