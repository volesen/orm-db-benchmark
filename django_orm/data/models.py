import random

from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        db_table = 'author'
        managed = False


class Album(models.Model):
    id = models.IntegerField(primary_key=True)

    title = models.CharField(max_length=255)
    price = models.IntegerField()

    author = models.ForeignKey(
        Author, related_name='albums', on_delete=models.CASCADE, db_column='author_id')

    class Meta:
        db_table = 'album'
        managed = False


class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    unit_price = models.FloatField()

    album = models.ForeignKey(
        'Album', related_name='tracks', on_delete=models.CASCADE, db_column='album_id')

    class Meta:
        db_table = 'track'
        managed = False
