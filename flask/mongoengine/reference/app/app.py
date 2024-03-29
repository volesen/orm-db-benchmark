from flask import Flask
from flask_mongoengine import MongoEngine

from serializer import AuthorSchema


author_schema = AuthorSchema(many=True)

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


# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    query = Author.objects.limit(amount)

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    query = Author.objects().paginate(page=page, per_page=10).items

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors
