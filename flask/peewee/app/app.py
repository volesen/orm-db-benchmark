import os

from flask import Flask
from peewee import prefetch, IntegerField, CharField, ForeignKeyField, FloatField, ForeignKeyField
from playhouse.flask_utils import FlaskDB

from serializer import AuthorSchema


app = Flask(__name__)
app.config['DATABASE_URL'] = os.environ.get('DATABASE_URL')

flask_db = FlaskDB(app)

author_schema = AuthorSchema(many=True)


class Author(flask_db.Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    publisher = CharField(max_length=255)
    address = CharField(max_length=255)


class Album(flask_db.Model):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    price = IntegerField()

    author = ForeignKeyField(Author, backref='albums')


class Track(flask_db.Model):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    unit_price = FloatField()

    album = ForeignKeyField(Album, backref='tracks')

# URL Endpoints
@app.route('/serialize/<int:amount>')
def serlialize_query(amount):
    # Query given amount of objects to serialize
    author_query = Author.select().limit(amount)

    query = prefetch(author_query, Album.select())

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    author_query = Author.select().paginate(page, 10)

    query = prefetch(author_query, Album.select(), Track.select())

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors
