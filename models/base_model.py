#!/usr/bin/python3
"""Module that implements BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """A class that defines common method and attributes for other clases"""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the base model"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns a customized string representation

        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'self.updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance:
        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()  # create a copy of __dict__
        # add __class__ key with class name as value
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            print(k, ":", v)
            if k in ("created_at", "updated_at"):
                # convert datetime{2022-11-21 16:06:40.075755}
                # to isoformat {2022-11-21T16:06:40.075755}
                v = self.__dict__[k].isoformat()
                print(k, ":", v)
                dict_1[k] = v
        return dict_1
