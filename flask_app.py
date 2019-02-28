from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from postgresql.sqlalchemy_model import Base, Author, Album, Track

app = Flask(__name__)

engine = create_engine('sqlite:///sqlite/test.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


@app.before_first_request
def init_db():
    Base.metadata.create_all(bind=engine)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def index():
    authors = db_session.query(Author).all()
    names = [author.name for author in authors]
    return ','.join(names), 202


if __name__ == '__main__':
    app.run(debug=True)
