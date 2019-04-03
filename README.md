# ORM benchmarking in a REST server context
Python REST server "setups" are benchmarked with an emphasises on ORM/ODM and JSON serializers.

In this benchmark the following databases are tested:
- Sqlite3
- PostgreSQL 11.1
- MongoDB 3.4.19

and the following ORM/ODM with wrappers:
- Django ORM with Django Rest Framework
- Peewee with Flask and Marshmallow
- Flask_SQLAlcehmy with Flask and Marshmallow
- Flask_Mongoengine with Flask and Marshmallow

For each ORM/ODM and DB pair (ORMs and MongoDB) the following things are benchmarked:
- Serialization of 100, 1,000, 10,000 and 100,000 objects (by a LIMIT query)
- Serialization of 10 objects by pagination

## Benchmarking methodology


Testing script measuring time (an estimate) for processing and serialization of DB content for a server
The time spent is measured using cURL through pycURL inspired by
- http://blog.cloudflare.com/a-question-of-timing/
- http://stackoverflow.com/questions/17638026/calculating-server-processing-time-with-curl



<sup id="a1">[1](#f1)</sup>

### Model


One-to-many relationships are modeled by embedded documents and reference fields respectivly for MongoDB.

## Results

The minimum time gives an estimate for a lower bound on process time.


## Conclusion




<hr>

<b id="f1">1</b> Footnote [↩](#a1)