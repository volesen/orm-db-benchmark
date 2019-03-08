import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from sqlalchemy_model import Base, Author, Album, Track


app = Flask(__name__)
app.config.update({
    # os.environ.get('DB_URI'),
    'SQLALCHEMY_DATABASE_URI': 'postgresql://root:password@localhost:5432/test',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})


# Initialize extensions
db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)

# Define Marshmallow JSON serialization schema


class AuthorSchema(ma.ModelSchema):
    class Meta:
        model = Author


class AlbumSchema(ma.ModelSchema):
    class Meta:
        model = Album


class TrackSchema(ma.ModelSchema):
    class Meta:
        model = Track


author_schema = AuthorSchema()
album_schema = AlbumSchema()
track_schema = TrackSchema()

# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    tracks = Track.query.limit(amount).all()

    # Return serialized objects
    serialized = track_schema.jsonify(tracks, many=True)

    return serialized


@app.route('/paginate/<int:page>')
def paginate_query(page):

    # Query objects by pagination
    tracks = Track.query.paginate(page, per_page=10).items

    # Return serialized objects
    serialized = track_schema.jsonify(tracks, many=True)

    return serialized


if __name__ == '__main__':
    app.run(debug=True)
