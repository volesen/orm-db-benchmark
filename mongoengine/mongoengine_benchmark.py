import re
import timeit

from mongoengine import connect
from mongoengine_model_refrence import Author, Album, Track

connect('test', host='localhost', port=27017)

regex = re.compile('.*bob.*')


def limit_query(size):
    Author.objects.limit(size)


def get_query():
    # As model embedding is used, I cant filter by id for track
    Author.objects.filter(albums__tracks__match={
                          'title': 'Vincent Phillips'})


def contain_query():
    Author.objects.filter(name__contains='John')


def like_query():
    Author.objects.filter(name__startswith='John')


query_size = [10**2, 10**3, 10**4, 10**5]

print(f'MongoDB benchmark with Mongoengine (10.000 total)')

print('Query size benchmark')
for size in query_size:
    timer = timeit.Timer("limit_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')

print('Get query benchmark')
timer = timeit.Timer("get_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')


print('"contains" query benchmark')
timer = timeit.Timer("contain_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')


print('"like" query benchmark')
timer = timeit.Timer("like_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')

print(Author.objects.filter(albums__tracks__match={
    'title': 'Curtis Myers'}))
