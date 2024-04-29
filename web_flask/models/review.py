#!/usr/bin/python3
"""The Review class definition"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """
    Define Review class represenation.

    Attributes:
    place_id (str): place id
    user_id(str): user id
    text (str): review text
    """

    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
