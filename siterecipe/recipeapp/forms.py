from django import forms
from .models import Category, Ingredients, Composition

class AddRecipeForm(forms.Form):
    recipe_title = forms.CharField(max_length=255)
    short_description = forms.CharField(widget=forms.Textarea)
    cooking_description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())




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