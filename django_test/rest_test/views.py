from rest_framework import viewsets

from rest_test.models import Author, Album, Track
from rest_test.serializers import AuthorSerializer, AlbumSerializer, TrackSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.prefetch_related('albums', 'albums__tracks')
    serializer_class = AuthorSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.prefetch_related('tracks')
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
