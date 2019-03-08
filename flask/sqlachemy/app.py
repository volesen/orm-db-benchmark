import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy_model import Base, Author, Album, Track

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy(app, model_class=Base)


@app.route('/paginate/')
def paginate_query():
    p = request.args.get('p', 0)
    
    return p, 202

@app.route('/serialize/')
def serliaze_query():
    n = request.args.get('n', 0)
    return p, 202


if __name__ == '__main__':
    app.run(debug=True)
