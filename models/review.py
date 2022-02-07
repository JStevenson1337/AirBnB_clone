#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review with inheritance from Base"""
    place_id = ''   # this will be the Place.id
    user_id = ''    # this will be the User.id
    text = ''

