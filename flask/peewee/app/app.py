import os
import logging

from flask import Flask
from peewee import prefetch

from peewee_model import Author, Album, Track
from serializer import AuthorSchema, AlbumSchema, TrackSchema


logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


author_schema = AuthorSchema(many=True)
album_schema = AlbumSchema()
track_schema = TrackSchema()


app = Flask(__name__)


# URL Endpoints
@app.route('/serialize/<int:amount>')
def serlialize_query(amount):
    # Query given amount of objects to serialize
    query = prefetch(Author.select().limit(amount), Album.select())


    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    query = prefetch(Author.select().paginate(page, 10), Album.select(), Track.select())

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors
