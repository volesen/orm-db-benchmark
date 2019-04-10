# Python REST stack benchmark
Introduction – Write about reason behind this blog. Why was it so important to test so many ORMs and Databases? What abut battle between SQL vs NoSQL. And why Django was so slow. You have to grab a reader attention withing first few sentences.

In this benchmark the following databases are tested:
- [Sqlite 3.27.2](https://www.sqlite.org/)
- [PostgreSQL 11.1](https://hub.docker.com/_/postgres)
- [MongoDB 3.4.19](https://hub.docker.com/_/mongo)

and the following ORM/ODM with thin wrappers:
- [Django 2.1.7](https://djangoproject.com/) with [Django Rest Framework 3.9.2](https://django-rest-framework.org/)
- [Peewee 3.9.3](https://peewee-orm.com/) with [Flask 1.0.2](http://flask.pocoo.org/) and [Marshmallow 2.19.1](https://marshmallow.readthedocs.io/)
- [Flask_SQLAlcehmy 2.3.2](http://flask-sqlalchemy.pocoo.org/) with [Flask 1.0.2](http://flask.pocoo.org/) and [Marshmallow 2.19.1](https://marshmallow.readthedocs.io/)
- [Flask_Mongoengine 0.9.5](http://docs.mongoengine.org/projects/flask-mongoengine/) with [Flask 1.0.2](http://flask.pocoo.org/) and [Marshmallow 2.19.1](https://marshmallow.readthedocs.io/)

For each compatible ORM/ODM and DB pair the following things are benchmarked:
- Serialization of 10 objects by pagination<sup id="a1">[1](#f1)</sup>
- Serialization of (10, 100, 1.000, 10.000 and 100.000) objects by `LIMIT` query

The benchmark results can be replicated with the following
```bash
$ docker-compose -d up
$ pipenv shell
$ python benchmark_serialization.py
```

## Benchmarking methodology
For each ORM/ODM and DB pair, the application is dockerized and served through the [Gunicorn 19.9.0](https://gunicorn.org/) as a wsgi-server.

Testing script measuring time (an estimate) for processing and serialization of DB content for a server
The time spent processing a request is estimated using cURL through pycURL as `TIME_STARTTRANSFER - TIME_CONNECT` inspired by
- [Cloudflare - A Question of Timing](http://blog.cloudflare.com/a-question-of-timing/)
- [Stackoverflow - Calculating Server Processing Time With Curl](http://stackoverflow.com/questions/17638026/calculating-server-processing-time-with-curl)s


### Model
The model used is as follows<sup id="a2">[2](#f2)</sup>
![UML diagram of model](model.png)

The number of rows are as follows:
- 100 authors
- 100 albums per author
- 10 tracks per album

A serialization of an author object would there requiere serialization of 1000 track objects.

## Results
The results are based on n = 20 measurements for each stack.

| Server | ORM/ODM                 | Serializer            | DB         | mean   | min    | max    | std    |
|--------|-------------------------|-----------------------|------------|--------|--------|--------|--------|
| Flask  | Mongoengine (Embedding) | Marshmallow           | MongoDB    | 1.028  | 1.018  | 1.044  | 0.0068 |
| Flask  | Mongoengine (Reference) | Marshmallow           | MongoDB    | 1.651  | 1.629  | 1.677  | 0.015  |
| Flask  | SQLAlchemy              | Marshmallow           | PostgreSQL | 0.6571 | 0.6408 | 0.7192 | 0.017  |
| Flask  | SQLAlchemy              | Marshmallow           | Sqlite     | 0.7282 | 0.7134 | 0.7436 | 0.0094 |
| Flask  | Peewee                  | Marshmallow           | PostgreSQL | 0.5534 | 0.5322 | 0.5799 | 0.015  |
| Flask  | Peewee                  | Marshmallow           | Sqlite     | 0.5873 | 0.5433 | 0.5873 | 0.014  |
| Django | Django ORM              | Django Rest Framework | PostgreSQL | 1.086  | 1.039  | 1.221  | 0.055  |
| Django | Django ORM              | Django Rest Framework | Sqlite     | 0.6706 | 0.6528 | 0.7387 | 0.019  |

The minimum time gives an estimate for a lower bound on process time.


## Caution (Remarks)
In terms of loading models dependent on several degrees of relationships, some consideration has to be made, to avoid the N+1 problem.
This can be achived by eager-loading in SQLAlchemy, where as it can be done by prefetching for Peewee and Django.


## Conclusion
In terms of choosing a REST stack for an API, some consideration has to be made when using MongoDB, wheter to use embedding or referencing for relationships, as embedding is more performant.

Suprisingly, the results indicate that Peewee is the more performant than SQLAlchemy in this context.


## Footnotes
<b id="f1">1</b> Using ORM/ODM pagination [↩](#a1)

<b id="f2">2</b> One-to-many relationships are modeled by [embedded documents](https://docs.mongodb.com/manual/tutorial/model-embedded-one-to-many-relationships-between-documents/) and [reference fields](https://docs.mongodb.com/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/) respectivly for MongoDB. [↩](#a2)