#!/usr/bin/python3
"""Module that implements BaseModel class"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
    """A class that defines common method and attributes for other clases"""

    def __init__(self, *args, **kwargs):
        """Initialize the base model"""
        from models import storage
        if not kwargs:  # if no dictionary (key&value) argument is passed
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.__set_from_dict(**kwargs)

    def __str__(self):
        """
        #### Returns: `[<class name>] (<self.id>) <self.__dict__>`
        A customized string representation
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates 'self.updated_at' with the current datetime"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        #### Returns:
        A dictionary containing all keys/values of __dict__ of the instance:
        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()  # create a copy of __dict__
        # add __class__ key with class name as value
        dict_1["__class__"] = self.__class__.__name__
        # converts datetime {2022-11-21 16:06:40.075755}
        # to isoformat {2022-11-21T16:06:40.075755}
        dict_1["created_at"] = self.created_at.isoformat()
        dict_1["updated_at"] = self.updated_at.isoformat()
        return dict_1

    def __set_from_dict(self, **kwargs):
        """Private method that creates a new instance from dict args"""
        for k, v in kwargs.items():
            if k != "__class__":
                if k in ("created_at", "updated_at"):
                    # Construct a date from the output of date.isoformat()
                    # setattr(x, 'y', v) is equivalent to x.y = v where;
                    # x is dict_name, y is the key and v is the value
                    setattr(self, k, datetime.fromisoformat(v))
                # otherwise create a key and value pair of other attributes
                else:
                    setattr(self, k, v)
