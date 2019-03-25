import os

from mongoengine import connect
from mongoengine_model_refrence import Track, Album, Author

NUM_AUTHORS = 10**2
NUM_ALBUMS = 10**2
NUM_TRACKS = 10**1


def populate_db():

    DB_URI = 'test'  # os.environ.get('DATABASE_URL')

    connect(db=DB_URI)

    print('Generating test data')

    for i in range(NUM_AUTHORS):
        albums = []
        for i in range(NUM_ALBUMS):
            # Generate Tracks
            tracks = [Track().save() for track in range(NUM_TRACKS)]

            # Create and append trakcs to album
            album = Album(tracks=tracks).save()
            albums.append(album)

        author = Author(albums=albums)
        author.save()


if __name__ == "__main__":
    populate_db()
