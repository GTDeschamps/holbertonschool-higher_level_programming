#!/usr/bin/python3
"""Create Link class to table in database"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


# create a base class
from model_state import Base
Base = declarative_base()


# define the State class
class City(Base):
    """ take the attribute of State in database"""

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'),
                      nullable=False)
