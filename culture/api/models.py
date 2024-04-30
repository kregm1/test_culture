from django.db import models


class Theatre(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    legal_entity = models.CharField(max_length=250)
    subordination = models.CharField(max_length=250)
    website = models.URLField(default=None)
    email = models.EmailField(default=None)
    inn = models.CharField(max_length=12)
    type = models.CharField(max_length=250, default='noncommercial')
    coordinates_x = models.FloatField(default=None)
    coordinates_y = models.FloatField(default=None)

