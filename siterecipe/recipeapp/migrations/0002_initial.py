# Generated by Django 5.1.4 on 2025-02-08 10:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipeapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='recipebase',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipes', to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='recipebase',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cat_recipe', to='recipeapp.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='recipebase',
            name='recipe_ingredients',
            field=models.ManyToManyField(related_name='ingredients_recipe', through='recipeapp.Composition', to='recipeapp.ingredients', verbose_name='Ингредиенты'),
        ),
        migrations.AddField(
            model_name='composition',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.recipebase'),
        ),
        migrations.AddField(
            model_name='composition',
            name='unit_measurer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.unitmeasure'),
        ),
    ]
