

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=256)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    state = models.CharField(max_length=30)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return self.username


class Product(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField()
    slug = models.SlugField()
    thumb = models.ImageField(blank=True)
    

