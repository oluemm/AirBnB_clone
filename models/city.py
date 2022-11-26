#!/usr/bin/python3
"""Module that implements City class
which inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    #### Public Class Attributes:
    * state_id:`(string)` - empty string
    * name:`(string)` - empty string
    """
    state_id = ""
    name = ""
