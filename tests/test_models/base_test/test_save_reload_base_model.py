#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
ids = "6e3de41f-b369-4acf-a5b4-9fb48e4d9e5f"
all_objs = storage.all()
# print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
    # if ids in obj:
    # print(obj)

# print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
# print(my_model)
