# Generated by Django 5.1.4 on 2025-01-18 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0011_unitmeasure'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitmeasure',
            name='unit_measure_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
