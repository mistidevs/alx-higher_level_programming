#!/usr/bin/python3
""" Base State Class """
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ Class with id and name of states abstractions """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False autoincrement=True)
    name = Column(String(128), nullable=False)
