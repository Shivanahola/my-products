from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    title = models.CharField(max_length=100)


class Dishes(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    products = models.TextField()
    recipe = models.TextField()
    image = models.CharField(max_length=200, default='')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

