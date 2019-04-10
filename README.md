# Python REST stack benchmark

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
- Serialization of 10 objects by pagination

The benchmark results can be replicated with the following

```bash
$ docker-compose -d up
$ pipenv intall
$ pipenv shell
$ python test_server_serialization.py
```

## Benchmarking methodology
For each ORM/ODM and DB pair, the application is dockerized and served thorugh the Gunicorn as a wsgi-server.

Testing script measuring time (an estimate) for processing and serialization of DB content for a server
The time spent processing a request is estimated using cURL through pycURL as `TIME_STARTTRANSFER - TIME_CONNECT` inspired by
- http://blog.cloudflare.com/a-question-of-timing/
- http://stackoverflow.com/questions/17638026/calculating-server-processing-time-with-curl



### Model

![UML diagram of model](model.png)

One-to-many relationships are modeled by embedded documents and reference fields respectivly for MongoDB.

## Results

The minimum time gives an estimate for a lower bound on process time.


## Conclusion



<sup id="a1">[1](#f1)</sup>

<hr>

<b id="f1">1</b> Footnote [↩](#a1)