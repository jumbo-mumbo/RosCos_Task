from django.urls import path
from .views import AlbumListView

urlpatterns = [path("albums/", AlbumListView.as_view(), name="album_list_view")]
