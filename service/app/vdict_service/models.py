from django.db import models


class Word(models.Model):
    name = models.TextField(unique=True, max_length=100)
    type = models.CharField(max_length=30)
