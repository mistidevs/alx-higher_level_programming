#!/usr/bin/python3
""" Deleting all entries that have 'a' """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Using sessions to accomplish this """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like("%a%")).delete(synchronize_session='fetch')
    session.commit()
    
    session.close()
