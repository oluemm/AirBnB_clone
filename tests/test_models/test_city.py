#!/usr/bin/python3
"""test module forcity class"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """test case for city class"""

    
    def setUP(self):
        self.city  = City()
        self.attr_list = ["state_id", "name"]
    
    def test_city_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(self.city.name), str)
        self.assertFalse(bool(getattr(self.city.attr)))               
