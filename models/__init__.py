#!/usr/bin/python3

# from engine.file_storage import FileStorage '''this works too'''
from models.engine.file_storage import FileStorage
from models.engine.file_storage import class_dict

storage = FileStorage()
storage.reload()
