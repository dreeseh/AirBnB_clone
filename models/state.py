#!/usr/bin/python3
"""
State Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage

class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ''

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    def cities(self):
        """
        Getter for cities
        """
        all.cities = storage.models.all(City)
        city_list = []
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
