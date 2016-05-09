from django.db import models


class Word(models.Model):
    name = models.TextField(unique=True, max_length=1000)
    type = models.CharField(max_length=30)
