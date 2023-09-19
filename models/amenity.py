#!/usr/bin/python3
""" State Module for HBNB project """
import models

from models.base_model import BaseModel
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Represent a amenity"""

    __tablename__ = "amenities"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        place_amenities= relationship('Place', secondary="place_amenity", back_populates="amenities")
    else:
        name = ""