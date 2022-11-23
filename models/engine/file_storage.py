#!/usr/bin/python3
"""
class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""


class FileStorage():
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances

    Private Class Attributes:

    __file_path: `(string)` - path to the JSON file
    __objects: `(dictionary)` - empty but will store all objects by <class name>.id

    Public instance methods:

    all(self): returns the dictionary __objects
    """
    # private class attributes
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects
