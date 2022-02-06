#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place with inheritance from Base"""
    city_id = ''    # this will be the City.id
    user_id = ''    # this will be the User.id
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
