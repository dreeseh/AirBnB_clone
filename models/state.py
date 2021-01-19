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

    __tablename__ = 'states'
    if getenv('HBNB_TPYE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state", passive_deletes=True)
    else:
        name = ''

        def cities(self):
            """
            Getter for cities
            """

            from models import storage
            cities = storage.all(City)
            city_list = []
            for city in cities.values():
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
