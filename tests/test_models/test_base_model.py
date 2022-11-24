#!/usr/bin/python3
"""
A module that contains the test suite for the BaseModel class
"""
import unittest
import os
from time import sleep
from datetime import datetime
from uuid import uuid4
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """"
    the unit test for models.base_model
    """

    def test_id(self):
        """
        checks that instance has Id assigned on initialization
        """
        x = BaseModel()
        self.assertTrue(hasattr(x, "id"))

    def test_str(self):
        """
        checks if the string representation is appropriate
        """
        x = BaseModel()
        self.assertEqual(type(str(x)), str)

    def test_ids_unique(self):
        """
        checks if the Ids genrated randomly are unique
        """
        x1 = BaseModel()
        x2 = BaseModel()
        self.assertNotEqual(x1.id, x2.id)

    def test_ids_str(self):
        """
        checks if the ID generated is str object
        """
        x = BaseModel()
        self.assertTrue(type(x.id) is str)

    def test_created_at_datetime(self):
        """
        cjecks that the attribute 'created_at" is a datetime
        """
        x = BaseModel()
        self.assertTrue(type(x.created_at) is datetime)

    def test_updated_at_datetime(self):
        """
        checks that the attribute 'updtae_at' is datetime object
        """
        x = BaseModel()
        self.assertTrue(type(x.updated_at) is datetime)

    def test_created_at_different(self):
        """
        checks the attribute 'created_at' of 2 models are different
        """

        x1 = BaseModel()
        sleep(0.02)
        x2 = BaseModel()
        sleep(0.02)
        self.assertLess(x1.created_at, x2.created_at)

    def test_args(self):
        """
        check the attribute 'args' not used
        """

        x = BaseModel(None)
        self.assertNotIn(None, x.__dict__.values())

    def test_created_at_less_update_at(self):
        """
        check that created_at == updated_at at initiallization
        """

        x = BaseModel()
        self.assertLess(x.created_at, x.updated_at)

    def test_saveMethodel(self):
        """Test save and reload methods"""
        from models import storage

        # create a new instance
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        # call our save method to save the model instance
        my_model.save()
        # now reload the file
        all_objs = storage.all()
        # get the newly added instance by looping to the end
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
        # compare loaded instance to created instance
        self.assertEqual(my_model, obj)


if __name__ == "__main__":
    unittest.main()
