#!/usr/bin/python3
""" State Module for HBNB project """
import models

from models.base_model import BaseModel
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship



class Amenity(BaseModel):
    """Represent a amenity"""
    if models.storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)