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
    """Test BaseModel"""