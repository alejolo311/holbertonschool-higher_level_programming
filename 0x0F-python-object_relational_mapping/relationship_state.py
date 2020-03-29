#!/usr/bin/python3
"""
State class
"""
from relationship_city import Base
from relationship_city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True
                )
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")
