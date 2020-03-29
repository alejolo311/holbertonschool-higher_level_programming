#!/usr/bin/python3
"""filter all the states that contains the a letter"""

from model_state import Base, State
from model_city import City
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
    for ci, st in session.query(City, State).filter(City.state_id == State.id):
        print("{}: ({}) {}".format(st.name, ci.id, ci.name))
    session.close()
