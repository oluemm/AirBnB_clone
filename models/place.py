#!/usr/bin/python3
"""Module that implements Place class
which inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    #### Public Class Attributes:
    * city_id:`(string)` - empty string
    * user_id:`(string)` - empty string
    * name:`(string)` - empty string
    * description:`(string)` - empty string
    * number_rooms:`(int)` - defaults to 0
    * number_bathrooms:`(int)` - defaults to 0
    * max_guest:`(int)` - defaults to 0
    * price_by_night:`(int)` - defaults to 0
    * latitude:`(float)` - defaults to 0.0
    * longitude:`(float)` - defaults to 0.0
    * amenity_ids:`(list)` - list of string - empty list
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
