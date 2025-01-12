from math import trunc

from django.db import models
from django.urls import reverse


class RecipeBase(models.Model):
    recipe_title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    cooking_description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_slug': self.slug})


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True)
    category_slug = models.SlugField(max_length=100, blank=True, db_index=True, default='')

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name
