#!/usr/bin/python3
""" Adding a new state """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Using sessions to accomplish this """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@\
localhost/{}'.format(user, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    state = session.query(State).filter_by(name=new_state.name).first()
    print(state.id)

    session.close()
