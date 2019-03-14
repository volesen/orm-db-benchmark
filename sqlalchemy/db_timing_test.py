import time
import timeit
import logging

from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_model import Base, Author, Album, Track
from sqlalchemy.engine import Engine

# Set DB interaction time logger
logging.basicConfig()
logger = logging.getLogger("app.sqltime")
logger.setLevel(logging.DEBUG)

# Set event handlders to time query
@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                          parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    logger.debug("Start Query: %s", statement)


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                         parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    logger.debug("Query Complete!")
    logger.debug("Total Time: %f", total)


# Set DB connection
#engine = create_engine('postgresql://root:password@localhost:5432/test', echo=False)
engine = create_engine('sqlite:///sqlite/test.db', echo=False)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base.metadata.create_all(bind=engine)

query_size = [10**2, 10**3, 10**4, 10**5]


def make_query(size):
    db_session.query(Author)\
        .limit(size)\
        .all()


'''
print('PostgreSQL with SQLAlchemy (average of 10.000 queries)')
for size in query_size:
    timer = timeit.Timer("make_query(size)", globals=globals())
    time = timer.timeit(number=10000)
    print(f'Query size: {size}, time: {time}')

db_session.remove()
'''
