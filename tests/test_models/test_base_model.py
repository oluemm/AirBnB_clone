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
from models.city import City


class TestBaseModel(unittest.TestCase):
    """"
    the unit test for models.base_model
    """

    @classmethod
    def setUp(self):
        self.base_ins_1 = BaseModel()
        self.base_ins_2 = BaseModel()
        self.city_ins_1 = City()

    def test_id(self):
        """
        Checks that instance has Id assigned on initialization
        """
        self.assertTrue(hasattr(self.base_ins_1, "id"))

    def test_str(self):
        """
        Checks if the string representation is appropriate
        """
        self.assertEqual(type(str(self.base_ins_1)), str)

    def test_ids_unique(self):
        """
        Checks if the Ids genrated randomly are unique
        """
        self.assertNotEqual(self.base_ins_1.id,
                            self.base_ins_2.id)

    def test_ids_str(self):
        """
        Checks if the ID generated is str object
        """
        self.assertTrue(type(self.base_ins_1.id) is str)

    def test_created_at_type(self):
        """
        Checks that the attribute 'created_at" is a datetime
        """
        self.assertTrue(type(self.base_ins_1.created_at) is datetime)

    def test_updated_at_type(self):
        """
        Checks that the attribute 'updated_at' is datetime object
        """
        self.assertTrue(type(self.base_ins_1.updated_at) is datetime)

    def test_created_at_different(self):
        """
        Checks the attribute 'created_at' of 2 models are different
        """
        self.assertLess(self.base_ins_1.created_at, self.base_ins_2.created_at)

    def test_args(self):
        """
        check the attribute 'args' not used
        """

        x = BaseModel(None)
        self.assertNotIn(None, x.__dict__.values())

    def test_created_at_less_update_at(self):
        """
        check that created_at < updated_at at initiallization
        """
        self.assertLess(self.base_ins_1.created_at,
                        self.base_ins_1.updated_at)

    def test_save_reload(self):
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

    def test_superclass(self):
        """Test superclass attribute"""
        self.assertTrue(issubclass(type(self.city_ins_1), BaseModel))

    def test_to_dict(self):
        self.assertEqual(type(
            self.base_ins_1.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
