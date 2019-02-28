# ORM and DB benchmarking methodology
In this benchmark the following databases are tested:
- Sqlite3
- PostgreSQL 11.1
- MongoDB 3.4.19
- Elasticseach (WIP)

and the following ORM/ODM:
- SQLAlcehmy with Flask
- Mongoengine with Flask
- Django ORM

One-to-many relationships are modeled by embedded documents for MongoDB.

For each data ORM and DB pair, a query of the following amount of records
- 100
- 1.000
- 10.000
- 100.000 (all)
by first is done.

The time spent on DB-interactions is observed in DB-logs, whereas the ORM/ODM serialization (and DB-interactions) is measured with the `timeit` python module.
The time for DB-interactions is not subtracted, as different ORM/ODM will not necessarily do operations by identical SQL queries. Therefore it is relevant to measure and take this into account.

# Results

