# Generated by Django 5.1.4 on 2025-01-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0010_alter_category_options_recipeingredients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnitMeasure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_measure_name', models.CharField(max_length=50)),
            ],
        ),
    ]
