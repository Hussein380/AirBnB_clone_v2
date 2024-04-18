#!/usr/bin/python3

"""
Module containing a class for managing database storage with SQLAchemy
"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

class DBStorage:
    """
    Class to manage database storage using SQLAlchemy.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage class by creating the engine and configuring the session.
        """
        # Retrieve environment variables for database connection
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        # Create the SQLAlchemy engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        # Drop all tables if environment is set t0 test
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
         Query all objects from the database or query objects of a specific class.
                 
         Args:
                cls (str or class, optional): Class to query objects for. Defaults to None.
                                             
        Returns:
                dict: Dictionary of objects queried from the database.
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return dic

    def new(self, obj):
        """
        Add a new object to the current database session.
        args:
              obj: Object to be added to the session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Save all changes made in the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete an object from the current database session.
        Args:
            obj: Object to be deleted from the session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload configurations and create a new database session.
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        self.__session.close()
