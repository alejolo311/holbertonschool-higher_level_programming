#!/usr/bin/python3
"""filter all the states that contains the a letter"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    DB_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, DB_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_mex = session.query(State).filter_by(id=2).first()
    try:
        new_mex.name = "New Mexico"
    except Exception:
        pass
    session.commit()
    session.close()
