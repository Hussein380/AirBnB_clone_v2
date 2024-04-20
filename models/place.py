#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
# Define a table to represent the many-to-many
# relationship between Place and Amenity
place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


# Define Place class
class Place(BaseModel, Base):
    """ This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: String of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids

    """
    __tablename__ = "places"
    # Define columns for the Place table
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    #  Check the environment variable to determine storage type
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Define relationship with Review and Amenity tables
        # if using database storage
        reviews = relationship("Review", cascade='all, delete, delete-orphan',
                               backref="place")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities")
    else:
        # Define properties for reviews and amenities if using file storage
        @property
        def reviews(self):
            """ Returns list of reviews for the place """
            # Get all objects from storage
            var = models.storage.all()
            # Initialize an empty list to store revies
            lista = []
            result = []
            # Iterate through all objects
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.place_id == self.id):
                    result.append(elem)
            return result

        @property
        def amenities(self):
            """ Return list of amenities ids """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """ Appends amenity ids to the attribute """
            # Check if the object is an empty and its id not in list
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                # Append the Amenity id to the list
                self.amenity_ids.append(obj.id)
