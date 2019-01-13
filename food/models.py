from django.db import models

from .choices import *
# Create your models here.

class Restaurants(models.Model):
    restaurant_name = models.CharField(max_length=50)
    restaurant_city = models.CharField(max_length=50)
    restaurant_type = models.CharField(max_length=50)
    what_we_ate = models.CharField(max_length=250)
    when_we_ate = models.DateTimeField()
    meal_cost = models.FloatField(default=0)
    rating_michael = models.IntegerField(choices=rating_choices, default=3)
    rating_coly = models.IntegerField(choices=rating_choices, default=3)
    would_come_again = models.IntegerField(choices=come_again_choices, default=0)




