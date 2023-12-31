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
    contain_a = session.query(State).filter(State.name.like('%a%')).all()

    for state in contain_a:
        session.delete(state)
    session.commit()

    # close session
    session.close()
