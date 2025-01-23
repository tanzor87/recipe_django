from math import trunc

from django.db import models
from django.urls import reverse


class UnitMeasure(models.Model):
    unit_measure_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.unit_measure_name


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_slug': self.slug})


class RecipeBase(models.Model):
    recipe_title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True)
    cooking_description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    recipe_ingredients = models.ManyToManyField(
        Ingredients,
        related_name='ingredients_recipe',
        through='Composition',
    )

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_id': self.pk})

    def __str__(self):
        return self.recipe_title


class Composition(models.Model):
    recipe = models.ForeignKey(RecipeBase, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    unit_measurer = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        if (float(str(self.quantity))).is_integer() and self.quantity != 0.0:
            q = int(float(str(self.quantity)))
            result = f'{self.ingredient} - {q} {self.unit_measurer}'
        elif self.quantity == 0.0:
            result = f'{self.ingredient} - {self.unit_measurer}'
        else:
            result = f'{self.ingredient} - {self.quantity} {self.unit_measurer}'
        return result


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True)
    category_slug = models.SlugField(max_length=100, unique=True, db_index=True)

    # class Meta:
    #     ordering = ['category_name']
    def get_absolut_url(self):
        return reverse('category', kwargs={'category_slug': self.category_slug})

    def __str__(self):
        return self.category_name
