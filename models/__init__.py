#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import class_dict


# initialize an instance of FileStorage called storage
storage = FileStorage()
# call the reload method
storage.reload()
