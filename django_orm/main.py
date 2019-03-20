from data.models import Author, Album, Track
import os
import timeit
import django

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Django project setup
django.setup()

query_size = [10**2, 10**3, 10**4, 10**5]


def make_query(size):
    # Forcing serialization to list
    list(Track.objects.select_related().all()[0:size])


def get_query():
    # Forcing serialization to list
    list(Author.objects.filter(albums__tracks__id=1))


print('PostgreSQL with Django ORM (average of 10.000 queries)')
print('Select limit query')
for size in query_size:
    timer = timeit.Timer("make_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')

print('FIlter by track id')
timer = timeit.Timer("get_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')
