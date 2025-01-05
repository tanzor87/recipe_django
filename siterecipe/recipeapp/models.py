from django.db import models


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255)
