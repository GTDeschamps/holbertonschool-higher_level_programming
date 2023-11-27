#!/usr/bin/python3
"""Start link class to table in database"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Establishing connection to Mysql server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

# Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()
