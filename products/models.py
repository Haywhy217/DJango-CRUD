from django.db import models

class Product(models.Model): 
    name = models.CharField(max_length=60)
    image_url = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=60)
    brand = models.CharField(max_length=15)
    price = models.FloatField()
    available = models.BooleanField(default=True)
