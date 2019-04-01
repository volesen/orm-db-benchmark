import os

from peewee import Model, IntegerField, CharField, ForeignKeyField, FloatField, ForeignKeyField
from playhouse.db_url import connect


database = connect(os.environ.get('DATABASE_URL'))


class BaseModel(Model):
    class Meta:
        database = database
        table_name = 'author'


class Author(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    publisher = CharField(max_length=255)
    address = CharField(max_length=255)


class Album(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    price = IntegerField()

    author = ForeignKeyField(Author, backref='albums')


class Track(BaseModel):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    unit_price = FloatField()

    album = ForeignKeyField(Album, backref='tracks')
