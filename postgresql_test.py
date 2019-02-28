import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from postgresql.sqlalchemy_model import Base, Author, Album, Track


engine = create_engine('sqlite:///sqlite/test.db', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.metadata.create_all(bind=engine)

query_size = [10**2, 10**3, 10**4, 10**5]


def make_query(size):
    db_session.query(Author)\
        .join(Album)\
        .join(Track)\
        .limit(size)\
        .all()


for size in query_size:
    timer = timeit.Timer("make_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')

db_session.remove()
