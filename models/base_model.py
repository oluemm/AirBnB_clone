#!/usr/bin/python3
"""Module that implements BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """A class that defines common method and attributes for other clases"""
    def __init__(self, *args, **kwargs) -> None:
        """Initialize the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) self.__dict__"

    def save(self):
        self.updated_at = datetime.now()
