# ORM and DB benchmarking methodology
In this benchmark the following databases are tested:
- Sqlite3
- PostgreSQL 11.1
- MongoDB 3.4.19

and the following ORM/ODM:
- Django ORM
- SQLAlcehmy with Flask
- Mongoengine with Flask

One-to-many relationships are modeled by embedded documents and reference fields for MongoDB.

For each 

For each ORM and DB pair (excluding Django ORM and MonoDB) the following queires are becnhmarked:
- Limit query ( limit in 10^2,.., 10^5 records)
- Get query (by id)  <sup id="a1">[1](#f1)</sup>
- Text search with "contains" query
- Text search with "like" query

For Django ORM, the Queryset object is forced to evaluate by 'repr(query)'.

The time spent on DB-interactions is observed in DB-logs, whereas the ORM/ODM serialization (and DB-interactions) is measured with the `timeit` python module.
The time for DB-interactions is not subtracted, as different ORM/ODM will not necessarily do operations by identical SQL queries. Therefore it is relevant to measure and take this into account.

<hr>

<b id="f1">1</b> For MogoDB with docuemt embedding a filter by "title" field is used [↩](#a1)

