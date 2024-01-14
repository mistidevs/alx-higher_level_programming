#!/usr/bin/python3
""" Querying all entries in a table to finf those with 'a' """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Using sessions to accomplish this """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    filtered_states = session.query(State).filter(State.name.like("%a%")).order_by(State.id).all()
    for state in filtered_states:
        print(f"{state.id}: {state.name}")

    session.close()