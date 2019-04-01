from peewee import Model, IntegerField, CharField, ForeignKeyField, FloatField, PostgresqlDatabase

db = PostgresqlDatabase('test', user='root',
                        password='password', host='0.0.0.0', port=5432)


class Author(Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    publisher = CharField(max_length=255)
    address = CharField(max_length=255)

    class Meta:
        database = db
        table_name = 'author'


class Album(Model):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    price = IntegerField()

    author = ForeignKeyField(Author, backref='albums')

    class Meta:
        database = db
        table_name = 'album'


class Track(Model):
    id = IntegerField(primary_key=True)
    title = CharField(max_length=255)
    unit_price = FloatField()

    album = ForeignKeyField(Album, backref='tracks')

    class Meta:
        database = db
        table_name = 'track'
