#!/usr/bin/python3
"""This is the user class"""
import models

from models.base_model import BaseModel
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel):
    """User class inherits from BaseModel
    Attributes:
        email (str): email address
        password (str): password
        first_name (str): first name
        last_name (str): last name
    """
    if models.storage_type == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete" ,backref="user")
        review = relationship("Review", cascade="all, delete" ,backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
