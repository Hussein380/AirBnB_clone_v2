#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv

# Check the value of the environment  variable HBNB_TYPE_STORAGE
# If it is set to "db", create a DBStorage instance, otherwise create a FileStorage instance
if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

# Reload the storage instance to load data from the storage system
storage.reload()
