
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from music.views import AlbumListView

router = DefaultRouter()
router.register(r'albums', AlbumListView, basename='album')

urlpatterns = [
    path('', include(router.urls))
]