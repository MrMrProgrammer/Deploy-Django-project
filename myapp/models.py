# myapp/models.py

from django.db import models

class FootballPlayer(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField()