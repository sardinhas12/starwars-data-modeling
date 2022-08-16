import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()
class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    user_name = Column(String(250))
    email = Column(String(250))
    password = Column(String(250))
   
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id=Column(Integer, ForeignKey('user.id'))
    character_id = Column(String(250), ForeignKey('character.id'))
    planet_id = Column(String(250), ForeignKey('planet.id'))

class Character (Base):
    __tablename__ = 'character'
    id = Column(String(250), primary_key = True)
    name = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    birth_year = Column(Integer)
    gender = Column(String(250))
    eye_color = Column(String(250))
    skin_color = Column(String(250))
    hair_color = Column(String(250))
    uid = Column(Integer)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(String(250), primary_key=True)
    name = Column(String(250))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(String (250)) 
    diameter = Column(Integer)
    population = Column(Integer) 
    surface_water = Column(Integer)
    uid = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')