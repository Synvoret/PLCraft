from django.db import models


class Crochet(models.Model):

    types = [
        ("Animal", "Animal"),
        ("People", "People"),
        ("Item", "Item"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="crochets/")
    type = models.CharField(max_length=10, choices=types)

    def __str__(self):
        return self.name
