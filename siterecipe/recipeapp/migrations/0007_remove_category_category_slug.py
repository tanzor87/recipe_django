# Generated by Django 5.1.4 on 2025-01-11 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0006_alter_category_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_slug',
        ),
    ]
