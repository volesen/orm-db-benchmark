from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_model import Base, Author, Album, Track

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite/test.db'

db = SQLAlchemy(app, model_class=Base)


@app.route('/')
def index():
    return '', 202


if __name__ == '__main__':
    app.run(debug=True)
