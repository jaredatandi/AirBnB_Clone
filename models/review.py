#!/usr/bin/python3
"""State class
"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """A Review class"""
    place_id = ''
    user_id = ''
    text = ''
