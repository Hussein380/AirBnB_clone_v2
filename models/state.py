#!/usr/bin/python3
""" This is the state class """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City


class State(BaseModel, Base):
    """ This is the class for State
    Atteributes:
        name: input name:
    """
    # Define table name for the State class
    if models.storage_t == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        name = ""

    if models.storage_t != "db":
        @property
        # Dfine cities property to retrieve cities associated with this state
        def cities(self):
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
