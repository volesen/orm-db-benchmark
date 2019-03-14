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


def make_query(size):
    db_session.query(Author)\
        .limit(size)\
        .all()


db_session.remove()
