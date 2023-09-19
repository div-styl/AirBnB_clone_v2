#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class User(BaseModel, Base):
    """Represent a user."""
    __tablename__ = 'users'
    email = Column(String(128), notnull=True)
    password = Column(String(128), notnull=True)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)