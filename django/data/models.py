import random

from django.db import models
from faker import Faker

faker = Faker()


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, default=faker.name)
    publisher = models.CharField(max_length=255, default=faker.company)
    address = models.CharField(max_length=255, default=faker.address)

    class Meta:
        db_table = 'author'
        managed = False


class Album(models.Model):
    id = models.IntegerField(primary_key=True)

    title = models.CharField(max_length=255, default=faker.name)
    price = models.IntegerField(default=random.randint(5, 9))

    author = models.ForeignKey(
        Author, related_name='albums', on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        db_table = 'album'
        managed = False


class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default=faker.name)
    unit_price = models.FloatField(default=0.99)

    album = models.ForeignKey(
        'Album', related_name='tracks', on_delete=models.CASCADE, db_column='album_id')

    class Meta:
        db_table = 'track'
        managed = False