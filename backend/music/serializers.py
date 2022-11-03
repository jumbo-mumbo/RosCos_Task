from rest_framework import serializers
from collections import OrderedDict


from .models import Album, Artist, Track


class TracksSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="*")

    class Meta:
        model = Track
        fields = ["name"]

    def to_representation(self, instance):
        return f"{instance.name}"


class AlbumSerializer(serializers.ModelSerializer):
    album = serializers.CharField(source="*")
    artist = serializers.CharField(source="get_artist_name")
    tracks = TracksSerializer(many=True)

    class Meta:
        model = Album
        fields = ["album", "name", "artist", "tracks"]

    def to_representation(self, instance):
        inst = super().to_representation(instance)
        new_inst = OrderedDict(
            ("artist@name" if k == "artist" else k, v) for k, v in inst.items()
        )
        return new_inst
