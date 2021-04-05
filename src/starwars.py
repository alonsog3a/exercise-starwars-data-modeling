import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(25))
    firstname=Column(String(25))
    lastname=Column(String(25))
    email=Column(String(25))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name=Column(String(25))
    birthday=Column(String(25))
    haircolor=Column(String(25))
    gender=Column(String(25))
    heigth=Column(String)

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name=Column(String(25))
    rotation=Column(String(25))
    terrain=Column(String(25))
    diameter=Column(String(25))
    gravity=Column(String(25))
    population=Column(String(25))

    def to_dict(self):
        return {}



class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)

    def to_dict(self):
        return {}        

## Draw from SQLAlchemy base
render_er(Base, 'starwars.png')