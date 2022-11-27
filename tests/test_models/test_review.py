#!/usr/bin/python3
"""test module for review class"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """test case for the review class"""

    review = Review()
    attr_list = [
                "place_id",
                "user_id",
                "text"
                ]

    def test_review_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attr(self):
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        for attr in self.attr_list:
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(bool(getattr(self.review, attr)))


if __name__ == "__main__":
    unittest.main()
