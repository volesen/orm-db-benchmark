import random

from faker import Faker
from mongoengine import Document, EmbeddedDocument, StringField, IntField, FloatField, EmbeddedDocumentListField


faker = Faker()


class Track(EmbeddedDocument):
    title = StringField(default=faker.name)
    unit_price = FloatField(default=0.99)


class Album(EmbeddedDocument):
    title = StringField(default=faker.name)
    price = IntField(default=random.randint(5, 9))

    tracks = EmbeddedDocumentListField(Track)


class Author(Document):
    name = StringField(default=faker.name)
    publisher = StringField(default=faker.company)
    address = StringField(default=faker.address)

    albums = EmbeddedDocumentListField(Album)


if __name__ == '__main__':
    pass
