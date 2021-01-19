#!/usr/bin/python3
"""
defines what goes into user class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class User(BaseModel, Base):
    """
    defines what goes in the users table
    """
    __tablename__ = 'users'

    if getenv('HBNB_TPYE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", cascade='all, delete-orphan',
                              backref='user')
        reviews = relationship("Review", cascade='all, delete-orphan',
                               backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
