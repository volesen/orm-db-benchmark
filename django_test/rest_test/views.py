from rest_framework import viewsets

from rest_test.models import Author, Album, Track
from rest_test.serializers import AuthorSerializer, AlbumSerializer, TrackSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
