#!/usr/bin/python3
"""Create Link class to table in database"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# create a base class
Base = declarative_base()


# define the State class
class State(Base):
    """ take the attribute of State in database"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
