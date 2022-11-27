""" A user module
"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """A User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
