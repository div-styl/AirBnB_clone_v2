#!/usr/bin/python3
""" basemodel the mother of all models """

import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class BaseModel:
    """ the base model which all other models inherit from """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ base model constructor """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            if "id" not in kwargs:
                kwargs["id"] = str(uuid4())
            if "created_at" not in kwargs:
                kwargs["created_at"] = datetime.utcnow()
            if "updated_at" not in kwargs:
                kwargs["updated_at"] = datetime.utcnow()
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ class string representation """
        class_name = self.__class__.__name__
        string = f"[{class_name}] ({self.id}) {self.__dict__}"
        return string

    def save(self):
        """ update the last updated time to now """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """ create new dict for the current class """
        new_dict = dict(self.__dict__)
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict
