from django import forms
from .models import Category, Ingredients, Composition

class AddRecipeForm(forms.Form):
    recipe_title = forms.CharField(
        max_length=255,
        label="Название рецепта",
        error_messages={
            'required': 'Без названия никак',
        },
    )
    short_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Краткое описание')
    cooking_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), label='Пошаговый рецепт')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label='Категория')




    # recipe_title = models.CharField(max_length=255, verbose_name='Название рецепта')
    # short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    # cooking_description = models.TextField(blank=True)
    # time_create = models.DateTimeField(auto_now_add=True)
    # time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    # category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    # recipe_ingredients = models.ManyToManyField(
    #     Ingredients,
    #     related_name='ingredients_recipe',
    #     through='Composition',
    # )