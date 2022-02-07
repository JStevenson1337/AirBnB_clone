#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity with inheritance from Base"""
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize Amenity"""
        super().__init__(*args, **kwargs)

    def __str__(self):
        """return string representation of Amenity"""
        return "[Amenity] ({}) {}".format(self.id, self.__dict__)
