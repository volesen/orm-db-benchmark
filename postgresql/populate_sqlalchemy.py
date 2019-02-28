import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_model import Author, Album, Track, Base

NUM_AUTHORS = 10**2
NUM_ALBUMS = 10**2 * NUM_AUTHORS
NUM_TRACKS = 10**1 * NUM_ALBUMS


def populate_db():

    #DB_URI = os.environ['DB_URI']
    #engine = create_engine('postgresql://root:password@localhost:5432/test')
    engine = create_engine('sqlite:///test.db')

    # Instantiate session
    session = sessionmaker()
    session.configure(bind=engine)

    # Create tables
    Base.metadata.create_all(engine)

    # Populate database
    s = session()

    print('Generating test data')

    for i in range(NUM_AUTHORS):
        author = Author()
        s.add(author)

    for i in range(NUM_ALBUMS):
        album = Album(author_id=i % NUM_AUTHORS+1)
        s.add(album)

    for i in range(NUM_TRACKS):
        track = Track(album_id=i % NUM_ALBUMS +1)
        s.add(track)

    print('Comitting test data to DB')

    s.commit()


if __name__ == "__main__":
    populate_db()
