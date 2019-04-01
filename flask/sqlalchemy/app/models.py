from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    publisher = Column(String(255))
    address = Column(String(255))

    albums = relationship("Album", back_populates="author", lazy='joined')


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    price = Column(Integer)

    author_id = Column(Integer, ForeignKey('author.id'), index=True)
    author = relationship("Author", back_populates="albums", lazy='joined')

    tracks = relationship("Track", back_populates="album", lazy='joined')


class Track(Base):
    __tablename__ = 'track'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    unit_price = Column(Float)

    album_id = Column(Integer, ForeignKey('album.id'), index=True)
    album = relationship("Album", back_populates="tracks", lazy='joined')
