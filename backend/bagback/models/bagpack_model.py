from django.db import models


class Bagpack(models.Model):

    seasons = [
        ("spring", "spring"),
        ("summer", "summer"),
        ("autumn", "autumn"),
        ("winter", "winter"),
    ]

    types = [
        ("single", "single"),
        ("multi", "multi"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="bagpacks/")
    season = models.CharField(max_length=10, choices=seasons)
    type = models.CharField(max_length=10, default="single", choices=types)

    def __str__(self):
        return self.name
