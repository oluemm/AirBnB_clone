#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review
    }


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances

    #### Private Class Attributes:

    - __file_path: `(string)` - path to the JSON file
    - __objects: `(dictionary)` - empty but will store all
    objects by <class name>.id

    #### Public Instance Methods:

    - all(self): returns the dictionary __objects
    - new(self, obj): sets in __objects the obj with key <obj class name>.id
    - save(self): serializes __objects to the JSON file (path: __file_path)
    - reload(self): deserializes the JSON file to __objects
    (only if the JSON file (__file_path) exists ; otherwise, do nothing.
    If the file doesn’t exist, no exception would be raised)

    """
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        #### Returns:
        `json`: the dictionary __objects
        """
        cls = FileStorage
        return cls.__objects

    def new(self, obj):
        """
        Sets in __objects the `obj` with key <obj class name>.id
        """
        cls = FileStorage
        # use the class name and object id as dict keys
        # eg. ClassName.objectid
        kyz = f"{obj.__class__.__name__}.{obj.id}"
        # create a k:v of the kyz and obj in __objects
        # ClassName.objectid: {"id":...}
        cls.__objects[kyz] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        cls = FileStorage
        json_file = cls.__file_path
        with open(json_file, mode="w") as f:
            dict_storage = {}  # initialize empty dict
            # get key and value from newly instantiated __objects
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            # dump as json string to file
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes existing JSON file to __objects
        """
        cls = FileStorage
        json_file = cls.__file_path
        try:
            with open(json_file, 'r') as f:
                # load the json file as instance object
                loaded_dict = json.load(f)
                # remember that we are working wit a nested dictionary
                # each value is a dict on its own
                for key in loaded_dict.keys():
                    class_name = loaded_dict[key]["__class__"]
                    instance = loaded_dict[key]
                    cls.__objects[key] = class_dict[class_name](**instance)
        except Exception:
            pass
