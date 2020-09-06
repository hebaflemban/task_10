from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)

    # Adding a relationship field
    owner = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
    	return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    restaurant = models.ForeignKey(Restaurant, on_delete = models.SET_NULL, blank=True, null=True)


    def __str__(self):
    	return self.name
