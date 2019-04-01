import random

from faker import Faker
from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
faker = Faker()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), default=faker.name)
    publisher = Column(String(255), default=faker.company)
    address = Column(String(255), default=faker.address)

    albums = relationship("Album", back_populates="author", lazy='joined')


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), default=faker.name)
    price = Column(Integer, default=random.randint(5, 9))

    author_id = Column(Integer, ForeignKey('author.id'), index=True)
    author = relationship("Author", back_populates="albums", lazy='joined')

    tracks = relationship("Track", back_populates="album", lazy='joined')


class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), default=faker.name)
    unit_price = Column(Float, default=0.99)

    album_id = Column(Integer, ForeignKey('album.id'), index=True)
    album = relationship("Album", back_populates="tracks", lazy='joined')
