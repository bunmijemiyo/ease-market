from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    contact = models.IntegerField()
