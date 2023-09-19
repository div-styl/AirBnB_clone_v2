#!/usr/bin/python3
""" Initialize the storage module """
from os import getenv

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
