#!/usr/bin/python3
import unittest
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

if __name__ == "__main__":
    unittest.main()


""" 
my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
 
"""
