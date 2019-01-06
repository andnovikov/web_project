import datetime

from django.db import models
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name

class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.item_name