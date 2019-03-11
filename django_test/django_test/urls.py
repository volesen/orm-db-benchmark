from django.urls import include, path
from rest_framework import routers

import rest_test.views 

#from django_test.rest_test.views import AuthorViewSet, AlbumViewSet, TrackViewSet

router = routers.DefaultRouter()
router.register(r'authors', rest_test.views.AuthorViewSet)
router.register(r'albums', rest_test.views.AlbumViewSet)
router.register(r'tracks', rest_test.views.TrackViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
