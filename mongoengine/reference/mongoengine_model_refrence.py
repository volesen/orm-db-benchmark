import random

from faker import Faker
from mongoengine import Document, EmbeddedDocument, StringField, IntField, FloatField, ListField, ReferenceField


faker = Faker()


class Track(Document):
    title = StringField(default=faker.name)
    unit_price = FloatField(default=0.99)


class Album(Document):
    title = StringField(default=faker.name)
    price = IntField(default=random.randint(5, 9))

    tracks = ListField(ReferenceField(Track))


class Author(Document):
    name = StringField(default=faker.name)
    publisher = StringField(default=faker.company)
    address = StringField(default=faker.address)

    albums = ListField(ReferenceField(Album))
