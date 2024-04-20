#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base


class Review(BaseModel, Base):
    """ Review class to store review information 
    Attributes:
        place: place id
        user_id: user id
        text: review description

    """
    __tablename__ = "reviews"

    # Review text description
    text = Column(String(1024), nullable=False)

    # Place ID associated with review
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)

    # User ID associated with the review
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
