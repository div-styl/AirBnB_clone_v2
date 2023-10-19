#!/usr/bin/python3
"""Defines the State class."""
import models
from models import city
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """Represent a state."""
    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name=""

    if storage_type == "db":
        @property
        def cities(self):
            cities_list = []
            everycity = models.storage.all(city)
            for all_City in everycity.values():
                if all_City.state_id == self.id:
                    cities_list.append(city)
            return cities_list