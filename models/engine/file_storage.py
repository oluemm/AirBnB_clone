#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel

class_dict = {"BaseModel": BaseModel}


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances

    #### Private Class Attributes:

    - __file_path: `(string)` - path to the JSON file
    - __objects: `(dictionary)` - empty but will store all
    objects by <class name>.id

    #### Public instance methods:

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
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes existing JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                # load the json file as instance object
                instance = json.load(f)
                for key in instance:
                    self.__objects[key] = (
                        class_dict[instance[key]["__class__"]](**instance[key])
                        )
        except Exception:
            pass
