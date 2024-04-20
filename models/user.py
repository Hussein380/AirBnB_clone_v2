#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review


# Creating a class for the
class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        email: email address
        password: password for your login
        first_name: first name
        last_name: Last name
    """
    # Defining table name for the user model
    __tablename__ = "users"

    # Defining columns for the user Table
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    # Defining relationships with other models
    # Relationship with the place model, cascade delete
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="user")
    # Relationship with the Review model, cascade delete
    reviews = relationship("Review", cascade='all, delete, delete-orphan',
                           backref="user")
