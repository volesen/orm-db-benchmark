import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_model import Base, Author, Album, Track

#engine = create_engine(
#    'postgresql://root:password@localhost:5432/test', echo=False)

engine = create_engine('sqlite:///test.db', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.metadata.create_all(bind=engine)

query_size = [10**2, 10**3, 10**4, 10**5]


def limit_query(size):
    db_session.query(Author)\
        .limit(size)\
        .all()

def get_query():
    db_session.query(Author)\
        .join(Album)\
        .join(Track)\
        .filter(Track.id == 1)\
        .first()

def contains_query():
    db_session.query(Author)\
        .filter(Author.name.contains('John')).first()


def like_query():
    db_session.query(Author)\
        .filter(Author.name.like('John%')).first()


DB_NAME = 'sqlite3'
print(f'{DB_NAME} benchmark with SQLAlchemy (10.000 average)')

print('"limit" query benchmark')
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


print('"like" query benchmark')
timer = timeit.Timer("like_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')


db_session.remove()
