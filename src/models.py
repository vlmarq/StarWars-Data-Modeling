import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

fav_characters = Table('user_people', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('person_id', Integer, ForeignKey('people.id'))
)

fav_planets = Table('user_planets', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('planet_id', Integer, ForeignKey('planets.id'))
)

fav_starships = Table('user_starships', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('starship_id', Integer, ForeignKey('starships.id'))
)

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    characters = relationship("Person", secondary=fav_characters)
    planets = relationship("Planet", secondary=fav_planets)
    starships = relationship("Starship", secondary=fav_starships)


class Person(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(100), nullable=False)
    height = Column(String(10))
    mass = Column(String(10))
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(10))
    gender = Column(String(10))
    homeworld_id = Column(String(200), ForeignKey("planets.id"))
    homeworld = relationship("Planet", back_populates="characters")


class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    characters = relationship("Person", uselist=False)
    name = Column(String(100), nullable=False)
    rotation_period = Column(String(100))
    orbital_period = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(200))
    gravity = Column(String(100))
    terrain = Column(String(200))
    surface_water = Column(String(100))
    population = Column(String(100))

class Starship(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    manufacturer = Column(String(100))
    cost_in_credits = Column(String(200))
    length = Column(String(100))
    max_atmosphering_speed = Column(String(100))
    crew = Column(String(100))
    passengers = Column(String(100))
    cargo_capacity = Column(String(100))
    consumables = Column(String(100))
    hyperdrive_rating = Column(String(100))
    mglt = Column(String(100))
    starship_class = Column(String(200))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')