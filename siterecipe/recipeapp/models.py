from django.db import models
from django.urls import reverse


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)


    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_slug': self.slug})
