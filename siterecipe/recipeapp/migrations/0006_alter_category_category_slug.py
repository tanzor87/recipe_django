# Generated by Django 5.1.4 on 2025-01-11 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0005_category_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True, default='', max_length=100),
        ),
    ]
