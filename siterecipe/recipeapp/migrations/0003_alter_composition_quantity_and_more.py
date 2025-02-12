# Generated by Django 5.1.4 on 2025-02-12 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='quantity',
            field=models.FloatField(verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='composition',
            name='unit_measurer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipeapp.unitmeasure', verbose_name='Единицы измерения'),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient_name',
            field=models.CharField(max_length=255, verbose_name='Ингредиент'),
        ),
    ]
