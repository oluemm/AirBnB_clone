#!/usr/bin/python3
"""Module that implements Review class
which inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    #### Public Class Attributes:
    * place_id:`(string)` - empty string
    * user_id:`(string)` - empty string
    * text:`(string)` - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
