#!/usr/bin/python3
"""
A module that contains the test suite for the BaseModel class
"""
import unittest
import os
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
        self.assertEqual(str(x),
                "[BaseMosel] ({}) {}".format(x.id, x.__dict__))

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


if __name__ == "__main__":
    unittest.main()
