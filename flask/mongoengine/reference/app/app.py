import os

from flask import Flask, jsonify
from marshmallow import fields
from flask_mongoengine import MongoEngine
from marshmallow_mongoengine import ModelSchema

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'mongodb://mongodb_reference'
}

db = MongoEngine(app)


class Track(db.Document):
    title = db.StringField()
    unit_price = db.FloatField()


class Album(db.Document):
    title = db.StringField()
    price = db.IntField()
    tracks = db.ListField(db.ReferenceField(Track))


class Author(db.Document):
    name = db.StringField()
    publisher = db.StringField()
    address = db.StringField()
    albums = db.ListField(db.ReferenceField(Album))


class TrackSchema(ModelSchema):
    class Meta:
        model = Track


class AlbumSchema(ModelSchema):
    class Meta:
        model = Album

    tracks = fields.Nested(TrackSchema, many=True)


class AuthorSchema(ModelSchema):
    class Meta:
        model = Author

    albums = fields.Nested(AlbumSchema, many=True)


track_schema = TrackSchema()
album_schema = AlbumSchema()
author_schema = AuthorSchema()


# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    authors = Author.objects.limit(amount)

    # Return serialized objects
    serialized = author_schema.dumps(authors, many=True)

    return serialized


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    authors = Author.objects().paginate(page=page, per_page=10).items

    # Return serialized objects
    serialized = author_schema.dumps(authors, many=True)

    return serialized
