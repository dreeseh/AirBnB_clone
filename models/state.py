#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """
    State class
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """
            return the list of City objects from storage linked to the State
            """
            from models import storage
            city_list = []
            for j in models.storage.all(City).values():
                if j.state_id == self.id:
                    city_list.append(j)
            return (city_list)
