#!/usr/bin/python3
""" Updating a state """
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
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter_by(id=2).update({"name": "New Mexico"})
    session.commit()

    session.close()
