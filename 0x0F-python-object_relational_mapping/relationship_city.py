#!/usr/bin/python3
"""
Module City class
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto",
                unique=True)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
