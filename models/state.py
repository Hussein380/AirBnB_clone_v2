#!/usr/bin/python3
""" This is the state class """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """ This is the class for State 
    Atteributes:
        name: input name
    """
    # Define table name for the State class
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                           backref="state")

    @property
    # Dfine cities property to retrieve cities associated with this state
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            # iterate through all instances
            # Replaces dots with spaces
            city = key.replace('.', ' ')
            # tokenize the string
            city = shlex.split(city)
            if city[0] == 'City':
                lista.append(var[key])
        # ietrate through city instance
        for elem in lista:
            # check if city belongs  to this states
            if (elem.state_id == self.id):
                result.append(elem)
        # Return the list of cities associated with this state
        return result
