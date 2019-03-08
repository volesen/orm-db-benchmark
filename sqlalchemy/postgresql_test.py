import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_model import Base, Author, Album, Track

engine = create_engine('postgresql://root:password@localhost:5432/test', echo=False)

#engine = create_engine('sqlite:///test.db', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.metadata.create_all(bind=engine)

query_size = [10**2, 10**3, 10**4, 10**5]


def get_query():
    db_session.query(Author)\
        .join(Album)\
        .join(Track)\
        .filter(Track.id==1)\
        .first()

def make_query(size):
    db_session.query(Author)\
        .limit(size)\
        .all()



for size in query_size:
    timer = timeit.Timer("make_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')


'''
print('Sqllite with Sqlchemy (10.000 average)')
timer = timeit.Timer("get_query()", globals=globals())
time = timer.timeit(number=10000)
print(f'Get query, time: {time}')
'''

db_session.remove()
