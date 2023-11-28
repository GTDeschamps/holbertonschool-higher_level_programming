#!/usr/bin/python3
"""Start link class to table in database"""


import sys
from model_state import Base, State

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

    # Fetch the state
    state_to_change = session.query(State).filter_by(id=2).first()

    if state_to_change:
        state_to_change.name = 'New Mexico'
        session.commit()

        # Retrieve and display new State
        print("{}".format(state_to_change.id))

    else:
        print("Not found")

    # close session
    session.close()
