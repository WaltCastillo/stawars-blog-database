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
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250))
    email = Column(String(250))

class Userfav(Base):
    __tablename__ = 'userfav'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    user_id = Column(Integer, nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    person_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=True)
    planet_id = Column(Integer, nullable=True)
    person_id = Column(Integer, nullable=True)
    vehicle_id = Column(Integer, nullable=True)

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, nullable=True)
    vehicle_id = Column(Integer, nullable=True)
    name = Column(String(50))
    heigth = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    birth_year = Column(Integer)
    gender = Column(String(50))

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(30))
    model = Column(Integer)
    passenger = Column(Integer)
    consumable = Column(String(30))
    starship_class = Column(String(30))
    lenght = Column(Integer)
    cargo_capacity = Column(Integer)
    hyperdrive_rating = Column(Integer)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')