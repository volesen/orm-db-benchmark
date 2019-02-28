import timeit
from mongoengine import connect
from mongodb.mongoengine_model import Author

connect('test', host='localhost', port=27017)

query_size = [10**2, 10**3, 10**4, 10**5]


def make_query(size):
    Author.objects.limit(size)
    
print('MongoDB with Mongoengine (average of 10.000 queries)')
for size in query_size:
    timer = timeit.Timer("make_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')
