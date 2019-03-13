import random
from flask import Flask, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test',
    'host': 'mongodb://localhost/'
}

db = MongoEngine(app)


class Track(db.EmbeddedDocument):
    title = db.StringField()
    unit_price = db.FloatField()


class Album(db.EmbeddedDocument):
    title = db.StringField()
    price = db.IntField()
    tracks = db.EmbeddedDocumentListField(Track)


class Author(db.Document):
    name = db.StringField()
    publisher = db.StringField()
    address = db.StringField()
    albums = db.EmbeddedDocumentListField(Album)


# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    tracks = Author.objects.limit(amount)

    # Return serialized objects
    return tracks.to_json()


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    authors = Author.objects().paginate(page=page, per_page=10).items

    # Return serialized objects
    return jsonify(authors)


if __name__ == '__main__':
    app.run(debug=True)
