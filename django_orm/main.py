import os
import timeit
import django
from django.db.models import Prefetch

# Django specific settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Django project setup
django.setup()

# Importing models
from data.models import Author, Album, Track


def limit_query(size):
    # Forcing sevaluation of QuerySet with repr, see
    # https://docs.djangoproject.com/en/dev/ref/models/querysets/#when-querysets-are-evaluated
    repr(Author.objects.all()[0:size])


def get_query():
    Author.objects.get(albums__tracks__id=1)


def contain_query():
    Author.objects.filter(name__contains='John').first()


def like_query():
    # query is equivalent to LIKE '%John'
    Author.objects.filter(name__startswith='John').first()


query_size = [10**2, 10**3, 10**4, 10**5]

queryset = Author.objects.get(id=1)

print(queryset.albums)

print(f'PostgreSQL with Django ORM (10.000 total)')

for size in query_size:
    timer = timeit.Timer("limit_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'"LIMIT" query, size: {size}, time: {time}')


timer = timeit.Timer("get_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'"GET" query, time: {time}')


timer = timeit.Timer("contain_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'"CONTAINS" query, time: {time}')


timer = timeit.Timer("like_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'"LIKE" query, time: {time}')
