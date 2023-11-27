#!/usr/bin/python3
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Establishing connection to Mysql server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create a session
    session = Session(engine)

    # Retrieve and display all State objects sorted by id
    cities = session.query(State, City).join(City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in cities:
        print("{}: {} {}".format(state.name, city.id, city.name))

    # close session
    session.close()
