#!/usr/bin/python3
""" Amenity class """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class Amenity with inheritance from Base"""
    name = ''

    def __init__(self, *args, **kwargs):
        """initialize Amenity"""
        super().__init__(*args, **kwargs)
