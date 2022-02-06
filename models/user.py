#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """class User with inheritance from Base"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
