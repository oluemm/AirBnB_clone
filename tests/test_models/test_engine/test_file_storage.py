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
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test Cases for the class."""
    pass