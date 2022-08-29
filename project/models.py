from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True)
    description = Column(String(100))
    trailer = Column(String(100))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    director_id = Column(Integer, ForeignKey('directors.id'))
    genre = relationship('Genre')
    director = relationship('Director')


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(1000), nullable=False)
    name = Column(String(100))
    surname = Column(String(100))
    #favorite_genre = Column(Integer, ForeignKey(f'{Genre.__tablename__}'))
