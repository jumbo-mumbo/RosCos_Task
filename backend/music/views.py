from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

from .models import Album
from .serializers import AlbumSerializer


class AlbumListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["name", "artist"]
