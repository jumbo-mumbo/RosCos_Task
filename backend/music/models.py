from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=255, help_text="Название Альбома")
    date = models.DateField(help_text="Год выпуска альбома")
    artist = models.ForeignKey(
        "Artist", on_delete=models.CASCADE, help_text="Имя автора"
    )

    class Meta:
        ordering = ["-name"]
        indexes = [models.Index(fields=["-name"])]

    def get_artist_name(self):
        return f"{self.artist.name}"

    def __str__(self) -> str:
        return f"{self.name}[{self.date.year}]"


class Artist(models.Model):
    name = models.CharField(max_length=255, help_text="Имя автора")

    class Meta:
        ordering = ["-name"]
        indexes = [models.Index(fields=["-name"])]

    def __str__(self) -> str:
        return f"{self.name}"


class Track(models.Model):
    name = models.CharField(max_length=255, help_text="Название трека")
    album = models.ForeignKey("Album", on_delete=models.CASCADE, related_name="tracks")

    def __str__(self) -> str:
        return f"[{self.album.name}] - {self.name}"
