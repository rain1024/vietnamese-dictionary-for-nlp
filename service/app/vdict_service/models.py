from django.db import models


class Word(models.Model):
    name = models.TextField()
    type = models.CharField(max_length=30)
