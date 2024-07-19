import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    favorites_characters = relationship('FavoriteCharacter', back_populates='user')
    favorites_planets = relationship('FavoritePlanet', back_populates='user')

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    user = relationship('User', back_populates='favorites_characters')
    character = relationship('Character', back_populates='favorites_characters')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer, nullable=False)
    gender = Column(String(50), nullable=False)
    created = Column(DateTime, nullable=False)
    url = Column(String(250), nullable=False)
    favorites_characters = relationship('FavoriteCharacter', back_populates='character')

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    user = relationship('User', back_populates='favorites_planets')
    planet = relationship('Planet', back_populates='favorites_planets')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    url = Column(String(250), nullable=False)
    favorites_planets = relationship('FavoritePlanet', back_populates='planet')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
