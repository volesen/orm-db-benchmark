import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from sqlalchemy_model import Base, Author, Album, Track


app = Flask(__name__)


# Initialize extensions
db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)


# Define Marshmallow JSON serialization schema
class TrackSchema(ma.ModelSchema):
    class Meta:
        model = Track


class AlbumSchema(ma.ModelSchema):
    class Meta:
        model = Album

    tracks = ma.Nested(TrackSchema, many=True)


class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author

    albums = ma.Nested(AlbumSchema, many=True)


author_schema = AuthorSchema()
album_schema = AlbumSchema()
track_schema = TrackSchema()

# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    authors = Author.query.limit(amount).all()

    # Return serialized objects
    serialized = author_schema.jsonify(authors, many=True)

    return serialized


@app.route('/paginate/<int:page>')
def paginate_query(page):

    # Query objects by pagination
    authors = Author.query.paginate(page, per_page=10).items

    # Return serialized objects
    serialized = author_schema.jsonify(authors, many=True)

    return serialized
