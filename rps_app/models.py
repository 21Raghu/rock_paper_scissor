from django.db import models

class Result(models.Model):
    user = models.CharField(max_length=10)
    comp = models.CharField(max_length=10)
    res = models.CharField(max_length=10)

