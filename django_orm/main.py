import os
import timeit
import django

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Django project setup
django.setup()

# Import models
from data.models import Author, Album, Track


# https://docs.djangoproject.com/en/dev/ref/models/querysets/#when-querysets-are-evaluated
def limit_query(size):
    # Forcing sevaluation of QuerySet with len
    len(Track.objects.select_related()[0:size])


def get_query():
    # Forcing serialization to list
    Author.objects.filter(albums__tracks__id=1).first()


def contain_query():
    Author.objects.filter(name__contains='John').first()


def like_query():
    Author.objects.filter(name__startswith='John').first()


query_size = [10**2, 10**3, 10**4, 10**5]

print(f'PostgreSQL with Django ORM (10.000 total)')

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
