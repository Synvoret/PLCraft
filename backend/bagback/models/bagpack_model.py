from django.db import models


class Bagpack(models.Model):

    seasons = [
        ("spring", "Spring"),
        ("summer", "Summer"),
        ("Autumn", "Autumn"),
        ("winter", "Winter"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="bagpacks/")
    season = models.CharField(max_length=10, choices=seasons)

    def __str__(self):
        return self.name
