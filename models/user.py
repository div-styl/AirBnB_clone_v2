#!/usr/bin/python3
"""This is the user class"""
import models

from models.base_model import BaseModel
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


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
        places = relationship("Place", backref="user")
        review = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)