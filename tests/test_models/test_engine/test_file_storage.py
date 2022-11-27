#!/usr/bin/python3
"""
A module that contains the test suite for the FileStorage class
"""
import unittest
import os
from time import sleep
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test Cases for the class."""

    def test_file_path_is_a_private_class_attr(self):
        """Checks that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Checks that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_with_arg(self):
        """Tests initialization with args"""
        with self.assertRaises(TypeError):
            FileStorage(None)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUp(self):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass
        self.base_model = BaseModel()
        self.user_model = User()
        self.state_model = State()
        self.city_model = City()
        self.place_model = Place()
        self.review_model = Review()
        self.amenity_model = Amenity()
        storage.save()

    def test_file_storage_save(self):
        """Test save and reload methods"""
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + self.base_model.id, save_text)
            self.assertIn("User." + self.user_model.id, save_text)
            self.assertIn("State." + self.state_model.id, save_text)
            self.assertIn("Place." + self.place_model.id, save_text)
            self.assertIn("City." + self.city_model.id, save_text)
            self.assertIn("Amenity." + self.amenity_model.id, save_text)
            self.assertIn("Review." + self.review_model.id, save_text)

    def test_all_method(self):
        """Tests all() method of the FileStorage class"""
        self.assertTrue(type(storage.all()) is dict)

    def test_new_method(self):
        """Tests the new() method of the FileStorage class"""

        # Checks that the objects created above are stored already
        self.assertIn("BaseModel." + self.base_model.id,
                      storage.all().keys())
        self.assertIn(self.base_model, storage.all().values())
        self.assertIn("User." + self.user_model.id, storage.all().keys())
        self.assertIn(self.user_model, storage.all().values())
        self.assertIn("State." + self.state_model.id, storage.all().keys())
        self.assertIn(self.state_model, storage.all().values())
        self.assertIn("Place." + self.place_model.id, storage.all().keys())
        self.assertIn(self.place_model, storage.all().values())
        self.assertIn("City." + self.city_model.id, storage.all().keys())
        self.assertIn(self.city_model, storage.all().values())
        self.assertIn("Amenity." + self.amenity_model.id,
                      storage.all().keys())
        self.assertIn(self.amenity_model, storage.all().values())
        self.assertIn("Review." + self.review_model.id,
                      storage.all().keys())
        self.assertIn(self.review_model, storage.all().values())

    @classmethod
    def tearDown(self):
        """Code to execute after tests are executed"""
        # Remove file.json if it exists
        try:
            os.remove("file.json")
        except IOError:
            pass

        # rename tmp.json from setUp() to file.json
        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
