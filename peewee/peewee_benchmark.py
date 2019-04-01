import timeit
import logging

from peewee import JOIN
from peewee_model import Author, Album, Track

# Setup logging to monitor SQL queries
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def limit_query(size):
    (Author
     .select()
     .limit(size))


def get_query():
    (Author
     .select()
     .join(Album)
     .join(Track)
     .where(Track.id == 1)
     .first())


def contains_query():
    (Author
     .select()
     .where(Author.name.contains('John'))
     .first())


query_size = [10**2, 10**3, 10**4, 10**5]

DB_NAME = 'PostgreSQL'
'''
print(f'{DB_NAME} benchmark with Peewee (10.000 average)')

print('"LIMIT" query benchmark')
for size in query_size:
    timer = timeit.Timer("limit_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')

print('Get query benchmark')
timer = timeit.Timer("get_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')


print('"contains" query benchmark')
timer = timeit.Timer("contains_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')

'''

first_author = (
                Author.
                select(Author, Album).
                join(Album, JOIN.INNER).
                first()
                )

print(list(first_author.albums))
