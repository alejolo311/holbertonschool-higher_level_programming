#!/usr/bin/python3

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """State class."""
    __tablename__ = 'state'

    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
