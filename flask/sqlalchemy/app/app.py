import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import Base, Author
from serializer import AuthorSchema


author_schema = AuthorSchema(many=True)


app = Flask(__name__)
app.config.update({
    'SQLALCHEMY_DATABASE_URI': os.environ.get('DATABASE_URL'),
    'SQLALCHEMY_TRACK_MODIFICATIONS': False
})

db = SQLAlchemy(app, model_class=Base)


# URL Endpoints
@app.route('/serialize/<int:amount>')
def serliaze_query(amount):
    # Query given amount of objects to serialize
    query = Author.query.limit(amount).all()

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors


@app.route('/paginate/<int:page>')
def paginate_query(page):
    # Query objects by pagination
    query = Author.query.paginate(page, per_page=10).items

    # Return serialized objects
    authors = author_schema.dumps(query)

    return authors
