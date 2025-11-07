from django.db import models


class Crochet(models.Model):

    categories = [
        ("animal", "animal"),
        ("people", "people"),
        ("item", "item"),
    ]

    types = [
        ("single", "single"),
        ("multi", "multi"),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="crochets/")
    category = models.CharField(max_length=10, default="animal", choices=categories)
    type = models.CharField(max_length=10, default="single", choices=types)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
