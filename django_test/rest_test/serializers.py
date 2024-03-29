from rest_test.models import Author, Album, Track
from rest_framework import serializers

# http://ses4j.github.io/2015/11/23/optimizing-slow-django-rest-framework-performance/
# Eager lodaing

class TrackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
